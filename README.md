# dimangite.github.io

Static GitHub Pages portfolio for Dimang Chhol (CS PhD), focused on predictive modeling, ML evaluation, and reproducible research engineering.

## Purpose
This repository publishes a concise, public-facing engineering portfolio. It intentionally exposes a sanitized workflow layer while active manuscript code, unpublished experiments, and submission artifacts remain private.

## Scope and boundaries
**In scope**
- Single-page portfolio UI and content
- Theme/language preference behavior
- Accessibility and responsive hardening
- Static-site deployment and lightweight quality checks

**Out of scope**
- Private research/manuscript repositories
- Analytics or tracking scripts
- Framework migrations and heavy build tooling

## Stack
- HTML5
- CSS3
- Vanilla JavaScript (theme toggle, language toggle, mobile navigation)
- GitHub Pages + GitHub Actions

## Architecture summary
- `index.html`: single-page structure, translation dictionary, UI behavior scripts
- `styles.css`: design tokens, layout, responsive rules, language-specific typography
- `privacy.html`: redirect entry point to `index.html#privacy`
- `.github/workflows/deploy.yml`: GitHub Pages deployment
- `.github/workflows/quality.yml`: lightweight static quality checks

See `ARCHITECTURE.md` for implementation details.

## i18n summary (EN / KO / KM)
- Supported UI languages: English (`en`), Korean (`ko`), Khmer (`km`)
- Translation strings are maintained in one inline dictionary in `index.html`
- UI text and key ARIA labels are updated through `data-i18n*` hooks
- Rule: when adding user-facing text, add keys for **all three languages** in one change

## Theme and persistence behavior
- Light/dark theme is controlled via `data-theme` on `<html>`
- Initial theme uses `prefers-color-scheme`, then localStorage override when present
- Language selection is persisted in localStorage and restored at startup

## Responsive/mobile support
- Desktop + mobile navigation with explicit toggle behavior
- Mobile-first spacing/typography tuning and overflow control
- Works as a static page with graceful degradation in constrained browsers

## Privacy note
- The site does not intentionally use third-party trackers or advertising cookies
- Only local browser preferences (theme/language) may be stored on-device
- Privacy content is available in-page at `#privacy` and via `privacy.html` redirect

## Deployment summary
- Live: **https://dimangite.github.io**
- Deployment workflow: `.github/workflows/deploy.yml`
- Triggered on push to `main` and manual `workflow_dispatch`

## Engineering signal mapping
| Repository signal | Evidence in this repo |
| --- | --- |
| Front-end engineering | Responsive layout, semantic sections, keyboard-accessible controls |
| i18n discipline | Trilingual dictionary (`en`/`ko`/`km`) + synchronized UI key usage |
| Deployment discipline | Dedicated GitHub Pages workflow with explicit build/deploy stages |
| Low-dependency design | Vanilla HTML/CSS/JS; no framework runtime |
| Privacy-aware design | No trackers, explicit privacy section, minimal local-only preference storage |
| Mobile hardening / graceful degradation | Mobile nav fallback, overflow-safe typography, static-first architecture |
| Quality awareness | Lightweight CI checks for static HTML sanity and repository links |

## Local preview
From repository root:

```bash
python -m http.server 8000
```

Open `http://localhost:8000`.

## Maintenance and quality
- Keep edits small, explicit, and production-safe for a static site
- CI (`quality.yml`) intentionally stays lightweight: HTML sanity checks + offline link checks
- Keep metadata (`canonical`, OG, robots, sitemap) truthful and minimal
- Avoid adding dependencies unless they provide clear maintenance value

## Repository structure
```text
.
├─ index.html
├─ styles.css
├─ privacy.html
├─ robots.txt
├─ sitemap.xml
├─ favicon.svg
├─ ARCHITECTURE.md
├─ CHANGELOG.md
└─ .github/
   └─ workflows/
      ├─ deploy.yml
      └─ quality.yml
```

## Minimal future improvements
- Add a real social preview image (`og:image`) when an approved asset is available
- Keep translation and metadata updates synchronized with any new sections
