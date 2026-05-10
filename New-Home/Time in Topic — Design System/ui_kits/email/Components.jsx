/* Email newsletter components — designed to look like a real email
   in an inbox preview, but as a *design* mock (HTML/CSS, not sendable). */
const { useState: useStateE } = React;

function InboxFrame({ children }) {
  return (
    <div style={ifr.outer}>
      <div style={ifr.chrome}>
        <div style={ifr.dots}>
          <span style={{...ifr.dot, background:"#FF5F56"}}></span>
          <span style={{...ifr.dot, background:"#FFBD2E"}}></span>
          <span style={{...ifr.dot, background:"#27C93F"}}></span>
        </div>
        <div style={ifr.url}>mail · Yesterday in AI</div>
        <div style={{width:60}}></div>
      </div>
      <div style={ifr.envelope}>
        <div style={ifr.metaRow}>
          <div>
            <div style={ifr.from}><span style={ifr.fromBold}>Yesterday in AI</span> &lt;daily@yesterdayinai.news&gt;</div>
            <div style={ifr.to}>to me</div>
          </div>
          <div style={ifr.date}>Apr 30, 2026, 6:02 AM</div>
        </div>
        <div style={ifr.subject}>Vol. 184 · OpenAI's $122B and what it changes for enterprise procurement</div>
        {children}
      </div>
    </div>
  );
}
const ifr = {
  outer: { maxWidth:720, margin:"32px auto", border:"1px solid var(--border)", borderRadius:10, overflow:"hidden", boxShadow:"var(--shadow-md)", background:"var(--bg)" },
  chrome: { background:"#EDEAE2", padding:"10px 14px", display:"flex", alignItems:"center", justifyContent:"space-between", borderBottom:"1px solid var(--border)" },
  dots: { display:"flex", gap:6 },
  dot: { width:11, height:11, borderRadius:999, display:"inline-block" },
  url: { fontFamily:"var(--font-mono)", fontSize:11, color:"var(--fg-muted)", whiteSpace:"nowrap" },
  envelope: { padding:"24px 28px 8px" },
  metaRow: { display:"flex", justifyContent:"space-between", alignItems:"flex-start", paddingBottom:14, borderBottom:"1px solid var(--border-soft)", marginBottom:18, gap:16 },
  from: { fontFamily:"var(--font-sans)", fontSize:13, color:"var(--fg-body)", whiteSpace:"nowrap", overflow:"hidden", textOverflow:"ellipsis" },
  fromBold: { fontWeight:600, color:"var(--fg)" },
  to: { fontFamily:"var(--font-sans)", fontSize:12, color:"var(--fg-muted)", marginTop:2 },
  date: { fontFamily:"var(--font-mono)", fontSize:11, color:"var(--fg-muted)", whiteSpace:"nowrap" },
  subject: { fontFamily:"var(--font-display)", fontWeight:700, fontSize:22, lineHeight:1.25, letterSpacing:"-0.02em", color:"var(--fg)", marginBottom:24 },
};

function EmailHeader({ edition }) {
  return (
    <div style={eh.wrap}>
      <Wordmark height={22} />
      <div style={eh.meta}>Vol. {edition.volume} · {edition.dateShort} · {edition.readMin} min</div>
    </div>
  );
}
const eh = {
  wrap: { display:"flex", justifyContent:"space-between", alignItems:"center", paddingBottom:24, borderBottom:"2px solid var(--ink-900)", marginBottom:28 },
  meta: { fontFamily:"var(--font-mono)", fontSize:11, letterSpacing:"0.06em", color:"var(--fg-muted)" },
};

function EmailMasthead() {
  return (
    <div style={emh.wrap}>
      <h1 style={emh.h}>Yesterday's news. Today's decisions.</h1>
      <p style={emh.p}>Five things from yesterday that change how you'll spend a meeting today.</p>
    </div>
  );
}
const emh = {
  wrap: { paddingBottom:24, marginBottom:24, borderBottom:"1px solid var(--border)" },
  h: { fontFamily:"var(--font-display)", fontWeight:700, fontSize:28, lineHeight:1.15, letterSpacing:"-0.025em", color:"var(--fg)", margin:"0 0 10px" },
  p: { fontFamily:"var(--font-serif)", fontSize:16, lineHeight:1.5, color:"var(--fg-body)", margin:0 },
};

function EmailTLDR({ items }) {
  return (
    <div style={etl.wrap}>
      <div style={etl.eyebrow}>The five</div>
      <ol style={etl.list}>
        {items.map((t,i)=>(
          <li key={i} style={etl.item}>
            <span style={etl.num}>{String(i+1).padStart(2,"0")}</span>
            <span style={etl.text}>{t}</span>
          </li>
        ))}
      </ol>
    </div>
  );
}
const etl = {
  wrap: { padding:"6px 0 28px", borderBottom:"1px solid var(--border)" },
  eyebrow: { fontFamily:"var(--font-mono)", fontSize:11, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--accent)", fontWeight:500, marginBottom:14 },
  list: { listStyle:"none", padding:0, margin:0, display:"flex", flexDirection:"column", gap:12 },
  item: { display:"flex", gap:14, alignItems:"baseline" },
  num: { fontFamily:"var(--font-mono)", fontSize:11, fontWeight:500, color:"var(--accent)", flex:"0 0 22px" },
  text: { fontFamily:"var(--font-serif)", fontSize:15, lineHeight:1.55, color:"var(--fg)" },
};

