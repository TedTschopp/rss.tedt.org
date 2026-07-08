---
name: rss-feed-hub-design
description: Use this skill to generate well-branded interfaces and assets for RSS Feed Hub (rss.tedt.org), either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping.
user-invocable: true
---

Read the README.md file within this skill, and explore the other available files.

Quick orientation:
- `readme.md` — brand brief: Swiss direction, content voice, visual foundations, iconography rules
- `styles.css` — link this one file to get every token (colors, type, spacing, motion)
- `components/` — React primitives (Button, Badge, Tag, Input, FormatButton, SectionHeader, FeedItem, FeedCard, StatusPill); each has a `.prompt.md` usage note
- `ui_kits/website/` — the full site rebuilt (home / feeds / about) with real content shapes
- `assets/` — logo family, favicon, social card, JSON feed glyph

Non-negotiables: colors come from the tokens (they're verbatim from the live site — never invent new ones); square corners; hairline rules over shadows; Archivo + IBM Plex Mono; Font Awesome 6 icons; no emoji, no gradients, no photography. Feed-format colors (RSS 2.0 / RSS 1.0 / Atom / JSON) and badge vocabulary (Essential / Important / Optional, Tech: …) are fixed.

If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.

If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.
