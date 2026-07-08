// About page: prose column + stats/links sidebar.
const DS_ABOUT = window.RSSFeedHubDesignSystem_2f2da6;

function AboutPage() {
  const { SectionHeader, Badge, Tag } = DS_ABOUT;
  const { site, feeds, statusApi } = window.RSSHUB_DATA;

  return (
    <main style={{ maxWidth: "var(--w-page)", margin: "0 auto", padding: "var(--sp-12) var(--sp-6) 0" }}>
      <h1 style={{
        fontFamily: "var(--font-sans)",
        fontWeight: 900,
        fontSize: "var(--fs-48)",
        letterSpacing: "-0.02em",
        lineHeight: 1.05,
        margin: 0,
      }}>About RSS Feed Hub</h1>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 320px", gap: "var(--sp-8)", marginTop: "var(--sp-6)", alignItems: "start" }}>
        <div style={{ maxWidth: "var(--w-prose)", display: "flex", flexDirection: "column", gap: "var(--sp-8)" }}>
          <p className="lead" style={{ margin: 0 }}>
            Welcome to RSS Feed Hub, your centralized source for curated AI and technology news feeds. This site automatically aggregates and monitors RSS feeds from various sources to keep you updated with the latest developments in artificial intelligence and technology.
          </p>

          <section>
            <SectionHeader title="How It Works" />
            <div style={{ marginTop: "var(--sp-4)", display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1px", background: "var(--border)", border: "1px solid var(--border)" }}>
              <HowCell n="01" t="Scrape Content" d="Automatically extract articles and news from target websites" />
              <HowCell n="02" t="Generate RSS" d="Convert scraped content into standard RSS feed format" />
              <HowCell n="03" t="Monitor Health" d="Continuously check feed status and entry counts" />
              <HowCell n="04" t="Update Regularly" d="Refresh content on a scheduled basis via GitHub Actions" />
            </div>
          </section>

          <section>
            <SectionHeader title="Priority Badges" />
            <p style={{ margin: "var(--sp-4) 0 0", fontSize: "var(--fs-14)" }}>
              Feed entries can include priority markers in their titles, converted to visual badges:
            </p>
            <div style={{ marginTop: "var(--sp-3)", border: "1px solid var(--border)", background: "var(--surface)" }}>
              <BadgeRow sym="[ ! ]" badge={<Badge kind="essential" />} d="Critical or urgent content" />
              <BadgeRow sym="[ * ]" badge={<Badge kind="important" />} d="High-priority content" />
              <BadgeRow sym="[ ~ ]" badge={<Badge kind="optional" />} d="Supplementary or nice-to-know content" />
              <BadgeRow sym="[ ⬢ ]" badge={<Badge kind="tech-transformational" />} d="Forces rethinking architecture/governance patterns" />
              <BadgeRow sym="[ ◼ ]" badge={<Badge kind="tech-important" />} d="Likely to change how teams build/run AI systems" />
              <BadgeRow sym="[ ◻ ]" badge={<Badge kind="tech-informational" />} d="Awareness-level technical signal" last />
            </div>
          </section>

          <section>
            <SectionHeader title="Broad AI News Sources" />
            <p style={{ margin: "var(--sp-4) 0 var(--sp-3)", fontSize: "var(--fs-14)" }}>
              The widest feed pulls from 21 sources across six categories:
            </p>
            <div style={{ display: "flex", gap: "6px", flexWrap: "wrap" }}>
              {feeds[4].categories.map((c) => <Tag key={c}>{c}</Tag>)}
            </div>
          </section>

          <section>
            <SectionHeader title="Technical Details" />
            <div style={{ marginTop: "var(--sp-4)", display: "flex", flexDirection: "column" }}>
              <TechRow k="Python" v="Web scraping with Beautiful Soup and Playwright" first />
              <TechRow k="GitHub Actions" v="Automated workflow execution, every 8 hours" />
              <TechRow k="GitHub Models" v="Optional LLM enrichment for Top Stories ranking" />
              <TechRow k="Jekyll" v="Static site generation" />
              <TechRow k="RSS · Atom · JSON" v="Standard syndication formats" />
            </div>
          </section>
        </div>

        <aside style={{ display: "flex", flexDirection: "column", gap: "var(--sp-6)", position: "sticky", top: "88px" }}>
          <div style={{ background: "var(--navy-500)", color: "#fff", padding: "var(--sp-6)" }}>
            <div style={{
              fontFamily: "var(--font-mono)",
              fontSize: "var(--fs-12)",
              letterSpacing: "var(--tr-eyebrow)",
              textTransform: "uppercase",
              color: "rgba(255,255,255,0.6)",
              marginBottom: "var(--sp-4)",
            }}>Quick Stats</div>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "var(--sp-4)" }}>
              <Stat n={statusApi.totalFiles} l="feed files" />
              <Stat n={statusApi.healthyFiles} l="healthy" accent />
              <Stat n={statusApi.totalEntries.toLocaleString()} l="total entries" wide />
              <Stat n={statusApi.pipeline.stories.toLocaleString()} l="stories indexed" wide />
            </div>
            <div style={{
              marginTop: "var(--sp-4)",
              paddingTop: "var(--sp-3)",
              borderTop: "1px solid rgba(255,255,255,0.2)",
              fontFamily: "var(--font-mono)",
              fontSize: "var(--fs-12)",
              color: "rgba(255,255,255,0.6)",
            }}>Last updated: {site.statusTimestamp}</div>
          </div>

          <div style={{ background: "var(--surface)", border: "1px solid var(--border)", padding: "var(--sp-6)" }}>
            <div style={{
              fontFamily: "var(--font-mono)",
              fontSize: "var(--fs-12)",
              letterSpacing: "var(--tr-eyebrow)",
              textTransform: "uppercase",
              color: "var(--text-muted)",
              marginBottom: "var(--sp-3)",
            }}>Useful Links</div>
            <SideLink icon="fab fa-github" label="Source Code" />
            <SideLink icon="fas fa-file-code" label="Status JSON" />
            {feeds.map((f) => <SideLink key={f.key} icon="fas fa-rss" label={f.name} />)}
          </div>
        </aside>
      </div>
    </main>
  );
}

