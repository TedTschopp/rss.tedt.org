---
layout: default
title: "About RSS Feed Hub"
---

{% assign enabled_feeds = site.feeds | where_exp: "feed", "feed.enabled != false" %}

<div class="page-shell">
    <h1>About RSS Feed Hub</h1>
    <div class="about-grid about-grid--offset">
        <div class="prose-shell">
            <p class="lead">RSS Feed Hub is a centralized source for curated AI, enterprise architecture, and technology news feeds. The site automatically aggregates, monitors, and republishes feed content in standard subscription formats.</p>

            <section class="content-section">
                <header class="section-header">
                    <div>
                        <div class="section-header__eyebrow">Model</div>
                        <h2 class="section-header__title">Operating Model</h2>
                    </div>
                </header>
                <div class="content-grid">
                    <div class="info-panel"><div class="info-row__index">01</div><h4>Collect</h4><p class="small">Configured sources are fetched by scheduled GitHub Actions workflows.</p></div>
                    <div class="info-panel"><div class="info-row__index">02</div><h4>Normalize</h4><p class="small">Items are cleaned, deduplicated, scored, and prepared for feed publication.</p></div>
                    <div class="info-panel"><div class="info-row__index">03</div><h4>Publish</h4><p class="small">Public feed files, status data, and site pages are committed and deployed through GitHub Pages.</p></div>
                </div>
            </section>

            <section class="content-section--large">
                <header class="section-header">
                    <div>
                        <div class="section-header__eyebrow">Use</div>
                        <h2 class="section-header__title">Source Attribution</h2>
                    </div>
                </header>
                <p class="section-copy">Feed entries are pointers back to source material. Aggregated feeds preserve source links and may include source attribution in titles or metadata depending on the feed configuration.</p>
            </section>

            <section class="content-section--large">
                <header class="section-header">
                    <div>
                        <div class="section-header__eyebrow">Limits</div>
                        <h2 class="section-header__title">Limits</h2>
                    </div>
                </header>
                <div class="info-panel info-panel--offset">
                    <div class="info-row"><span class="info-row__index">API</span><span>Source feeds can be rate-limited, unavailable, empty, or temporarily malformed.</span></div>
                    <div class="info-row"><span class="info-row__index">LLM</span><span>LLM enrichment is optional and can run in degraded mode when model access is unavailable.</span></div>
                    <div class="info-row"><span class="info-row__index">TIME</span><span>Archive files appear only after retention rules produce older items.</span></div>
                </div>
            </section>

            <section class="content-section">
                <header class="section-header">
                    <div>
                        <div class="section-header__eyebrow">Directory</div>
                        <h2 class="section-header__title">Available Feeds</h2>
                    </div>
                    <span class="section-header__meta">{{ enabled_feeds.size }} PUBLIC FEEDS</span>
                </header>
                <div class="feed-stack">
                    {% for feed in enabled_feeds %}
                        {% include feed-card.html feed=feed index=forloop.index %}
                    {% endfor %}
                </div>
            </section>

            <section class="content-section--large">
                <header class="section-header">
                    <div>
                        <div class="section-header__eyebrow">Process</div>
                        <h2 class="section-header__title">How It Works</h2>
                    </div>
                </header>
                <div class="help-grid">
                    <div class="info-panel"><div class="info-row__index">01</div><h4>Scrape Content</h4><p class="small">Automatically extract articles and news from target websites.</p></div>
                    <div class="info-panel"><div class="info-row__index">02</div><h4>Generate RSS</h4><p class="small">Convert scraped content into standard RSS, Atom, and JSON Feed formats.</p></div>
                    <div class="info-panel"><div class="info-row__index">03</div><h4>Monitor Health</h4><p class="small">Continuously check feed status, validity, freshness, and entry counts.</p></div>
                    <div class="info-panel"><div class="info-row__index">04</div><h4>Update Regularly</h4><p class="small">Refresh content on a scheduled basis via GitHub Actions.</p></div>
                </div>
            </section>

            <section class="content-section--large">
                <header class="section-header">
                    <div>
                        <div class="section-header__eyebrow">Badges</div>
                        <h2 class="section-header__title">Priority Badges</h2>
                    </div>
                </header>
                <p class="section-copy">Feed entries can include priority indicators in their titles. The site converts those markers to badges in feed previews.</p>
                <div class="info-panel info-panel--offset">
                    <div class="info-row"><span class="info-row__index">[ ! ]</span><span><span class="pri-badge essential">Essential</span> Critical or urgent content</span></div>
                    <div class="info-row"><span class="info-row__index">[ * ]</span><span><span class="pri-badge important">Important</span> High-priority content</span></div>
                    <div class="info-row"><span class="info-row__index">[ ~ ]</span><span><span class="pri-badge optional">Optional</span> Supplementary or nice-to-know content</span></div>
                    <div class="info-row"><span class="info-row__index">[ ◻ ]</span><span><span class="tech-badge informational">Tech: Informational</span> Awareness-level technical signal</span></div>
                    <div class="info-row"><span class="info-row__index">[ ◼ ]</span><span><span class="tech-badge tech-important">Tech: Important</span> Likely to change how teams build or run AI systems</span></div>
                    <div class="info-row"><span class="info-row__index">[ ⬢ ]</span><span><span class="tech-badge transformational">Tech: Transformational</span> Forces rethinking architecture or governance patterns</span></div>
                </div>
            </section>

            <section class="content-section--large">
                <header class="section-header">
                    <div>
                        <div class="section-header__eyebrow">Stack</div>
                        <h2 class="section-header__title">Technical Details</h2>
                    </div>
                </header>
                <div class="info-panel info-panel--offset">
                    <div class="info-row"><span class="info-row__index">PY</span><span><strong>Python</strong> Web scraping and feed aggregation with Playwright, Beautiful Soup, and Feedgen</span></div>
                    <div class="info-row"><span class="info-row__index">GA</span><span><strong>GitHub Actions</strong> Scheduled workflow execution and generated artifact commits</span></div>
                    <div class="info-row"><span class="info-row__index">JK</span><span><strong>Jekyll</strong> Static site generation for GitHub Pages</span></div>
                    <div class="info-row"><span class="info-row__index">RSS</span><span><strong>RSS / Atom / JSON</strong> Standard syndication formats for subscribers</span></div>
                </div>
            </section>
        </div>

        <aside>
            <div class="info-panel info-panel--navy">
                <div class="card-kicker card-kicker--inverse">Quick Stats</div>
                <div class="metric-grid" id="quick-stats">
                    <div class="metric"><div class="metric__value">--</div><div class="metric__label">feed files</div></div>
                    <div class="metric"><div class="metric__value metric__value--accent">--</div><div class="metric__label">healthy</div></div>
                    <div class="metric metric--wide"><div class="metric__value">--</div><div class="metric__label">total entries</div></div>
                </div>
                <div class="data-line metric-updated" id="quick-stats-updated">Last updated: unknown</div>
            </div>

            <div class="info-panel info-panel--sidebar-offset">
                <div class="card-kicker">Useful Links</div>
                {% if site.github_url %}
                <a class="side-link" href="{{ site.github_url }}" target="_blank" rel="noopener"><i class="fab fa-github" aria-hidden="true"></i> Source Code</a>
                {% endif %}
                <a class="side-link" href="{{ site.baseurl }}/api/rss_status.json"><i class="fas fa-file-code" aria-hidden="true"></i> Status JSON</a>
                {% for feed in enabled_feeds %}
                <a class="side-link" href="{{ feed.url }}"><i class="fas fa-rss" aria-hidden="true"></i> {{ feed.name }}</a>
                {% endfor %}
            </div>
        </aside>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/rss_status.json')
        .then(function(response) { return response.json(); })
        .then(function(data) {
            let totalEntries = 0;
            let healthyFeeds = 0;
            let totalFeeds = 0;

            if (data.feeds) {
                Object.values(data.feeds).forEach(function(feed) {
                    totalFeeds += 1;
                    if (feed.exists && feed.valid_xml) healthyFeeds += 1;
                    totalEntries += feed.entry_count || 0;
                });
            }

            document.getElementById('quick-stats').innerHTML = `
                <div class="metric"><div class="metric__value">${totalFeeds}</div><div class="metric__label">feed files</div></div>
                <div class="metric"><div class="metric__value metric__value--accent">${healthyFeeds}</div><div class="metric__label">healthy</div></div>
                <div class="metric metric--wide"><div class="metric__value">${totalEntries}</div><div class="metric__label">total entries</div></div>
            `;
            document.getElementById('quick-stats-updated').textContent = 'Last updated: ' + (data.timestamp ? new Date(data.timestamp).toLocaleString() : 'unknown');
        })
        .catch(function(error) {
            console.error('Error loading stats:', error);
            document.getElementById('quick-stats').innerHTML = '<div class="small">Unable to load statistics</div>';
        });
});
</script>