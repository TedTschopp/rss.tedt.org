import tempfile
import unittest
from pathlib import Path
from threading import Barrier, Lock
from unittest.mock import patch

from pipeline.llm_enrich import enrich_stories


class FakeEmbeddingClient:
    embed_calls = 0
    embed_inputs = []
    summary_titles = []

    @classmethod
    def reset(cls):
        cls.embed_calls = 0
        cls.embed_inputs = []
        cls.summary_titles = []

    def __init__(self, token, timeout_sec):
        self.token = token
        self.timeout_sec = timeout_sec

    def embed(self, texts, model="openai/text-embedding-3-small"):
        FakeEmbeddingClient.embed_calls += 1
        FakeEmbeddingClient.embed_inputs.append(list(texts))
        return {
            "vectors": [[float(index), 0.0] for index, _text in enumerate(texts, start=1)],
            "usage": {"total_tokens": len(texts)},
            "latency_ms": 1,
            "model": model,
            "input_hash": "batch-input-hash",
        }

    def summarize(self, title, summary, model="openai/gpt-4.1-mini"):
        FakeEmbeddingClient.summary_titles.append(title)
        return {
            "summary": f"Summary for {title}",
            "topics": ["AI"],
            "entities": [],
            "usage": {},
            "latency_ms": 1,
            "model": model,
            "input_hash": f"summary-{title}",
        }


class ConcurrentSummaryClient(FakeEmbeddingClient):
    active_calls = 0
    max_active_calls = 0
    barrier = Barrier(2, timeout=1.0)
    lock = Lock()

    @classmethod
    def reset(cls):
        super().reset()
        cls.active_calls = 0
        cls.max_active_calls = 0
        cls.barrier = Barrier(2, timeout=1.0)

    def summarize(self, title, summary, model="openai/gpt-4.1-mini"):
        with self.lock:
            type(self).active_calls += 1
            type(self).max_active_calls = max(type(self).max_active_calls, type(self).active_calls)
        try:
            self.barrier.wait()
            return super().summarize(title, summary, model=model)
        finally:
            with self.lock:
                type(self).active_calls -= 1


