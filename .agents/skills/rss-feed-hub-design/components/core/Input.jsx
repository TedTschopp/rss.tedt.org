import React from "react";

/**
 * Square text input. With `copyable`, renders the live site's copy-URL
 * group: readonly value + a copy button that flips to a success check.
 */
export function Input({
  value,
  defaultValue,
  onChange,
  placeholder,
  label,
  readOnly = false,
  copyable = false,
  size = "md",
  type = "text",
  style,
}) {
  const [focus, setFocus] = React.useState(false);
  const [copied, setCopied] = React.useState(false);
  const dims = size === "sm"
    ? { font: "var(--fs-12)", pad: "5px 8px" }
    : { font: "var(--fs-14)", pad: "8px 10px" };

  const copy = () => {
    const text = value != null ? value : defaultValue;
    if (navigator.clipboard && text) navigator.clipboard.writeText(String(text));
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const inputEl = (
    <input
      type={type}
      value={value}
      defaultValue={defaultValue}
      onChange={onChange}
      placeholder={placeholder}
      readOnly={readOnly || copyable}
      onFocus={() => setFocus(true)}
      onBlur={() => setFocus(false)}
      style={{
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
        transition: "border-color var(--dur-1) var(--ease)",
      }}
    />
  );

  return (
    <label style={{ display: "block", ...style }}>
      {label ? (
        <span style={{
          display: "block",
          fontFamily: "var(--font-mono)",
          fontSize: "var(--fs-12)",
          letterSpacing: "var(--tr-eyebrow)",
          textTransform: "uppercase",
          color: "var(--text-muted)",
          marginBottom: "6px",
        }}>{label}</span>
      ) : null}
      <span style={{ display: "flex" }}>
        {inputEl}
        {copyable ? (
          <button
            type="button"
            onClick={copy}
            aria-label="Copy to clipboard"
            style={{
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
              whiteSpace: "nowrap",
            }}
          >
            <i className={copied ? "fas fa-check" : "fas fa-copy"} aria-hidden="true"></i>
            {copied ? "Copied!" : "Copy"}
          </button>
        ) : null}
      </span>
    </label>
  );
}
