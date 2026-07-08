// Shared sample data for the RSS Feed Hub UI kit.
// Feed registry mirrors _config.yml (enabled feeds only); status numbers
// mirror api/rss_status.json (2026-07-07 snapshot). Entry lists are sample
// rows in the shape the pipeline emits (priority + tech markers parsed
// from [ ! ] [ * ] [ ~ ] / [ ◻ ] [ ◼ ] [ ⬢ ] title suffixes).

window.RSSHUB_DATA = {
  site: {
    name: "RSS Feed Hub",
    description: "Curated RSS feeds for AI Insights and Technology News",
    url: "https://rss.tedt.org",
    github: "https://github.com/TedTschopp/rss.tedt.org",
    owner: "Ted Tschopp",
    statusTimestamp: "2026-07-07 18:08 UTC",
    overallStatus: "warning",
  },

  feeds: [
    {
      key: "ai_rss_feed",
      name: "Ted Tschopp's AI News",
      description: "Latest AI News and Ratings from Ted Tschopp",
      url: "https://rss.tedt.org/ai_rss_feed.xml",
      formats: {
        rss2: "/ai_rss_feed.xml",
        rss1: "/ai_rss_feed_rss1.xml",
        atom: "/ai_rss_feed.atom",
        json: "/ai_rss_feed.json",
      },
      status: { health: "healthy", entries: 50, updated: "2026-07-07" },
      items: [
        { title: "Building more with GPT-5.1-Codex-Max", date: "2026-07-07", priority: "essential", tech: "transformational", href: "#" },
        { title: "Mixpanel security incident: what OpenAI users need to know", date: "2026-07-07", priority: "essential", tech: "important", href: "#" },
        { title: "1 million business customers putting AI to work", date: "2026-07-06", priority: "important", tech: "important", href: "#" },
        { title: "Wayfair boosts catalog accuracy and support speed with OpenAI", date: "2026-07-06", priority: "important", tech: "informational", href: "#" },
        { title: "How Scania accelerates work with AI across its global workforce", date: "2026-07-05", priority: "optional", tech: "informational", href: "#" },
      ],
    },
    {
      key: "aggregated_wes_ai_news",
      name: "Wes's AI News",
      description: "Latest AI News and Commentary from Wes",
      url: "https://rss.tedt.org/aggregated_wes_ai_news.xml",
      formats: {
        rss2: "/aggregated_wes_ai_news.xml",
        rss1: "/aggregated_wes_ai_news_rss1.xml",
        atom: "/aggregated_wes_ai_news.atom",
        json: "/aggregated_wes_ai_news.json",
      },
      status: { health: "healthy", entries: 30, updated: "2026-07-07" },
      items: [
        { title: "Agentic coding tools compared: a week in the trenches", date: "2026-07-07", href: "#" },
        { title: "Why local models keep winning the privacy argument", date: "2026-07-06", href: "#" },
        { title: "The quiet death of the fine-tuning UI", date: "2026-07-05", href: "#" },
      ],
    },
    {
      key: "top_stories",
      name: "Top Stories (LLM Aggregated)",
      description: "Cross-source ranked stories with optional GitHub Models enrichment",
      url: "https://rss.tedt.org/feeds/top.xml",
      formats: {
        rss2: "/feeds/top.xml",
        rss1: "/feeds/top_rss1.xml",
        atom: "/feeds/top.atom",
        json: "/feeds/top.json",
      },
      status: { health: "healthy", entries: 80, updated: "2026-07-07" },
      items: [
        { title: "OpenAI raises $122 billion, and the floor on enterprise AI just moved", date: "2026-07-07", priority: "essential", tech: "transformational", href: "#" },
        { title: "Samsung and SK join OpenAI's Stargate initiative", date: "2026-07-07", priority: "important", href: "#" },
        { title: "Cerebras adds 750 MW of inference capacity to the regional mix", date: "2026-07-06", priority: "important", tech: "important", href: "#" },
        { title: "Detecting and reducing scheming in frontier models", date: "2026-07-06", priority: "optional", tech: "informational", href: "#" },
      ],
    },
    {
      key: "aggregated_ea",
      name: "Enterprise Architecture Aggregated News",
      description: "Enterprise Architecture multi-source aggregated feed",
      url: "https://rss.tedt.org/aggregated_ea.xml",
      formats: {
        rss2: "/aggregated_ea.xml",
        rss1: "/aggregated_ea_rss1.xml",
        atom: "/aggregated_ea.atom",
        json: "/aggregated_ea.json",
      },
      status: { health: "healthy", entries: 26, updated: "2026-07-07" },
      items: [
        { title: "The Open Group publishes TOGAF guidance for AI governance", date: "2026-07-07", href: "#" },
        { title: "Forrester: EA teams are becoming AI portfolio managers", date: "2026-07-06", href: "#" },
        { title: "LeanIX on application rationalization after the M&A wave", date: "2026-07-04", href: "#" },
      ],
    },
    {
      key: "aggregated_broad_ai_news",
      name: "Broad AI News",
      description: "Broad AI ecosystem signals from labs, research, communities, and newsletters",
      url: "https://rss.tedt.org/aggregated_broad_ai_news.xml",
      formats: {
        rss2: "/aggregated_broad_ai_news.xml",
        rss1: "/aggregated_broad_ai_news_rss1.xml",
        atom: "/aggregated_broad_ai_news.atom",
        json: "/aggregated_broad_ai_news.json",
      },
      status: { health: "healthy", entries: 200, updated: "2026-07-07" },
      categories: ["AI Labs", "Hacker News", "Reddit", "arXiv", "Newsletters", "Extras"],
      items: [
        { title: "LLMs prefer resumes they generated themselves", date: "2026-07-07", href: "#" },
        { title: "Show HN: an eval kit for agent traces", date: "2026-07-07", href: "#" },
        { title: "SimpleQA keeps factuality evaluation intentionally narrow", date: "2026-07-06", href: "#" },
        { title: "Mistral-Next quietly hits Hugging Face with permissive license", date: "2026-07-06", href: "#" },
      ],
    },
  ],

  // api/rss_status.json snapshot (real values, 2026-07-07)
  statusApi: {
    totalFiles: 8,
    healthyFiles: 6,
    totalEntries: 1081,
    pipeline: { apiItems: 80, stories: 2060, clusters: 2058, llmCalls: 11, llmOk: 11 },
    aggregationHealth: [
      { feed: "aggregated_wes_ai_news.xml", sources: 1, attempted: 1, withItems: 1, failures: 0, failureRate: "0.00" },
      { feed: "aggregated_ea.xml", sources: 7, attempted: 6, withItems: 5, failures: 1, failureRate: "16.67" },
      { feed: "aggregated_broad_ai_news.xml", sources: 21, attempted: 14, withItems: 9, failures: 0, failureRate: "0.00" },
    ],
  },
};
