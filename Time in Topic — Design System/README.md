# Yesterday in AI — Design System

A daily editorial product covering the AI news that matters in **enterprise AI** from the last 24 hours. Mixed business + technical readership: CTOs, CIOs, ML engineers, AI product managers, and AI-curious operators at Fortune 500s and growth-stage tech companies.

## Source materials

- **Site:** https://tedt.org/Daily-Report/AI/
- **Top stories feed:** https://rss.tedt.org/feeds/top.json
- **Full AI feed:** https://rss.tedt.org/ai_rss_feed.json
- A reference snapshot of feed structure and observed editorial patterns is in `reference/content-sample.md`.

> **Note:** The brand was an unbranded concept when this design system was authored. The visual identity, name treatment, color, and type were designed from scratch to match the editorial product — they should be reviewed against any future Figma direction the user has in mind.

---

## Index

| File / folder | What it is |
|---|---|
| `README.md` | This file. |
| `colors_and_type.css` | All design tokens (color, type, spacing, radius, motion). Drop into any HTML file. |
| `SKILL.md` | Cross-compatible skill manifest for Claude Code. |
| `assets/` | Logos (wordmark + monogram), favicons. |
| `reference/` | Source content snapshot — feed shape, headline examples, editorial voice samples. |
| `preview/` | Self-contained HTML cards for each token group. Rendered by the Design System tab. |
| `ui_kits/website/` | Daily news website UI kit (homepage). React components + interactive `index.html`. |
| `ui_kits/article/` | Story / article detail page UI kit. |
| `ui_kits/email/` | Email newsletter UI kit (designed for the 6 a.m. ET daily send). |
| `ui_kits/_shared/` | Shared sample editorial data (`data.js`) consumed by every UI kit. |

---

## Brand snapshot

- **Name:** Yesterday in AI (always written in full)
- **Wordmark:** Source Serif 4 Bold "Yesterday" + a thin slash + Inter Tight Medium "in AI"
- **Voice:** authoritative, analytical, no hype. Slightly wry on transitions.
- **Tagline (working):** "The AI news that matters, in 5 minutes."

---

## Content fundamentals

### Voice & tone
- **Authoritative, not breathless.** No exclamation points. No "BREAKING." No "🚨".
- **Analytical, not promotional.** We're not selling AI; we're explaining what changed.
- **Mildly wry on transitions** is fine ("clarifying about a week of confusion"). Keep it dry.
- **Specific over vague.** Numbers, names, model versions — never "a major company" when "Wayfair" will do.
- **Second-person where it earns its keep.** "If you run security at a Fortune 500, this is your problem." Avoid first person except in the editorial sign-off.

### Casing
- **Sentence case for headlines.** Not Title Case. "OpenAI raises $122 billion in new funding" — not "OpenAI Raises $122 Billion in New Funding."
- **Section labels are uppercase eyebrows** (mono, tracked, 12px). "ENTERPRISE OPS" / "BIG MOVES" / "POLICY".
- **Product names exactly as the company writes them.** GPT-5.1-Codex-Max, ChatGPT Enterprise, Codex (capitalized).
- **No emoji in editorial copy.** Ever. We use mono glyphs (e.g. `→`, `↗`, `·`) for typographic accents instead.

### Story structure (the canonical pattern)
Every story below the TL;DR must include:
1. **Headline** — declarative, sentence case, ≤ 12 words.
2. **Why it matters** — 1–2 sentence prose paragraph. Plain, factual.
3. **As a leader:** — single sentence, what an exec or decision-maker should do, watch, or decide.
4. **As an individual:** — single sentence, what an IC / practitioner should do.
5. **Source:** — Publisher · short link.

### Vocabulary cheatsheet
- ✅ "ship", "rolled out", "launched", "deprecated", "GA"
- ✅ "leaders", "individuals", "operators", "practitioners"
- ❌ "game-changer", "revolutionary", "leverages", "synergize", "10x"
- ❌ "thought leader", "AI-powered" (as an adjective by itself), "robust"

