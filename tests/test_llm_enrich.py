import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline.llm_enrich import enrich_stories


class FakeEmbeddingClient:
    embed_calls = 0
    embed_inputs = []

    @classmethod
    def reset(cls):
        cls.embed_calls = 0
        cls.embed_inputs = []

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
        raise AssertionError("summary should not be called in these tests")


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


if __name__ == "__main__":
    unittest.main()
