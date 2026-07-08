/**
 * Category tag — mono, hairline-bordered, square. For source categories
 * (AI Labs, Reddit, arXiv…) and filter facets.
 */
export interface TagProps {
  /** Filled navy when the facet is selected. @default false */
  active?: boolean;
  /** Makes the tag clickable (filter behavior) */
  onClick?: () => void;
  children?: React.ReactNode;
  style?: React.CSSProperties;
}

export declare function Tag(props: TagProps): JSX.Element;
