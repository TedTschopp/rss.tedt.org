# Email newsletter UI kit

The 6 a.m. ET daily, designed as it would appear in a desktop mail client.

## Files
- `index.html` — interactive email mock (in an inbox-style frame).
- `Components.jsx` — `InboxFrame`, `EmailHeader`, `EmailMasthead`, `EmailTLDR`, `EmailStory`, `EmailQuickHits`, `EmailLookingAhead`, `EmailSignoff`, `EmailFooter`.

## Design notes
- Width capped at **720px** (`--w-email`) — single-column, no rail.
- Section eyebrows + accent rules carry over from the website. Type scale is one step smaller across the board.
- The dark "Looking ahead" block is full-bleed inside the email (`margin: 32px -28px 0`), echoing the website's inverted block.
- Footer is centered (the only place we deviate from left-align in the system) — this is an email convention readers expect, and breaking it draws the wrong kind of attention.

## Note on send-readiness
This is a **design mockup**, not a sendable HTML email. It uses CSS Grid, system fonts via custom properties, etc. Translating to a sendable template (tables, inlined styles, system-font fallbacks) is a separate engineering pass — but the visual targets are here.
