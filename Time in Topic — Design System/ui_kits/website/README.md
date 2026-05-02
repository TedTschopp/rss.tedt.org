# Website UI kit — Yesterday in AI

The daily reading experience: masthead → TL;DR → ranked sections → Quick Hits → Looking Ahead → Sign-off.

## Files
- `index.html` — interactive homepage. Open this.
- `Components.jsx` — all components (Header, Masthead, TLDR, SectionHeader, StoryCard, QuickHits, LookingAhead, SubscribeBlock, Footer).

## Components

| Component | Purpose |
|---|---|
| `Header` | Sticky top bar with wordmark, nav, search, subscribe CTA. Backdrop-blurred. |
| `Masthead` | Volume number + date + headline + lede for the day's edition. |
| `TLDR` | Numbered, hairline-separated 3–5 bullet summary. Mono numerals in accent color. |
| `SectionHeader` | 2px ink-900 rule + tracked mono eyebrow + serif lede. One per section. |
| `StoryCard` | Headline (serif) + Why-it-matters (serif) + Leader/IC rows (sans, hairline-separated) + Source link. |
| `QuickHits` | Bulleted brief list with arrow-up-right links. |
| `LookingAhead` | Inverted dark block (ink-900) — visual anchor at end of edition. |
| `SubscribeBlock` | Sidebar email capture, single accent eyebrow. |
| `Footer` | Standard editorial footer with column groups and fine print. |

## Layout
Two-column: 1fr article column + 320px sticky rail. Collapses to single column under 900px. Page max 1200px (`--w-page`).

## Notes
- All components reference design tokens from `../../colors_and_type.css`. They will not render correctly without it.
- No emoji anywhere. Source links use `arrow-up-right` from Lucide.
- Sample data from `../_shared/data.js` reflects observed structure of the real feed.
