/* Shared Tweaks panel for all UI kits — controls font set + accent color.
   Requires: React, Babel, tweaks-panel.jsx, font-tweaks.js to be loaded first. */

const { useState: useStateT, useEffect: useEffectT } = React;

window.YIATweaks = function YIATweaks({ defaults }) {
  const [t, setTweak] = useTweaks(defaults);

  useEffectT(() => {
    applyFontSet(t.fontSet);
  }, [t.fontSet]);

  useEffectT(() => {
    document.documentElement.style.setProperty("--accent", t.accent);
  }, [t.accent]);

  return (
    <TweaksPanel title="Tweaks">
      <TweakSection label="Typography" />
      <TweakRadio
        label="Font set"
        value={t.fontSet}
        options={["original", "tedt"]}
        onChange={(v) => setTweak("fontSet", v)}
      />
      <div style={{
        fontSize: 10.5, lineHeight: 1.4, color: "rgba(41,38,27,.55)",
        padding: "2px 0 4px", fontFamily: "ui-sans-serif, system-ui",
      }}>
        {window.YIA_FONT_SETS[t.fontSet]?.note}
      </div>
      <TweakSection label="Accent" />
      <TweakColor
        label="Signal color"
        value={t.accent}
        onChange={(v) => setTweak("accent", v)}
      />
    </TweaksPanel>
  );
};

window.YIA_TWEAK_DEFAULTS = {
  fontSet: "original",
  accent: "#D9531E",
};
