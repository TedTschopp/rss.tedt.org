The site's central object — a complete feed card with index, name, description, format buttons, copy-URL group, health line and entries preview.

```jsx
<FeedCard
  index={1}
  name="Ted Tschopp's AI News"
  description="Latest AI News and Ratings from Ted Tschopp"
  url="https://rss.tedt.org/ai_rss_feed.xml"
  formats={{ rss2: "/ai_rss_feed.xml", rss1: "/ai_rss_feed_rss1.xml", atom: "/ai_rss_feed.atom", json: "/ai_rss_feed.json" }}
  status={{ health: "healthy", entries: 50, updated: "2026-07-07" }}
  items={[{ title: "OpenAI raises $122B", date: "2026-07-07", priority: "essential" }]}
/>
```

- All sub-blocks are optional — omit `items` for a compact directory card.
- Composes FormatGroup, Input (copyable), StatusPill, FeedItem; don't rebuild those inline.
