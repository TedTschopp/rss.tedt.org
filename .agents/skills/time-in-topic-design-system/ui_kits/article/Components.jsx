/* Article detail components */
const { useState: useStateA } = React;

function ArticleHeader() {
  return (
    <header style={ah.bar}>
      <div style={ah.inner}>
        <a href="../website/index.html" style={ah.brand}>
          <Wordmark height={24} />
        </a>
        <a href="../website/index.html" style={ah.back}>← All stories</a>
      </div>
    </header>
  );
}
const ah = {
  bar: { position:"sticky", top:0, zIndex:10, background:"rgba(251,250,247,0.85)", backdropFilter:"blur(8px)", borderBottom:"1px solid var(--border-soft)" },
  inner: { maxWidth:760, margin:"0 auto", padding:"14px 32px", display:"flex", alignItems:"center", justifyContent:"space-between" },
  brand: { display:"flex" },
  back: { fontFamily:"var(--font-mono)", fontSize:12, color:"var(--fg-muted)", textDecoration:"none", letterSpacing:"0.04em", whiteSpace:"nowrap" }
};

function ArticleHero({ section, story, date }) {
  return (
    <div style={hero.wrap}>
      <div style={hero.meta}>
        <span style={{...hero.tag, color: section.color}}>{section.tag}</span>
        <span style={hero.dot}>·</span>
        <span style={hero.date}>{date}</span>
        <span style={hero.dot}>·</span>
        <span style={hero.read}>5 min read</span>
      </div>
      <h1 style={hero.h1}>{story.headline}</h1>
      <p style={hero.lede}>{story.why}</p>
      <div style={hero.actions}>
        <button style={hero.btnPrimary}>Save story</button>
        <button style={hero.btnGhost}><i data-lucide="share-2" style={{width:14,height:14}}></i> Share</button>
        <a href={story.source.url} style={hero.btnAccent} target="_blank" rel="noreferrer">{story.source.name} <i data-lucide="arrow-up-right" style={{width:13,height:13,marginLeft:2}}></i></a>
      </div>
    </div>
  );
}
const hero = {
  wrap: { padding:"56px 0 40px", borderBottom:"1px solid var(--border)" },
  meta: { display:"flex", alignItems:"center", gap:10, marginBottom:20, flexWrap:"wrap" },
  tag: { fontFamily:"var(--font-mono)", fontSize:11, fontWeight:500, letterSpacing:"0.08em", textTransform:"uppercase", padding:"5px 10px", border:"1px solid var(--border)", borderRadius:999, whiteSpace:"nowrap" },
  dot: { color:"var(--fg-faint)" },
  date: { fontFamily:"var(--font-mono)", fontSize:12, color:"var(--fg-muted)", whiteSpace:"nowrap" },
  read: { fontFamily:"var(--font-mono)", fontSize:12, color:"var(--fg-muted)", whiteSpace:"nowrap" },
  h1: { fontFamily:"var(--font-display)", fontWeight:700, fontSize:48, lineHeight:1.08, letterSpacing:"-0.03em", color:"var(--fg)", margin:"0 0 20px" },
  lede: { fontFamily:"var(--font-serif)", fontSize:22, lineHeight:1.5, color:"var(--fg-body)", margin:"0 0 28px", maxWidth:680 },
  actions: { display:"flex", gap:10, alignItems:"center" },
  btnPrimary: { background:"var(--ink-900)", color:"var(--ink-0)", border:"none", borderRadius:4, padding:"10px 14px", fontFamily:"var(--font-sans)", fontSize:14, fontWeight:500, cursor:"pointer", whiteSpace:"nowrap" },
  btnGhost: { background:"transparent", color:"var(--fg)", border:"1px solid var(--border-strong)", borderRadius:4, padding:"9px 14px", fontFamily:"var(--font-sans)", fontSize:14, cursor:"pointer", display:"inline-flex", alignItems:"center", gap:6, whiteSpace:"nowrap" },
  btnAccent: { background:"var(--accent)", color:"#fff", borderRadius:4, padding:"10px 14px", fontFamily:"var(--font-sans)", fontSize:14, fontWeight:500, textDecoration:"none", display:"inline-flex", alignItems:"center", whiteSpace:"nowrap" },
};

