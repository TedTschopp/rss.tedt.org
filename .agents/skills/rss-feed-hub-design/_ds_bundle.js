/* @ds-bundle: {"format":4,"namespace":"RSSFeedHubDesignSystem_2f2da6","components":[{"name":"Badge","sourcePath":"components/core/Badge.jsx"},{"name":"Button","sourcePath":"components/core/Button.jsx"},{"name":"Input","sourcePath":"components/core/Input.jsx"},{"name":"Tag","sourcePath":"components/core/Tag.jsx"},{"name":"FeedCard","sourcePath":"components/feeds/FeedCard.jsx"},{"name":"FeedItem","sourcePath":"components/feeds/FeedItem.jsx"},{"name":"FormatButton","sourcePath":"components/feeds/FormatButton.jsx"},{"name":"FormatGroup","sourcePath":"components/feeds/FormatButton.jsx"},{"name":"SectionHeader","sourcePath":"components/feeds/SectionHeader.jsx"},{"name":"StatusPill","sourcePath":"components/feeds/StatusPill.jsx"}],"sourceHashes":{"components/core/Badge.jsx":"b2081dda75fd","components/core/Button.jsx":"0df3e3960340","components/core/Input.jsx":"2189a2337a5e","components/core/Tag.jsx":"35082e6f8a71","components/feeds/FeedCard.jsx":"7973ce5140a3","components/feeds/FeedItem.jsx":"9098f6f7cd57","components/feeds/FormatButton.jsx":"a9e79ba1c686","components/feeds/SectionHeader.jsx":"4ff58e7346c4","components/feeds/StatusPill.jsx":"9cae83dfb4eb","ui_kits/website/AboutPage.jsx":"25a6c6911972","ui_kits/website/Chrome.jsx":"62215f797285","ui_kits/website/FeedsPage.jsx":"88bb0e4f3d89","ui_kits/website/HomePage.jsx":"0f6e363887ca","ui_kits/website/data.js":"dfe5281218d9"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.RSSFeedHubDesignSystem_2f2da6 = window.RSSFeedHubDesignSystem_2f2da6 || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/core/Badge.jsx
try { (() => {
const BADGE_KINDS = {
  essential: {
    bg: "var(--pri-essential)",
    fg: "#fff",
    label: "Essential"
  },
  important: {
    bg: "var(--pri-important)",
    fg: "var(--pri-important-ink)",
    label: "Important"
  },
  optional: {
    bg: "var(--pri-optional)",
    fg: "#fff",
    label: "Optional"
  },
  "tech-informational": {
    bg: "var(--tech-informational)",
    fg: "#fff",
    label: "Tech: Informational"
  },
  "tech-important": {
    bg: "var(--tech-important)",
    fg: "#fff",
    label: "Tech: Important"
  },
  "tech-transformational": {
    bg: "var(--tech-transformational)",
    fg: "#fff",
    label: "Tech: Transformational"
  },
  healthy: {
    bg: "var(--success)",
    fg: "#fff",
    label: "Healthy"
  },
  warning: {
    bg: "var(--warning)",
    fg: "var(--warning-ink)",
    label: "Warning"
  },
  unknown: {
    bg: "var(--pri-optional)",
    fg: "#fff",
    label: "Unknown"
  }
};

/**
 * Priority / tech-impact / status badge. Styling verbatim from the live
 * site's .pri-badge: uppercase, 0.60rem, 600, 3px radius.
 */
function Badge({
  kind = "optional",
  children,
  style
}) {
  const k = BADGE_KINDS[kind] || BADGE_KINDS.optional;
  return /*#__PURE__*/React.createElement("span", {
    style: {
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
      ...style
    }
  }, children || k.label);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Badge.jsx", error: String((e && e.message) || e) }); }

// components/core/Button.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const BTN_VARIANTS = {
  primary: {
    bg: "var(--navy-500)",
    bd: "var(--navy-500)",
    fg: "#fff",
    hbg: "var(--navy-700)",
    hbd: "var(--navy-700)",
    hfg: "#fff"
  },
  accent: {
    bg: "var(--orange-500)",
    bd: "var(--orange-500)",
    fg: "#fff",
    hbg: "var(--orange-600)",
    hbd: "var(--orange-600)",
    hfg: "#fff"
  },
  outline: {
    bg: "transparent",
    bd: "var(--navy-500)",
    fg: "var(--navy-500)",
    hbg: "var(--navy-500)",
    hbd: "var(--navy-500)",
    hfg: "#fff"
  },
  "outline-accent": {
    bg: "transparent",
    bd: "var(--orange-500)",
    fg: "var(--orange-500)",
    hbg: "var(--orange-500)",
    hbd: "var(--orange-500)",
    hfg: "#fff"
  },
  "outline-ink": {
    bg: "transparent",
    bd: "var(--ink-900)",
    fg: "var(--ink-900)",
    hbg: "var(--ink-900)",
    hbd: "var(--ink-900)",
    hfg: "#fff"
  },
  ghost: {
    bg: "transparent",
    bd: "transparent",
    fg: "var(--navy-500)",
    hbg: "var(--ink-100)",
    hbd: "transparent",
    hfg: "var(--navy-700)"
  }
};
const BTN_SIZES = {
  sm: {
    font: "var(--fs-12)",
    pad: "4px 10px",
    gap: "6px"
  },
  md: {
    font: "var(--fs-14)",
    pad: "8px 16px",
    gap: "8px"
  },
  lg: {
    font: "var(--fs-16)",
    pad: "12px 24px",
    gap: "8px"
  }
};

/**
 * Flat, square Swiss button. Outline variants fill with their border
 * color on hover (live-site behavior); solids darken one step.
 */
