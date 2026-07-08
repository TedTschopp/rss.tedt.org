import type { FeedItemProps } from "./FeedItem";

/**
 * One card per feed: mono index + 2px ink top rule, name, description,
 * format buttons, copy-URL group, health status, recent-entries preview.
 */
export interface FeedCardProps {
  /** Renders as zero-padded mono counter ("01") */
  index?: number;
  name: string;
  description?: string;
  /** Absolute feed URL for the copy group */
  url?: string;
  /** Format → URL map; renders a FormatGroup */
  formats?: { rss2?: string; rss1?: string; atom?: string; json?: string };
  /** From api/rss_status.json */
  status?: { health: "healthy" | "warning" | "unknown" | "external"; entries?: number; updated?: string };
  /** Recent entries preview */
  items?: FeedItemProps[];
  /** @default "Recent Entries" */
  previewLabel?: string;
  style?: React.CSSProperties;
}

export declare function FeedCard(props: FeedCardProps): JSX.Element;
