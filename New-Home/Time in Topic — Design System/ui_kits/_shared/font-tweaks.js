/* Yesterday in AI — Font tweak controller.
   Loads tedt.org-aligned fonts in addition to the originals,
   then swaps the --font-* CSS variables based on user choice. */

/* Add font imports for tedt.org-aligned set (originals already loaded by colors_and_type.css) */
(function loadTedtFonts() {
  if (document.getElementById("yia-tedt-fonts")) return;
  const link = document.createElement("link");
  link.id = "yia-tedt-fonts";
  link.rel = "stylesheet";
  link.href = "https://fonts.googleapis.com/css2?family=Cal+Sans&family=Inter:wght@400;500;600;700&family=Fira+Code:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap";
  document.head.appendChild(link);
})();

const FONT_SETS = {
  original: {
    label: "Original",
    sans:  '"Inter Tight", -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif',
    serif: '"Source Serif 4", "Iowan Old Style", Georgia, "Times New Roman", serif',
    mono:  '"JetBrains Mono", "SF Mono", ui-monospace, "Roboto Mono", Menlo, Consolas, monospace',
    display: '"Source Serif 4", "Iowan Old Style", Georgia, serif',
    note: "Source Serif 4 + Inter Tight + JetBrains Mono",
  },
  tedt: {
    label: "tedt.org",
    sans:  'Inter, "Noto Sans", "Helvetica Neue", -apple-system, system-ui, sans-serif',
    serif: '"Libre Baskerville", "Iowan Old Style", Georgia, serif',
    mono:  '"Fira Code", SFMono-Regular, Menlo, Monaco, Consolas, monospace',
    display: '"Cal Sans", "Titillium Web", "Optima", "Arsenal", sans-serif',
    note: "Cal Sans (display) + Libre Baskerville (prose) + Inter + Fira Code",
  },
};

function applyFontSet(key) {
  const set = FONT_SETS[key] || FONT_SETS.original;
  const r = document.documentElement.style;
  r.setProperty("--font-sans",    set.sans);
  r.setProperty("--font-serif",   set.serif);
  r.setProperty("--font-mono",    set.mono);
  r.setProperty("--font-display", set.display);
}
window.YIA_FONT_SETS = FONT_SETS;
window.applyFontSet = applyFontSet;
