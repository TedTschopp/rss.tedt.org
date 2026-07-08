/**
 * Feed-health status chip + mono meta ("50 entries | Updated: date").
 * Health derives from api/rss_status.json (exists && valid_xml → healthy).
 */
export interface StatusPillProps {
  /** @default "unknown" */
  status?: "healthy" | "warning" | "unknown" | "external";
  /** Entry count from status JSON */
  entries?: number;
  /** Human date string, e.g. "2026-07-07" */
  updated?: string;
  style?: React.CSSProperties;
}

export declare function StatusPill(props: StatusPillProps): JSX.Element;
