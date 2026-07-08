// Site chrome: NavBar, Masthead, Footer.
const DS_CHROME = window.RSSFeedHubDesignSystem_2f2da6;

function NavBar({ current, onNav }) {
  const links = [
    { id: "home", label: "Home" },
    { id: "feeds", label: "RSS Feeds" },
    { id: "about", label: "About" },
  ];
  return (
    <nav style={{
      background: "var(--surface)",
      borderBottom: "1px solid var(--border)",
      position: "sticky",
      top: 0,
      zIndex: 100,
    }}>
      <div style={{
        maxWidth: "var(--w-page)",
        margin: "0 auto",
        padding: "0 var(--sp-6)",
        display: "flex",
        alignItems: "stretch",
        gap: "var(--sp-6)",
        height: "64px",
      }}>
        <a
          href="#home"
          onClick={(e) => { e.preventDefault(); onNav("home"); }}
          style={{ display: "flex", alignItems: "center", gap: "10px", textDecoration: "none", marginRight: "auto" }}
        >
          <img src="../../assets/logo.png" alt="RSS Feed Hub" width="32" height="32" />
          <span style={{
            fontFamily: "var(--font-sans)",
            fontWeight: 900,
            fontSize: "18px",
            letterSpacing: "-0.01em",
            color: "var(--navy-500)",
            lineHeight: 1,
            textTransform: "uppercase",
          }}>RSS Feed Hub</span>
        </a>
        {links.map((l) => (
          <NavLink key={l.id} active={current === l.id} onClick={() => onNav(l.id)}>{l.label}</NavLink>
        ))}
        <NavLink href="https://github.com/TedTschopp/rss.tedt.org">
          <i className="fab fa-github" aria-hidden="true" style={{ marginRight: "6px" }}></i>GitHub
        </NavLink>
      </div>
    </nav>
  );
}

function NavLink({ active, onClick, href, children }) {
  const [hover, setHover] = React.useState(false);
  return (
    <a
      href={href || "#"}
      target={href ? "_blank" : undefined}
      rel={href ? "noopener" : undefined}
      onClick={href ? undefined : (e) => { e.preventDefault(); onClick(); }}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        display: "flex",
        alignItems: "center",
        fontFamily: "var(--font-sans)",
        fontSize: "var(--fs-14)",
        fontWeight: 600,
        color: active ? "var(--text-heading)" : hover ? "var(--text-heading)" : "var(--text-muted)",
        textDecoration: "none",
        borderBottom: `3px solid ${active ? "var(--orange-500)" : "transparent"}`,
        borderTop: "3px solid transparent",
        transition: "color var(--dur-1) var(--ease)",
      }}
    >
      {children}
    </a>
  );
}

function Masthead() {
  const site = window.RSSHUB_DATA.site;
  const feeds = window.RSSHUB_DATA.feeds;
  const totalEntries = feeds.reduce((n, f) => n + (f.status.entries || 0), 0);
  return (
    <header style={{ borderBottom: "1px solid var(--border)", background: "var(--bg)" }}>
      <div style={{ maxWidth: "var(--w-page)", margin: "0 auto", padding: "var(--sp-12) var(--sp-6) var(--sp-8)" }}>
        <div style={{
          fontFamily: "var(--font-mono)",
          fontSize: "var(--fs-12)",
          letterSpacing: "var(--tr-eyebrow)",
          textTransform: "uppercase",
          color: "var(--accent)",
          marginBottom: "var(--sp-3)",
        }}>rss.tedt.org</div>
        <h1 style={{
          fontFamily: "var(--font-sans)",
          fontWeight: 900,
          fontSize: "clamp(48px, 8vw, 88px)",
          lineHeight: 0.95,
          letterSpacing: "-0.02em",
          textTransform: "uppercase",
          color: "var(--text-heading)",
          margin: 0,
        }}>
          RSS Feed<br />Hub<span style={{ color: "var(--orange-500)" }}>.</span>
        </h1>
        <div style={{
          display: "flex",
          alignItems: "flex-end",
          justifyContent: "space-between",
          gap: "var(--sp-6)",
          flexWrap: "wrap",
          marginTop: "var(--sp-6)",
        }}>
          <p style={{ fontSize: "var(--fs-18)", maxWidth: "42rem", margin: 0 }}>{site.description}. Aggregated, ranked, and monitored automatically — subscribe in the format your reader speaks.</p>
          <span style={{ fontFamily: "var(--font-mono)", fontSize: "var(--fs-12)", color: "var(--text-muted)", whiteSpace: "nowrap" }}>
            {feeds.length} FEEDS · {totalEntries} ENTRIES · UPDATED {feeds[0].status.updated}
          </span>
        </div>
      </div>
    </header>
  );
}

