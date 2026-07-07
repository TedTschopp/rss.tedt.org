from pathlib import Path
import unittest

import yaml

from scripts import config
from scripts.validate_workflow import validate as validate_workflow


class PathContractTests(unittest.TestCase):
    def test_status_path_contract(self):
        self.assertEqual(config.STATUS_REPORT_FILE, "api/rss_status.json")
        self.assertIn("/api/rss_status.json", Path("feeds.html").read_text(encoding="utf-8"))
        self.assertIn("/api/rss_status.json", Path("about.md").read_text(encoding="utf-8"))

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

    def test_workflow_contract_validator_passes(self):
        self.assertEqual(validate_workflow(verbose=False), [])

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
        self.assertIn("{% if feed.enabled != false %}", about_template)
        self.assertIn("site.feeds | where_exp", index_template)
        self.assertIn("site.feeds | where_exp", feeds_template)
        self.assertNotIn("const allFeeds = {{ site.feeds | jsonify }}", index_template)
        self.assertNotIn("const allFeeds = {{ site.feeds | jsonify }}", feeds_template)

    def test_default_layout_delegates_core_metadata_to_seo_tag(self):
        layout = Path("_layouts/default.html").read_text(encoding="utf-8")
        self.assertIn("{% seo %}", layout)
        self.assertNotIn("<title>{% if page.title %}", layout)
        self.assertNotIn("<meta name=\"description\" content=\"{% if page.description %}", layout)


if __name__ == "__main__":
    unittest.main()