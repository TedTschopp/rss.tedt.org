import React from "react";

/**
 * Category tag — mono, hairline-bordered, square. For source categories
 * (AI Labs, Reddit, arXiv…) and feed facets. Quiet by default; `active`
 * fills navy.
 */
export function Tag({ active = false, onClick, children, style }) {
  const [hover, setHover] = React.useState(false);
  const interactive = typeof onClick === "function";
  return (
    <span
      onClick={onClick}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        display: "inline-block",
        fontFamily: "var(--font-mono)",
        fontSize: "var(--fs-11)",
        fontWeight: 500,
        letterSpacing: "0.04em",
        textTransform: "uppercase",
        padding: "3px 8px",
        background: active ? "var(--navy-500)" : hover && interactive ? "var(--ink-100)" : "transparent",
        color: active ? "#fff" : "var(--text-muted)",
        border: `1px solid ${active ? "var(--navy-500)" : "var(--border)"}`,
        cursor: interactive ? "pointer" : "default",
        transition: "background var(--dur-1) var(--ease), color var(--dur-1) var(--ease)",
        userSelect: "none",
        whiteSpace: "nowrap",
        ...style,
      }}
    >
      {children}
    </span>
  );
}
