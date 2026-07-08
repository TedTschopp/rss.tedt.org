Flat square button for all actions; use `primary` (solid navy) for the main action, `outline` for secondary, `outline-accent` sparingly for orange emphasis.

```jsx
<Button variant="primary" icon="fas fa-rss">Subscribe</Button>
<Button variant="outline" size="sm" href="/feeds/">All feeds</Button>
```

- Variants: `primary`, `accent`, `outline`, `outline-accent`, `outline-ink`, `ghost`. Outlines fill with their border color on hover (live-site behavior).
- Sizes `sm | md | lg`. `icon` takes a Font Awesome class (load FA 6 CDN).
- For feed-format buttons (RSS 2.0 / Atom / JSON) use `FormatButton` instead — never recolor `Button` to a format color.
