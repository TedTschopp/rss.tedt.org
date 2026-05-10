/* Components for the Yesterday in AI website UI kit. */
/* @jsx React.createElement */
const { useState } = React;

function Header({ onSubscribe }) {
  return (
    <header style={hdr.bar}>
      <div style={hdr.inner}>
        <a href="#" style={hdr.brand}>
          <Wordmark height={28} />
        </a>
        <nav style={hdr.nav}>
          <a href="#" style={hdr.navLink}>Today</a>
          <a href="#" style={hdr.navLink}>Archive</a>
          <a href="#" style={hdr.navLink}>Sections</a>
          <a href="#" style={hdr.navLink}>About</a>
        </nav>
        <div style={hdr.right}>
          <button style={hdr.search} aria-label="Search"><i data-lucide="search" style={{width:18,height:18}}></i></button>
          <button style={hdr.subscribe} onClick={onSubscribe}>Subscribe</button>
        </div>
      </div>
    </header>
  );
}
const hdr = {
  bar: { position:"sticky", top:0, zIndex:10, background:"rgba(251,250,247,0.85)", backdropFilter:"blur(8px)", borderBottom:"1px solid var(--border-soft)" },
  inner: { maxWidth:1200, margin:"0 auto", padding:"14px 32px", display:"flex", alignItems:"center", justifyContent:"space-between", gap:32 },
  brand: { display:"flex", alignItems:"center", textDecoration:"none" },
  nav: { display:"flex", gap:28 },
  navLink: { fontFamily:"var(--font-sans)", fontSize:14, fontWeight:500, color:"var(--fg)", textDecoration:"none" },
  right: { display:"flex", gap:10, alignItems:"center" },
  search: { width:36, height:36, border:"1px solid var(--border)", background:"var(--bg)", borderRadius:4, cursor:"pointer", color:"var(--fg)", display:"flex", alignItems:"center", justifyContent:"center" },
  subscribe: { background:"var(--ink-900)", color:"var(--ink-0)", border:"none", borderRadius:4, padding:"9px 16px", fontFamily:"var(--font-sans)", fontSize:14, fontWeight:500, cursor:"pointer" },
};

function Masthead({ edition }) {
  return (
    <div style={mh.wrap}>
      <div style={mh.eyebrow}>Vol. {edition.volume} · {edition.dateShort} · {edition.readMin} min read</div>
      <h1 style={mh.title}>The AI news that mattered yesterday.</h1>
      <p style={mh.lede}>{edition.storyCount} stories from {edition.date}, sorted by what changes your work — not by what trended.</p>
    </div>
  );
}
const mh = {
  wrap: { padding:"56px 0 40px", borderBottom:"1px solid var(--border)" },
  eyebrow: { fontFamily:"var(--font-mono)", fontSize:12, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--fg-muted)", marginBottom:18 },
  title: { fontFamily:"var(--font-display)", fontWeight:700, fontSize:64, lineHeight:1.05, letterSpacing:"-0.03em", color:"var(--fg)", margin:"0 0 16px", maxWidth:900 },
  lede: { fontFamily:"var(--font-serif)", fontSize:20, lineHeight:1.5, color:"var(--fg-body)", margin:0, maxWidth:680 },
};

function TLDR({ items }) {
  return (
    <section style={tl.box}>
      <div style={tl.eyebrow}>TL;DR</div>
      <ol style={tl.list}>
        {items.map((t, i) => <li key={i} style={tl.item}><span style={tl.num}>{String(i+1).padStart(2,"0")}</span><span>{t}</span></li>)}
      </ol>
    </section>
  );
}
const tl = {
  box: { padding:"32px 0 48px", borderBottom:"1px solid var(--border-soft)" },
  eyebrow: { fontFamily:"var(--font-mono)", fontSize:12, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--fg)", marginBottom:18, fontWeight:500 },
  list: { listStyle:"none", padding:0, margin:0, display:"flex", flexDirection:"column", gap:14 },
  item: { fontFamily:"var(--font-serif)", fontSize:18, lineHeight:1.55, color:"var(--fg)", display:"flex", gap:18, alignItems:"baseline" },
  num: { fontFamily:"var(--font-mono)", fontSize:12, color:"var(--accent)", flex:"0 0 24px", fontWeight:500 },
};

