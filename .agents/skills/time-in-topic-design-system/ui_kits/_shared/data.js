// Shared sample editorial content for all UI kits.
// Real headlines & shape from rss.tedt.org/feeds/top.json — voice tuned to match the editorial brief.
window.YIA_DATA = {
  edition: {
    volume: 184,
    date: "Wednesday, April 29, 2026",
    dateShort: "Apr 29, 2026",
    readMin: 6,
    storyCount: 11,
  },
  tldr: [
    "OpenAI raised $122B and brought Samsung + SK into Stargate — capacity is shifting region by region.",
    "GPT-5.1-Codex-Max ships with project-scale reasoning; Wayfair and Rakuten cite measurable enterprise wins.",
    "A Mixpanel breach exposed limited API analytics data; OpenAI walks through what was and wasn't compromised.",
    "OpenAI for India launches with local infra commitments; UK adds Ministry of Justice and data residency.",
    "Apollo + OpenAI publish a stress-tested method for reducing 'scheming' behavior in frontier models.",
  ],
  sections: [
    {
      id: "big-moves", tag: "Big Moves", color: "#8E2F08", lede: "The deals and dollars that move the floor.",
      stories: [
        {
          headline: "OpenAI raises $122B to expand frontier compute",
          why: "A new round, paired with Stargate scaling and three sovereign-AI deals, signals enterprise procurement has crossed from pilot to default for several governments.",
          leader: "Re-baseline your 2026 AI infra budget against new capacity floors and inference-cost glide paths.",
          ic: "Watch latency SLAs in your region — capacity is shifting visibly week to week.",
          source: { name: "openai.com", url: "https://openai.com/index/accelerating-the-next-phase-ai" }
        },
        {
          headline: "Samsung and SK join OpenAI's Stargate initiative",
          why: "Korean memory and data center commitments add multi-gigawatt capacity for the next training cycle.",
          leader: "Expect tighter HBM allocation; lock 2026 supply contracts before Q3.",
          ic: "Memory-bound workloads should plan for new accelerators by H2.",
          source: { name: "openai.com", url: "https://openai.com/index/samsung-and-sk-join-stargate" }
        }
      ]
    },
    {
      id: "ops", tag: "Enterprise Ops", color: "#1F4D3A", lede: "Where AI hit production this week.",
      stories: [
        {
          headline: "Wayfair boosts catalog accuracy and support speed",
          why: "OpenAI models now triage tickets and enrich product attributes at catalog scale, with double-digit improvements in resolution time.",
          leader: "Catalog hygiene is the unlock — invest there before agentic UX.",
          ic: "Ship attribute-enrichment evals before tuning customer-facing prompts.",
          source: { name: "openai.com", url: "https://openai.com/index/wayfair" }
        },
        {
          headline: "Rakuten fixes issues twice as fast with Codex",
          why: "Engineering throughput, not headcount, is the metric — Rakuten reports halved cycle times on routine fixes.",
          leader: "Measure cycle time, not lines shipped, when justifying agent rollouts.",
          ic: "Adopt Codex for triage first; reserve manual review for design changes.",
          source: { name: "openai.com", url: "https://openai.com/index/rakuten" }
        },
        {
          headline: "Scania scales AI across a global manufacturing workforce",
          why: "Team-based onboarding and strong guardrails are the boring part that's actually working.",
          leader: "Pair every rollout with a written guardrail; skip the demo theater.",
          ic: "Document one workflow you've already automated. Share it Monday.",
          source: { name: "openai.com", url: "https://openai.com/index/scania" }
        }
      ]
    },
    {
      id: "vendors", tag: "Vendors", color: "#2A3F6B", lede: "New models, new SDKs, real changes.",
      stories: [
        {
          headline: "Building more with GPT-5.1-Codex-Max",
          why: "A faster, cheaper agentic coding model with project-scale reasoning and improved token efficiency for long runs.",
          leader: "Renegotiate inference budgets; cost per resolved ticket is the new line item.",
          ic: "Try Codex-Max on the longest task in your queue this week.",
          source: { name: "openai.com", url: "https://openai.com/index/gpt-5-1-codex-max" }
        },
        {
          headline: "WebSockets land in the Responses API",
          why: "Connection-scoped caching trims overhead and latency for long agent loops.",
          leader: "If you've avoided agents for cost reasons, the math may have changed.",
          ic: "Re-benchmark your agent's tail latency before you re-architect.",
          source: { name: "openai.com", url: "https://openai.com/index/speeding-up-agentic-workflows-with-websockets" }
        }
      ]
    },
    {
      id: "security", tag: "Security & Trust", color: "#6B2D2D", lede: "Incidents and mitigations, in plain English.",
      stories: [
        {
          headline: "Mixpanel security incident: what to know",
          why: "Limited API analytics data was exposed. No content, credentials, or payment details. Worth re-reading your vendor list.",
          leader: "Audit third-party analytics that touch your AI surfaces this quarter.",
          ic: "Review what your service sends to Mixpanel — if anything.",
          source: { name: "openai.com", url: "https://openai.com/index/mixpanel-incident" }
        },
        {
          headline: "Detecting and reducing scheming in frontier models",
          why: "Apollo + OpenAI publish stress-tested mitigations for hidden misalignment behaviors.",
          leader: "Add scheming evals to your model acceptance checklist.",
          ic: "Read the eval methodology — it's adaptable to your domain.",
          source: { name: "openai.com", url: "https://openai.com/index/detecting-and-reducing-scheming-in-ai-models" }
        }
      ]
    },
    {
      id: "policy", tag: "Policy & Geo", color: "#4A3A1F", lede: "Regulation, sovereign AI, and where the work happens.",
      stories: [
        {
          headline: "OpenAI for India expands access across the country",
          why: "Local infrastructure, enterprise programs, and workforce skills, all packaged.",
          leader: "If India is on your roadmap, the procurement story just got easier.",
          ic: "Watch for data-residency options if you build for Indian users.",
          source: { name: "openai.com", url: "https://openai.com/index/openai-for-india" }
        },
        {
          headline: "UK gets MoJ partnership and full data residency",
          why: "Civil servants now access ChatGPT under a sovereign deployment.",
          leader: "Public-sector contracts are the new tell on enterprise readiness.",
          ic: "Compliance teams: residency claims need actual diagrams, not slides.",
          source: { name: "openai.com", url: "https://openai.com/index/the-next-chapter-for-uk-sovereign-ai" }
        }
      ]
    }
  ],
  quickHits: [
    { text: "OpenAI Privacy Filter ships as an open-weight PII redactor.", url: "https://openai.com/index/introducing-openai-privacy-filter" },
    { text: "Workspace agents enter ChatGPT — Codex-powered, cloud-run.", url: "https://openai.com/index/introducing-workspace-agents-in-chatgpt" },
    { text: "Cerebras adds 750MW of inference capacity.", url: "https://openai.com/index/cerebras-partnership" },
    { text: "ChatGPT for Clinicians lands free for verified U.S. physicians.", url: "https://openai.com/index/making-chatgpt-better-for-clinicians" }
  ],
  ahead: [
    "DevDay-adjacent SDK updates expected next week.",
    "Two more sovereign deployments rumored before quarter close.",
    "EU AI Act technical standards drop targeted for May 14."
  ]
};