function ArticleBody({ story }) {
  return (
    <article style={ab.wrap}>
      <p style={ab.p}>{story.why} The implications, however, run deeper than a headline number. Procurement timelines that were measured in quarters six months ago now resolve in weeks; the companies that move first on capacity are the ones with the spare engineering bandwidth to actually deploy.</p>
      <p style={ab.p}>This isn't a story about a model. It's a story about the operating-system layer of enterprise AI maturing under load. Three signals worth tracking:</p>
      <ul style={ab.ul}>
        <li style={ab.li}>Capacity announcements are being paired with named customers — a credibility move.</li>
        <li style={ab.li}>Region-level commitments (UK, India, Korea) are now table stakes for procurement.</li>
        <li style={ab.li}>Inference cost per resolved task is replacing tokens-per-dollar as the industry's KPI.</li>
      </ul>

      <div style={ab.callout}>
        <div style={ab.cTitle}>What it changes</div>
        <div style={ab.cRow}><span style={ab.cLabel}>As a leader</span><span style={ab.cText}>{story.leader}</span></div>
        <div style={ab.cRow}><span style={ab.cLabel}>As an individual</span><span style={ab.cText}>{story.ic}</span></div>
      </div>

      <p style={ab.p}>The competitive read is straightforward: the floor on what counts as a serious AI deployment has risen. Two years ago, a pilot was ambitious. Last year, a working internal copilot was enough. This year, the question is whether your AI surface area can absorb a 5× increase in throughput without a re-architect.</p>
      <p style={ab.p}>If you're not asking that question, your competitors already are.</p>

      <div style={ab.sourceRow}>
        <div style={ab.sLabel}>Source</div>
        <a style={ab.sLink} href={story.source.url} target="_blank" rel="noreferrer">{story.source.url} <i data-lucide="arrow-up-right" style={{width:13,height:13,marginLeft:4}}></i></a>
      </div>
    </article>
  );
}
const ab = {
  wrap: { padding:"40px 0 32px", maxWidth:680 },
  p: { fontFamily:"var(--font-serif)", fontSize:19, lineHeight:1.65, color:"var(--fg-body)", margin:"0 0 22px" },
  ul: { margin:"0 0 24px", paddingLeft:24 },
  li: { fontFamily:"var(--font-serif)", fontSize:18, lineHeight:1.6, color:"var(--fg-body)", marginBottom:8 },
  callout: { background:"var(--bg-subtle)", borderLeft:"2px solid var(--accent)", padding:"22px 26px", margin:"32px 0", borderRadius:"0 8px 8px 0" },
  cTitle: { fontFamily:"var(--font-mono)", fontSize:11, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--fg-muted)", marginBottom:14 },
  cRow: { display:"grid", gridTemplateColumns:"140px 1fr", gap:14, padding:"6px 0" },
  cLabel: { fontFamily:"var(--font-mono)", fontSize:11, letterSpacing:"0.06em", textTransform:"uppercase", color:"var(--fg-muted)" },
  cText: { fontFamily:"var(--font-sans)", fontSize:15, lineHeight:1.5, color:"var(--fg)" },
  sourceRow: { borderTop:"1px solid var(--border)", paddingTop:18, marginTop:32, display:"flex", flexDirection:"column", gap:6 },
  sLabel: { fontFamily:"var(--font-mono)", fontSize:11, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--fg-muted)" },
  sLink: { fontFamily:"var(--font-mono)", fontSize:13, color:"var(--accent)", textDecoration:"none", display:"inline-flex", alignItems:"center" },
};

function RelatedStrip({ stories }) {
  return (
    <section style={rs.wrap}>
      <div style={rs.eyebrow}>Read next</div>
      <div style={rs.grid}>
        {stories.map((s,i)=>(
          <a key={i} href="#" style={rs.card}>
            <div style={rs.h}>{s.headline}</div>
            <div style={rs.src}>{s.source.name} ↗</div>
          </a>
        ))}
      </div>
    </section>
  );
}
const rs = {
  wrap: { borderTop:"2px solid var(--ink-900)", paddingTop:18, marginTop:48 },
  eyebrow: { fontFamily:"var(--font-mono)", fontSize:12, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--fg)", fontWeight:500, marginBottom:24 },
  grid: { display:"grid", gridTemplateColumns:"repeat(3, 1fr)", gap:18 },
  card: { display:"flex", flexDirection:"column", gap:8, padding:"18px 20px", border:"1px solid var(--border)", borderRadius:8, textDecoration:"none", background:"var(--bg-elev)" },
  h: { fontFamily:"var(--font-display)", fontWeight:700, fontSize:18, lineHeight:1.25, letterSpacing:"-0.015em", color:"var(--fg)" },
  src: { fontFamily:"var(--font-mono)", fontSize:11, color:"var(--accent)" },
};

Object.assign(window, { ArticleHeader, ArticleHero, ArticleBody, RelatedStrip });
