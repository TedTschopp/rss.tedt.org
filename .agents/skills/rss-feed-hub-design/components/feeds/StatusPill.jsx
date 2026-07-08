import React from "react";

const STATUS = {
  healthy: { color: "var(--success)", icon: "fas fa-check-circle", label: "healthy" },
  warning: { color: "var(--warning-ink)", bg: "var(--warning)", icon: "fas fa-exclamation-triangle", label: "warning" },
  unknown: { color: "#fff", bg: "var(--pri-optional)", icon: "fas fa-question-circle", label: "unknown" },
  external: { color: "#fff", bg: "var(--cyan-500)", icon: "fas fa-up-right-from-square", label: "external" },
};

/**
 * Feed-health status: flat square chip + mono meta line
 * ("50 entries | Updated: 2026-07-07").
 */
export function StatusPill({ status = "unknown", entries, updated, style }) {
  const s = STATUS[status] || STATUS.unknown;
  return (
    <span style={{ display: "inline-flex", alignItems: "center", gap: "8px", flexWrap: "wrap", ...style }}>
      <span style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "5px",
        fontFamily: "var(--font-sans)",
        fontSize: "0.60rem",
        fontWeight: 600,
        letterSpacing: "var(--tr-badge)",
        textTransform: "uppercase",
        padding: "2px 6px",
        borderRadius: "var(--r-1)",
        background: s.bg || s.color,
        color: s.bg ? s.color : "#fff",
      }}>
        <i className={s.icon} aria-hidden="true" style={{ fontSize: "0.9em" }}></i>
        {s.label}
      </span>
      {entries != null || updated ? (
        <span style={{
          fontFamily: "var(--font-mono)",
          fontSize: "var(--fs-12)",
          color: "var(--text-muted)",
        }}>
          {entries != null ? `${entries} entries` : null}
          {entries != null && updated ? " | " : null}
          {updated ? `Updated: ${updated}` : null}
        </span>
      ) : null}
    </span>
  );
}
