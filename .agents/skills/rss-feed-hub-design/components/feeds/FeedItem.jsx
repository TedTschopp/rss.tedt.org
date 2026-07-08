import React from "react";
import { Badge } from "../core/Badge.jsx";

const PRI_ROW = {
  essential: { bg: "rgba(220,53,69,.08)",  bar: "rgba(220,53,69,.6)" },
  important: { bg: "rgba(255,193,7,.12)",  bar: "rgba(255,193,7,.7)" },
  optional:  { bg: "rgba(108,117,125,.10)", bar: "rgba(108,117,125,.55)" },
};

/**
 * One feed entry: optional priority/tech badges, title link, mono date.
 * Prioritized rows get the live site's tint + 3px left bar.
 */
export function FeedItem({ title, href = "#", date, priority, tech, style }) {
  const [hover, setHover] = React.useState(false);
  const row = priority ? PRI_ROW[priority] : null;

  return (
    <div
      style={{
        display: "flex",
        alignItems: "baseline",
        gap: "8px",
        padding: row ? "4px 6px" : "4px 0",
        background: row ? row.bg : "transparent",
        borderLeft: row ? `var(--bw-bar) solid ${row.bar}` : "var(--bw-bar) solid transparent",
        lineHeight: 1.35,
        ...style,
      }}
    >
      <span style={{ flex: 1, minWidth: 0 }}>
        {priority ? <Badge kind={priority} style={{ marginRight: "6px", position: "relative", top: "-1px" }} /> : null}
        {tech ? <Badge kind={"tech-" + tech} style={{ marginRight: "6px", position: "relative", top: "-1px" }} /> : null}
        <a
          href={href}
          rel="noopener noreferrer"
          onMouseEnter={() => setHover(true)}
          onMouseLeave={() => setHover(false)}
          style={{
            color: hover ? "var(--accent)" : "var(--text-heading)",
            fontWeight: 600,
            fontSize: "var(--fs-14)",
            textDecoration: hover ? "underline" : "none",
            textUnderlineOffset: "0.15em",
            transition: "color var(--dur-1) var(--ease)",
          }}
        >
          {title}
        </a>
      </span>
      {date ? (
        <span style={{
          fontFamily: "var(--font-mono)",
          fontSize: "0.65rem",
          color: "var(--text-muted)",
          flex: "none",
        }}>({date})</span>
      ) : null}
    </div>
  );
}
