# SKILL: Yesterday in AI design system

Use this when designing for **Yesterday in AI**, a daily editorial product covering enterprise AI news.

## Where to start

1. **Read `README.md` at the project root.** It contains the full brand brief — voice, visual foundations, color, type, motion, iconography. Don't skip it.
2. **Load `colors_and_type.css`** from any HTML file you create. It defines all design tokens (color, type, spacing, radius, shadow, motion). Reference tokens via CSS custom properties — never hard-code colors or font stacks.
3. **Reuse the components in `ui_kits/`** before building from scratch. There are three kits:
   - `ui_kits/website/` — daily homepage (Header, Masthead, TLDR, SectionHeader, StoryCard, QuickHits, LookingAhead, SubscribeBlock, Footer)
   - `ui_kits/article/` — story detail (ArticleHeader, ArticleHero, ArticleBody, RelatedStrip)
   - `ui_kits/email/` — newsletter (InboxFrame, EmailHeader, EmailMasthead, EmailTLDR, EmailStory, EmailQuickHits, EmailLookingAhead, EmailSignoff, EmailFooter)
4. **Use shared sample data** from `ui_kits/_shared/data.js` (`window.YIA_DATA`) so new screens stay in voice without inventing copy.

## Non-negotiables

- **No emoji.** Use mono glyphs (`→`, `↗`, `·`) for typographic accents.
- **Sentence case for headlines.** Eyebrows are uppercase mono, tracked.
- **One accent color** (`--accent`, burnt sienna). It's for links, the dateline accent, and the source caret. Never as a fill behind text.
- **Hairline rules over shadows.** Default cards are bordered, not shadowed.
- **No gradients, no patterns, no stock photography.** Warm paper background only.
- **Lucide icons** (CDN) at 1.5px stroke. See `README.md` → Iconography for the canonical set.
- **No bouncy / spring motion.** 120–320ms transitions on `--ease`; collapse to 0ms under `prefers-reduced-motion`.

## Editorial story shape

Every story below the TL;DR follows this pattern:

```
Headline (sentence case, ≤12 words)
Why it matters (1–2 sentences, plain prose)
As a leader: <one sentence>
As an individual: <one sentence>
Source: Publisher · short link
```

When mocking new content, follow this. The `StoryCard` component renders it; sample data demonstrates voice.

## Layout widths

| Token | Value | Use |
|---|---|---|
| `--w-prose` | 680px | Article body, max measure |
| `--w-page` | 1200px | Homepage container |
| `--w-wide` | 1440px | Reserved for marketing pages |
| `--w-email` | 720px | Newsletter |

## When something is missing

- No icon? Pick the closest Lucide and flag the substitution.
- No image? Use type — a large numeric pull-quote or a mono-labeled chart. Don't generate art.
- No copy? Pull from `_shared/data.js` rather than inventing. If you must invent, follow the voice rules in README → Content Fundamentals.

## When in doubt

This system is closer to **Stratechery** than to **a tech company landing page**. Strong typographic hierarchy, generous reading width, restraint everywhere, one warm accent doing all the signaling work. If a design choice feels playful, ornamental, or "fun," it is probably wrong for this brand.
