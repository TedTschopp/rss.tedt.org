Feed-format download buttons in the fixed brand colors (RSS 2.0 orange, RSS 1.0 light orange, Atom purple, JSON dark→gold). `FormatGroup` renders a feed's whole format row.

```jsx
<FormatGroup formats={{ rss2: "/ai_rss_feed.xml", rss1: "/ai_rss_feed_rss1.xml", atom: "/ai_rss_feed.atom", json: "/ai_rss_feed.json" }} />
<FormatButton format="json" href="/feeds/top.json" size="md" />
```

- Format colors are brand-fixed — never reuse them for anything else.
- JSON inlines the site's SVG glyph (no FA equivalent); others need FA 6 CDN.