### Headline examples (real, from feed)
- "Building more with GPT-5.1-Codex-Max"
- "1 million business customers putting AI to work"
- "Mixpanel security incident: what OpenAI users need to know"
- "Wayfair boosts catalog accuracy and support speed with OpenAI"

---

## Visual foundations

### Motif: editorial newspaper, modernized
The visual register is closer to **Stratechery / The Information** than to **a tech company landing page**. Strong typographic hierarchy, generous reading width, hairline rules, and one warm accent color doing all the signaling work.

### Color
- **Warm paper background** (`#FBFAF7`) — not pure white. Sets a printed-page feel and reduces glare on long reads.
- **Ink-900** (`#14110B`) for headlines and max contrast. Not pure black.
- **One accent only:** `signal-500` (`#D9531E`, burnt sienna). Used for links, the dateline accent, the active filter, and the "SOURCE" caret. **Never** as a section background.
- **Section tags** are low-chroma desaturated colors used only inside the small section pill. Never as fills elsewhere.

### Type
- **Display & headlines:** Source Serif 4 (substituting GT Sectra). Tight tracking. -0.03em on display.
- **UI & body:** Inter Tight (substituting Söhne). 16px body, 1.55 line-height.
- **Long-form prose:** Source Serif 4 at 18px, 1.65 line-height — set on `.prose`. Article body uses serif intentionally.
- **Metadata, timestamps, source attributions, eyebrows:** JetBrains Mono. Always uppercase + tracked for eyebrows; lowercase for inline meta.

> **Font substitutions:** We're using the closest free Google Fonts equivalents (Inter Tight ≈ Söhne, Source Serif 4 ≈ GT Sectra, JetBrains Mono ≈ Berkeley Mono). **If you have licensed copies, please drop them into `fonts/` and update `colors_and_type.css`.**

### Spacing & layout
- **4px base.** Tokens go 4 → 8 → 12 → 16 → 20 → 24 → 32 → 40 → 48 → 64 → 80 → 96.
- **Reading column is 680px** (`--w-prose`). The article page never exceeds this for body text — even when the header bleeds full-width.
- **Page max is 1200px** (`--w-page`). Wide layouts (homepage with rail) use 1440px (`--w-wide`).
- Vertical rhythm: section breaks get `--sp-16` (64px) on desktop, `--sp-10` (40px) on mobile.

### Backgrounds & imagery
- **No gradient backgrounds.** None.
- **No hand-drawn illustrations.** None.
- **No repeating patterns or textures** beyond the warm paper color itself.
- **Imagery role: minimal and editorial.** When imagery is used (rare), it's a single full-bleed editorial photo at the top of an article, treated with a slight warm desaturation. Charts are typography-led: large numbers, mono labels, hairline rules — not coloured bar charts.
- **No stock photos of "businesspeople pointing at screens."** If we don't have a real photo, we use type.

### Borders, rules, dividers
- **Hairlines are king.** Use `border-soft` (`var(--ink-100)`) for ambient dividers, `border` (`var(--ink-200)`) for cards, `border-strong` (ink-900) for emphasis dividers above section headers.
- **No box-shadow on cards by default.** Cards on the homepage are bordered, not shadowed. Shadows are reserved for the menu/popover layer (`--shadow-pop`).
- **Section headers** use a 2px solid `--border-strong` rule above the eyebrow.

### Radii
- **Almost square.** `--r-1` (2px) is the default.
- Buttons & inputs: `--r-2` (4px).
- Cards (when used): `--r-3` (8px).
- **Pills only for tags / status,** never for primary buttons.

### Shadows
- `--shadow-1` — single hairline shadow for raised UI (e.g. floating filter bar)
- `--shadow-2` — for menus
- `--shadow-pop` — modals, command palettes
- **Default cards have no shadow** (border only).