function SectionHeader({ section, idx }) {
  return (
    <div style={sh.wrap}>
      <div style={sh.eyebrowRow}>
        <span style={{...sh.eyebrow, color: section.color}}>{section.tag} · {String(idx).padStart(2,"0")}</span>
        <span style={sh.count}>{section.stories.length} stor{section.stories.length === 1 ? "y" : "ies"}</span>
      </div>
      <h2 style={sh.title}>{section.lede}</h2>
    </div>
  );
}
const sh = {
  wrap: { borderTop:"2px solid var(--ink-900)", paddingTop:18, marginTop:56, marginBottom:24 },
  eyebrowRow: { display:"flex", justifyContent:"space-between", alignItems:"center", marginBottom:8 },
  eyebrow: { fontFamily:"var(--font-mono)", fontSize:12, fontWeight:500, letterSpacing:"0.08em", textTransform:"uppercase" },
  count: { fontFamily:"var(--font-mono)", fontSize:11, color:"var(--fg-muted)" },
  title: { fontFamily:"var(--font-heading)", fontWeight:400, fontSize:32, lineHeight:1.15, letterSpacing:0, color:"var(--fg)", margin:0 },
};

function StoryCard({ story, onOpen, hover }) {
  const [h, setH] = useState(false);
  return (
    <article
      onClick={() => onOpen && onOpen(story)}
      onMouseEnter={()=>setH(true)} onMouseLeave={()=>setH(false)}
      style={{...sc.card, borderTopColor: h ? "var(--ink-900)" : "var(--border)", cursor: onOpen ? "pointer" : "default"}}>
      <h3 style={sc.headline}>{story.headline}</h3>
      <p style={sc.why}>{story.why}</p>
      <div style={sc.row}><span style={sc.label}>As a leader</span><span style={sc.text}>{story.leader}</span></div>
      <div style={sc.row}><span style={sc.label}>As an individual</span><span style={sc.text}>{story.ic}</span></div>
      <a href={story.source.url} onClick={e=>e.stopPropagation()} style={sc.source} target="_blank" rel="noreferrer">
        {story.source.name} <i data-lucide="arrow-up-right" style={{width:13,height:13,marginLeft:2}}></i>
      </a>
    </article>
  );
}
const sc = {
  card: { borderTop:"1px solid var(--border)", padding:"24px 0 28px", transition:"border-color 120ms" },
  headline: { fontFamily:"var(--font-display)", fontWeight:700, fontSize:30, lineHeight:1.18, letterSpacing:"-0.025em", color:"var(--fg)", margin:"0 0 12px" },
  why: { fontFamily:"var(--font-serif)", fontSize:18, lineHeight:1.55, color:"var(--fg-body)", margin:"0 0 18px", maxWidth:680 },
  row: { display:"grid", gridTemplateColumns:"140px 1fr", gap:18, padding:"8px 0", borderTop:"1px solid var(--border-soft)" },
  label: { fontFamily:"var(--font-mono)", fontSize:11, letterSpacing:"0.06em", textTransform:"uppercase", color:"var(--fg-muted)", paddingTop:2 },
  text: { fontFamily:"var(--font-sans)", fontSize:15, lineHeight:1.5, color:"var(--fg)" },
  source: { display:"inline-flex", alignItems:"center", fontFamily:"var(--font-mono)", fontSize:12, color:"var(--accent)", marginTop:14, textDecoration:"none" },
};

function QuickHits({ items }) {
  return (
    <section style={qh.wrap}>
      <div style={sh.eyebrowRow}>
        <span style={{...sh.eyebrow, color:"#4A4A4A"}}>Quick Hits · 06</span>
        <span style={sh.count}>{items.length} items</span>
      </div>
      <ul style={qh.list}>
        {items.map((it,i)=>(
          <li key={i} style={qh.item}>
            <span style={qh.bullet}>·</span>
            <span style={qh.text}>{it.text} <a href={it.url} style={qh.link} target="_blank" rel="noreferrer"><i data-lucide="arrow-up-right" style={{width:11,height:11}}></i></a></span>
          </li>
        ))}
      </ul>
    </section>
  );
}
const qh = {
  wrap: { borderTop:"2px solid var(--ink-900)", paddingTop:18, marginTop:56 },
  list: { listStyle:"none", padding:0, margin:"24px 0 0", display:"flex", flexDirection:"column", gap:10 },
  item: { display:"flex", gap:12, alignItems:"baseline" },
  bullet: { fontFamily:"var(--font-mono)", color:"var(--accent)" },
  text: { fontFamily:"var(--font-serif)", fontSize:17, lineHeight:1.55, color:"var(--fg)" },
  link: { color:"var(--accent)", marginLeft:4, display:"inline-flex" },
};

