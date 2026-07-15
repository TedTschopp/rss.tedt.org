import os
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from threading import Barrier, Lock
from unittest.mock import patch

from pipeline.io_utils import write_json
from pipeline.publish import publish_outputs


class FakeClient:
    relevance_calls = 0
    importance_calls = 0

    @classmethod
    def reset(cls):
        cls.relevance_calls = 0
        cls.importance_calls = 0

    def check_ai_relevance(self, title, summary, rubric, model=None, article=""):
        FakeClient.relevance_calls += 1
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
        FakeClient.importance_calls += 1
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

    def rewrite_output_cleanup(self, title, summary, source_context, model=None):
        return {
            "title": "Clean AI story",
            "description": "Clean AI summary",
            "model": model or "fake-model",
            "input_hash": "cleanup-hash",
            "latency_ms": 1,
            "usage": {},
        }


class ConcurrentPublishClient(FakeClient):
    active_relevance_calls = 0
    max_active_relevance_calls = 0
    relevance_barrier = Barrier(2, timeout=1.0)
    lock = Lock()

    @classmethod
    def reset(cls):
        super().reset()
        cls.active_relevance_calls = 0
        cls.max_active_relevance_calls = 0
        cls.relevance_barrier = Barrier(2, timeout=1.0)

    def check_ai_relevance(self, title, summary, rubric, model=None, article=""):
        with self.lock:
            type(self).active_relevance_calls += 1
            type(self).max_active_relevance_calls = max(
                type(self).max_active_relevance_calls,
                type(self).active_relevance_calls,
            )
        try:
            self.relevance_barrier.wait()
            return super().check_ai_relevance(title, summary, rubric, model=model, article=article)
        finally:
            with self.lock:
                type(self).active_relevance_calls -= 1


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

            with patch.dict(os.environ, {"GH_MODELS_TOKEN": "test-token"}):
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

            with patch.dict(os.environ, {"GH_MODELS_TOKEN": "test-token"}):
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

    def test_backfill_bounds_uncached_article_fetches_and_model_work(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            stories = [
                self._story(f"s{index}", f"https://example.com/{index}")
                for index in range(1, 4)
            ]
            FakeClient.reset()
            with patch.dict(os.environ, {"GH_MODELS_TOKEN": "test-token"}):
                with patch("pipeline.publish.GitHubModelsClient", return_value=FakeClient()):
                    with patch("pipeline.publish.MultiFeedGenerator", FakeFeedGenerator):
                        with patch(
                            "pipeline.publish._fetch_article_with_url",
                            side_effect=lambda url, _timeout, _max_chars: (url, "Article markdown"),
                        ) as fetch_mock:
                            publish_outputs(
                                stories,
                                str(Path(temp_dir) / "api" / "feed.json"),
                                str(Path(temp_dir) / "feeds" / "top"),
                                llm_cache={},
                                config={
                                    "backfill_mode": True,
                                    "publish_top_n": 3,
                                    "article_cache_enabled": False,
                                    "article_fetch_max_urls": 1,
                                    "output_cleanup_enabled": False,
                                    "llm_rate_limit_requests_per_window": 0,
                                    "llm_rate_limit_min_interval_sec": 0.0,
                                    "ai_keywords": ["ai"],
                                },
                            )

        self.assertEqual(fetch_mock.call_count, 1)
        self.assertEqual(FakeClient.relevance_calls, 1)

    def test_backfill_failed_fetch_does_not_starve_next_url(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            article_cache_path = str(Path(temp_dir) / "article-cache.json")
            stories = [
                self._story(f"s{index}", f"https://example.com/{index}")
                for index in range(1, 3)
            ]
            config = {
                "backfill_mode": True,
                "publish_top_n": 2,
                "article_cache_enabled": True,
                "article_cache_path": article_cache_path,
                "article_fetch_max_urls": 1,
                "output_cleanup_enabled": False,
                "llm_rate_limit_requests_per_window": 0,
                "llm_rate_limit_min_interval_sec": 0.0,
                "ai_keywords": ["ai"],
            }

            with patch.dict(os.environ, {"GH_MODELS_TOKEN": "test-token"}):
                with patch("pipeline.publish.GitHubModelsClient", return_value=FakeClient()):
                    with patch("pipeline.publish.MultiFeedGenerator", FakeFeedGenerator):
                        with patch(
                            "pipeline.publish._fetch_article_with_url",
                            side_effect=RuntimeError("unavailable"),
                        ):
                            _payload, cache = publish_outputs(
                                stories,
                                str(Path(temp_dir) / "api" / "feed.json"),
                                str(Path(temp_dir) / "feeds" / "top"),
                                llm_cache={},
                                config=config,
                            )
                        fetched_urls = []
                        with patch(
                            "pipeline.publish._fetch_article_with_url",
                            side_effect=lambda url, _timeout, _max_chars: fetched_urls.append(url) or (url, "Article"),
                        ):
                            publish_outputs(
                                stories,
                                str(Path(temp_dir) / "api" / "feed.json"),
                                str(Path(temp_dir) / "feeds" / "top"),
                                llm_cache=cache,
                                config=config,
                            )

        self.assertEqual(fetched_urls, ["https://example.com/2"])

    def test_grading_call_caps_count_only_cache_misses(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            api_path = str(Path(temp_dir) / "api" / "feed.json")
            base_feed_path = str(Path(temp_dir) / "feeds" / "top")
            stories = [
                self._story(f"s{index}", f"https://example.com/{index}")
                for index in range(1, 4)
            ]
            config = {
                "publish_top_n": 3,
                "output_cleanup_enabled": False,
                "article_cache_enabled": False,
                "ai_relevance_max_calls": 1,
                "importance_max_calls": 1,
                "llm_rate_limit_requests_per_window": 0,
                "llm_rate_limit_min_interval_sec": 0.0,
                "ai_keywords": ["ai"],
            }

            with patch.dict(os.environ, {"GH_MODELS_TOKEN": "test-token"}):
                with patch("pipeline.publish.GitHubModelsClient", return_value=FakeClient()):
                    with patch("pipeline.publish.MultiFeedGenerator", FakeFeedGenerator):
                        with patch(
                            "pipeline.publish._fetch_article_with_url",
                            side_effect=lambda url, _timeout, _max_chars: (url, "Article markdown"),
                        ):
                            _payload, cache = publish_outputs(
                                [stories[0]],
                                api_path,
                                base_feed_path,
                                llm_cache={},
                                config=config,
                            )
                            FakeClient.reset()
                            llm_status = {}
                            _payload, updated_cache = publish_outputs(
                                stories,
                                api_path,
                                base_feed_path,
                                llm_cache=cache,
                                llm_status=llm_status,
                                config=config,
                            )

        self.assertEqual(FakeClient.relevance_calls, 1)
        self.assertEqual(FakeClient.importance_calls, 1)
        self.assertIn("ai_relevance", updated_cache["s2"])
        self.assertIn("importance", updated_cache["s2"])
        self.assertNotIn("ai_relevance", updated_cache.get("s3", {}))
        self.assertNotIn("importance", updated_cache.get("s3", {}))
        self.assertEqual(llm_status["backlog"]["ai_relevance"], {"before": 2, "remaining": 1})
        self.assertEqual(llm_status["backlog"]["importance"], {"before": 0, "remaining": 0})

    def test_publish_workers_run_relevance_calls_concurrently(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            stories = [
                self._story("s1", "https://example.com/1"),
                self._story("s2", "https://example.com/2"),
            ]
            client = ConcurrentPublishClient()
            ConcurrentPublishClient.reset()
            with patch("pipeline.publish._resolve_llm_client", return_value=(client, None, "OpenAI")):
                with patch("pipeline.publish.MultiFeedGenerator", FakeFeedGenerator):
                    with patch(
                        "pipeline.publish._fetch_article_with_url",
                        side_effect=lambda url, _timeout, _max_chars: (url, "Article markdown"),
                    ):
                        _payload, cache = publish_outputs(
                            stories,
                            str(Path(temp_dir) / "api" / "feed.json"),
                            str(Path(temp_dir) / "feeds" / "top"),
                            llm_cache={},
                            config={
                                "llm_provider": "openai",
                                "llm_workers": 2,
                                "openai_rate_limit_requests_per_minute": 60000,
                                "publish_top_n": 2,
                                "article_cache_enabled": False,
                                "output_cleanup_enabled": False,
                                "ai_relevance_max_calls": 2,
                                "importance_max_calls": 2,
                                "llm_rate_limit_min_interval_sec": 0.0,
                                "ai_keywords": ["ai"],
                            },
                        )

        self.assertEqual(ConcurrentPublishClient.max_active_relevance_calls, 2)
        self.assertIn("importance", cache["s1"])
        self.assertIn("importance", cache["s2"])

    def test_output_cleanup_does_not_recreate_relevance_backlog(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            llm_status = {}
            story = self._story("s1", "https://example.com/1")
            with patch.dict(os.environ, {"GH_MODELS_TOKEN": "test-token"}):
                with patch("pipeline.publish.GitHubModelsClient", return_value=FakeClient()):
                    with patch("pipeline.publish.MultiFeedGenerator", FakeFeedGenerator):
                        with patch(
                            "pipeline.publish._fetch_article_with_url",
                            return_value=(story["canonical_url"], "Article markdown"),
                        ):
                            publish_outputs(
                                [story],
                                str(Path(temp_dir) / "api" / "feed.json"),
                                str(Path(temp_dir) / "feeds" / "top"),
                                llm_cache={},
                                llm_status=llm_status,
                                config={
                                    "publish_top_n": 1,
                                    "output_cleanup_top_n": 1,
                                    "article_cache_enabled": False,
                                    "llm_rate_limit_requests_per_window": 0,
                                    "llm_rate_limit_min_interval_sec": 0.0,
                                    "ai_keywords": ["ai"],
                                },
                            )

        self.assertEqual(llm_status["backlog_remaining"], 0)
        self.assertEqual(llm_status["backlog"]["ai_relevance"]["remaining"], 0)

if __name__ == "__main__":
    unittest.main()