### Hover, press, focus states
- **Hover on links:** color goes `--accent` → `--accent-hover` (`#B8410F`); underline thickens from 1px → 2px.
- **Hover on buttons:** background darkens by one step (e.g. `--ink-900` → solid black). No scale transforms.
- **Press on buttons:** `transform: translateY(1px)` + slight color darken (`--accent-press`).
- **Hover on cards:** border goes from `--border` → `--border-strong`; background tints from `--bg` → `--bg-subtle`. No lift, no shadow change.
- **Focus rings:** 2px `--accent` outline with 2px offset. Visible on keyboard nav only (`:focus-visible`).

### Motion
- **Fast and subtle.** `--dur-1` (120ms) for hover state changes. `--dur-2` (200ms) for menu opens. `--dur-3` (320ms) for page transitions.
- **Easing:** `--ease` (`cubic-bezier(0.2, 0.6, 0.2, 1)`) for most things; `--ease-out` for entrances.
- **No bounces, no spring physics, no slide-from-bottom modals.** This is editorial, not playful.
- **Reduced-motion:** all transitions collapse to `0ms` when `prefers-reduced-motion: reduce`.

### Transparency & blur
- Used sparingly. The sticky header on scroll uses `backdrop-filter: blur(8px)` over `rgba(251, 250, 247, 0.85)`. That's it. No frosted-glass cards, no translucent overlays elsewhere.

### Cards
- **Default:** 1px border `--border`, 0 shadow, `--r-3` radius, `--bg-elev` (white) background, `--sp-6` padding.
- **Hover:** border `--border-strong`, background unchanged.
- Story cards on the homepage are flatter still — bordered top + bottom only, no side borders. (See `ui_kits/website`.)

### Iconography vibe
- Stroke icons only, 1.5px stroke weight. **Lucide** via CDN. See `ICONOGRAPHY` below.

---

## Iconography

We use **Lucide Icons** (https://lucide.dev) loaded from CDN. Justification: matches our 1.5px-stroke, geometric, neutral aesthetic; comprehensive set; permissive ISC license; identical visual weight across the whole library.

### Usage
```html
<!-- CDN -->
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>

<!-- in markup -->
<i data-lucide="arrow-up-right"></i>

<script>lucide.createIcons();</script>
```

### Conventions
- **Stroke weight:** always 1.5px (Lucide default).
- **Size:** 16px for inline UI, 20px for buttons, 24px for nav, 32px+ for marketing.
- **Color:** inherits from `currentColor`. Use `--fg-muted` for ambient icons, `--fg` for active, `--accent` only on the source-link arrow (`arrow-up-right`).
- **No emoji** anywhere in the product — including section labels. Ever.
- **No icon-only buttons** without an `aria-label`.

### The icon set we lean on
`arrow-up-right` (source link), `arrow-right` (next), `chevron-down` (menu), `bookmark`, `bookmark-check`, `share-2`, `clock` (read time), `calendar` (date), `mail` (newsletter signup), `search`, `menu`, `x`, `filter`, `external-link`.

### When Lucide doesn't have it
Substitute the closest match and **flag the substitution in code review**. Do not draw custom SVGs unless the brand warrants it (e.g. the wordmark + monogram in `assets/`).

---

## Caveats / open questions

- **Color direction:** Burnt sienna was chosen as a single warm accent. Two alternatives explored briefly but not built into tokens: **electric blue** (`#1E5BD9`, technical/cool register) and **graphite-on-cream** (no chroma at all, B&W with one signal weight). If the burnt sienna feels too editorial, we can swap by changing `--signal-*` values only.
- **Logo:** The wordmark is typographic, no symbol. A monogram lockup (a literal "Y/AI" mark) is provided as an alternate in `assets/`.
- **Font licensing:** Inter Tight, Source Serif 4, and JetBrains Mono are free. The system was *designed* assuming Söhne / GT Sectra / Berkeley Mono — if you license them, swap and the system holds.

