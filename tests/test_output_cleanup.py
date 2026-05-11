import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline.llm_client import GitHubModelsClient
from pipeline.publish import publish_outputs


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


class FakeSession:
    def __init__(self, responses):
        self.headers = {}
        self.responses = list(responses)
        self.payloads = []

    def post(self, url, json=None, timeout=None):
        self.payloads.append(json)
        return FakeResponse(
            {
                "choices": [
                    {
                        "message": {
                            "content": self.responses.pop(0),
                        }
                    }
                ],
                "usage": {"total_tokens": 25},
            }
        )


class FakeOutputCleanupClient:
    seen_title_model = None
    seen_description_model = None

    def __init__(self, token, timeout_sec):
        self.token = token
        self.timeout_sec = timeout_sec

    def rewrite_output_title(self, title, summary, source_context, model):
        FakeOutputCleanupClient.seen_title_model = model
        return {
            "title": "OpenAI Adds Enterprise Data Controls",
            "usage": {"total_tokens": 10},
            "latency_ms": 1,
            "model": model,
            "input_hash": "title-input-hash",
        }

    def rewrite_output_description(self, title, summary, source_context, model):
        FakeOutputCleanupClient.seen_description_model = model
        return {
            "description": "OpenAI introduced enterprise data controls for governed AI deployments.",
            "usage": {"total_tokens": 15},
            "latency_ms": 1,
            "model": model,
            "input_hash": "description-input-hash",
        }


class OutputCleanupTests(unittest.TestCase):
    def test_rewrite_methods_use_prompt_folder_and_return_clean_text(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            prompts_dir = Path(temp_dir)
            cleanup_dir = prompts_dir / "output_cleanup"
            cleanup_dir.mkdir()
            (cleanup_dir / "title_system.txt").write_text("Rewrite title system prompt.", encoding="utf-8")
            (cleanup_dir / "title_user.txt").write_text(
                "Title: {title}\nSummary: {summary}\nSources: {source_context}",
                encoding="utf-8",
            )
            (cleanup_dir / "title_schema.json").write_text(
                json.dumps(
                    {
                        "type": "json_schema",
                        "json_schema": {
                            "name": "output_title_rewrite",
                            "schema": {
                                "type": "object",
                                "properties": {"title": {"type": "string"}},
                                "required": ["title"],
                                "additionalProperties": False,
                            },
                        },
                    }
                ),
                encoding="utf-8",
            )
            (cleanup_dir / "description_system.txt").write_text("Rewrite description system prompt.", encoding="utf-8")
            (cleanup_dir / "description_user.txt").write_text(
                "Title: {title}\nSummary: {summary}\nSources: {source_context}",
                encoding="utf-8",
            )
            (cleanup_dir / "description_schema.json").write_text(
                json.dumps(
                    {
                        "type": "json_schema",
                        "json_schema": {
                            "name": "output_description_rewrite",
                            "schema": {
                                "type": "object",
                                "properties": {"description": {"type": "string"}},
                                "required": ["description"],
                                "additionalProperties": False,
                            },
                        },
                    }
                ),
                encoding="utf-8",
            )

            client = GitHubModelsClient(token="test-token")
            client.prompts_dir = prompts_dir
            client.session = FakeSession(
                [
                    json.dumps({"title": "Clean output title"}),
                    json.dumps({"description": "Clean output description."}),
                ]
            )

            title_result = client.rewrite_output_title("Raw Title", "Raw summary", "Source context", model="test-model")
            description_result = client.rewrite_output_description("Raw Title", "Raw summary", "Source context", model="test-model")

            self.assertEqual(title_result["title"], "Clean output title")
            self.assertEqual(description_result["description"], "Clean output description.")
            self.assertEqual(client.session.payloads[0]["messages"][0]["content"], "Rewrite title system prompt.")
            self.assertIn("Source context", client.session.payloads[0]["messages"][1]["content"])
            self.assertEqual(client.session.payloads[1]["messages"][0]["content"], "Rewrite description system prompt.")

    def test_publish_outputs_uses_rewritten_title_and_description(self):
        old_env = dict(os.environ)
        story = {
            "story_id": "story-1",
            "title": "Raw OpenAI data controls headline",
            "summary": "Raw summary with uneven wording.",
            "canonical_url": "https://example.com/story",
            "url": "https://example.com/story",
            "source_name": "Example Source",
            "source_type": "rss",
            "source_category": "rss",
            "published": "2020-01-01T00:00:00Z",
            "score": 100,
            "mentions": [],
            "sources": [],
            "alternate_links": [],
            "cluster_id": "cluster-1",
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            api_path = Path(temp_dir) / "feed.json"
            base_feed_path = Path(temp_dir) / "top"
            try:
                os.environ["GH_MODELS_TOKEN"] = "test-token"
                with patch("pipeline.publish.GitHubModelsClient", FakeOutputCleanupClient):
                    payload, cache = publish_outputs(
                        [story],
                        str(api_path),
                        str(base_feed_path),
                        llm_cache={},
                        config={
                            "publish_top_n": 1,
                            "output_cleanup_top_n": 1,
                            "output_cleanup_model": "test-cleanup-model",
                            "importance_backfill_days": 0,
                            "ai_keywords": ["openai"],
                        },
                    )
            finally:
                os.environ.clear()
                os.environ.update(old_env)

            self.assertEqual(payload["items"][0]["title"], "OpenAI Adds Enterprise Data Controls")
            self.assertEqual(
                payload["items"][0]["summary"],
                "OpenAI introduced enterprise data controls for governed AI deployments.",
            )
            self.assertEqual(payload["items"][0]["originalTitle"], "Raw OpenAI data controls headline")
            self.assertEqual(payload["items"][0]["originalSummary"], "Raw summary with uneven wording.")
            self.assertEqual(FakeOutputCleanupClient.seen_title_model, "test-cleanup-model")
            self.assertEqual(FakeOutputCleanupClient.seen_description_model, "test-cleanup-model")
            self.assertEqual(cache["story-1"]["output_cleanup"]["title"], "OpenAI Adds Enterprise Data Controls")

            xml_text = (base_feed_path.with_suffix(".xml")).read_text(encoding="utf-8")
            self.assertIn("OpenAI Adds Enterprise Data Controls", xml_text)
            self.assertIn("OpenAI introduced enterprise data controls", xml_text)
            self.assertNotIn("Raw OpenAI data controls headline", xml_text)


if __name__ == "__main__":
    unittest.main()