function Button({
  variant = "primary",
  size = "md",
  icon,
  href,
  target,
  disabled = false,
  onClick,
  style,
  children
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
    ...style
  };
  const inner = /*#__PURE__*/React.createElement(React.Fragment, null, icon ? /*#__PURE__*/React.createElement("i", {
    className: icon,
    "aria-hidden": "true",
    style: {
      fontSize: "0.9em"
    }
  }) : null, children);
  const handlers = {
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => {
      setHover(false);
      setActive(false);
    },
    onMouseDown: () => setActive(true),
    onMouseUp: () => setActive(false),
    onClick: disabled ? undefined : onClick
  };
  if (href && !disabled) {
    return /*#__PURE__*/React.createElement("a", _extends({
      href: href,
      target: target,
      rel: target ? "noopener" : undefined,
      style: css
    }, handlers), inner);
  }
  return /*#__PURE__*/React.createElement("button", _extends({
    type: "button",
    disabled: disabled,
    style: css
  }, handlers), inner);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Button.jsx", error: String((e && e.message) || e) }); }

// components/core/Input.jsx
try { (() => {
/**
 * Square text input. With `copyable`, renders the live site's copy-URL
 * group: readonly value + a copy button that flips to a success check.
 */
function Input({
  value,
  defaultValue,
  onChange,
  placeholder,
  label,
  readOnly = false,
  copyable = false,
  size = "md",
  type = "text",
  style
}) {
  const [focus, setFocus] = React.useState(false);
  const [copied, setCopied] = React.useState(false);
  const dims = size === "sm" ? {
    font: "var(--fs-12)",
    pad: "5px 8px"
  } : {
    font: "var(--fs-14)",
    pad: "8px 10px"
  };
  const copy = () => {
    const text = value != null ? value : defaultValue;
    if (navigator.clipboard && text) navigator.clipboard.writeText(String(text));
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };
  const inputEl = /*#__PURE__*/React.createElement("input", {
    type: type,
    value: value,
    defaultValue: defaultValue,
    onChange: onChange,
    placeholder: placeholder,
    readOnly: readOnly || copyable,
    onFocus: () => setFocus(true),
    onBlur: () => setFocus(false),
    style: {
      flex: 1,
      minWidth: 0,
      fontFamily: copyable ? "var(--font-mono)" : "var(--font-sans)",
      fontSize: copyable ? "var(--fs-12)" : dims.font,
      padding: dims.pad,
      color: "var(--text-body)",
      background: "#fff",
      border: `1px solid ${focus ? "var(--focus-ring)" : "var(--border)"}`,
      borderRadius: "var(--r-0)",
      outline: "none",
      transition: "border-color var(--dur-1) var(--ease)"
    }
  });
  return /*#__PURE__*/React.createElement("label", {
    style: {
      display: "block",
      ...style
    }
  }, label ? /*#__PURE__*/React.createElement("span", {
    style: {
      display: "block",
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      letterSpacing: "var(--tr-eyebrow)",
      textTransform: "uppercase",
      color: "var(--text-muted)",
      marginBottom: "6px"
    }
  }, label) : null, /*#__PURE__*/React.createElement("span", {
    style: {
      display: "flex"
    }
  }, inputEl, copyable ? /*#__PURE__*/React.createElement("button", {
    type: "button",
    onClick: copy,
    "aria-label": "Copy to clipboard",
    style: {
      display: "inline-flex",
      alignItems: "center",
      gap: "6px",
      fontFamily: "var(--font-sans)",
      fontSize: "var(--fs-12)",
      fontWeight: 600,
      padding: dims.pad,
      background: copied ? "var(--success)" : "transparent",
      color: copied ? "#fff" : "var(--ink-500)",
      border: `1px solid ${copied ? "var(--success)" : "var(--border)"}`,
      borderLeft: 0,
      cursor: "pointer",
      transition: "background var(--dur-1) var(--ease), color var(--dur-1) var(--ease)",
      whiteSpace: "nowrap"
    }
  }, /*#__PURE__*/React.createElement("i", {
    className: copied ? "fas fa-check" : "fas fa-copy",
    "aria-hidden": "true"
  }), copied ? "Copied!" : "Copy") : null));
}
Object.assign(__ds_scope, { Input });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Input.jsx", error: String((e && e.message) || e) }); }

// components/core/Tag.jsx
try { (() => {
/**
 * Category tag — mono, hairline-bordered, square. For source categories
 * (AI Labs, Reddit, arXiv…) and feed facets. Quiet by default; `active`
 * fills navy.
 */
function Tag({
  active = false,
  onClick,
  children,
  style
}) {
  const [hover, setHover] = React.useState(false);
  const interactive = typeof onClick === "function";
  return /*#__PURE__*/React.createElement("span", {
    onClick: onClick,
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    style: {
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
      ...style
    }
  }, children);
}
Object.assign(__ds_scope, { Tag });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Tag.jsx", error: String((e && e.message) || e) }); }

// components/feeds/FeedItem.jsx
try { (() => {
const PRI_ROW = {
  essential: {
    bg: "rgba(220,53,69,.08)",
    bar: "rgba(220,53,69,.6)"
  },
  important: {
    bg: "rgba(255,193,7,.12)",
    bar: "rgba(255,193,7,.7)"
  },
  optional: {
    bg: "rgba(108,117,125,.10)",
    bar: "rgba(108,117,125,.55)"
  }
};

/**
 * One feed entry: optional priority/tech badges, title link, mono date.
 * Prioritized rows get the live site's tint + 3px left bar.
 */
function FeedItem({
  title,
  href = "#",
  date,
  priority,
  tech,
  style
}) {
  const [hover, setHover] = React.useState(false);
  const row = priority ? PRI_ROW[priority] : null;
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "baseline",
      gap: "8px",
      padding: row ? "4px 6px" : "4px 0",
      background: row ? row.bg : "transparent",
      borderLeft: row ? `var(--bw-bar) solid ${row.bar}` : "var(--bw-bar) solid transparent",
      lineHeight: 1.35,
      ...style
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      flex: 1,
      minWidth: 0
    }
  }, priority ? /*#__PURE__*/React.createElement(__ds_scope.Badge, {
    kind: priority,
    style: {
      marginRight: "6px",
      position: "relative",
      top: "-1px"
    }
  }) : null, tech ? /*#__PURE__*/React.createElement(__ds_scope.Badge, {
    kind: "tech-" + tech,
    style: {
      marginRight: "6px",
      position: "relative",
      top: "-1px"
    }
  }) : null, /*#__PURE__*/React.createElement("a", {
    href: href,
    rel: "noopener noreferrer",
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    style: {
      color: hover ? "var(--accent)" : "var(--text-heading)",
      fontWeight: 600,
      fontSize: "var(--fs-14)",
      textDecoration: hover ? "underline" : "none",
      textUnderlineOffset: "0.15em",
      transition: "color var(--dur-1) var(--ease)"
    }
  }, title)), date ? /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "0.65rem",
      color: "var(--text-muted)",
      flex: "none"
    }
  }, "(", date, ")") : null);
}
Object.assign(__ds_scope, { FeedItem });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/feeds/FeedItem.jsx", error: String((e && e.message) || e) }); }

// components/feeds/FormatButton.jsx
try { (() => {
const JSON_GLYPH_PATH = "M213.333333 128h85.333334v85.333333H213.333333v213.333334a85.333333 85.333333 0 0 1-85.333333 85.333333 85.333333 85.333333 0 0 1 85.333333 85.333333v213.333334h85.333334v85.333333H213.333333c-45.653333-11.52-85.333333-38.4-85.333333-85.333333v-170.666667a85.333333 85.333333 0 0 0-85.333333-85.333333H0v-85.333334h42.666667a85.333333 85.333333 0 0 0 85.333333-85.333333V213.333333a85.333333 85.333333 0 0 1 85.333333-85.333333m597.333334 0a85.333333 85.333333 0 0 1 85.333333 85.333333v170.666667a85.333333 85.333333 0 0 0 85.333333 85.333333h42.666667v85.333334h-42.666667a85.333333 85.333333 0 0 0-85.333333 85.333333v170.666667a85.333333 85.333333 0 0 1-85.333333 85.333333h-85.333334v-85.333333h85.333334v-213.333334a85.333333 85.333333 0 0 1 85.333333-85.333333 85.333333 85.333333 0 0 1-85.333333-85.333333V213.333333h-85.333334V128h85.333334m-298.666667 512a42.666667 42.666667 0 0 1 42.666667 42.666667 42.666667 42.666667 0 0 1-42.666667 42.666666 42.666667 42.666667 0 0 1-42.666667-42.666666 42.666667 42.666667 0 0 1 42.666667-42.666667m-170.666667 0a42.666667 42.666667 0 0 1 42.666667 42.666667 42.666667 42.666667 0 0 1-42.666667 42.666666 42.666667 42.666667 0 0 1-42.666666-42.666666 42.666667 42.666667 0 0 1 42.666666-42.666667m341.333334 0a42.666667 42.666667 0 0 1 42.666666 42.666667 42.666667 42.666667 0 0 1-42.666666 42.666666 42.666667 42.666667 0 0 1-42.666667-42.666666 42.666667 42.666667 0 0 1 42.666667-42.666667z";
const FORMATS = {
  rss2: {
    label: "RSS 2.0",
    color: "var(--format-rss2)",
    hoverFg: "#fff",
    icon: "fas fa-rss"
  },
  rss1: {
    label: "RSS 1.0",
    color: "var(--format-rss1)",
    hoverFg: "#fff",
    icon: "fas fa-rss"
  },
  atom: {
    label: "Atom",
    color: "var(--format-atom)",
    hoverFg: "#fff",
    icon: "fas fa-atom"
  },
  json: {
    label: "JSON",
    color: "var(--format-json)",
    hoverFg: "var(--format-json-gold)",
    icon: null
  }
};

/**
 * Outline button in the fixed syndication-format brand color; fills with
 * that color on hover (JSON flips text to gold — live-site behavior).
 * JSON has no Font Awesome glyph, so it inlines the site's SVG path.
 */
function FormatButton({
  format = "rss2",
  href = "#",
  size = "sm",
  style
}) {
  const [hover, setHover] = React.useState(false);
  const f = FORMATS[format] || FORMATS.rss2;
  const dims = size === "sm" ? {
    font: "var(--fs-12)",
    pad: "4px 10px"
  } : {
    font: "var(--fs-14)",
    pad: "8px 14px"
  };
  return /*#__PURE__*/React.createElement("a", {
    href: href,
    target: "feed_" + format,
    rel: "noopener",
    title: f.label,
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    style: {
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
      ...style
    }
  }, f.icon ? /*#__PURE__*/React.createElement("i", {
    className: f.icon,
    "aria-hidden": "true",
    style: {
      fontSize: "0.9em"
    }
  }) : /*#__PURE__*/React.createElement("svg", {
    viewBox: "0 0 1024 1024",
    width: "1em",
    height: "1em",
    fill: "currentColor",
    "aria-hidden": "true",
    style: {
      display: "block"
    }
  }, /*#__PURE__*/React.createElement("path", {
    d: JSON_GLYPH_PATH
  })), f.label);
}

/** Row of format buttons for a feed's available formats, in canonical order. */
function FormatGroup({
  formats,
  size = "sm",
  style
}) {
  const order = ["rss2", "rss1", "atom", "json"];
  return /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      gap: "4px",
      flexWrap: "wrap",
      ...style
    }
  }, order.filter(k => formats && formats[k]).map(k => /*#__PURE__*/React.createElement(FormatButton, {
    key: k,
    format: k,
    href: formats[k],
    size: size
  })));
}
Object.assign(__ds_scope, { FormatButton, FormatGroup });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/feeds/FormatButton.jsx", error: String((e && e.message) || e) }); }

// components/feeds/SectionHeader.jsx
try { (() => {
/**
 * Swiss section header: 2px ink rule on top, mono eyebrow, bold title,
 * optional meta/action on the right baseline.
 */
function SectionHeader({
  eyebrow,
  title,
  meta,
  action,
  style
}) {
  return /*#__PURE__*/React.createElement("header", {
    style: {
      borderTop: "var(--bw-rule) solid var(--border-strong)",
      paddingTop: "var(--sp-3)",
      display: "flex",
      alignItems: "flex-end",
      justifyContent: "space-between",
      gap: "var(--sp-4)",
      flexWrap: "wrap",
      ...style
    }
  }, /*#__PURE__*/React.createElement("div", null, eyebrow ? /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      fontWeight: 500,
      letterSpacing: "var(--tr-eyebrow)",
      textTransform: "uppercase",
      color: "var(--accent)",
      marginBottom: "4px"
    }
  }, eyebrow) : null, /*#__PURE__*/React.createElement("h2", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 700,
      fontSize: "var(--fs-28)",
      lineHeight: "var(--lh-tight)",
      letterSpacing: "var(--tr-tight)",
      color: "var(--text-heading)",
      margin: 0
    }
  }, title)), meta ? /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      color: "var(--text-muted)",
      paddingBottom: "4px"
    }
  }, meta) : null, action || null);
}
Object.assign(__ds_scope, { SectionHeader });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/feeds/SectionHeader.jsx", error: String((e && e.message) || e) }); }

