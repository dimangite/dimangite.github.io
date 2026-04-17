## Navigation Duplication Fix Plan

- Root cause confirmed: `index.html` rendered two separate nav trees (`desktop-nav` and `mobile-nav`) with identical links, and the mobile copy remained a second semantic/navigation structure even when visually hidden.
- Refactored the header to one canonical semantic nav list shared by desktop and mobile layouts.
- Updated the menu toggle state so closed mobile navigation is hidden both visually and from the accessibility tree.
- Verified the updated structure preserves translations, theme toggle behavior, section anchors, and responsive desktop/mobile nav behavior in the code paths.

## Review Pass — Navigation and Translation Quality

### Start entry
- Date/time: 2026-04-17 (review session)
- Scope: verify the completed single-nav refactor against the review standard, and audit user-facing wording and all three translation dictionaries (`en`, `ko`, `km`) for professionalism and natural phrasing.
- Files to inspect: `index.html`, `styles.css`, `plan.md`. Out of scope: SEO, redesign, animation, repo housekeeping.

### Completion entry
- Date/time: 2026-04-17 (review session, same sitting)
- Reviewed:
  - `index.html` header markup, nav toggle wiring, primary-nav structure, event handlers, and `syncNavigationState()` logic.
  - `styles.css` header, nav-toggle, `.site-nav`, and responsive mobile breakpoint (≤ 900px).
  - `translations.en`, `translations.ko`, `translations.km` dictionaries end-to-end (nav, hero, focus, work, timeline, awards, research, privacy, footer, aria labels).
- Nav verdict: structurally and semantically correct. Single `<nav id="primary-nav" class="site-nav">`, single `<ul class="nav-list">`, no `desktop-nav` / `mobile-nav` / `mobileMenuAria` residue anywhere in the repo. `aria-controls`, `aria-expanded`, `hidden`, and `.is-open` are all routed through `syncNavigationState()`, which is called from toggle click, link click, outside click, Escape, and breakpoint change. CSS `.site-nav:not(.is-open) { display: none }` at ≤ 900px guards the mobile closed state even if JS is delayed, so there is no FOUC and no exposed closed-menu nav list in the accessibility tree.
- Changes made in this pass:
  - `styles.css`: consolidated two adjacent `.nav-toggle { ... }` blocks into one rule (display plus all other properties). Cosmetic cleanup only; no behavioral change.
  - `index.html` (Korean dictionary only):
    - `heroTitle` (ko): dropped colloquial "그리고"; the clean comma-enumerated list reads more professional.
    - `workCard1Desc` (ko): removed the adjacent "가능한 / 가능한" repetition by rephrasing "재현 가능한 출력 생성을 위한 재사용 가능한" to "재현 가능한 출력을 지원하는 재사용성 높은".
    - `workCard3Desc` (ko): replaced stiff literal "감사 대응 가능한" with more natural "감사에 활용 가능한" for "audit-ready comparison reports".
  - English and Khmer dictionaries: no changes required. English copy is already concise and restrained; Khmer wording preserves official institution names and standard technical terms per instruction.
- Verification performed:
  - `index.html` contains exactly one `<nav>` and one `.nav-list`.
  - No references to `desktop-nav`, `mobile-nav`, or `mobileMenuAria` remain in `index.html` or `styles.css`.
  - All `data-i18n` keys used in markup exist in all three translation dictionaries (spot-checked nav keys, hero, work cards, timeline, awards, research, privacy, footer).
  - Theme toggle, language toggle, section anchors, and responsive breakpoint logic were left untouched.
  - Could not verify: live headless-browser rendering across viewports (Edge blocked by sandbox crashpad permissions in this environment, same as the prior run).
- Final verdict: ACCEPTED. Nav refactor is correct and maintainable; translation quality is now consistent and professionally phrased across all three languages.

## Visual Refinement Pass — Dark Palette and Footer Alignment

### Start entry
- Date/time: 2026-04-17 (current session)
- Scope: refine dark-mode palette from blue-heavy navy to neutral slate/charcoal, and correct footer alignment coherence without redesigning structure or content.
- Files in scope: `styles.css` (primary), `index.html` (audit only), `plan.md`.

### Completion entry
- Date/time: 2026-04-17 (current session, same sitting)
- Issue A findings (dark mode):
  - Existing dark tokens were strongly blue (`#0f1520`, `#161f2f`, `#2c3a52`, bright blue accent), making page/background/surfaces too hue-adjacent and less professional.
  - Secondary text and muted hierarchy were not separated enough for restrained dark readability.
- Issue A fixes applied (`styles.css`):
  - Replaced dark palette tokens with a neutral slate/charcoal system:
    - `--bg: #0b0d10`, `--surface: #11151a`, `--surface-raised: #161b22`, `--border: #232a33`
    - `--text: #e6edf3`, `--text-secondary: #a9b4c0`, `--muted: #7d8896`
    - `--accent: #6aa0ff`, `--accent-hover: #8ab4ff`, `--accent-rgb: 106, 160, 255`
    - chip tokens: `--chip-bg: rgba(106, 160, 255, 0.08)`, `--chip-border: rgba(106, 160, 255, 0.22)`
  - Added tokenized header/overlay backgrounds (`--header-bg`, `--overlay-bg`) and applied them to sticky header/mobile nav for clearer separation from page background.
  - Updated tags/chips to low-contrast filled pills with restrained borders via shared chip tokens.
  - Tuned secondary text usage on cards/timeline/supporting metadata to improve hierarchy and reduce harshness.
- Issue B findings (footer alignment):
  - Footer blocks used inconsistent vertical spacing contracts (`contact-links`, privacy note, and bottom row each with independent offsets), making alignment feel optically off.
  - Bottom row used `justify-content: space-between` with a single content group, which created an unintentional layout signal.
- Issue B fixes applied (`styles.css`):
  - Unified footer alignment flow with `.site-footer .container` as a single left-aligned vertical stack.
  - Removed offset margins from `.contact-links` and `.footer-privacy-note` and used consistent container-driven spacing.
  - Made `.footer-bottom` full-width but left-anchored (`justify-content: flex-start`) with preserved responsive behavior.
  - Allowed `.footer-controls` to wrap cleanly and stay aligned across narrow widths.
- Verification summary:
  - Desktop and mobile footer layout rules now share one coherent left edge and spacing contract.
  - Dark palette tokens now read neutral dark/slate rather than navy-blue, with clearer surface/header separation.
  - Light mode token values and page structure were kept intact.
