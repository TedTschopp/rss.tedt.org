# GAI Briefing Recovery

The ratings page currently stops at September 25, 2026. Its HTML still embeds
3,929 historical rows, while its paginated table displays only 50. The scraper
reads the complete inline history, retaining publisher ratings and rationales,
then supplements it with dated selections from <https://gaiinsights.com/articles>.
The main feed retains 60 days; older selections remain in `ai_rss_feed_archive.xml`.

`derived/gai_briefings.json` retains recovered versions of the articles page,
their source and capture URLs, page dates, checksums, and estimates. Historical
capture timestamps are evidence of retrieval, never replacement publication
dates. Undated versions require an unambiguous date shared by their matching
published ratings. The Internet Archive does not provide every daily edition.

Missing ratings use Essential, Important, or Optional with **(Estimated)** in
every feed format and an explicitly estimated rationale. The six selections in
the September 29 briefing have reviewed estimates and specific historical GAI
examples. Later unrated selections use a deterministic nearest-example estimate
from published titles and rationales, with the method, confidence, and examples
retained in the saved data. Estimates never become training examples. When a
publisher rating becomes available, it takes precedence in the current feed.
Matching dated titles also recognize original links versus publisher archive links.

The normal seven-day freshness gate applies to the newest dated selection from
either source. Neither an archive retrieval nor a rebuild makes old stories fresh.
If both sources are stale, the run still fails. If the ratings source cannot be
fetched, prior ratings may be supplemented by a fresh dated briefing; source
failures remain visible in `reports/gai_recovery_report.json`, public
`api/rss_status.json`, and the Actions health summary. A supplemented feed is
reported as a warning so that estimated ratings are visible to operators.

The October 3 recovery records the available archive captures and coverage gaps
in `derived/gai_briefings.json`. Inspect that evidence and the recovery report
before describing the historical coverage as complete.

Run the parser, provenance, estimate, retention, and freshness regression checks:

```bash
python -m unittest tests.test_gai_inline_payload_parser tests.test_gai_briefings -v
```
