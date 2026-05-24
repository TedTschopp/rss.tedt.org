import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from pipeline.io_utils import write_json
from pipeline.publish import publish_outputs


class FakeClient:
    def check_ai_relevance(self, title, summary, rubric, model=None, article=""):
        return {
            "is_ai_related": True,
            "decision": "proceed",
            "confidence": "high",
            "primary_ai_topic": "ai",
            "rationale": "relevant",
            "evidence": [],
            "model": model or "fake-model",
            "input_hash": "relevance-hash",
            "latency_ms": 1,
            "usage": {},
        }

    def grade_importance(self, title, summary, rubric, model=None, article=""):
        return {
            "business_level": 2,
            "technical_level": 2,
            "business_impact": "[ * ]",
            "technical_impact": "[ ◼ ]",
            "risk_impact": "medium",
            "enterprise_readiness": "medium",
            "labor_workflow_impact": "medium",
            "confidence": "high",
            "attention_priority": "monitor",
            "development_summary": "summary",
            "reason_codes": [],
            "recommended_action": "watch",
            "rationale": "important",
            "watch_items": [],
            "business_rationale": "biz",
            "technical_rationale": "tech",
            "model": model or "fake-model",
            "input_hash": "importance-hash",
            "latency_ms": 1,
            "usage": {},
        }


class FakeFeedGenerator:
    def __init__(self, *args, **kwargs):
        self.items = []

    def add_item(self, **kwargs):
        self.items.append(kwargs)

    def write_all_formats(self, base_feed_path):
        base = Path(base_feed_path)
        base.parent.mkdir(parents=True, exist_ok=True)
        for suffix in [".xml", ".atom", ".json", "_rss1.xml"]:
            (base.parent / f"{base.name}{suffix}").write_text("", encoding="utf-8")


class PublishTests(unittest.TestCase):
    def _story(self, story_id: str, url: str) -> dict:
        return {
            "story_id": story_id,
            "title": "AI story",
            "summary": "AI summary",
            "published": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "canonical_url": url,
            "url": url,
            "source_name": "Example",
            "source_type": "rss",
            "source_category": "ai",
            "score": 10,
            "mentions": [],
        }

    def test_article_cache_hit_skips_fetch(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            cache_path = Path(temp_dir) / "article_cache.json"
            url = "https://example.com/a"
            write_json(
                str(cache_path),
                {
                    url: {
                        "markdown": "cached markdown",
                        "fetched_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                    }
                },
            )

            api_path = str(Path(temp_dir) / "api" / "feed.json")
            base_feed_path = str(Path(temp_dir) / "feeds" / "top")
            ranked = [self._story("s1", url)]

            with patch("pipeline.publish.GitHubModelsClient", return_value=FakeClient()):
                with patch("pipeline.publish.MultiFeedGenerator", FakeFeedGenerator):
                    with patch("pipeline.publish.fetch_article_markdown") as fetch_mock:
                        publish_outputs(
                            ranked,
                            api_path,
                            base_feed_path,
                            llm_cache={},
                            config={
                                "request_timeout_sec": 5,
                                "output_cleanup_enabled": False,
                                "article_cache_enabled": True,
                                "article_cache_path": str(cache_path),
                                "article_cache_ttl_hours": 48,
                            },
                        )

            self.assertEqual(fetch_mock.call_count, 0)

    def test_duplicate_urls_fetched_once(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            cache_path = Path(temp_dir) / "article_cache.json"
            api_path = str(Path(temp_dir) / "api" / "feed.json")
            base_feed_path = str(Path(temp_dir) / "feeds" / "top")
            url = "https://example.com/shared"
            ranked = [self._story("s1", url), self._story("s2", url)]

            with patch("pipeline.publish.GitHubModelsClient", return_value=FakeClient()):
                with patch("pipeline.publish.MultiFeedGenerator", FakeFeedGenerator):
                    with patch("pipeline.publish.fetch_article_markdown", return_value="fresh markdown") as fetch_mock:
                        publish_outputs(
                            ranked,
                            api_path,
                            base_feed_path,
                            llm_cache={},
                            config={
                                "request_timeout_sec": 5,
                                "output_cleanup_enabled": False,
                                "article_cache_enabled": True,
                                "article_cache_path": str(cache_path),
                                "article_cache_ttl_hours": 48,
                                "article_fetch_workers": 4,
                            },
                        )

            self.assertEqual(fetch_mock.call_count, 1)


if __name__ == "__main__":
    unittest.main()
