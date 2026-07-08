import React from "react";
import { Input } from "../core/Input.jsx";
import { FormatGroup } from "./FormatButton.jsx";
import { StatusPill } from "./StatusPill.jsx";
import { FeedItem } from "./FeedItem.jsx";

/**
 * The site's central object: one card per feed. Mono index + 2px ink top
 * rule, name, description, format buttons, copy-URL group, health line,
 * and a recent-entries preview. Square, bordered, flat.
 */
export function FeedCard({
  index,
  name,
  description,
  url,
  formats,
  status,
  items = [],
  previewLabel = "Recent Entries",
  style,
}) {
  const [hover, setHover] = React.useState(false);
  return (
    <article
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        background: "var(--surface)",
        border: `1px solid ${hover ? "var(--border-strong)" : "var(--border)"}`,
        borderTop: "var(--bw-rule) solid var(--border-strong)",
        padding: "var(--sp-6)",
        transition: "border-color var(--dur-1) var(--ease)",
        display: "flex",
        flexDirection: "column",
        gap: "var(--sp-4)",
        ...style,
      }}
    >
      <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", gap: "var(--sp-4)", flexWrap: "wrap" }}>
        <div style={{ minWidth: 0 }}>
          {index != null ? (
            <div style={{
              fontFamily: "var(--font-mono)",
              fontSize: "var(--fs-12)",
              color: "var(--accent)",
              marginBottom: "4px",
            }}>{String(index).padStart(2, "0")}</div>
          ) : null}
          <h3 style={{
            fontFamily: "var(--font-sans)",
            fontWeight: 700,
            fontSize: "var(--fs-21)",
            lineHeight: "var(--lh-snug)",
            letterSpacing: "var(--tr-tight)",
            color: "var(--text-heading)",
            margin: 0,
          }}>{name}</h3>
          {description ? (
            <p style={{ fontSize: "var(--fs-14)", color: "var(--text-muted)", margin: "4px 0 0" }}>{description}</p>
          ) : null}
        </div>
        {formats ? <FormatGroup formats={formats} /> : null}
      </div>

      {url ? <Input copyable size="sm" defaultValue={url} /> : null}

      {status ? (
        <StatusPill status={status.health} entries={status.entries} updated={status.updated} />
      ) : null}

      {items.length > 0 ? (
        <div>
          <div style={{
            fontFamily: "var(--font-mono)",
            fontSize: "var(--fs-12)",
            letterSpacing: "var(--tr-eyebrow)",
            textTransform: "uppercase",
            color: "var(--text-muted)",
            borderBottom: "1px solid var(--border)",
            paddingBottom: "6px",
            marginBottom: "8px",
          }}>{previewLabel}</div>
          <div style={{ display: "flex", flexDirection: "column", gap: "4px" }}>
            {items.map((it, i) => <FeedItem key={i} {...it} />)}
          </div>
        </div>
      ) : null}
    </article>
  );
}
