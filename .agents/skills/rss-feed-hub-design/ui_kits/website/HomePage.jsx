// Homepage: masthead + one full-width card per feed with entry previews.
const DS_HOME = window.RSSFeedHubDesignSystem_2f2da6;

function HomePage({ onNav }) {
  const { SectionHeader, FeedCard, Button } = DS_HOME;
  const feeds = window.RSSHUB_DATA.feeds;
  const totalEntries = feeds.reduce((n, f) => n + (f.status.entries || 0), 0);

  return (
    <div>
      <Masthead />
      <main style={{ maxWidth: "var(--w-page)", margin: "0 auto", padding: "var(--sp-12) var(--sp-6) 0" }}>
        <SectionHeader
          eyebrow="FEEDS"
          title="RSS Feeds"
          meta={`${feeds.length} FEEDS · ${totalEntries} ENTRIES`}
        />
        <div style={{ display: "flex", flexDirection: "column", gap: "var(--sp-6)", marginTop: "var(--sp-6)" }}>
          {feeds.map((f, i) => (
            <FeedCard
              key={f.key}
              index={i + 1}
              name={f.name}
              description={f.description}
              formats={f.formats}
              status={f.status}
              items={f.items}
            />
          ))}
        </div>
        <div style={{
          marginTop: "var(--sp-12)",
          borderTop: "var(--bw-rule) solid var(--border-strong)",
          paddingTop: "var(--sp-6)",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          gap: "var(--sp-6)",
          flexWrap: "wrap",
        }}>
          <p style={{ margin: 0, maxWidth: "36rem" }}>
            Need feed URLs, health details, or subscription help? The feeds page lists every format with copy-ready links.
          </p>
          <Button variant="outline-ink" onClick={() => onNav("feeds")}>All feeds &amp; formats</Button>
        </div>
      </main>
    </div>
  );
}

Object.assign(window, { HomePage });
