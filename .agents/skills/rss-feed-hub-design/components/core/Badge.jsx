import React from "react";

const BADGE_KINDS = {
  essential:                { bg: "var(--pri-essential)", fg: "#fff", label: "Essential" },
  important:                { bg: "var(--pri-important)", fg: "var(--pri-important-ink)", label: "Important" },
  optional:                 { bg: "var(--pri-optional)",  fg: "#fff", label: "Optional" },
  "tech-informational":     { bg: "var(--tech-informational)",    fg: "#fff", label: "Tech: Informational" },
  "tech-important":         { bg: "var(--tech-important)",        fg: "#fff", label: "Tech: Important" },
  "tech-transformational":  { bg: "var(--tech-transformational)", fg: "#fff", label: "Tech: Transformational" },
  healthy:                  { bg: "var(--success)", fg: "#fff", label: "Healthy" },
  warning:                  { bg: "var(--warning)", fg: "var(--warning-ink)", label: "Warning" },
  unknown:                  { bg: "var(--pri-optional)", fg: "#fff", label: "Unknown" },
};

/**
 * Priority / tech-impact / status badge. Styling verbatim from the live
 * site's .pri-badge: uppercase, 0.60rem, 600, 3px radius.
 */
export function Badge({ kind = "optional", children, style }) {
  const k = BADGE_KINDS[kind] || BADGE_KINDS.optional;
  return (
    <span
      style={{
        display: "inline-block",
        fontFamily: "var(--font-sans)",
        fontSize: "0.60rem",
        letterSpacing: "var(--tr-badge)",
        textTransform: "uppercase",
        padding: "2px 5px",
        borderRadius: "var(--r-1)",
        fontWeight: 600,
        background: k.bg,
        color: k.fg,
        lineHeight: 1.4,
        whiteSpace: "nowrap",
        ...style,
      }}
    >
      {children || k.label}
    </span>
  );
}
