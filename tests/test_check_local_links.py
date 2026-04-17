import tempfile
import unittest
from pathlib import Path

from scripts.check_local_links import (
    check_link,
    collect_local_link_errors,
    has_fragment_target,
    markdown_slug,
    resolve_candidate,
)


class LinkCheckerTests(unittest.TestCase):
    def test_markdown_slug_normalizes_headings(self):
        self.assertEqual(markdown_slug("  Hello, World!  "), "hello-world")
        self.assertEqual(markdown_slug("A   B---C"), "a-b-c")

    def test_has_fragment_target_finds_html_id_and_name(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            html = Path(tmpdir) / "page.html"
            html.write_text('<div id="top"></div><a name="anchor"></a>', encoding="utf-8")
            self.assertTrue(has_fragment_target(html, "top"))
            self.assertTrue(has_fragment_target(html, "anchor"))
            self.assertFalse(has_fragment_target(html, "missing"))

    def test_has_fragment_target_finds_markdown_headings(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            md = Path(tmpdir) / "doc.md"
            md.write_text("# Intro\n\n## Deep Dive\n", encoding="utf-8")
            self.assertTrue(has_fragment_target(md, "intro"))
            self.assertTrue(has_fragment_target(md, "deep-dive"))
            self.assertFalse(has_fragment_target(md, "not-there"))

    def test_resolve_candidate_handles_relative_absolute_and_fragment_only(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            source = root / "docs" / "README.md"
            source.parent.mkdir(parents=True)
            source.write_text("", encoding="utf-8")

            self.assertEqual(resolve_candidate(source, "guide.md", root), root / "docs" / "guide.md")
            self.assertEqual(resolve_candidate(source, "/index.html", root), root / "index.html")
            self.assertEqual(resolve_candidate(source, "#intro", root), source)

    def test_check_link_ignores_external_and_non_file_schemes(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            source = root / "README.md"
            source.write_text("", encoding="utf-8")
            errors = []
            cache = {}

            for link in [
                "https://example.com",
                "http://example.com",
                "mailto:test@example.com",
                "tel:+123",
                "javascript:void(0)",
                "data:text/plain,abc",
                "",
                "   ",
            ]:
                check_link(link, source, root, cache, errors)

            self.assertEqual(errors, [])

    def test_check_link_reports_missing_target(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            source = root / "README.md"
            source.write_text("", encoding="utf-8")
            errors = []

            check_link("missing.md", source, root, {}, errors)

            self.assertEqual(len(errors), 1)
            self.assertIn("missing target", errors[0])

    def test_check_link_reports_path_escape(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            source = root / "docs" / "README.md"
            source.parent.mkdir(parents=True)
            source.write_text("", encoding="utf-8")

            outside = root.parent / f"{root.name}-outside.md"
            outside.write_text("", encoding="utf-8")
            self.addCleanup(lambda: outside.unlink(missing_ok=True))

            errors = []
            check_link(f"../../{outside.name}", source, root, {}, errors)

            self.assertEqual(len(errors), 1)
            self.assertIn("resolves outside repository", errors[0])

    def test_check_link_reports_missing_fragment(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            source = root / "README.md"
            target = root / "index.html"
            source.write_text("", encoding="utf-8")
            target.write_text('<div id="exists"></div>', encoding="utf-8")

            errors = []
            check_link("index.html#missing", source, root, {}, errors)

            self.assertEqual(len(errors), 1)
            self.assertIn("missing fragment target", errors[0])

    def test_collect_local_link_errors_detects_valid_and_invalid_links(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            readme = root / "README.md"
            index = root / "index.html"
            doc = root / "doc.md"

            index.write_text('<section id="top"></section><a href="doc.md#details">doc</a>', encoding="utf-8")
            doc.write_text("## Details\n", encoding="utf-8")
            readme.write_text(
                "[ok](index.html#top)\n[missing](missing.md)\n",
                encoding="utf-8",
            )

            errors = collect_local_link_errors([readme, index, doc], root)

            self.assertEqual(len(errors), 1)
            self.assertIn("missing target", errors[0])


if __name__ == "__main__":
    unittest.main()
