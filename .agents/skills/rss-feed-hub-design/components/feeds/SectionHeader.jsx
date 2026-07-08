import React from "react";

/**
 * Swiss section header: 2px ink rule on top, mono eyebrow, bold title,
 * optional meta/action on the right baseline.
 */
export function SectionHeader({ eyebrow, title, meta, action, style }) {
  return (
    <header
      style={{
        borderTop: "var(--bw-rule) solid var(--border-strong)",
        paddingTop: "var(--sp-3)",
        display: "flex",
        alignItems: "flex-end",
        justifyContent: "space-between",
        gap: "var(--sp-4)",
        flexWrap: "wrap",
        ...style,
      }}
    >
      <div>
        {eyebrow ? (
          <div style={{
            fontFamily: "var(--font-mono)",
            fontSize: "var(--fs-12)",
            fontWeight: 500,
            letterSpacing: "var(--tr-eyebrow)",
            textTransform: "uppercase",
            color: "var(--accent)",
            marginBottom: "4px",
          }}>{eyebrow}</div>
        ) : null}
        <h2 style={{
          fontFamily: "var(--font-sans)",
          fontWeight: 700,
          fontSize: "var(--fs-28)",
          lineHeight: "var(--lh-tight)",
          letterSpacing: "var(--tr-tight)",
          color: "var(--text-heading)",
          margin: 0,
        }}>{title}</h2>
      </div>
      {meta ? (
        <span style={{
          fontFamily: "var(--font-mono)",
          fontSize: "var(--fs-12)",
          color: "var(--text-muted)",
          paddingBottom: "4px",
        }}>{meta}</span>
      ) : null}
      {action || null}
    </header>
  );
}
