# Portfolio Site Current-State Plan

_Last updated: 2026-05-05_

## Purpose

This repository is the public portfolio site for `https://dimangite.github.io/`.

It presents a restrained academic/engineering profile for a Computer Science PhD student focused on reproducible ML evaluation, predictive modeling, research tooling, and public project artifacts. The site is intentionally static, low-dependency, and GitHub Pages-native.

## Current Repository Structure

```text
.
├── .claude/                  # Local/agent working notes if present; not part of runtime site
├── .github/workflows/        # GitHub Actions workflows
│   ├── deploy.yml            # GitHub Pages deployment
│   ├── quality.yml           # Static quality/local link validation
│   └── codeql-analysis.yml   # CodeQL/code scanning workflow
├── scripts/                  # Repository utility scripts
│   └── check_local_links.py  # Local internal-link validation
├── tests/                    # Unit tests for repository scripts/checks
├── .gitignore
├── ARCHITECTURE.md           # Architecture and documentation diagrams
├── CHANGELOG.md              # Site/project change log
├── README.md                 # Repository overview
├── _config.yml               # GitHub Pages/Jekyll compatibility config
├── favicon.svg
├── index.html                # Main public portfolio page
├── plan.md                   # Current-state plan and operating notes
├── privacy.html              # Privacy note page
├── robots.txt
├── sitemap.xml
└── styles.css                # Main site styling and responsive behavior
```

## Current Runtime Surface

### Main site

- URL: `https://dimangite.github.io/`
- Entry point: `index.html`
- Styling: `styles.css`
- Deployment target: GitHub Pages
- Runtime model: static HTML/CSS/JavaScript only

### Major public sections

- About / hero profile
- Profiles and records evidence strip
- Research scope
- Public research record
- Career timeline
- Tech stack
- Repository artifacts
- Contact and links
- Privacy/footer controls

### Current repository artifact cards

The `Repository Artifacts` section currently includes:

1. GitHub Profile README
2. Portfolio Source & Deployment
3. Site Quality Checks
4. System Design Lab

The System Design Lab card links to the live documentation site while allowing the source repository to remain private until ready for publication.

## Current Architecture

The repository follows a static-site architecture:

```text
Browser
  -> GitHub Pages static hosting
    -> index.html
    -> styles.css
    -> favicon.svg
    -> privacy.html
    -> sitemap.xml / robots.txt

Developer workflow
  -> Pull request or direct branch update
  -> quality.yml / local checks
  -> deploy.yml
  -> GitHub Pages deployment
```

## Current Design System

The site uses a compact, portfolio-oriented visual system.

### Light mode tokens

- Background: `#f7f8fa`
- Surface: `#ffffff`
- Raised surface: `#f1f4f8`
- Text: `#1d2430`
- Secondary text: `#4e5b70`
- Muted text: `#667489`
- Border: `#d8dde5`
- Accent: `#2f5eb8`

### Dark mode tokens

- Background: `#0b0d10`
- Surface: `#11151a`
- Raised surface: `#161b22`
- Text: `#e6edf3`
- Secondary text: `#a9b4c0`
- Muted text: `#7d8896`
- Border: `#232a33`
- Accent: `#6aa0ff`

### UI behavior

- Theme preference is stored locally in the browser.
- Language preference is stored locally in the browser.
- The site avoids advertising cookies and third-party tracking scripts.
- Khmer font loading is lazy/conditional to reduce default render-blocking cost.

## Current Internationalization State

`index.html` contains inline translation dictionaries for:

- English (`en`)
- Korean (`ko`)
- Khmer (`km`)

Important rule: when changing user-facing text with `data-i18n`, update all three dictionaries in the same change. Do not patch only English.

## Current CI/CD and Verification

### Workflows

- `.github/workflows/deploy.yml`
  - Publishes the static site to GitHub Pages.
- `.github/workflows/quality.yml`
  - Runs repository quality checks.
- `.github/workflows/codeql-analysis.yml`
  - Runs CodeQL/code scanning where supported by repository settings.

### Local verification commands

Run before merging site changes:

```bash
python scripts/check_local_links.py
python -m unittest discover -s tests -v
```

For HTML/CSS/JS edits, also manually verify:

- Desktop viewport
- Mobile viewport around the 900px navigation breakpoint
- Theme toggle behavior
- Language toggle behavior
- Footer controls
- Internal anchors
- External links opening correctly

## Current Governance Rules

1. Keep the site static and GitHub Pages-compatible.
2. Do not add build tooling unless there is a clear maintenance benefit.
3. Do not add analytics, advertising cookies, or unnecessary third-party scripts.
4. Do not expose private research data, lab credentials, database details, or unpublished manuscript artifacts.
5. Keep portfolio copy factual and restrained.
6. Maintain all three language dictionaries when changing translated content.
7. Treat `index.html` as high-risk because markup, translation dictionaries, and behavior are co-located.
8. Prefer small PRs with one purpose: content, style, workflow, or documentation.

## Current Known State

Completed:

- Main portfolio static site is live.
- Trilingual support exists for the main page.
- Dark/light theme support exists.
- Mobile navigation exists.
- Privacy page exists.
- `robots.txt` and `sitemap.xml` exist.
- Quality workflow and deploy workflow exist.
- CodeQL workflow exists.
- Architecture documentation exists in `ARCHITECTURE.md`.
- System Design Lab is already listed in Repository Artifacts.

Needs periodic review:

- Keep `README.md`, `ARCHITECTURE.md`, and this `plan.md` synchronized after structural changes.
- Ensure new artifact cards have EN/KO/KM translations.
- Ensure GitHub Pages deployment remains active after workflow or repository-setting changes.
- Ensure public links still resolve after repository visibility changes.

## Active Next Steps

### 1. Keep documentation synchronized

When repository structure changes, update:

- `README.md`
- `ARCHITECTURE.md`
- `plan.md`

### 2. Validate System Design Lab integration

After System Design Lab visual polish is merged and deployed:

- Confirm the live demo link works from the main portfolio.
- Confirm the repository-private wording remains accurate.
- If the source repository becomes public later, update the card copy and translations.

### 3. Preserve visual consistency

Any satellite project linked from this portfolio should reuse the main portfolio design language where practical:

- compact header
- simple footer
- small circular theme control in footer
- restrained accent color
- neutral dark mode
- no oversized gradient-heavy landing-page treatment

## Definition of Done for Future Portfolio Changes

A change is complete only when:

- Relevant files are updated.
- Local link checks pass.
- Unit tests pass.
- Desktop and mobile layouts are visually checked.
- Theme/language behavior is checked when affected.
- Public-facing copy is factual and professional.
- No private or sensitive material is exposed.