function HowCell({ n, t, d }) {
  return (
    <div style={{ background: "var(--surface)", padding: "var(--sp-4)" }}>
      <div style={{ fontFamily: "var(--font-mono)", fontSize: "var(--fs-12)", color: "var(--accent)", marginBottom: "6px" }}>{n}</div>
      <div style={{ fontWeight: 700, fontSize: "var(--fs-16)", color: "var(--text-heading)" }}>{t}</div>
      <div style={{ fontSize: "var(--fs-14)", color: "var(--text-muted)", marginTop: "4px" }}>{d}</div>
    </div>
  );
}

function BadgeRow({ sym, badge, d, last = false }) {
  return (
    <div style={{
      display: "flex",
      alignItems: "center",
      gap: "var(--sp-4)",
      padding: "10px var(--sp-4)",
      borderBottom: last ? "none" : "1px solid var(--ink-100)",
      fontSize: "var(--fs-14)",
    }}>
      <code style={{ flex: "none", width: "44px", textAlign: "center" }}>{sym}</code>
      <span style={{ flex: "none", width: "160px" }}>{badge}</span>
      <span style={{ color: "var(--text-muted)" }}>{d}</span>
    </div>
  );
}

function TechRow({ k, v, first = false }) {
  return (
    <div style={{
      display: "flex",
      gap: "var(--sp-4)",
      padding: "8px 0",
      borderTop: first ? "none" : "1px solid var(--ink-100)",
      fontSize: "var(--fs-14)",
    }}>
      <strong style={{ flex: "none", width: "150px", color: "var(--text-heading)" }}>{k}</strong>
      <span style={{ color: "var(--text-muted)" }}>{v}</span>
    </div>
  );
}

function Stat({ n, l, accent = false, wide = false }) {
  return (
    <div style={{ gridColumn: wide ? "1 / -1" : "auto" }}>
      <div style={{
        fontFamily: "var(--font-mono)",
        fontWeight: 600,
        fontSize: "var(--fs-28)",
        lineHeight: 1.1,
        color: accent ? "var(--cyan-500)" : "#fff",
      }}>{n}</div>
      <div style={{ fontFamily: "var(--font-mono)", fontSize: "var(--fs-12)", color: "rgba(255,255,255,0.6)" }}>{l}</div>
    </div>
  );
}

function SideLink({ icon, label }) {
  const [hover, setHover] = React.useState(false);
  return (
    <a
      href="#"
      onClick={(e) => e.preventDefault()}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        display: "flex",
        alignItems: "center",
        gap: "10px",
        fontSize: "var(--fs-14)",
        color: hover ? "var(--accent)" : "var(--navy-500)",
        textDecoration: hover ? "underline" : "none",
        textUnderlineOffset: "0.15em",
        padding: "5px 0",
        transition: "color var(--dur-1) var(--ease)",
      }}
    >
      <i className={icon} aria-hidden="true" style={{ width: "16px", textAlign: "center", fontSize: "13px" }}></i>
      {label}
    </a>
  );
}

Object.assign(window, { AboutPage });