function LookingAhead({ items }) {
  return (
    <section style={la.wrap}>
      <div style={la.eyebrow}>Looking Ahead</div>
      <ul style={la.list}>
        {items.map((t,i)=><li key={i} style={la.item}>{t}</li>)}
      </ul>
    </section>
  );
}
const la = {
  wrap: { background:"var(--ink-900)", color:"var(--ink-0)", padding:"40px 40px 44px", marginTop:64, borderRadius:8 },
  eyebrow: { fontFamily:"var(--font-mono)", fontSize:12, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--ink-300)", marginBottom:16 },
  list: { listStyle:"none", padding:0, margin:0, display:"flex", flexDirection:"column", gap:10 },
  item: { fontFamily:"var(--font-serif)", fontSize:18, lineHeight:1.5, color:"var(--ink-0)" },
};

function SubscribeBlock() {
  const [email, setEmail] = useState("");
  const [done, setDone] = useState(false);
  return (
    <aside style={sb.wrap}>
      <div style={sb.eyebrow}>Daily, 6 a.m. ET</div>
      <h3 style={sb.h}>Get this in your inbox.</h3>
      <p style={sb.p}>One email. The day's enterprise AI news, with what to do about it. No tracking pixels.</p>
      {done ? (
        <div style={sb.done}>✓ Check your inbox to confirm.</div>
      ) : (
        <form style={sb.form} onSubmit={e=>{e.preventDefault();setDone(true);}}>
          <input style={sb.input} type="email" placeholder="you@company.com" value={email} onChange={e=>setEmail(e.target.value)} required />
          <button style={sb.btn}>Subscribe</button>
        </form>
      )}
      <div style={sb.fine}>30k+ readers · unsubscribe anytime</div>
    </aside>
  );
}
const sb = {
  wrap: { border:"1px solid var(--border)", borderRadius:8, padding:"28px 28px 24px", background:"var(--bg-elev)" },
  eyebrow: { fontFamily:"var(--font-mono)", fontSize:11, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--accent)", marginBottom:12 },
  h: { fontFamily:"var(--font-display)", fontWeight:700, fontSize:24, letterSpacing:"-0.02em", margin:"0 0 8px", color:"var(--fg)" },
  p: { fontFamily:"var(--font-sans)", fontSize:14, lineHeight:1.5, color:"var(--fg-body)", margin:"0 0 16px" },
  form: { display:"flex", gap:8 },
  input: { flex:1, fontFamily:"var(--font-sans)", fontSize:14, padding:"10px 12px", border:"1px solid var(--border)", borderRadius:4, outline:"none", background:"var(--bg)" },
  btn: { background:"var(--ink-900)", color:"var(--ink-0)", border:"none", borderRadius:4, padding:"10px 14px", fontFamily:"var(--font-sans)", fontSize:14, fontWeight:500, cursor:"pointer" },
  done: { fontFamily:"var(--font-sans)", fontSize:14, color:"var(--accent)", padding:"10px 0" },
  fine: { fontFamily:"var(--font-mono)", fontSize:11, color:"var(--fg-muted)", marginTop:10 },
};

function Footer() {
  return (
    <footer style={ft.wrap}>
      <div style={ft.row}>
        <Wordmark height={22} />
        <div style={ft.cols}>
          <div style={ft.col}><div style={ft.label}>Read</div><a style={ft.link} href="#">Today</a><a style={ft.link} href="#">Archive</a><a style={ft.link} href="#">Sections</a></div>
          <div style={ft.col}><div style={ft.label}>About</div><a style={ft.link} href="#">Mission</a><a style={ft.link} href="#">Sources</a><a style={ft.link} href="#">Methodology</a></div>
          <div style={ft.col}><div style={ft.label}>Follow</div><a style={ft.link} href="#">RSS</a><a style={ft.link} href="#">JSON Feed</a><a style={ft.link} href="#">LinkedIn</a></div>
        </div>
      </div>
      <div style={ft.fine}>© 2026 Yesterday in AI · Edited daily, 6 a.m. ET · No tracking, no paywall.</div>
    </footer>
  );
}
const ft = {
  wrap: { borderTop:"1px solid var(--border)", padding:"40px 0 32px", marginTop:80 },
  row: { display:"flex", justifyContent:"space-between", alignItems:"flex-start", gap:48, flexWrap:"wrap" },
  cols: { display:"flex", gap:48 },
  col: { display:"flex", flexDirection:"column", gap:6 },
  label: { fontFamily:"var(--font-mono)", fontSize:11, letterSpacing:"0.08em", textTransform:"uppercase", color:"var(--fg-muted)", marginBottom:4 },
  link: { fontFamily:"var(--font-sans)", fontSize:14, color:"var(--fg)", textDecoration:"none" },
  fine: { fontFamily:"var(--font-mono)", fontSize:11, color:"var(--fg-muted)", marginTop:32, paddingTop:18, borderTop:"1px solid var(--border-soft)" },
};

Object.assign(window, { Header, Masthead, TLDR, SectionHeader, StoryCard, QuickHits, LookingAhead, SubscribeBlock, Footer });
