/* Shared brand wordmark — renders as HTML, not SVG, so loaded webfonts apply. */
function Wordmark({ height = 28, color = "var(--fg)", accent = "var(--accent)" }) {
  const scale = height / 28;
  return (
    <span aria-label="Yesterday in AI" role="img" style={{
      display: "inline-flex",
      alignItems: "baseline",
      gap: 8 * scale,
      lineHeight: 1,
      whiteSpace: "nowrap",
      color,
    }}>
      <span style={{
        fontFamily: "var(--font-serif)",
        fontWeight: 700,
        fontSize: 22 * scale,
        letterSpacing: "-0.03em",
      }}>Yesterday</span>
      <span style={{
        display: "inline-block",
        width: 1.5 * scale,
        height: 18 * scale,
        background: accent,
        transform: "rotate(18deg)",
        borderRadius: 1,
      }}></span>
      <span style={{
        fontFamily: "var(--font-sans)",
        fontWeight: 500,
        fontSize: 15 * scale,
        letterSpacing: "-0.01em",
      }}>in AI</span>
    </span>
  );
}
window.Wordmark = Wordmark;
