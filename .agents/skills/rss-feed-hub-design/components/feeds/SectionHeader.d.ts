/**
 * Swiss section header: 2px ink top rule, mono orange eyebrow, bold title,
 * optional mono meta or action element right-aligned on the baseline.
 */
export interface SectionHeaderProps {
  /** Mono uppercase kicker above the title, e.g. "FEEDS" */
  eyebrow?: string;
  title: React.ReactNode;
  /** Mono data string on the right, e.g. "5 FEEDS · 386 ENTRIES" */
  meta?: React.ReactNode;
  /** Right-aligned element (e.g. a Button) — overrides meta placement */
  action?: React.ReactNode;
  style?: React.CSSProperties;
}

export declare function SectionHeader(props: SectionHeaderProps): JSX.Element;
