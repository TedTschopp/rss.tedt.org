/**
 * Flat, square Swiss button. Outline variants fill with their border color
 * on hover; solids darken one step. No radius, no shadow, no transforms.
 */
export interface ButtonProps {
  /** Visual style. Solid navy is the primary action. @default "primary" */
  variant?: "primary" | "accent" | "outline" | "outline-accent" | "outline-ink" | "ghost";
  /** @default "md" */
  size?: "sm" | "md" | "lg";
  /** Font Awesome class, e.g. "fas fa-rss" */
  icon?: string;
  /** Render as <a> */
  href?: string;
  target?: string;
  disabled?: boolean;
  onClick?: () => void;
  style?: React.CSSProperties;
  children?: React.ReactNode;
}

export declare function Button(props: ButtonProps): JSX.Element;
