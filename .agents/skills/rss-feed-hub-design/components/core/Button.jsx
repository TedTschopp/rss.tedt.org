import React from "react";

const BTN_VARIANTS = {
  primary:          { bg: "var(--navy-500)",  bd: "var(--navy-500)",   fg: "#fff",               hbg: "var(--navy-700)",  hbd: "var(--navy-700)",  hfg: "#fff" },
  accent:           { bg: "var(--orange-500)", bd: "var(--orange-500)", fg: "#fff",              hbg: "var(--orange-600)", hbd: "var(--orange-600)", hfg: "#fff" },
  outline:          { bg: "transparent", bd: "var(--navy-500)",   fg: "var(--navy-500)",   hbg: "var(--navy-500)",   hbd: "var(--navy-500)",   hfg: "#fff" },
  "outline-accent": { bg: "transparent", bd: "var(--orange-500)", fg: "var(--orange-500)", hbg: "var(--orange-500)", hbd: "var(--orange-500)", hfg: "#fff" },
  "outline-ink":    { bg: "transparent", bd: "var(--ink-900)",    fg: "var(--ink-900)",    hbg: "var(--ink-900)",    hbd: "var(--ink-900)",    hfg: "#fff" },
  ghost:            { bg: "transparent", bd: "transparent",       fg: "var(--navy-500)",   hbg: "var(--ink-100)",    hbd: "transparent",       hfg: "var(--navy-700)" },
};

const BTN_SIZES = {
  sm: { font: "var(--fs-12)", pad: "4px 10px",  gap: "6px" },
  md: { font: "var(--fs-14)", pad: "8px 16px",  gap: "8px" },
  lg: { font: "var(--fs-16)", pad: "12px 24px", gap: "8px" },
};

/**
 * Flat, square Swiss button. Outline variants fill with their border
 * color on hover (live-site behavior); solids darken one step.
 */
export function Button({
  variant = "primary",
  size = "md",
  icon,
  href,
  target,
  disabled = false,
  onClick,
  style,
  children,
}) {
  const [hover, setHover] = React.useState(false);
  const [active, setActive] = React.useState(false);
  const v = BTN_VARIANTS[variant] || BTN_VARIANTS.primary;
  const s = BTN_SIZES[size] || BTN_SIZES.md;
  const lit = (hover || active) && !disabled;

  const css = {
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    gap: s.gap,
    fontFamily: "var(--font-sans)",
    fontSize: s.font,
    fontWeight: 600,
    lineHeight: 1.2,
    padding: s.pad,
    background: lit ? v.hbg : v.bg,
    color: lit ? v.hfg : v.fg,
    border: `1px solid ${lit ? v.hbd : v.bd}`,
    borderRadius: "var(--r-0)",
    cursor: disabled ? "not-allowed" : "pointer",
    opacity: disabled ? 0.5 : 1,
    textDecoration: "none",
    transition: "background var(--dur-1) var(--ease), color var(--dur-1) var(--ease), border-color var(--dur-1) var(--ease)",
    userSelect: "none",
    ...style,
  };

  const inner = (
    <React.Fragment>
      {icon ? <i className={icon} aria-hidden="true" style={{ fontSize: "0.9em" }}></i> : null}
      {children}
    </React.Fragment>
  );

  const handlers = {
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => { setHover(false); setActive(false); },
    onMouseDown: () => setActive(true),
    onMouseUp: () => setActive(false),
    onClick: disabled ? undefined : onClick,
  };

  if (href && !disabled) {
    return <a href={href} target={target} rel={target ? "noopener" : undefined} style={css} {...handlers}>{inner}</a>;
  }
  return <button type="button" disabled={disabled} style={css} {...handlers}>{inner}</button>;
}
