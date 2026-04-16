# dimangite.github.io

Public GitHub Pages portfolio for Dimang Chhol, a CS PhD student focused on predictive modeling, ML evaluation, and reproducible research engineering.

## Overview
This repository hosts a minimal static portfolio site. It presents public-facing research engineering capabilities while keeping active SCI manuscript code, unpublished experiments, and submission artifacts private.

## Tech stack
- HTML5
- CSS3
- Vanilla JavaScript (theme, language switch, responsive navigation)
- GitHub Pages (Jekyll-based deployment workflow)

## Features
- Professional single-page portfolio structure
- Light/dark theme toggle with persisted preference
- Multilingual UI: English (EN), Korean (KO), Khmer (KM)
- Mobile navigation and keyboard-accessible primary controls

## Local preview
Run a local static server from the repository root:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Deployment (GitHub Pages)
Live site: **https://dimangite.github.io**

The site is deployed through `.github/workflows/deploy.yml` on pushes to `main` and manual `workflow_dispatch`.

## Language support note
EN, KO, and KM content are maintained in the inline translation dictionary in `index.html`. Keep all three in sync when updating visible text.
