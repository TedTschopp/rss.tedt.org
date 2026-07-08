/**
 * Outline button in the fixed syndication-format brand color; fills on
 * hover. RSS 2.0 #FF6600 · RSS 1.0 #F88920 · Atom #8b5cf6 · JSON #292929→gold.
 */
export interface FormatButtonProps {
  /** @default "rss2" */
  format?: "rss2" | "rss1" | "atom" | "json";
  /** Feed URL. @default "#" */
  href?: string;
  /** @default "sm" */
  size?: "sm" | "md";
  style?: React.CSSProperties;
}

export declare function FormatButton(props: FormatButtonProps): JSX.Element;

/** Row of FormatButtons in canonical order (rss2, rss1, atom, json). */
export interface FormatGroupProps {
  /** Map of format → URL; missing keys are skipped */
  formats: { rss2?: string; rss1?: string; atom?: string; json?: string };
  /** @default "sm" */
  size?: "sm" | "md";
  style?: React.CSSProperties;
}

export declare function FormatGroup(props: FormatGroupProps): JSX.Element;
