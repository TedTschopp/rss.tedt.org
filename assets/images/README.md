# RSS Feed Hub Images

This directory contains images used by the Jekyll site:

- `favicon.svg` - Primary browser favicon
- `favicon.ico` - Legacy browser favicon fallback
- `favicon-16x16.png` / `favicon-32x32.png` - PNG favicon fallbacks
- `apple-touch-icon.png` - iOS home screen icon (180x180)
- `icon-192.png` / `icon-512.png` - Web manifest icons
- `logo.png` - Site logo used in navigation and structured metadata
- `social-card.png` - Open Graph and Twitter preview image

## Creating Custom Images

To replace these placeholder images:

1. **Social Card**: Create a 1.9:1 preview image named `social-card.png`
2. **Logo**: Create a square or compact transparent PNG named `logo.png`
3. **Favicons**: Update `favicon.svg`, `favicon.ico`, and PNG fallbacks together
4. **App Icons**: Update `apple-touch-icon.png`, `icon-192.png`, and `icon-512.png`

## SVG Icons Alternative

For better scalability, consider using SVG icons instead of PNG files. Update the references in `_config.yml` and `_layouts/default.html` accordingly.
