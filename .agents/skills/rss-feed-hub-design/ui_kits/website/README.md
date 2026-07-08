# UI Kit — rss.tedt.org website

Interactive recreation of the RSS Feed Hub site in the Swiss system. Three screens, navigable from the top bar (state persists in localStorage):

- **Home** — masthead + one `FeedCard` per enabled feed with entry previews (priority/tech badges as on the live homepage)
- **RSS Feeds** — directory grid with copy-ready URLs, health status, Top Stories Manager callout, "How to Use RSS Feeds"
- **About** — prose column (How It Works, Priority Badges, Technical Details) + navy Quick Stats sidebar

Content is real: feed registry from `_config.yml`, status numbers from `api/rss_status.json` (2026-07-07 snapshot), entry rows in the pipeline's title-marker shape. Sample data lives in `data.js` (`window.RSSHUB_DATA`).

Composes the published components (`FeedCard`, `FormatButton`, `SectionHeader`, `StatusPill`, `FeedItem`, `Badge`, `Tag`, `Button`, `Input`) — chrome (NavBar/Masthead/Footer) is kit-local in `Chrome.jsx`.
