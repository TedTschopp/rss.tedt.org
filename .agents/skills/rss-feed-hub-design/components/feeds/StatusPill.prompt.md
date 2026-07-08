Feed-health chip (healthy green / warning amber / unknown gray / external cyan) with mono entry-count + updated meta.

```jsx
<StatusPill status="healthy" entries={50} updated="2026-07-07" />
```

- Health rule from the live site: `exists && valid_xml` → healthy, else warning.
- Needs Font Awesome 6 CDN for the status icons.
