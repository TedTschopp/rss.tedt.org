/**
 * Priority / tech-impact / feed-health badge. Uppercase, 3px radius, colors
 * verbatim from the live site. Default label comes from the kind.
 */
export interface BadgeProps {
  /**
   * Business priority ([ ! ] [ * ] [ ~ ]), technical impact ([ ⬢ ] [ ◼ ] [ ◻ ]),
   * or feed health. @default "optional"
   */
  kind?:
    | "essential"
    | "important"
    | "optional"
    | "tech-informational"
    | "tech-important"
    | "tech-transformational"
    | "healthy"
    | "warning"
    | "unknown";
  /** Override the default label text */
  children?: React.ReactNode;
  style?: React.CSSProperties;
}

export declare function Badge(props: BadgeProps): JSX.Element;