function EmailStory({ story, section, index }) {
  return (
    <div style={es.wrap}>
      <div style={es.eyebrow}><span style={{color: section.color}}>{section.tag}</span> · Story {String(index).padStart(2,"0")}</div>
      <h2 style={es.h}>{story.headline}</h2>
      <p style={es.why}>{story.why}</p>
      <div style={es.tableLike}>
        <div style={es.row}><div style={es.lbl}>Leader</div><div style={es.val}>{story.leader}</div></div>
        <div style={es.row}><div style={es.lbl}>Individual</div><div style={es.val}>{story.ic}</div></div>
      </div>
      <a href={story.source.url} style={es.src} target="_blank" rel="noreferrer">→ {story.source.name}</a>
    </div>
  );
}
const es = {
  wrap: { padding:"28px 0", borderBottom:"1px solid var(--border)" },
  eyebrow: { fontFamily:"var(--font-mono)", fontSize:11, fontWeight:500, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--fg-muted)", marginBottom:10 },
  h: { fontFamily:"var(--font-display)", fontWeight:700, fontSize:22, lineHeight:1.2, letterSpacing:"-0.02em", color:"var(--fg)", margin:"0 0 12px" },
  why: { fontFamily:"var(--font-serif)", fontSize:16, lineHeight:1.5, color:"var(--fg-body)", margin:"0 0 16px" },
  tableLike: { display:"flex", flexDirection:"column", gap:0, marginBottom:14 },
  row: { display:"grid", gridTemplateColumns:"96px 1fr", gap:14, padding:"8px 0", borderTop:"1px solid var(--border-soft)" },
  lbl: { fontFamily:"var(--font-mono)", fontSize:10, letterSpacing:"0.06em", textTransform:"uppercase", color:"var(--fg-muted)", paddingTop:2 },
  val: { fontFamily:"var(--font-sans)", fontSize:14, lineHeight:1.5, color:"var(--fg)" },
  src: { fontFamily:"var(--font-mono)", fontSize:12, color:"var(--accent)", textDecoration:"none" },
};

function EmailQuickHits({ items }) {
  return (
    <div style={eqh.wrap}>
      <div style={eqh.eyebrow}>Also worth a click</div>
      <ul style={eqh.list}>
        {items.map((it,i)=>(
          <li key={i} style={eqh.item}>· <a href={it.url} style={eqh.link} target="_blank" rel="noreferrer">{it.text}</a></li>
        ))}
      </ul>
    </div>
  );
}
const eqh = {
  wrap: { padding:"24px 0", borderBottom:"1px solid var(--border)" },
  eyebrow: { fontFamily:"var(--font-mono)", fontSize:11, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--fg-muted)", fontWeight:500, marginBottom:14 },
  list: { listStyle:"none", padding:0, margin:0, display:"flex", flexDirection:"column", gap:8 },
  item: { fontFamily:"var(--font-serif)", fontSize:15, lineHeight:1.5, color:"var(--fg)" },
  link: { color:"var(--fg)", textDecoration:"underline", textDecorationColor:"var(--accent)", textUnderlineOffset:"3px" },
};

function EmailLookingAhead({ items }) {
  return (
    <div style={ela.wrap}>
      <div style={ela.eyebrow}>Looking ahead</div>
      <ul style={ela.list}>
        {items.map((t,i)=><li key={i} style={ela.item}>{t}</li>)}
      </ul>
    </div>
  );
}
const ela = {
  wrap: { background:"var(--ink-900)", color:"var(--ink-0)", padding:"28px 28px 30px", margin:"32px -28px 0", borderRadius:0 },
  eyebrow: { fontFamily:"var(--font-mono)", fontSize:11, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--ink-300)", marginBottom:14 },
  list: { listStyle:"none", padding:0, margin:0, display:"flex", flexDirection:"column", gap:8 },
  item: { fontFamily:"var(--font-serif)", fontSize:15, lineHeight:1.5, color:"var(--ink-0)" },
};

function EmailSignoff() {
  return (
    <div style={eso.wrap}>
      <p style={eso.p}>That's yesterday. Reply if something changed your day — we read everything.</p>
      <p style={eso.sig}>— The Yesterday in AI desk</p>
    </div>
  );
}
const eso = {
  wrap: { padding:"28px 28px 24px", margin:"0 -28px", borderTop:"1px solid var(--border)" },
  p: { fontFamily:"var(--font-serif)", fontStyle:"italic", fontSize:15, lineHeight:1.5, color:"var(--fg-body)", margin:"0 0 8px" },
  sig: { fontFamily:"var(--font-mono)", fontSize:12, color:"var(--fg-muted)", margin:0 },
};

function EmailFooter() {
  return (
    <div style={efo.wrap}>
      <div style={efo.brand}>Yesterday in AI · daily@yesterdayinai.news</div>
      <div style={efo.links}>
        <a href="#" style={efo.link}>View in browser</a> · <a href="#" style={efo.link}>Manage preferences</a> · <a href="#" style={efo.link}>Unsubscribe</a>
      </div>
      <div style={efo.fine}>You're getting this because you asked for one email a day. We don't track opens, clicks, or pixels.</div>
    </div>
  );
}
const efo = {
  wrap: { padding:"22px 28px 28px", margin:"0 -28px", background:"var(--bg-subtle)", textAlign:"center" },
  brand: { fontFamily:"var(--font-mono)", fontSize:11, color:"var(--fg-muted)", marginBottom:8, letterSpacing:"0.04em" },
  links: { fontFamily:"var(--font-sans)", fontSize:12, color:"var(--fg-muted)", marginBottom:10 },
  link: { color:"var(--fg-muted)", textDecoration:"underline" },
  fine: { fontFamily:"var(--font-mono)", fontSize:10, color:"var(--fg-faint)", lineHeight:1.5, maxWidth:480, margin:"0 auto" },
};

Object.assign(window, { InboxFrame, EmailHeader, EmailMasthead, EmailTLDR, EmailStory, EmailQuickHits, EmailLookingAhead, EmailSignoff, EmailFooter });
