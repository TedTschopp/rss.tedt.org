# RSS Feed Hub — Design System

A **Swiss-inspired** (International Typographic Style) design system for **RSS Feed Hub** (https://rss.tedt.org/) — Ted Tschopp's personal news-aggregation site. The site collects news from many sources (AI labs, Hacker News, Reddit, arXiv, newsletters, enterprise-architecture blogs), runs it through a GitHub Actions + Python pipeline with optional LLM enrichment, and republishes it as unified RSS/Atom/JSON feeds with health monitoring.

**One product, one surface:** the Jekyll website (home, feeds directory, about, status). The feeds themselves are the payload; the site is a typographic directory of them.

## Sources

- **Live site:** https://rss.tedt.org/
- **GitHub repo (site + pipeline):** https://github.com/TedTschopp/rss.tedt.org — key files: `_layouts/default.html` (all live CSS), `index.html`, `feeds.html`, `about.md`, `_config.yml` (feed registry), `api/rss_status.json` (health data shape)
- **Uploaded brand assets:** `uploads/` → copied to `assets/` (logo, favicons, social card)
- **Prior art in repo:** `.agents/skills/time-in-topic-design-system/` — an editorial design system for "Yesterday in AI" (a *different* product concept: serif, burnt-sienna). Referenced for conventions only; this system is its Swiss counterpart for the Hub itself.

Explore the repo further to ground new designs — the real pages and the status JSON are the ground truth for content and data shapes.

## The Swiss direction

The existing site is Bootstrap 5 + Inter with a warm paper background and a strong flat palette (navy / orange / cyan — the same triad as the logo). This system keeps **every color from the live code verbatim** and re-houses them in International-Typographic-Style clothing:

- One grotesque family at many weights (Archivo), one mono for data (IBM Plex Mono)
- Exposed grid, hairline rules, flush-left ragged-right, square corners
- Flat surfaces — borders instead of shadows
- Big, confident type scale; uppercase mono eyebrows for wayfinding
- Orange plays the classic "Swiss red" accent role; navy is the structural brand color

## Content fundamentals

**Voice:** plain, functional, service-manual. The site explains itself without marketing (“Subscribe to our curated RSS feeds to stay updated…”, “RSS feeds are updated automatically.”). Imperative for instructions (“Copy the RSS feed URL from above”). First person plural sparingly (“our system”), second person for the reader.

**Casing:**
- Page headings are **Title Case** on the live site (“Available Feeds”, “How It Works”, “Feed Status Monitoring”). Keep for page/section headings.
- Feed names are proper nouns, often possessive: “Ted Tschopp's AI News”, “Wes's AI News”, “Top Stories (LLM Aggregated)”, “Enterprise Architecture Aggregated News”, “Broad AI News”.
- Badge vocabulary is fixed: **Essential / Important / Optional** (business priority) and **Tech: Informational / Tech: Important / Tech: Transformational** (technical impact). Badges render uppercase.
- Eyebrows/meta (new in this system): mono, uppercase, tracked — `FEED STATUS`, `50 ENTRIES · UPDATED 2026-07-07`.

**Vocabulary:** “feeds”, “entries”, “sources”, “aggregated”, “curated”, “healthy”, “archive”, “retention”. Format names exactly: **RSS 2.0, RSS 1.0, Atom, JSON**. Timestamps and counts are data — set them in mono.

**Emoji:** none in the product UI (the repo README uses a few; the site does not). Priority symbols `[ ! ] [ * ] [ ~ ]` and tech symbols `[ ◻ ] [ ◼ ] [ ⬢ ]` are *data markers* in feed titles that the UI converts to badges — show the symbols only when documenting the convention.

**Example copy, in voice:**
- “Curated RSS feeds for AI Insights and Technology News” (site description)
- “Cross-source ranked stories with optional GitHub Models enrichment”
- “Merged headlines from configured external sources”
- “Archive not yet created (no items older than 60 days)” (error strings are plain sentences)

## Visual foundations

**Color.** Warm paper `#f8f6f0`, near-black ink `#1f2126`. Brand triad from the logo: navy `#00446f` (structure: nav, footer, primary buttons), orange `#e86027` (the accent — active states, markers, link hover), cyan `#00a9e0` (info only). Status: success `#00b339`, warning `#f2bc57`, danger `#f90041`. Feed-format colors are brand-fixed and never repurposed: RSS 2.0 `#FF6600`, RSS 1.0 `#F88920`, Atom `#8b5cf6`, JSON `#292929` (+ gold `#f5a623` hover). Priority-badge colors verbatim from live code: `#dc3545` / `#ffc107` / `#6c757d`; tech badges `#676869` / `#00446f` / `#00a9e0`. Large fields of navy are welcome (footer, masthead blocks); orange is used small and sharp.

**Type.** One grotesque: **Archivo** (400–900) — SUBSTITUTE for Helvetica/Univers; the live site uses Inter, kept as fallback in the stack. Data voice: **IBM Plex Mono** (timestamps, URLs, counts, eyebrows, status). Display is black-weight (900), tight (−0.02em), often uppercase, set solid (0.95). Body 16/1.6 as on the live site. Scale: 11 · 12 · 14 · 16 · 18 · 21 · 28 · 36 · 48 · 64 · 88.

**Spacing & grid.** 4px base, big jumps (…48 · 64 · 96 · 128). Page 1200px, prose 680px, 24px gutters. The grid is visible: columns of hairline-ruled content, section headers spanning the full measure.

**Backgrounds & imagery.** Flat paper only — no gradients, no textures, no patterns, no photography. The only image assets are the logo/icon family and the social card. Charts and “imagery” are typographic: big mono numbers, rules, flat color blocks.

**Borders & rules.** Hairlines `#c8c7c3` (1px) divide everything; 2px ink `#1f2126` rules announce sections (top rule above section headers); 3px colored left-bars mark priority rows (from live `.rss-items`). Border-first, always.

**Radii.** Square. `0px` on cards, buttons, inputs. The single exception: badges keep the live 3px. No pills.

**Shadows.** None on cards or buttons (flat + bordered). One overlay shadow (`0 .5rem 1rem rgba(7,9,15,.15)`, from the live hover) reserved for menus/modals.

**Hover & press.** Links: navy → orange, underline 1px → 2px. Outline buttons fill with their border color (existing site behavior). Solid buttons darken one step (navy → `#003354`). Press: darken again; no transforms, no scaling. Rows: background tints to `#e5e3dc`-subtle or border strengthens to ink. Focus: 2px orange outline, offset 2px, `:focus-visible` only.

**Motion.** 120ms (hover) / 200ms (open) on `cubic-bezier(0.2,0,0,1)`. No bounces, no springs, no parallax. Collapses to 0ms under `prefers-reduced-motion`.

**Transparency & blur.** Not used. Surfaces are opaque; the one allowance is a sticky header at ~97% paper if needed.

**Cards.** White `#ffffff` on paper, 1px hairline border, square, no shadow, 24px padding. Hover: border strengthens to ink. Feed cards lead with a mono index number and a 2px top rule.

## Iconography

- **Icon system: Font Awesome 6 Free** (the live site's system), via CDN: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css`. Solid style. Canonical glyphs used by the product: `fa-rss`, `fa-atom`, `fa-copy`, `fa-check`, `fa-check-circle`, `fa-exclamation-triangle`, `fa-github` (brands), `fa-question-circle`, `fa-info-circle`, `fa-chart-line`, `fa-link`, `fa-file-code`.
- **JSON Feed icon:** Font Awesome has none; the site uses an inline SVG path — copied verbatim to `assets/json.svg` (also inlined inside the `FormatButton` component). Do not redraw it.
- Icons are small and functional (1em, inline with labels), never decorative heroes. Color inherits `currentColor`.
- **Unicode-as-data:** `[ ! ] [ * ] [ ~ ] [ ◻ ] [ ◼ ] [ ⬢ ]` appear in raw feed titles and are converted to badges by the UI.
- **No emoji. No hand-drawn SVGs.**
- **Logo:** `assets/logo.png` — navy rounded square, white RSS ring, cyan + orange satellite nodes (hub-and-spoke). Also `favicon.svg`, `icon-512.png`, `apple-touch-icon.png`, `social-card.png` (1.9:1 OG image). Use the PNG at 32px in nav; don't recolor or redraw it.

## Index

| Path | What it is |
|---|---|
| `readme.md` | This file — brand brief + manifest |
| `styles.css` | Global CSS entry (imports everything under `tokens/`) |
| `tokens/colors.css` | Full palette + semantic aliases |
| `tokens/typography.css` | Families, scale, weights, tracking (+ Google Fonts import) |
| `tokens/layout.css` | Spacing, radii, borders, shadow, widths, motion |
| `tokens/base.css` | Base element styles + `.h1…`, `.eyebrow`, `.meta` classes |
| `assets/` | Logo family, social card, `json.svg` |
| `guidelines/` | Specimen cards for the Design System tab |
| `components/core/` | `Button`, `Badge`, `Tag`, `Input` |
| `components/feeds/` | `FormatButton`, `SectionHeader`, `FeedItem`, `FeedCard`, `StatusPill` |
| `ui_kits/website/` | rss.tedt.org rebuilt in the system — interactive home / feeds / about |
| `SKILL.md` | Agent-skill manifest |

### Component inventory (source-derived)

No component library exists in the source (plain Bootstrap classes), so this inventory maps 1:1 to UI patterns found in the live pages: buttons + outline format buttons (`index.html`, `feeds.html`), priority/tech badges (`index.html`), feed cards with format groups + preview lists (`index.html`, `feeds.html`), status line (`feeds.html` + `api/rss_status.json`), section headers (`.section-title`), copy-URL input group (`feeds.html`), category tags (`sources.yml` categories). **Intentional additions:** none.

## Caveats

- **Fonts are substitutes:** Archivo ≈ Helvetica/Univers register (live site ships Inter — kept in the fallback stack). IBM Plex Mono is new (the data voice). Both load from Google Fonts CDN; no font binaries ship with this system.
- Derived tints (`--navy-100`, `--orange-100`, `--ink-100`, `--ink-400`, hover steps `#003354`/`#c94d1a`) are the only non-source colors; each is marked `(derived)` in `tokens/colors.css`.
- The live badge colors (`#dc3545`, `#ffc107`, `#6c757d`) are Bootstrap defaults that differ from the theme's own `--danger #f90041` / `--warning #f2bc57`; the system keeps both and documents the split rather than reconciling it.
