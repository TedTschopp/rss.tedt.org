Square text input; `copyable` turns it into the feed-URL copy group (mono readonly field + Copy → green "Copied!" for 2s).

```jsx
<Input label="Feed URL" copyable defaultValue="https://rss.tedt.org/ai_rss_feed.xml" />
<Input placeholder="Search feeds" />
```

- `label` renders as a mono uppercase eyebrow.
- Copy button needs Font Awesome 6 CDN for its icons.