// components/feeds/StatusPill.jsx
try { (() => {
const STATUS = {
  healthy: {
    color: "var(--success)",
    icon: "fas fa-check-circle",
    label: "healthy"
  },
  warning: {
    color: "var(--warning-ink)",
    bg: "var(--warning)",
    icon: "fas fa-exclamation-triangle",
    label: "warning"
  },
  unknown: {
    color: "#fff",
    bg: "var(--pri-optional)",
    icon: "fas fa-question-circle",
    label: "unknown"
  },
  external: {
    color: "#fff",
    bg: "var(--cyan-500)",
    icon: "fas fa-up-right-from-square",
    label: "external"
  }
};

/**
 * Feed-health status: flat square chip + mono meta line
 * ("50 entries | Updated: 2026-07-07").
 */
function StatusPill({
  status = "unknown",
  entries,
  updated,
  style
}) {
  const s = STATUS[status] || STATUS.unknown;
  return /*#__PURE__*/React.createElement("span", {
    style: {
      display: "inline-flex",
      alignItems: "center",
      gap: "8px",
      flexWrap: "wrap",
      ...style
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
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
      color: s.bg ? s.color : "#fff"
    }
  }, /*#__PURE__*/React.createElement("i", {
    className: s.icon,
    "aria-hidden": "true",
    style: {
      fontSize: "0.9em"
    }
  }), s.label), entries != null || updated ? /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      color: "var(--text-muted)"
    }
  }, entries != null ? `${entries} entries` : null, entries != null && updated ? " | " : null, updated ? `Updated: ${updated}` : null) : null);
}
Object.assign(__ds_scope, { StatusPill });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/feeds/StatusPill.jsx", error: String((e && e.message) || e) }); }

// components/feeds/FeedCard.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * The site's central object: one card per feed. Mono index + 2px ink top
 * rule, name, description, format buttons, copy-URL group, health line,
 * and a recent-entries preview. Square, bordered, flat.
 */
