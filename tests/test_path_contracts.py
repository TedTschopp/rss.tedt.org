from pathlib import Path
import unittest

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


if __name__ == "__main__":
    unittest.main()