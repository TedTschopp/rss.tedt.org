Single feed-entry row with priority/tech badges, title link and mono pubdate; prioritized entries get the tinted row + 3px left bar.

```jsx
<FeedItem
  title="OpenAI raises $122 billion in new funding"
  href="https://openai.com/"
  date="2026-07-07"
  priority="essential"
  tech="transformational"
/>
```

- `priority`: essential | important | optional (from `[ ! ] [ * ] [ ~ ]` title markers).
- `tech`: transformational | important | informational (from `[ ⬢ ] [ ◼ ] [ ◻ ]`).
- Stack rows in a plain column with 4px gap; no dividers between entries.
