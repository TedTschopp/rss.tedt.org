Fixed-vocabulary badge for entry priority ([ ! ] → Essential), technical impact ([ ⬢ ] → Tech: Transformational) and feed health (healthy/warning).

```jsx
<Badge kind="essential" />
<Badge kind="tech-transformational" />
<Badge kind="healthy">healthy</Badge>
```

- Kinds: `essential | important | optional | tech-informational | tech-important | tech-transformational | healthy | warning | unknown`.
- Labels are fixed vocabulary — omit `children` to get the canonical label.
- Colors are verbatim live-site values; never invent new badge kinds.
