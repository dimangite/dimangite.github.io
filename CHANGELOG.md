# Changelog

All notable changes to this repository are documented here.

## [Unreleased]

### Added
- `ARCHITECTURE.md` to document site structure, design decisions, and maintenance practices.
- `CHANGELOG.md` to keep repository-level change tracking explicit and truthful.
- `.github/workflows/quality.yml` for lightweight static quality checks.
- `robots.txt` and `sitemap.xml` for minimal, maintainable crawl/index metadata.
- `favicon.svg` as a simple local favicon asset (no external dependency).

### Changed
- `README.md` upgraded with clearer scope boundaries, architecture summary, maintenance expectations, and engineering-signal mapping.
- `index.html` metadata hardened with canonical URL, Open Graph/Twitter summary metadata, theme-color hints, and favicon references.
- `privacy.html` metadata refined for redirect semantics (`noindex,follow`), canonical URL, and consistent head metadata.
- Khmer typography strategy in `styles.css` strengthened with system-first fallback ordering and language-specific readability/wrapping safeguards.

### Repository state reflected in this release train
- Single-page portfolio flow with an integrated in-page privacy section and `privacy.html` redirect compatibility path.
- Timeline organization for employment, education/qualifications, and awards/scholarships.
- Footer/contact and verification-link presentation aligned with a compact static-site layout.
- Mobile and constrained-browser hardening for navigation and text overflow behavior.
