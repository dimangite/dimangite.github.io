#!/usr/bin/env python3
"""Validate repository-local links in markdown and HTML files."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_LINK_PATTERN = re.compile(
    r"""(?:href|src)=(?:["']([^"']+)["']|([^\s>]+))""",
    re.IGNORECASE,
)
IGNORED_PREFIXES = ("mailto:", "tel:", "javascript:", "data:")


def markdown_slug(heading: str) -> str:
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug)
    return slug.strip("-")


def has_fragment_target(target: Path, fragment: str, target_text: dict[Path, str] | None = None) -> bool:
    if target_text is None:
        target_text = {}

    text = target_text.get(target)
    if text is None:
        if not target.exists():
            return False
        text = target.read_text(encoding="utf-8")
        target_text[target] = text

    escaped_fragment = re.escape(fragment)
    if re.search(
        rf"""(?:id|name)=["']{escaped_fragment}["']""",
        text,
        re.IGNORECASE,
    ):
        return True

    if target.suffix.lower() in {".md", ".markdown"}:
        heading_pattern = re.compile(
            r"^\s{0,3}#{1,6}\s+(.+)(?:\s+#+)?\s*$",
            re.MULTILINE,
        )
        slugs = {markdown_slug(h) for h in heading_pattern.findall(text)}
        return fragment in slugs

    return False


def resolve_candidate(source_file: Path, link: str, repo_root: Path) -> Path:
    parsed = urlparse(link)
    path_part = parsed.path

    if not path_part:
        return source_file
    if path_part.startswith("/"):
        return repo_root / path_part.lstrip("/")
    return (source_file.parent / path_part).resolve()


def check_link(
    raw_link: str,
    source_file: Path,
    repo_root: Path,
    target_text: dict[Path, str],
    errors: list[str],
) -> None:
    link = raw_link.strip()
    if not link or link.startswith(IGNORED_PREFIXES):
        return

    parsed = urlparse(link)
    if parsed.scheme in ("http", "https"):
        return

    candidate = resolve_candidate(source_file, link, repo_root)

    try:
        candidate.relative_to(repo_root)
    except ValueError:
        errors.append(f"{source_file}: {link} resolves outside repository")
        return

    if not candidate.exists():
        errors.append(f"{source_file}: missing target for {link}")
        return

    if parsed.fragment and not has_fragment_target(candidate, parsed.fragment, target_text):
        errors.append(f"{source_file}: missing fragment target for {link}")


def collect_local_link_errors(targets: list[Path], repo_root: Path) -> list[str]:
    target_text: dict[Path, str] = {}
    errors: list[str] = []

    for target in targets:
        text = target.read_text(encoding="utf-8")
        target_text[target] = text

        for match in MARKDOWN_LINK_PATTERN.findall(text):
            check_link(match, target, repo_root, target_text, errors)

        for quoted, unquoted in HTML_LINK_PATTERN.findall(text):
            check_link(quoted or unquoted, target, repo_root, target_text, errors)

    return errors


def main() -> int:
    repo_root = Path(".").resolve()
    targets = [
        repo_root / "README.md",
        repo_root / "ARCHITECTURE.md",
        repo_root / "CHANGELOG.md",
        repo_root / "index.html",
        repo_root / "privacy.html",
    ]

    errors = collect_local_link_errors(targets, repo_root)

    if errors:
        print("Local link check failures:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Local link checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
