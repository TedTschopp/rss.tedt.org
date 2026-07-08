/**
 * Square text input with optional mono copy-URL mode (readonly value +
 * copy button that flips to a green check for 2s — live-site behavior).
 */
export interface InputProps {
  value?: string;
  defaultValue?: string;
  onChange?: (e: any) => void;
  placeholder?: string;
  /** Mono uppercase eyebrow above the field */
  label?: string;
  readOnly?: boolean;
  /** Copy-URL group: mono readonly field + Copy button. @default false */
  copyable?: boolean;
  /** @default "md" */
  size?: "sm" | "md";
  /** @default "text" */
  type?: string;
  style?: React.CSSProperties;
}

export declare function Input(props: InputProps): JSX.Element;
