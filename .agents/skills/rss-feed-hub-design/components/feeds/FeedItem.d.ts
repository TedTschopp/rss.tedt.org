/**
 * One feed entry row: priority/tech badges, bold title link, mono date.
 * Prioritized rows get an 8–12% tint + 3px left bar (live-site treatment).
 */
export interface FeedItemProps {
  title: string;
  /** @default "#" */
  href?: string;
  /** ISO date shown in mono parens, e.g. "2026-07-07" */
  date?: string;
  /** Business priority from [ ! ] [ * ] [ ~ ] markers */
  priority?: "essential" | "important" | "optional";
  /** Technical impact from [ ⬢ ] [ ◼ ] [ ◻ ] markers */
  tech?: "transformational" | "important" | "informational";
  style?: React.CSSProperties;
}

export declare function FeedItem(props: FeedItemProps): JSX.Element;