function FeedCard({
  index,
  name,
  description,
  url,
  formats,
  status,
  items = [],
  previewLabel = "Recent Entries",
  style
}) {
  const [hover, setHover] = React.useState(false);
  return /*#__PURE__*/React.createElement("article", {
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    style: {
      background: "var(--surface)",
      border: `1px solid ${hover ? "var(--border-strong)" : "var(--border)"}`,
      borderTop: "var(--bw-rule) solid var(--border-strong)",
      padding: "var(--sp-6)",
      transition: "border-color var(--dur-1) var(--ease)",
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp-4)",
      ...style
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "flex-start",
      justifyContent: "space-between",
      gap: "var(--sp-4)",
      flexWrap: "wrap"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      minWidth: 0
    }
  }, index != null ? /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      color: "var(--accent)",
      marginBottom: "4px"
    }
  }, String(index).padStart(2, "0")) : null, /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 700,
      fontSize: "var(--fs-21)",
      lineHeight: "var(--lh-snug)",
      letterSpacing: "var(--tr-tight)",
      color: "var(--text-heading)",
      margin: 0
    }
  }, name), description ? /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: "var(--fs-14)",
      color: "var(--text-muted)",
      margin: "4px 0 0"
    }
  }, description) : null), formats ? /*#__PURE__*/React.createElement(__ds_scope.FormatGroup, {
    formats: formats
  }) : null), url ? /*#__PURE__*/React.createElement(__ds_scope.Input, {
    copyable: true,
    size: "sm",
    defaultValue: url
  }) : null, status ? /*#__PURE__*/React.createElement(__ds_scope.StatusPill, {
    status: status.health,
    entries: status.entries,
    updated: status.updated
  }) : null, items.length > 0 ? /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      letterSpacing: "var(--tr-eyebrow)",
      textTransform: "uppercase",
      color: "var(--text-muted)",
      borderBottom: "1px solid var(--border)",
      paddingBottom: "6px",
      marginBottom: "8px"
    }
  }, previewLabel), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "4px"
    }
  }, items.map((it, i) => /*#__PURE__*/React.createElement(__ds_scope.FeedItem, _extends({
    key: i
  }, it))))) : null);
}
Object.assign(__ds_scope, { FeedCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/feeds/FeedCard.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/AboutPage.jsx
try { (() => {
// About page: prose column + stats/links sidebar.
const DS_ABOUT = window.RSSFeedHubDesignSystem_2f2da6;
function AboutPage() {
  const {
    SectionHeader,
    Badge,
    Tag
  } = DS_ABOUT;
  const {
    site,
    feeds,
    statusApi
  } = window.RSSHUB_DATA;
  return /*#__PURE__*/React.createElement("main", {
    style: {
      maxWidth: "var(--w-page)",
      margin: "0 auto",
      padding: "var(--sp-12) var(--sp-6) 0"
    }
  }, /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 900,
      fontSize: "var(--fs-48)",
      letterSpacing: "-0.02em",
      lineHeight: 1.05,
      margin: 0
    }
  }, "About RSS Feed Hub"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1fr 320px",
      gap: "var(--sp-8)",
      marginTop: "var(--sp-6)",
      alignItems: "start"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--w-prose)",
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp-8)"
    }
  }, /*#__PURE__*/React.createElement("p", {
    className: "lead",
    style: {
      margin: 0
    }
  }, "Welcome to RSS Feed Hub, your centralized source for curated AI and technology news feeds. This site automatically aggregates and monitors RSS feeds from various sources to keep you updated with the latest developments in artificial intelligence and technology."), /*#__PURE__*/React.createElement("section", null, /*#__PURE__*/React.createElement(SectionHeader, {
    title: "How It Works"
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: "var(--sp-4)",
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: "1px",
      background: "var(--border)",
      border: "1px solid var(--border)"
    }
  }, /*#__PURE__*/React.createElement(HowCell, {
    n: "01",
    t: "Scrape Content",
    d: "Automatically extract articles and news from target websites"
  }), /*#__PURE__*/React.createElement(HowCell, {
    n: "02",
    t: "Generate RSS",
    d: "Convert scraped content into standard RSS feed format"
  }), /*#__PURE__*/React.createElement(HowCell, {
    n: "03",
    t: "Monitor Health",
    d: "Continuously check feed status and entry counts"
  }), /*#__PURE__*/React.createElement(HowCell, {
    n: "04",
    t: "Update Regularly",
    d: "Refresh content on a scheduled basis via GitHub Actions"
  }))), /*#__PURE__*/React.createElement("section", null, /*#__PURE__*/React.createElement(SectionHeader, {
    title: "Priority Badges"
  }), /*#__PURE__*/React.createElement("p", {
    style: {
      margin: "var(--sp-4) 0 0",
      fontSize: "var(--fs-14)"
    }
  }, "Feed entries can include priority markers in their titles, converted to visual badges:"), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: "var(--sp-3)",
      border: "1px solid var(--border)",
      background: "var(--surface)"
    }
  }, /*#__PURE__*/React.createElement(BadgeRow, {
    sym: "[ ! ]",
    badge: /*#__PURE__*/React.createElement(Badge, {
      kind: "essential"
    }),
    d: "Critical or urgent content"
  }), /*#__PURE__*/React.createElement(BadgeRow, {
    sym: "[ * ]",
    badge: /*#__PURE__*/React.createElement(Badge, {
      kind: "important"
    }),
    d: "High-priority content"
  }), /*#__PURE__*/React.createElement(BadgeRow, {
    sym: "[ ~ ]",
    badge: /*#__PURE__*/React.createElement(Badge, {
      kind: "optional"
    }),
    d: "Supplementary or nice-to-know content"
  }), /*#__PURE__*/React.createElement(BadgeRow, {
    sym: "[ \u2B22 ]",
    badge: /*#__PURE__*/React.createElement(Badge, {
      kind: "tech-transformational"
    }),
    d: "Forces rethinking architecture/governance patterns"
  }), /*#__PURE__*/React.createElement(BadgeRow, {
    sym: "[ \u25FC ]",
    badge: /*#__PURE__*/React.createElement(Badge, {
      kind: "tech-important"
    }),
    d: "Likely to change how teams build/run AI systems"
  }), /*#__PURE__*/React.createElement(BadgeRow, {
    sym: "[ \u25FB ]",
    badge: /*#__PURE__*/React.createElement(Badge, {
      kind: "tech-informational"
    }),
    d: "Awareness-level technical signal",
    last: true
  }))), /*#__PURE__*/React.createElement("section", null, /*#__PURE__*/React.createElement(SectionHeader, {
    title: "Broad AI News Sources"
  }), /*#__PURE__*/React.createElement("p", {
    style: {
      margin: "var(--sp-4) 0 var(--sp-3)",
      fontSize: "var(--fs-14)"
    }
  }, "The widest feed pulls from 21 sources across six categories:"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "6px",
      flexWrap: "wrap"
    }
  }, feeds[4].categories.map(c => /*#__PURE__*/React.createElement(Tag, {
    key: c
  }, c)))), /*#__PURE__*/React.createElement("section", null, /*#__PURE__*/React.createElement(SectionHeader, {
    title: "Technical Details"
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: "var(--sp-4)",
      display: "flex",
      flexDirection: "column"
    }
  }, /*#__PURE__*/React.createElement(TechRow, {
    k: "Python",
    v: "Web scraping with Beautiful Soup and Playwright",
    first: true
  }), /*#__PURE__*/React.createElement(TechRow, {
    k: "GitHub Actions",
    v: "Automated workflow execution, every 8 hours"
  }), /*#__PURE__*/React.createElement(TechRow, {
    k: "GitHub Models",
    v: "Optional LLM enrichment for Top Stories ranking"
  }), /*#__PURE__*/React.createElement(TechRow, {
    k: "Jekyll",
    v: "Static site generation"
  }), /*#__PURE__*/React.createElement(TechRow, {
    k: "RSS \xB7 Atom \xB7 JSON",
    v: "Standard syndication formats"
  })))), /*#__PURE__*/React.createElement("aside", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp-6)",
      position: "sticky",
      top: "88px"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      background: "var(--navy-500)",
      color: "#fff",
      padding: "var(--sp-6)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      letterSpacing: "var(--tr-eyebrow)",
      textTransform: "uppercase",
      color: "rgba(255,255,255,0.6)",
      marginBottom: "var(--sp-4)"
    }
  }, "Quick Stats"), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: "var(--sp-4)"
    }
  }, /*#__PURE__*/React.createElement(Stat, {
    n: statusApi.totalFiles,
    l: "feed files"
  }), /*#__PURE__*/React.createElement(Stat, {
    n: statusApi.healthyFiles,
    l: "healthy",
    accent: true
  }), /*#__PURE__*/React.createElement(Stat, {
    n: statusApi.totalEntries.toLocaleString(),
    l: "total entries",
    wide: true
  }), /*#__PURE__*/React.createElement(Stat, {
    n: statusApi.pipeline.stories.toLocaleString(),
    l: "stories indexed",
    wide: true
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: "var(--sp-4)",
      paddingTop: "var(--sp-3)",
      borderTop: "1px solid rgba(255,255,255,0.2)",
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      color: "rgba(255,255,255,0.6)"
    }
  }, "Last updated: ", site.statusTimestamp)), /*#__PURE__*/React.createElement("div", {
    style: {
      background: "var(--surface)",
      border: "1px solid var(--border)",
      padding: "var(--sp-6)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      letterSpacing: "var(--tr-eyebrow)",
      textTransform: "uppercase",
      color: "var(--text-muted)",
      marginBottom: "var(--sp-3)"
    }
  }, "Useful Links"), /*#__PURE__*/React.createElement(SideLink, {
    icon: "fab fa-github",
    label: "Source Code"
  }), /*#__PURE__*/React.createElement(SideLink, {
    icon: "fas fa-file-code",
    label: "Status JSON"
  }), feeds.map(f => /*#__PURE__*/React.createElement(SideLink, {
    key: f.key,
    icon: "fas fa-rss",
    label: f.name
  }))))));
}
function HowCell({
  n,
  t,
  d
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      background: "var(--surface)",
      padding: "var(--sp-4)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      color: "var(--accent)",
      marginBottom: "6px"
    }
  }, n), /*#__PURE__*/React.createElement("div", {
    style: {
      fontWeight: 700,
      fontSize: "var(--fs-16)",
      color: "var(--text-heading)"
    }
  }, t), /*#__PURE__*/React.createElement("div", {
    style: {
      fontSize: "var(--fs-14)",
      color: "var(--text-muted)",
      marginTop: "4px"
    }
  }, d));
}
function BadgeRow({
  sym,
  badge,
  d,
  last = false
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      gap: "var(--sp-4)",
      padding: "10px var(--sp-4)",
      borderBottom: last ? "none" : "1px solid var(--ink-100)",
      fontSize: "var(--fs-14)"
    }
  }, /*#__PURE__*/React.createElement("code", {
    style: {
      flex: "none",
      width: "44px",
      textAlign: "center"
    }
  }, sym), /*#__PURE__*/React.createElement("span", {
    style: {
      flex: "none",
      width: "160px"
    }
  }, badge), /*#__PURE__*/React.createElement("span", {
    style: {
      color: "var(--text-muted)"
    }
  }, d));
}
function TechRow({
  k,
  v,
  first = false
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      gap: "var(--sp-4)",
      padding: "8px 0",
      borderTop: first ? "none" : "1px solid var(--ink-100)",
      fontSize: "var(--fs-14)"
    }
  }, /*#__PURE__*/React.createElement("strong", {
    style: {
      flex: "none",
      width: "150px",
      color: "var(--text-heading)"
    }
  }, k), /*#__PURE__*/React.createElement("span", {
    style: {
      color: "var(--text-muted)"
    }
  }, v));
}
function Stat({
  n,
  l,
  accent = false,
  wide = false
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      gridColumn: wide ? "1 / -1" : "auto"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontWeight: 600,
      fontSize: "var(--fs-28)",
      lineHeight: 1.1,
      color: accent ? "var(--cyan-500)" : "#fff"
    }
  }, n), /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      color: "rgba(255,255,255,0.6)"
    }
  }, l));
}
function SideLink({
  icon,
  label
}) {
  const [hover, setHover] = React.useState(false);
  return /*#__PURE__*/React.createElement("a", {
    href: "#",
    onClick: e => e.preventDefault(),
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    style: {
      display: "flex",
      alignItems: "center",
      gap: "10px",
      fontSize: "var(--fs-14)",
      color: hover ? "var(--accent)" : "var(--navy-500)",
      textDecoration: hover ? "underline" : "none",
      textUnderlineOffset: "0.15em",
      padding: "5px 0",
      transition: "color var(--dur-1) var(--ease)"
    }
  }, /*#__PURE__*/React.createElement("i", {
    className: icon,
    "aria-hidden": "true",
    style: {
      width: "16px",
      textAlign: "center",
      fontSize: "13px"
    }
  }), label);
}
Object.assign(window, {
  AboutPage
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/AboutPage.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/Chrome.jsx
try { (() => {
// Site chrome: NavBar, Masthead, Footer.
const DS_CHROME = window.RSSFeedHubDesignSystem_2f2da6;
function NavBar({
  current,
  onNav
}) {
  const links = [{
    id: "home",
    label: "Home"
  }, {
    id: "feeds",
    label: "RSS Feeds"
  }, {
    id: "about",
    label: "About"
  }];
  return /*#__PURE__*/React.createElement("nav", {
    style: {
      background: "var(--surface)",
      borderBottom: "1px solid var(--border)",
      position: "sticky",
      top: 0,
      zIndex: 100
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--w-page)",
      margin: "0 auto",
      padding: "0 var(--sp-6)",
      display: "flex",
      alignItems: "stretch",
      gap: "var(--sp-6)",
      height: "64px"
    }
  }, /*#__PURE__*/React.createElement("a", {
    href: "#home",
    onClick: e => {
      e.preventDefault();
      onNav("home");
    },
    style: {
      display: "flex",
      alignItems: "center",
      gap: "10px",
      textDecoration: "none",
      marginRight: "auto"
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/logo.png",
    alt: "RSS Feed Hub",
    width: "32",
    height: "32"
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 900,
      fontSize: "18px",
      letterSpacing: "-0.01em",
      color: "var(--navy-500)",
      lineHeight: 1,
      textTransform: "uppercase"
    }
  }, "RSS Feed Hub")), links.map(l => /*#__PURE__*/React.createElement(NavLink, {
    key: l.id,
    active: current === l.id,
    onClick: () => onNav(l.id)
  }, l.label)), /*#__PURE__*/React.createElement(NavLink, {
    href: "https://github.com/TedTschopp/rss.tedt.org"
  }, /*#__PURE__*/React.createElement("i", {
    className: "fab fa-github",
    "aria-hidden": "true",
    style: {
      marginRight: "6px"
    }
  }), "GitHub")));
}
function NavLink({
  active,
  onClick,
  href,
  children
}) {
  const [hover, setHover] = React.useState(false);
  return /*#__PURE__*/React.createElement("a", {
    href: href || "#",
    target: href ? "_blank" : undefined,
    rel: href ? "noopener" : undefined,
    onClick: href ? undefined : e => {
      e.preventDefault();
      onClick();
    },
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    style: {
      display: "flex",
      alignItems: "center",
      fontFamily: "var(--font-sans)",
      fontSize: "var(--fs-14)",
      fontWeight: 600,
      color: active ? "var(--text-heading)" : hover ? "var(--text-heading)" : "var(--text-muted)",
      textDecoration: "none",
      borderBottom: `3px solid ${active ? "var(--orange-500)" : "transparent"}`,
      borderTop: "3px solid transparent",
      transition: "color var(--dur-1) var(--ease)"
    }
  }, children);
}
function Masthead() {
  const site = window.RSSHUB_DATA.site;
  const feeds = window.RSSHUB_DATA.feeds;
  const totalEntries = feeds.reduce((n, f) => n + (f.status.entries || 0), 0);
  return /*#__PURE__*/React.createElement("header", {
    style: {
      borderBottom: "1px solid var(--border)",
      background: "var(--bg)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--w-page)",
      margin: "0 auto",
      padding: "var(--sp-12) var(--sp-6) var(--sp-8)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      letterSpacing: "var(--tr-eyebrow)",
      textTransform: "uppercase",
      color: "var(--accent)",
      marginBottom: "var(--sp-3)"
    }
  }, "rss.tedt.org"), /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 900,
      fontSize: "clamp(48px, 8vw, 88px)",
      lineHeight: 0.95,
      letterSpacing: "-0.02em",
      textTransform: "uppercase",
      color: "var(--text-heading)",
      margin: 0
    }
  }, "RSS Feed", /*#__PURE__*/React.createElement("br", null), "Hub", /*#__PURE__*/React.createElement("span", {
    style: {
      color: "var(--orange-500)"
    }
  }, ".")), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "flex-end",
      justifyContent: "space-between",
      gap: "var(--sp-6)",
      flexWrap: "wrap",
      marginTop: "var(--sp-6)"
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: "var(--fs-18)",
      maxWidth: "42rem",
      margin: 0
    }
  }, site.description, ". Aggregated, ranked, and monitored automatically \u2014 subscribe in the format your reader speaks."), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      color: "var(--text-muted)",
      whiteSpace: "nowrap"
    }
  }, feeds.length, " FEEDS \xB7 ", totalEntries, " ENTRIES \xB7 UPDATED ", feeds[0].status.updated))));
}
function Footer({
  onNav
}) {
  const site = window.RSSHUB_DATA.site;
  const feeds = window.RSSHUB_DATA.feeds;
  return /*#__PURE__*/React.createElement("footer", {
    style: {
      background: "var(--navy-500)",
      color: "#fff",
      marginTop: "var(--sp-16)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--w-page)",
      margin: "0 auto",
      padding: "var(--sp-8) var(--sp-6)",
      display: "grid",
      gridTemplateColumns: "2fr 1fr 1fr",
      gap: "var(--sp-8)"
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      alignItems: "center",
      gap: "10px",
      marginBottom: "var(--sp-3)"
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: "../../assets/logo.png",
    alt: "",
    width: "28",
    height: "28"
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      fontWeight: 900,
      fontSize: "16px",
      textTransform: "uppercase",
      letterSpacing: "-0.01em"
    }
  }, site.name)), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: "var(--fs-14)",
      color: "var(--text-on-dark-muted)",
      maxWidth: "30rem",
      margin: 0
    }
  }, site.description)), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(FooterHead, null, "RSS Feeds"), feeds.map(f => /*#__PURE__*/React.createElement(FooterLink, {
    key: f.key,
    href: f.url
  }, f.name))), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(FooterHead, null, "Site"), /*#__PURE__*/React.createElement(FooterLink, {
    onClick: () => onNav("home")
  }, "Home"), /*#__PURE__*/React.createElement(FooterLink, {
    onClick: () => onNav("feeds")
  }, "RSS Feeds"), /*#__PURE__*/React.createElement(FooterLink, {
    onClick: () => onNav("about")
  }, "About"), /*#__PURE__*/React.createElement(FooterLink, {
    href: site.github
  }, "Source Code"), /*#__PURE__*/React.createElement(FooterLink, {
    href: "#"
  }, "Status JSON"))), /*#__PURE__*/React.createElement("div", {
    style: {
      borderTop: "1px solid rgba(255,255,255,0.2)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: "var(--w-page)",
      margin: "0 auto",
      padding: "var(--sp-4) var(--sp-6)",
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      gap: "var(--sp-4)",
      flexWrap: "wrap"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      color: "var(--text-on-dark-muted)"
    }
  }, "\xA9 2026 ", site.owner, ". All rights reserved."), /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      color: "var(--text-on-dark-muted)"
    }
  }, /*#__PURE__*/React.createElement("i", {
    className: "fab fa-github",
    "aria-hidden": "true",
    style: {
      marginRight: "8px"
    }
  }), "Powered by Jekyll"))));
}
function FooterHead({
  children
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      letterSpacing: "var(--tr-eyebrow)",
      textTransform: "uppercase",
      color: "var(--text-on-dark-muted)",
      marginBottom: "var(--sp-3)"
    }
  }, children);
}
function FooterLink({
  href,
  onClick,
  children
}) {
  const [hover, setHover] = React.useState(false);
  return /*#__PURE__*/React.createElement("a", {
    href: href || "#",
    onClick: onClick ? e => {
      e.preventDefault();
      onClick();
    } : undefined,
    onMouseEnter: () => setHover(true),
    onMouseLeave: () => setHover(false),
    style: {
      display: "block",
      fontSize: "var(--fs-14)",
      color: hover ? "#fff" : "rgba(255,255,255,0.75)",
      textDecoration: hover ? "underline" : "none",
      textUnderlineOffset: "0.15em",
      marginBottom: "8px",
      transition: "color var(--dur-1) var(--ease)"
    }
  }, children);
}
Object.assign(window, {
  NavBar,
  Masthead,
  Footer
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/Chrome.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/FeedsPage.jsx
try { (() => {
// Feeds directory: manager callout, 2-col feed cards with URL copy +
// status, and the "How to Use RSS Feeds" section.
const DS_FEEDS = window.RSSFeedHubDesignSystem_2f2da6;
function FeedsPage() {
  const {
    SectionHeader,
    FeedCard,
    Button
  } = DS_FEEDS;
  const feeds = window.RSSHUB_DATA.feeds;
  return /*#__PURE__*/React.createElement("main", {
    style: {
      maxWidth: "var(--w-page)",
      margin: "0 auto",
      padding: "var(--sp-12) var(--sp-6) 0"
    }
  }, /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: "var(--font-sans)",
      fontWeight: 900,
      fontSize: "var(--fs-48)",
      letterSpacing: "-0.02em",
      lineHeight: 1.05,
      margin: 0
    }
  }, "RSS Feeds"), /*#__PURE__*/React.createElement("p", {
    className: "lead",
    style: {
      maxWidth: "42rem",
      margin: "var(--sp-4) 0 0"
    }
  }, "Subscribe to our curated RSS feeds to stay updated with the latest AI and technology news."), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: "var(--sp-6)",
      border: "1px solid var(--border)",
      borderTop: "var(--bw-rule) solid var(--orange-500)",
      background: "var(--surface)",
      padding: "var(--sp-4) var(--sp-6)",
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      gap: "var(--sp-4)",
      flexWrap: "wrap"
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      margin: 0,
      fontSize: "var(--fs-14)"
    }
  }, /*#__PURE__*/React.createElement("strong", null, "Managing Top Stories inputs?"), " Use the Top Stories Manager to edit included feeds and adjust ranking weights."), /*#__PURE__*/React.createElement(Button, {
    size: "sm",
    variant: "outline"
  }, "Open Top Stories Manager")), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "repeat(auto-fit, minmax(420px, 1fr))",
      gap: "var(--sp-6)",
      marginTop: "var(--sp-8)"
    }
  }, feeds.map((f, i) => /*#__PURE__*/React.createElement(FeedCard, {
    key: f.key,
    index: i + 1,
    name: f.name,
    description: f.description,
    url: f.url,
    formats: f.formats,
    status: f.status,
    items: f.items.slice(0, 3).map(({
      title,
      date,
      href
    }) => ({
      title,
      date,
      href
    }))
  }))), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: "var(--sp-16)"
    }
  }, /*#__PURE__*/React.createElement(SectionHeader, {
    eyebrow: "HELP",
    title: "How to Use RSS Feeds"
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "grid",
      gridTemplateColumns: "1fr 1fr",
      gap: "var(--sp-6)",
      marginTop: "var(--sp-6)"
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      background: "var(--surface)",
      border: "1px solid var(--border)",
      padding: "var(--sp-6)"
    }
  }, /*#__PURE__*/React.createElement("h4", {
    style: {
      margin: "0 0 var(--sp-3)"
    }
  }, "Popular RSS Readers"), /*#__PURE__*/React.createElement(HelpList, {
    rows: [["Feedly", "Web-based RSS reader"], ["Inoreader", "Feature-rich RSS service"], ["NewsBlur", "Social RSS reader"], ["RSS Guard", "Desktop RSS client"], ["NetNewsWire", "macOS/iOS RSS reader"]]
  })), /*#__PURE__*/React.createElement("div", {
    style: {
      background: "var(--surface)",
      border: "1px solid var(--border)",
      padding: "var(--sp-6)"
    }
  }, /*#__PURE__*/React.createElement("h4", {
    style: {
      margin: "0 0 var(--sp-3)"
    }
  }, "How to Subscribe"), /*#__PURE__*/React.createElement(HelpList, {
    ordered: true,
    rows: [["Copy", "the RSS feed URL from the card above"], ["Open", "your preferred RSS reader"], ["Add", "a new feed / subscription"], ["Paste", "the RSS URL"], ["Save", "and enjoy automatic updates"]]
  })))));
}
function HelpList({
  rows,
  ordered = false
}) {
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column"
    }
  }, rows.map(([lead, rest], i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    style: {
      display: "flex",
      gap: "12px",
      alignItems: "baseline",
      padding: "8px 0",
      borderTop: i === 0 ? "none" : "1px solid var(--ink-100)",
      fontSize: "var(--fs-14)"
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      fontFamily: "var(--font-mono)",
      fontSize: "var(--fs-12)",
      color: "var(--accent)",
      flex: "none",
      width: "22px"
    }
  }, ordered ? String(i + 1).padStart(2, "0") : "·"), /*#__PURE__*/React.createElement("span", null, /*#__PURE__*/React.createElement("strong", null, lead), " ", rest))));
}
Object.assign(window, {
  FeedsPage
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/FeedsPage.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/HomePage.jsx
try { (() => {
// Homepage: masthead + one full-width card per feed with entry previews.
const DS_HOME = window.RSSFeedHubDesignSystem_2f2da6;
function HomePage({
  onNav
}) {
  const {
    SectionHeader,
    FeedCard,
    Button
  } = DS_HOME;
  const feeds = window.RSSHUB_DATA.feeds;
  const totalEntries = feeds.reduce((n, f) => n + (f.status.entries || 0), 0);
  return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(Masthead, null), /*#__PURE__*/React.createElement("main", {
    style: {
      maxWidth: "var(--w-page)",
      margin: "0 auto",
      padding: "var(--sp-12) var(--sp-6) 0"
    }
  }, /*#__PURE__*/React.createElement(SectionHeader, {
    eyebrow: "FEEDS",
    title: "RSS Feeds",
    meta: `${feeds.length} FEEDS · ${totalEntries} ENTRIES`
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: "flex",
      flexDirection: "column",
      gap: "var(--sp-6)",
      marginTop: "var(--sp-6)"
    }
  }, feeds.map((f, i) => /*#__PURE__*/React.createElement(FeedCard, {
    key: f.key,
    index: i + 1,
    name: f.name,
    description: f.description,
    formats: f.formats,
    status: f.status,
    items: f.items
  }))), /*#__PURE__*/React.createElement("div", {
    style: {
      marginTop: "var(--sp-12)",
      borderTop: "var(--bw-rule) solid var(--border-strong)",
      paddingTop: "var(--sp-6)",
      display: "flex",
      alignItems: "center",
      justifyContent: "space-between",
      gap: "var(--sp-6)",
      flexWrap: "wrap"
    }
  }, /*#__PURE__*/React.createElement("p", {
    style: {
      margin: 0,
      maxWidth: "36rem"
    }
  }, "Need feed URLs, health details, or subscription help? The feeds page lists every format with copy-ready links."), /*#__PURE__*/React.createElement(Button, {
    variant: "outline-ink",
    onClick: () => onNav("feeds")
  }, "All feeds & formats"))));
}
Object.assign(window, {
  HomePage
});
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/HomePage.jsx", error: String((e && e.message) || e) }); }

// ui_kits/website/data.js
try { (() => {
// Shared sample data for the RSS Feed Hub UI kit.
// Feed registry mirrors _config.yml (enabled feeds only); status numbers
// mirror api/rss_status.json (2026-07-07 snapshot). Entry lists are sample
// rows in the shape the pipeline emits (priority + tech markers parsed
// from [ ! ] [ * ] [ ~ ] / [ ◻ ] [ ◼ ] [ ⬢ ] title suffixes).

window.RSSHUB_DATA = {
  site: {
    name: "RSS Feed Hub",
    description: "Curated RSS feeds for AI Insights and Technology News",
    url: "https://rss.tedt.org",
    github: "https://github.com/TedTschopp/rss.tedt.org",
    owner: "Ted Tschopp",
    statusTimestamp: "2026-07-07 18:08 UTC",
    overallStatus: "warning"
  },
  feeds: [{
    key: "ai_rss_feed",
    name: "Ted Tschopp's AI News",
    description: "Latest AI News and Ratings from Ted Tschopp",
    url: "https://rss.tedt.org/ai_rss_feed.xml",
    formats: {
      rss2: "/ai_rss_feed.xml",
      rss1: "/ai_rss_feed_rss1.xml",
      atom: "/ai_rss_feed.atom",
      json: "/ai_rss_feed.json"
    },
    status: {
      health: "healthy",
      entries: 50,
      updated: "2026-07-07"
    },
    items: [{
      title: "Building more with GPT-5.1-Codex-Max",
      date: "2026-07-07",
      priority: "essential",
      tech: "transformational",
      href: "#"
    }, {
      title: "Mixpanel security incident: what OpenAI users need to know",
      date: "2026-07-07",
      priority: "essential",
      tech: "important",
      href: "#"
    }, {
      title: "1 million business customers putting AI to work",
      date: "2026-07-06",
      priority: "important",
      tech: "important",
      href: "#"
    }, {
      title: "Wayfair boosts catalog accuracy and support speed with OpenAI",
      date: "2026-07-06",
      priority: "important",
      tech: "informational",
      href: "#"
    }, {
      title: "How Scania accelerates work with AI across its global workforce",
      date: "2026-07-05",
      priority: "optional",
      tech: "informational",
      href: "#"
    }]
  }, {
    key: "aggregated_wes_ai_news",
    name: "Wes's AI News",
    description: "Latest AI News and Commentary from Wes",
    url: "https://rss.tedt.org/aggregated_wes_ai_news.xml",
    formats: {
      rss2: "/aggregated_wes_ai_news.xml",
      rss1: "/aggregated_wes_ai_news_rss1.xml",
      atom: "/aggregated_wes_ai_news.atom",
      json: "/aggregated_wes_ai_news.json"
    },
    status: {
      health: "healthy",
      entries: 30,
      updated: "2026-07-07"
    },
    items: [{
      title: "Agentic coding tools compared: a week in the trenches",
      date: "2026-07-07",
      href: "#"
    }, {
      title: "Why local models keep winning the privacy argument",
      date: "2026-07-06",
      href: "#"
    }, {
      title: "The quiet death of the fine-tuning UI",
      date: "2026-07-05",
      href: "#"
    }]
  }, {
    key: "top_stories",
    name: "Top Stories (LLM Aggregated)",
    description: "Cross-source ranked stories with optional GitHub Models enrichment",
    url: "https://rss.tedt.org/feeds/top.xml",
    formats: {
      rss2: "/feeds/top.xml",
      rss1: "/feeds/top_rss1.xml",
      atom: "/feeds/top.atom",
      json: "/feeds/top.json"
    },
    status: {
      health: "healthy",
      entries: 80,
      updated: "2026-07-07"
    },
    items: [{
      title: "OpenAI raises $122 billion, and the floor on enterprise AI just moved",
      date: "2026-07-07",
      priority: "essential",
      tech: "transformational",
      href: "#"
    }, {
      title: "Samsung and SK join OpenAI's Stargate initiative",
      date: "2026-07-07",
      priority: "important",
      href: "#"
    }, {
      title: "Cerebras adds 750 MW of inference capacity to the regional mix",
      date: "2026-07-06",
      priority: "important",
      tech: "important",
      href: "#"
    }, {
      title: "Detecting and reducing scheming in frontier models",
      date: "2026-07-06",
      priority: "optional",
      tech: "informational",
      href: "#"
    }]
  }, {
    key: "aggregated_ea",
    name: "Enterprise Architecture Aggregated News",
    description: "Enterprise Architecture multi-source aggregated feed",
    url: "https://rss.tedt.org/aggregated_ea.xml",
    formats: {
      rss2: "/aggregated_ea.xml",
      rss1: "/aggregated_ea_rss1.xml",
      atom: "/aggregated_ea.atom",
      json: "/aggregated_ea.json"
    },
    status: {
      health: "healthy",
      entries: 26,
      updated: "2026-07-07"
    },
    items: [{
      title: "The Open Group publishes TOGAF guidance for AI governance",
      date: "2026-07-07",
      href: "#"
    }, {
      title: "Forrester: EA teams are becoming AI portfolio managers",
      date: "2026-07-06",
      href: "#"
    }, {
      title: "LeanIX on application rationalization after the M&A wave",
      date: "2026-07-04",
      href: "#"
    }]
  }, {
    key: "aggregated_broad_ai_news",
    name: "Broad AI News",
    description: "Broad AI ecosystem signals from labs, research, communities, and newsletters",
    url: "https://rss.tedt.org/aggregated_broad_ai_news.xml",
    formats: {
      rss2: "/aggregated_broad_ai_news.xml",
      rss1: "/aggregated_broad_ai_news_rss1.xml",
      atom: "/aggregated_broad_ai_news.atom",
      json: "/aggregated_broad_ai_news.json"
    },
    status: {
      health: "healthy",
      entries: 200,
      updated: "2026-07-07"
    },
    categories: ["AI Labs", "Hacker News", "Reddit", "arXiv", "Newsletters", "Extras"],
    items: [{
      title: "LLMs prefer resumes they generated themselves",
      date: "2026-07-07",
      href: "#"
    }, {
      title: "Show HN: an eval kit for agent traces",
      date: "2026-07-07",
      href: "#"
    }, {
      title: "SimpleQA keeps factuality evaluation intentionally narrow",
      date: "2026-07-06",
      href: "#"
    }, {
      title: "Mistral-Next quietly hits Hugging Face with permissive license",
      date: "2026-07-06",
      href: "#"
    }]
  }],
  // api/rss_status.json snapshot (real values, 2026-07-07)
  statusApi: {
    totalFiles: 8,
    healthyFiles: 6,
    totalEntries: 1081,
    pipeline: {
      apiItems: 80,
      stories: 2060,
      clusters: 2058,
      llmCalls: 11,
      llmOk: 11
    },
    aggregationHealth: [{
      feed: "aggregated_wes_ai_news.xml",
      sources: 1,
      attempted: 1,
      withItems: 1,
      failures: 0,
      failureRate: "0.00"
    }, {
      feed: "aggregated_ea.xml",
      sources: 7,
      attempted: 6,
      withItems: 5,
      failures: 1,
      failureRate: "16.67"
    }, {
      feed: "aggregated_broad_ai_news.xml",
      sources: 21,
      attempted: 14,
      withItems: 9,
      failures: 0,
      failureRate: "0.00"
    }]
  }
};
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/website/data.js", error: String((e && e.message) || e) }); }

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.Button = __ds_scope.Button;

__ds_ns.Input = __ds_scope.Input;

__ds_ns.Tag = __ds_scope.Tag;

__ds_ns.FeedCard = __ds_scope.FeedCard;

__ds_ns.FeedItem = __ds_scope.FeedItem;

__ds_ns.FormatButton = __ds_scope.FormatButton;

__ds_ns.FormatGroup = __ds_scope.FormatGroup;

__ds_ns.SectionHeader = __ds_scope.SectionHeader;

__ds_ns.StatusPill = __ds_scope.StatusPill;

})();