function Footer({ onNav }) {
  const site = window.RSSHUB_DATA.site;
  const feeds = window.RSSHUB_DATA.feeds;
  return (
    <footer style={{ background: "var(--navy-500)", color: "#fff", marginTop: "var(--sp-16)" }}>
      <div style={{
        maxWidth: "var(--w-page)",
        margin: "0 auto",
        padding: "var(--sp-8) var(--sp-6)",
        display: "grid",
        gridTemplateColumns: "2fr 1fr 1fr",
        gap: "var(--sp-8)",
      }}>
        <div>
          <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "var(--sp-3)" }}>
            <img src="../../assets/logo.png" alt="" width="28" height="28" />
            <span style={{ fontWeight: 900, fontSize: "16px", textTransform: "uppercase", letterSpacing: "-0.01em" }}>{site.name}</span>
          </div>
          <p style={{ fontSize: "var(--fs-14)", color: "var(--text-on-dark-muted)", maxWidth: "30rem", margin: 0 }}>{site.description}</p>
        </div>
        <div>
          <FooterHead>RSS Feeds</FooterHead>
          {feeds.map((f) => <FooterLink key={f.key} href={f.url}>{f.name}</FooterLink>)}
        </div>
        <div>
          <FooterHead>Site</FooterHead>
          <FooterLink onClick={() => onNav("home")}>Home</FooterLink>
          <FooterLink onClick={() => onNav("feeds")}>RSS Feeds</FooterLink>
          <FooterLink onClick={() => onNav("about")}>About</FooterLink>
          <FooterLink href={site.github}>Source Code</FooterLink>
          <FooterLink href="#">Status JSON</FooterLink>
        </div>
      </div>
      <div style={{ borderTop: "1px solid rgba(255,255,255,0.2)" }}>
        <div style={{
          maxWidth: "var(--w-page)",
          margin: "0 auto",
          padding: "var(--sp-4) var(--sp-6)",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: "var(--sp-4)",
          flexWrap: "wrap",
        }}>
          <span style={{ fontFamily: "var(--font-mono)", fontSize: "var(--fs-12)", color: "var(--text-on-dark-muted)" }}>© 2026 {site.owner}. All rights reserved.</span>
          <span style={{ fontFamily: "var(--font-mono)", fontSize: "var(--fs-12)", color: "var(--text-on-dark-muted)" }}>
            <i className="fab fa-github" aria-hidden="true" style={{ marginRight: "8px" }}></i>Powered by Jekyll
          </span>
        </div>
      </div>
    </footer>
  );
}

function FooterHead({ children }) {
  return <div style={{
    fontFamily: "var(--font-mono)",
    fontSize: "var(--fs-12)",
    letterSpacing: "var(--tr-eyebrow)",
    textTransform: "uppercase",
    color: "var(--text-on-dark-muted)",
    marginBottom: "var(--sp-3)",
  }}>{children}</div>;
}

function FooterLink({ href, onClick, children }) {
  const [hover, setHover] = React.useState(false);
  return (
    <a
      href={href || "#"}
      onClick={onClick ? (e) => { e.preventDefault(); onClick(); } : undefined}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        display: "block",
        fontSize: "var(--fs-14)",
        color: hover ? "#fff" : "rgba(255,255,255,0.75)",
        textDecoration: hover ? "underline" : "none",
        textUnderlineOffset: "0.15em",
        marginBottom: "8px",
        transition: "color var(--dur-1) var(--ease)",
      }}
    >{children}</a>
  );
}

Object.assign(window, { NavBar, Masthead, Footer });
