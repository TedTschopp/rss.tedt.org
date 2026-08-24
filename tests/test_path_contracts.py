from pathlib import Path
import json
import unittest

import yaml

from scripts import config
from scripts.validate_workflow import validate as validate_workflow


class PathContractTests(unittest.TestCase):
    def test_status_path_contract(self):
        self.assertEqual(config.STATUS_REPORT_FILE, "api/rss_status.json")
        self.assertIn("/api/rss_status.json", Path("feeds.html").read_text(encoding="utf-8"))
        self.assertIn("/api/rss_status.json", Path("about.md").read_text(encoding="utf-8"))
        self.assertIn("/api/rss_status.json", Path("status.html").read_text(encoding="utf-8"))

    def test_internal_artifact_paths_are_not_root_level(self):
        self.assertEqual(config.PREVIOUS_DATA_FILE, "derived/previous_data.json")
        self.assertEqual(config.AGGREGATOR_CACHE_FILE, "derived/aggregator_cache.json")
        self.assertEqual(config.SKIPPED_SOURCES_FILE, "derived/skipped_sources.json")
        self.assertEqual(config.AGGREGATION_REPORTS_DIR, "reports/aggregation")

    def test_reference_rubric_path_exists(self):
        relevance_path = Path("Docs/reference/ai-relevance-rubric.md")
        rubric_path = Path("Docs/reference/business-and-technical-importance-rubric.md")
        self.assertTrue(relevance_path.is_file())
        self.assertTrue(rubric_path.is_file())

    def test_public_feed_paths_remain_at_root(self):
        for path_text in [
            "ai_rss_feed.xml",
            "ai_rss_feed.atom",
            "ai_rss_feed.json",
            "ai_rss_feed_rss1.xml",
            "aggregated_ea.xml",
            "aggregated_broad_ai_news.xml",
            "feeds/top.xml",
        ]:
            self.assertTrue(Path(path_text).is_file(), path_text)

        for deleted_path in [
            "aggregated_osr_ttrpg.xml",
            "aggregated_osr_ttrpg_archive.xml",
            "reports/aggregation/aggregated_osr_ttrpg_health.json",
            "Docs/reference/osr-rss-feeds.md",
            "aggregated_wes_ai_news.xml",
            "aggregated_wes_ai_news.atom",
            "aggregated_wes_ai_news.json",
            "aggregated_wes_ai_news_rss1.xml",
            "reports/aggregation/aggregated_wes_ai_news_health.json",
            "reports/aggregation/aggregated_wes_ai_news_report.md",
        ]:
            self.assertFalse(Path(deleted_path).exists(), deleted_path)

    def test_config_uses_unified_feed_list_only(self):
        site_config_text = Path("_config.yml").read_text(encoding="utf-8")
        site_config = yaml.safe_load(site_config_text)
        self.assertNotIn("aggregated_feeds", site_config)
        self.assertNotIn("aggregated_osr_ttrpg", site_config_text)
        self.assertNotIn("OSR & TTRPG", site_config_text)
        self.assertNotIn("aggregated_wes_ai_news", site_config_text)
        self.assertNotIn("Wes's AI News", site_config_text)

    def test_public_json_feed_self_urls_match_file_paths(self):
        for path in [
            Path("ai_rss_feed.json"),
            Path("aggregated_external.json"),
            Path("aggregated_ea.json"),
            Path("aggregated_broad_ai_news.json"),
            Path("feeds/top.json"),
        ]:
            payload = json.loads(path.read_text(encoding="utf-8"))
            expected = f"https://rss.tedt.org/{path.as_posix()}"
            self.assertEqual(payload.get("feed_url"), expected)
            self.assertNotIn(".xml/feed.json", payload.get("feed_url", ""))

    def test_workflow_contract_validator_passes(self):
        self.assertEqual(validate_workflow(verbose=False), [])

    def test_workflow_limits_openai_output_cleanup_volume(self):
        workflow = Path(".github/workflows/scrape-and-generate-rss.yml").read_text(encoding="utf-8")
        self.assertIn("inputs.backfill && '10000'", workflow)
        self.assertIn("github.event.schedule != '30 3 * * *' && '20' || '50'", workflow)
        self.assertNotIn("PIPELINE_OUTPUT_CLEANUP_TOP_N: ${{ github.event_name == 'schedule' && github.event.schedule != '30 3 * * *' && '80' || '200' }}", workflow)

    def test_workflow_exposes_bounded_backfill_dispatch(self):
        workflow = Path(".github/workflows/scrape-and-generate-rss.yml").read_text(encoding="utf-8")
        self.assertIn("backfill:", workflow)
        self.assertIn("backfill_batch_size:", workflow)
        self.assertIn("PIPELINE_BACKFILL_MODE:", workflow)
        self.assertIn("PIPELINE_LLM_EMBEDDING_MAX_STORIES:", workflow)
        self.assertIn("PIPELINE_LLM_WORKERS:", workflow)
        self.assertIn("PIPELINE_AI_RELEVANCE_MAX_CALLS:", workflow)
        self.assertIn("PIPELINE_IMPORTANCE_MAX_CALLS:", workflow)
        self.assertIn("PIPELINE_OUTPUT_CLEANUP_MAX_CALLS:", workflow)
        self.assertIn("PIPELINE_ARTICLE_FETCH_MAX_URLS:", workflow)

    def test_backfill_batch_choices_fit_the_workflow_timeout(self):
        workflow = Path(".github/workflows/scrape-and-generate-rss.yml").read_text(encoding="utf-8")
        backfill_input = workflow.split("backfill_batch_size:", 1)[1].split("push:", 1)[0]
        self.assertIn("default: '250'", backfill_input)
        self.assertIn("- '500'", backfill_input)
        self.assertNotIn("- '1000'", backfill_input)

    def test_backfill_continuation_is_opt_in_and_bounded(self):
        workflow = Path(".github/workflows/scrape-and-generate-rss.yml").read_text(encoding="utf-8")
        self.assertIn("continue_backfill:", workflow)
        self.assertIn("backfill_runs_remaining:", workflow)
        self.assertIn("actions: write", workflow)
        self.assertIn("python -m scripts.backfill_continuation", workflow)
        self.assertIn("gh workflow run scrape-and-generate-rss.yml", workflow)
        self.assertIn("-f continue_backfill=true", workflow)
        self.assertIn("-f backfill_runs_remaining=", workflow)

    def test_scrape_concurrency_does_not_cancel_active_backfill(self):
        workflow = yaml.safe_load(Path(".github/workflows/scrape-and-generate-rss.yml").read_text(encoding="utf-8"))
        concurrency = workflow["jobs"]["scrape-and-generate-rss"]["concurrency"]
        self.assertFalse(concurrency["cancel-in-progress"])

    def test_scheduled_deployment_skips_cancelled_workflows(self):
        workflow = yaml.safe_load(Path(".github/workflows/scrape-and-generate-rss.yml").read_text(encoding="utf-8"))
        condition = workflow["jobs"]["deploy-after-scrape"]["if"]
        self.assertEqual(condition, "${{ always() && !cancelled() && github.event_name != 'push' }}")

    def test_workflow_rejects_oversized_staged_blobs_before_commit(self):
        workflow = Path(".github/workflows/scrape-and-generate-rss.yml").read_text(encoding="utf-8")
        self.assertIn("MAX_STAGED_BLOB_BYTES=90000000", workflow)
        self.assertIn("git diff --staged --name-only --diff-filter=ACM -z", workflow)
        self.assertIn("exceeds the 90 MB workflow limit", workflow)

    def test_site_metadata_contract(self):
        site_config = yaml.safe_load(Path("_config.yml").read_text(encoding="utf-8"))
        self.assertEqual(site_config["url"], "https://rss.tedt.org")
        self.assertEqual(site_config["source_url"], "https://github.com/TedTschopp/rss.tedt.org")
        self.assertEqual(site_config["github_url"], "https://github.com/TedTschopp/rss.tedt.org")
        self.assertEqual(site_config["logo"], "assets/images/logo.png")
        self.assertEqual(site_config["favicon"], "assets/images/favicon.svg")
        self.assertEqual(site_config["image"], "assets/images/social-card.png")
        default_image = site_config["defaults"][0]["values"]["image"]
        self.assertEqual(default_image["path"], "/assets/images/social-card.png")
        self.assertEqual(default_image["width"], 1731)
        self.assertEqual(default_image["height"], 909)
        self.assertNotIn("yourusername", Path("_config.yml").read_text(encoding="utf-8"))

    def test_site_templates_do_not_advertise_disabled_feeds(self):
        sitemap_template = Path("sitemap.xml").read_text(encoding="utf-8")
        about_template = Path("about.md").read_text(encoding="utf-8")
        index_template = Path("index.html").read_text(encoding="utf-8")
        feeds_template = Path("feeds.html").read_text(encoding="utf-8")
        self.assertIn("{% if feed.enabled != false %}", sitemap_template)
        self.assertIn("site.feeds | where_exp", about_template)
        self.assertIn("site.feeds | where_exp", index_template)
        self.assertIn("site.feeds | where_exp", feeds_template)
        self.assertNotIn("const allFeeds = {{ site.feeds | jsonify }}", index_template)
        self.assertNotIn("const allFeeds = {{ site.feeds | jsonify }}", feeds_template)

    def test_default_layout_delegates_core_metadata_to_seo_tag(self):
        layout = Path("_layouts/default.html").read_text(encoding="utf-8")
        self.assertIn("{% seo %}", layout)
        self.assertNotIn("<title>{% if page.title %}", layout)
        self.assertNotIn("<meta name=\"description\" content=\"{% if page.description %}", layout)

    def test_site_uses_rss_feed_hub_design_system(self):
        layout = Path("_layouts/default.html").read_text(encoding="utf-8")
        self.assertIn("/assets/css/rss-feed-hub.css", layout)
        self.assertIn("class=\"site-nav\"", layout)
        self.assertIn("/status/", layout)
        self.assertNotIn("bootstrap@", layout.lower())
        self.assertNotIn("Inter:wght", layout)

        css_path = Path("assets/css/rss-feed-hub.css")
        self.assertTrue(css_path.is_file())
        css = css_path.read_text(encoding="utf-8")
        self.assertIn("tokens/colors.css", css)
        self.assertIn("--format-rss2", css)
        self.assertIn("font-family: var(--font-mono)", css)

        for page_path in ["index.html", "feeds.html", "about.md"]:
            page = Path(page_path).read_text(encoding="utf-8")
            self.assertIn("feed-card", page, page_path)
            self.assertNotIn("box-shadow", page, page_path)

    def test_site_has_production_content_pages(self):
        self.assertTrue(Path("status.html").is_file())
        sitemap = Path("sitemap.xml").read_text(encoding="utf-8")
        self.assertIn("/status/", sitemap)

        production_terms = {
            "index.html": ["What This Site Publishes", "Update Cadence", "Operational Status"],
            "feeds.html": ["Format Guide", "Subscription Notes", "Operational Status"],
            "about.md": ["Operating Model", "Source Attribution", "Limits"],
            "status.html": ["Feed Status", "Pipeline Status", "Operational Notes"],
            "404.html": ["Page Not Found", "Available Routes", "feed-card"],
        }
        for path_text, terms in production_terms.items():
            text = Path(path_text).read_text(encoding="utf-8")
            for term in terms:
                self.assertIn(term, text, f"{term} missing from {path_text}")


if __name__ == "__main__":
    unittest.main()