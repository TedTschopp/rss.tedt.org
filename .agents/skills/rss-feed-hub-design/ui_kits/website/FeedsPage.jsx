// Feeds directory: manager callout, 2-col feed cards with URL copy +
// status, and the "How to Use RSS Feeds" section.
const DS_FEEDS = window.RSSFeedHubDesignSystem_2f2da6;

function FeedsPage() {
  const { SectionHeader, FeedCard, Button } = DS_FEEDS;
  const feeds = window.RSSHUB_DATA.feeds;

  return (
    <main style={{ maxWidth: "var(--w-page)", margin: "0 auto", padding: "var(--sp-12) var(--sp-6) 0" }}>
      <h1 style={{
        fontFamily: "var(--font-sans)",
        fontWeight: 900,
        fontSize: "var(--fs-48)",
        letterSpacing: "-0.02em",
        lineHeight: 1.05,
        margin: 0,
      }}>RSS Feeds</h1>
      <p className="lead" style={{ maxWidth: "42rem", margin: "var(--sp-4) 0 0" }}>
        Subscribe to our curated RSS feeds to stay updated with the latest AI and technology news.
      </p>

      <div style={{
        marginTop: "var(--sp-6)",
        border: "1px solid var(--border)",
        borderTop: "var(--bw-rule) solid var(--orange-500)",
        background: "var(--surface)",
        padding: "var(--sp-4) var(--sp-6)",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        gap: "var(--sp-4)",
        flexWrap: "wrap",
      }}>
        <p style={{ margin: 0, fontSize: "var(--fs-14)" }}>
          <strong>Managing Top Stories inputs?</strong> Use the Top Stories Manager to edit included feeds and adjust ranking weights.
        </p>
        <Button size="sm" variant="outline">Open Top Stories Manager</Button>
      </div>

      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(420px, 1fr))",
        gap: "var(--sp-6)",
        marginTop: "var(--sp-8)",
      }}>
        {feeds.map((f, i) => (
          <FeedCard
            key={f.key}
            index={i + 1}
            name={f.name}
            description={f.description}
            url={f.url}
            formats={f.formats}
            status={f.status}
            items={f.items.slice(0, 3).map(({ title, date, href }) => ({ title, date, href }))}
          />
        ))}
      </div>

      <div style={{ marginTop: "var(--sp-16)" }}>
        <SectionHeader eyebrow="HELP" title="How to Use RSS Feeds" />
        <div style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "var(--sp-6)",
          marginTop: "var(--sp-6)",
        }}>
          <div style={{ background: "var(--surface)", border: "1px solid var(--border)", padding: "var(--sp-6)" }}>
            <h4 style={{ margin: "0 0 var(--sp-3)" }}>Popular RSS Readers</h4>
            <HelpList rows={[
              ["Feedly", "Web-based RSS reader"],
              ["Inoreader", "Feature-rich RSS service"],
              ["NewsBlur", "Social RSS reader"],
              ["RSS Guard", "Desktop RSS client"],
              ["NetNewsWire", "macOS/iOS RSS reader"],
            ]} />
          </div>
          <div style={{ background: "var(--surface)", border: "1px solid var(--border)", padding: "var(--sp-6)" }}>
            <h4 style={{ margin: "0 0 var(--sp-3)" }}>How to Subscribe</h4>
            <HelpList ordered rows={[
              ["Copy", "the RSS feed URL from the card above"],
              ["Open", "your preferred RSS reader"],
              ["Add", "a new feed / subscription"],
              ["Paste", "the RSS URL"],
              ["Save", "and enjoy automatic updates"],
            ]} />
          </div>
        </div>
      </div>
    </main>
  );
}

function HelpList({ rows, ordered = false }) {
  return (
    <div style={{ display: "flex", flexDirection: "column" }}>
      {rows.map(([lead, rest], i) => (
        <div key={i} style={{
          display: "flex",
          gap: "12px",
          alignItems: "baseline",
          padding: "8px 0",
          borderTop: i === 0 ? "none" : "1px solid var(--ink-100)",
          fontSize: "var(--fs-14)",
        }}>
          <span style={{
            fontFamily: "var(--font-mono)",
            fontSize: "var(--fs-12)",
            color: "var(--accent)",
            flex: "none",
            width: "22px",
          }}>{ordered ? String(i + 1).padStart(2, "0") : "·"}</span>
          <span><strong>{lead}</strong> {rest}</span>
        </div>
      ))}
    </div>
  );
}

Object.assign(window, { FeedsPage });