class LLMEnrichTests(unittest.TestCase):
    def _story(self, story_id, title="AI story", summary="AI summary"):
        return {
            "story_id": story_id,
            "title": title,
            "summary": summary,
        }

    def test_cached_embedding_context_skips_embedding_api_call(self):
        story = self._story("story-1")
        cache = {
            "story-1": {
                "embedding": [0.1, 0.2],
                "embedding_context_hash": "placeholder",
            }
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            log_path = str(Path(temp_dir) / "llm_call_log.jsonl")
            FakeEmbeddingClient.reset()
            with patch("pipeline.llm_enrich.GitHubModelsClient", FakeEmbeddingClient):
                with patch.dict("os.environ", {"GH_MODELS_TOKEN": "token"}):
                    # Prime the expected context hash by running once with a real call.
                    _stories, primed_cache, _meta = enrich_stories(
                        [dict(story)],
                        {},
                        log_path,
                        {
                            "llm_top_n": 1,
                            "llm_chat_max_calls": 0,
                            "llm_rate_limit_requests_per_window": 0,
                            "llm_rate_limit_min_interval_sec": 0.0,
                        },
                    )
                    FakeEmbeddingClient.reset()
                    stories, updated_cache, meta = enrich_stories(
                        [dict(story)],
                        primed_cache,
                        log_path,
                        {
                            "llm_top_n": 1,
                            "llm_chat_max_calls": 0,
                            "llm_rate_limit_requests_per_window": 0,
                            "llm_rate_limit_min_interval_sec": 0.0,
                        },
                    )

        self.assertEqual(FakeEmbeddingClient.embed_calls, 0)
        self.assertEqual(meta["calls"], 0)
        self.assertEqual(stories[0]["llm"]["embedding_dim"], 2)
        self.assertEqual(updated_cache["story-1"]["embedding"], [1.0, 0.0])

    def test_only_uncached_embeddings_are_sent_to_embedding_api(self):
        stories = [
            self._story("story-1", "Cached title", "Cached summary"),
            self._story("story-2", "Fresh title", "Fresh summary"),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            log_path = str(Path(temp_dir) / "llm_call_log.jsonl")
            FakeEmbeddingClient.reset()
            with patch("pipeline.llm_enrich.GitHubModelsClient", FakeEmbeddingClient):
                with patch.dict("os.environ", {"GH_MODELS_TOKEN": "token"}):
                    _stories, primed_cache, _meta = enrich_stories(
                        [dict(stories[0])],
                        {},
                        log_path,
                        {
                            "llm_top_n": 1,
                            "llm_chat_max_calls": 0,
                            "llm_rate_limit_requests_per_window": 0,
                            "llm_rate_limit_min_interval_sec": 0.0,
                        },
                    )
                    FakeEmbeddingClient.reset()
                    enriched, updated_cache, meta = enrich_stories(
                        [dict(stories[0]), dict(stories[1])],
                        primed_cache,
                        log_path,
                        {
                            "llm_top_n": 2,
                            "llm_chat_max_calls": 0,
                            "llm_rate_limit_requests_per_window": 0,
                            "llm_rate_limit_min_interval_sec": 0.0,
                        },
                    )

        self.assertEqual(FakeEmbeddingClient.embed_calls, 1)
        self.assertEqual(len(FakeEmbeddingClient.embed_inputs[0]), 1)
        self.assertIn("Fresh title", FakeEmbeddingClient.embed_inputs[0][0])
        self.assertEqual(meta["calls"], 1)
        self.assertEqual(enriched[0]["llm"]["embedding_dim"], 2)
        self.assertEqual(enriched[1]["llm"]["embedding_dim"], 2)
        self.assertIn("embedding_context_hash", updated_cache["story-1"])
        self.assertIn("embedding_context_hash", updated_cache["story-2"])

    def test_cached_summaries_do_not_consume_call_limit(self):
        stories = [
            self._story("story-1", "Cached title"),
            self._story("story-2", "First missing title"),
            self._story("story-3", "Second missing title"),
        ]
        cache = {
            "story-1": {
                "summary": "Cached summary",
                "topics": ["AI"],
            }
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            log_path = str(Path(temp_dir) / "llm_call_log.jsonl")
            FakeEmbeddingClient.reset()
            with patch("pipeline.llm_enrich.GitHubModelsClient", FakeEmbeddingClient):
                with patch.dict("os.environ", {"GH_MODELS_TOKEN": "token"}):
                    _stories, updated_cache, meta = enrich_stories(
                        stories,
                        cache,
                        log_path,
                        {
                            "llm_top_n": 3,
                            "llm_chat_max_calls": 1,
                            "llm_rate_limit_requests_per_window": 0,
                            "llm_rate_limit_min_interval_sec": 0.0,
                        },
                    )

        self.assertEqual(FakeEmbeddingClient.summary_titles, ["First missing title"])
        self.assertIn("summary", updated_cache["story-2"])
        self.assertNotIn("summary", updated_cache["story-3"])
        self.assertEqual(meta["backlog"]["summaries"], {"before": 2, "remaining": 1})

    def test_summary_workers_run_model_calls_concurrently(self):
        stories = [
            self._story("story-1", "First title"),
            self._story("story-2", "Second title"),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            log_path = str(Path(temp_dir) / "llm_call_log.jsonl")
            ConcurrentSummaryClient.reset()
            client = ConcurrentSummaryClient("token", 25)
            with patch("pipeline.llm_enrich._resolve_llm_client", return_value=(client, None, "OpenAI")):
                _stories, updated_cache, meta = enrich_stories(
                    stories,
                    {},
                    log_path,
                    {
                        "llm_provider": "openai",
                        "llm_top_n": 2,
                        "llm_chat_max_calls": 2,
                        "llm_workers": 2,
                        "openai_rate_limit_requests_per_minute": 60000,
                        "llm_rate_limit_min_interval_sec": 0.0,
                    },
                )

        self.assertEqual(ConcurrentSummaryClient.max_active_calls, 2)
        self.assertIn("summary", updated_cache["story-1"])
        self.assertIn("summary", updated_cache["story-2"])
        self.assertEqual(meta["backlog"]["summaries"], {"before": 2, "remaining": 0})

    def test_uncached_embeddings_are_split_into_bounded_batches(self):
        stories = [self._story(f"story-{index}") for index in range(5)]

        with tempfile.TemporaryDirectory() as temp_dir:
            log_path = str(Path(temp_dir) / "llm_call_log.jsonl")
            FakeEmbeddingClient.reset()
            with patch("pipeline.llm_enrich.GitHubModelsClient", FakeEmbeddingClient):
                with patch.dict("os.environ", {"GH_MODELS_TOKEN": "token"}):
                    _stories, _cache, meta = enrich_stories(
                        stories,
                        {},
                        log_path,
                        {
                            "llm_top_n": 5,
                            "llm_chat_max_calls": 0,
                            "llm_embedding_batch_size": 2,
                            "llm_rate_limit_requests_per_window": 0,
                            "llm_rate_limit_min_interval_sec": 0.0,
                        },
                    )

        self.assertEqual([len(batch) for batch in FakeEmbeddingClient.embed_inputs], [2, 2, 1])
        self.assertEqual(meta["calls"], 3)
        self.assertEqual(meta["backlog"]["embeddings"], {"before": 5, "remaining": 0})

    def test_embedding_story_cap_leaves_remaining_work_for_next_run(self):
        stories = [self._story(f"story-{index}") for index in range(5)]

        with tempfile.TemporaryDirectory() as temp_dir:
            log_path = str(Path(temp_dir) / "llm_call_log.jsonl")
            FakeEmbeddingClient.reset()
            with patch("pipeline.llm_enrich.GitHubModelsClient", FakeEmbeddingClient):
                with patch.dict("os.environ", {"GH_MODELS_TOKEN": "token"}):
                    _stories, _cache, meta = enrich_stories(
                        stories,
                        {},
                        log_path,
                        {
                            "llm_top_n": 5,
                            "llm_chat_max_calls": 0,
                            "llm_embedding_batch_size": 2,
                            "llm_embedding_max_stories": 3,
                            "llm_rate_limit_requests_per_window": 0,
                            "llm_rate_limit_min_interval_sec": 0.0,
                        },
                    )

        self.assertEqual([len(batch) for batch in FakeEmbeddingClient.embed_inputs], [2, 1])
        self.assertEqual(meta["backlog"]["embeddings"], {"before": 5, "remaining": 2})


if __name__ == "__main__":
    unittest.main()
