import React from "react";

const JSON_GLYPH_PATH = "M213.333333 128h85.333334v85.333333H213.333333v213.333334a85.333333 85.333333 0 0 1-85.333333 85.333333 85.333333 85.333333 0 0 1 85.333333 85.333333v213.333334h85.333334v85.333333H213.333333c-45.653333-11.52-85.333333-38.4-85.333333-85.333333v-170.666667a85.333333 85.333333 0 0 0-85.333333-85.333333H0v-85.333334h42.666667a85.333333 85.333333 0 0 0 85.333333-85.333333V213.333333a85.333333 85.333333 0 0 1 85.333333-85.333333m597.333334 0a85.333333 85.333333 0 0 1 85.333333 85.333333v170.666667a85.333333 85.333333 0 0 0 85.333333 85.333333h42.666667v85.333334h-42.666667a85.333333 85.333333 0 0 0-85.333333 85.333333v170.666667a85.333333 85.333333 0 0 1-85.333333 85.333333h-85.333334v-85.333333h85.333334v-213.333334a85.333333 85.333333 0 0 1 85.333333-85.333333 85.333333 85.333333 0 0 1-85.333333-85.333333V213.333333h-85.333334V128h85.333334m-298.666667 512a42.666667 42.666667 0 0 1 42.666667 42.666667 42.666667 42.666667 0 0 1-42.666667 42.666666 42.666667 42.666667 0 0 1-42.666667-42.666666 42.666667 42.666667 0 0 1 42.666667-42.666667m-170.666667 0a42.666667 42.666667 0 0 1 42.666667 42.666667 42.666667 42.666667 0 0 1-42.666667 42.666666 42.666667 42.666667 0 0 1-42.666666-42.666666 42.666667 42.666667 0 0 1 42.666666-42.666667m341.333334 0a42.666667 42.666667 0 0 1 42.666666 42.666667 42.666667 42.666667 0 0 1-42.666666 42.666666 42.666667 42.666667 0 0 1-42.666667-42.666666 42.666667 42.666667 0 0 1 42.666667-42.666667z";

const FORMATS = {
  rss2: { label: "RSS 2.0", color: "var(--format-rss2)", hoverFg: "#fff", icon: "fas fa-rss" },
  rss1: { label: "RSS 1.0", color: "var(--format-rss1)", hoverFg: "#fff", icon: "fas fa-rss" },
  atom: { label: "Atom",    color: "var(--format-atom)", hoverFg: "#fff", icon: "fas fa-atom" },
  json: { label: "JSON",    color: "var(--format-json)", hoverFg: "var(--format-json-gold)", icon: null },
};

/**
 * Outline button in the fixed syndication-format brand color; fills with
 * that color on hover (JSON flips text to gold — live-site behavior).
 * JSON has no Font Awesome glyph, so it inlines the site's SVG path.
 */
export function FormatButton({ format = "rss2", href = "#", size = "sm", style }) {
  const [hover, setHover] = React.useState(false);
  const f = FORMATS[format] || FORMATS.rss2;
  const dims = size === "sm"
    ? { font: "var(--fs-12)", pad: "4px 10px" }
    : { font: "var(--fs-14)", pad: "8px 14px" };

  return (
    <a
      href={href}
      target={"feed_" + format}
      rel="noopener"
      title={f.label}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "6px",
        fontFamily: "var(--font-mono)",
        fontSize: dims.font,
        fontWeight: 500,
        lineHeight: 1.2,
        padding: dims.pad,
        background: hover ? f.color : "transparent",
        color: hover ? f.hoverFg : f.color,
        border: `1px solid ${f.color}`,
        borderRadius: "var(--r-0)",
        textDecoration: "none",
        transition: "background var(--dur-1) var(--ease), color var(--dur-1) var(--ease)",
        whiteSpace: "nowrap",
        ...style,
      }}
    >
      {f.icon ? (
        <i className={f.icon} aria-hidden="true" style={{ fontSize: "0.9em" }}></i>
      ) : (
        <svg viewBox="0 0 1024 1024" width="1em" height="1em" fill="currentColor" aria-hidden="true" style={{ display: "block" }}>
          <path d={JSON_GLYPH_PATH} />
        </svg>
      )}
      {f.label}
    </a>
  );
}

/** Row of format buttons for a feed's available formats, in canonical order. */
export function FormatGroup({ formats, size = "sm", style }) {
  const order = ["rss2", "rss1", "atom", "json"];
  return (
    <span style={{ display: "inline-flex", gap: "4px", flexWrap: "wrap", ...style }}>
      {order.filter((k) => formats && formats[k]).map((k) => (
        <FormatButton key={k} format={k} href={formats[k]} size={size} />
      ))}
    </span>
  );
}
