Mono uppercase category tag for source facets (AI Labs, Hacker News, Reddit, arXiv, Newsletters) — square, hairline border.

```jsx
<Tag>AI Labs</Tag>
<Tag active onClick={() => setFilter("reddit")}>Reddit</Tag>
```

- `active` fills navy; pass `onClick` to make it a filter chip.
- Not a priority badge — use `Badge` for Essential/Important/Optional.
