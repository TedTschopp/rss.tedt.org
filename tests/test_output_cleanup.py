import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from xml.etree import ElementTree as ET

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
    seen_title_source_context = None
    seen_description_source_context = None
    seen_description_summary = None
    title_calls = 0
    description_calls = 0

    @classmethod
    def reset(cls):
        cls.seen_title_model = None
        cls.seen_description_model = None
        cls.seen_title_source_context = None
        cls.seen_description_source_context = None
        cls.seen_description_summary = None
        cls.title_calls = 0
        cls.description_calls = 0

    def __init__(self, token, timeout_sec):
        self.token = token
        self.timeout_sec = timeout_sec

    def rewrite_output_title(self, title, summary, source_context, model):
        FakeOutputCleanupClient.title_calls += 1
        FakeOutputCleanupClient.seen_title_model = model
        FakeOutputCleanupClient.seen_title_source_context = source_context
        return {
            "title": "OpenAI Adds Enterprise Data Controls",
            "usage": {"total_tokens": 10},
            "latency_ms": 1,
            "model": model,
            "input_hash": "title-input-hash",
        }

    def rewrite_output_description(self, title, summary, source_context, model):
        FakeOutputCleanupClient.description_calls += 1
        FakeOutputCleanupClient.seen_description_model = model
        FakeOutputCleanupClient.seen_description_summary = summary
        FakeOutputCleanupClient.seen_description_source_context = source_context
        return {
            "description": "OpenAI introduced enterprise data controls for governed AI deployments.",
            "usage": {"total_tokens": 15},
            "latency_ms": 1,
            "model": model,
            "input_hash": "description-input-hash",
        }


class OutputCleanupTests(unittest.TestCase):
    def test_title_rewrite_includes_standard_headline_instructions(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            prompts_dir = temp_path / "prompts"
            cleanup_dir = prompts_dir / "output_cleanup"
            cleanup_dir.mkdir(parents=True)
            headline_instructions = temp_path / "Headline-Generation-Instructions.md"
            headline_instructions.write_text(
                "# Headline Generation Instructions\n\n"
                "Rewrite article titles into concise, factual, Techmeme-style headlines.\n\n"
                "The headline should generally be 18-35 words.\n\n"
                "Use attribution when needed and avoid hype.",
                encoding="utf-8",
            )
            (cleanup_dir / "title_system.txt").write_text("Application title prompt.", encoding="utf-8")
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

            client = GitHubModelsClient(token="test-token")
            client.prompts_dir = prompts_dir
            client.headline_instructions_path = headline_instructions
            client.session = FakeSession([json.dumps({"title": "Microsoft adds Copilot Studio approval workflows for enterprise admins"})])

            client.rewrite_output_title("Raw Title", "Raw summary", "Source context", model="test-model")

            system_message = client.session.payloads[0]["messages"][0]["content"]
            self.assertIn("Techmeme-style headlines", system_message)
            self.assertIn("18-35 words", system_message)
            self.assertIn("Application title prompt.", system_message)
            self.assertIn("Return JSON matching the provided schema", system_message)

    def test_description_rewrite_includes_standard_article_summary_instructions(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            prompts_dir = temp_path / "prompts"
            cleanup_dir = prompts_dir / "output_cleanup"
            cleanup_dir.mkdir(parents=True)
            article_summary_instructions = temp_path / "Article-Summary.md"
            article_summary_instructions.write_text(
                "You are an expert news summarizer. Your job is to turn a news article "
                "into a brief, polished, formatted description of 1 to 3 paragraphs.\n\n"
                "Return the final formatted description only.",
                encoding="utf-8",
            )
            (cleanup_dir / "description_system.txt").write_text("Application description prompt.", encoding="utf-8")
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
            client.article_summary_instructions_path = article_summary_instructions
            client.session = FakeSession([json.dumps({"description": "Microsoft added approval workflows for enterprise AI admins."})])

            client.rewrite_output_description("Raw Title", "Raw summary", "Source context", model="test-model")

            system_message = client.session.payloads[0]["messages"][0]["content"]
            self.assertIn("brief, polished, formatted description", system_message)
            self.assertIn("1 to 3 paragraphs", system_message)
            self.assertIn("Application description prompt.", system_message)
            self.assertIn("Return JSON matching the provided schema", system_message)

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
            client.headline_instructions_path = prompts_dir / "missing-headline-instructions.md"
            client.article_summary_instructions_path = prompts_dir / "missing-article-summary-instructions.md"
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
                    with patch("pipeline.publish._fetch_article_with_url", return_value=("https://example.com/story", "")):
                        payload, cache = publish_outputs(
                            [story],
                            str(api_path),
                            str(base_feed_path),
                            llm_cache={},
                            config={
                                "publish_top_n": 1,
                                "output_cleanup_top_n": 1,
                                "output_cleanup_model": "test-cleanup-model",
                                "llm_rate_limit_requests_per_window": 0,
                                "llm_rate_limit_min_interval_sec": 0.0,
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

    def test_publish_outputs_reuses_cached_cleanup_and_skips_model_call(self):
        old_env = dict(os.environ)
        story = {
            "story_id": "story-cache",
            "title": "Raw OpenAI headline",
            "summary": "Raw OpenAI summary.",
            "canonical_url": "https://example.com/cache-story",
            "url": "https://example.com/cache-story",
            "source_name": "Example Source",
            "source_type": "rss",
            "source_category": "rss",
            "published": "2020-01-01T00:00:00Z",
            "score": 100,
            "mentions": [],
            "sources": [],
            "alternate_links": [],
            "cluster_id": "cluster-cache",
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            api_path = Path(temp_dir) / "feed.json"
            base_feed_path = Path(temp_dir) / "top"
            try:
                os.environ["GH_MODELS_TOKEN"] = "test-token"
                FakeOutputCleanupClient.reset()
                with patch("pipeline.publish.GitHubModelsClient", FakeOutputCleanupClient):
                    with patch("pipeline.publish._fetch_article_with_url", return_value=("https://example.com/cache-story", "")):
                        first_payload, cache = publish_outputs(
                            [story],
                            str(api_path),
                            str(base_feed_path),
                            llm_cache={},
                            config={
                                "publish_top_n": 1,
                                "output_cleanup_top_n": 1,
                                "output_cleanup_model": "test-cleanup-model",
                                "importance_backfill_days": 0,
                                "llm_rate_limit_requests_per_window": 0,
                                "llm_rate_limit_min_interval_sec": 0.0,
                                "ai_keywords": ["openai"],
                            },
                        )
                        second_payload, _second_cache = publish_outputs(
                            [dict(story)],
                            str(api_path),
                            str(base_feed_path),
                            llm_cache=cache,
                            config={
                                "publish_top_n": 1,
                                "output_cleanup_top_n": 1,
                                "output_cleanup_model": "test-cleanup-model",
                                "importance_backfill_days": 0,
                                "llm_rate_limit_requests_per_window": 0,
                                "llm_rate_limit_min_interval_sec": 0.0,
                                "ai_keywords": ["openai"],
                            },
                        )
            finally:
                os.environ.clear()
                os.environ.update(old_env)

            self.assertEqual(FakeOutputCleanupClient.title_calls, 1)
            self.assertEqual(FakeOutputCleanupClient.description_calls, 1)
            self.assertEqual(first_payload["items"][0]["summary"], second_payload["items"][0]["summary"])
            self.assertEqual(second_payload["items"][0]["title"], "OpenAI Adds Enterprise Data Controls")

    def test_publish_outputs_applies_cached_cleanup_when_new_cleanup_calls_disabled(self):
        old_env = dict(os.environ)
        story = {
            "story_id": "story-disabled-cache",
            "title": "Raw OpenAI cached headline",
            "summary": "Raw cached summary.",
            "canonical_url": "https://example.com/disabled-cache-story",
            "url": "https://example.com/disabled-cache-story",
            "source_name": "Example Source",
            "source_type": "rss",
            "source_category": "rss",
            "published": "2020-01-01T00:00:00Z",
            "score": 100,
            "mentions": [],
            "sources": [],
            "alternate_links": [],
            "cluster_id": "cluster-disabled-cache",
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            api_path = Path(temp_dir) / "feed.json"
            base_feed_path = Path(temp_dir) / "top"
            try:
                os.environ["GH_MODELS_TOKEN"] = "test-token"
                FakeOutputCleanupClient.reset()
                with patch("pipeline.publish.GitHubModelsClient", FakeOutputCleanupClient):
                    with patch(
                        "pipeline.publish._fetch_article_with_url",
                        return_value=("https://example.com/disabled-cache-story", ""),
                    ):
                        _first_payload, cache = publish_outputs(
                            [story],
                            str(api_path),
                            str(base_feed_path),
                            llm_cache={},
                            config={
                                "publish_top_n": 1,
                                "output_cleanup_top_n": 1,
                                "output_cleanup_model": "test-cleanup-model",
                                "importance_backfill_days": 0,
                                "llm_rate_limit_requests_per_window": 0,
                                "llm_rate_limit_min_interval_sec": 0.0,
                                "ai_keywords": ["openai"],
                            },
                        )
                os.environ.pop("GH_MODELS_TOKEN", None)
                with patch(
                    "pipeline.publish._fetch_article_with_url",
                    return_value=("https://example.com/disabled-cache-story", ""),
                ):
                    second_payload, _second_cache = publish_outputs(
                        [dict(story)],
                        str(api_path),
                        str(base_feed_path),
                        llm_cache=cache,
                        config={
                            "publish_top_n": 1,
                            "output_cleanup_enabled": False,
                            "output_cleanup_top_n": 1,
                            "output_cleanup_model": "test-cleanup-model",
                            "importance_backfill_days": 0,
                            "ai_keywords": ["openai"],
                        },
                    )
            finally:
                os.environ.clear()
                os.environ.update(old_env)

            self.assertEqual(FakeOutputCleanupClient.title_calls, 1)
            self.assertEqual(FakeOutputCleanupClient.description_calls, 1)
            self.assertEqual(second_payload["items"][0]["title"], "OpenAI Adds Enterprise Data Controls")
            self.assertEqual(
                second_payload["items"][0]["summary"],
                "OpenAI introduced enterprise data controls for governed AI deployments.",
            )

    def test_publish_outputs_sends_fetched_article_to_output_cleanup(self):
        old_env = dict(os.environ)
        story = {
            "story_id": "story-futo",
            "title": "FUTO Swipe - A new swipe typing model",
            "summary": "Comments",
            "canonical_url": "https://swipe.futo.tech/",
            "url": "https://news.ycombinator.com/item?id=123",
            "source_name": "Hacker News",
            "source_type": "social",
            "source_category": "hackernews",
            "published": "2020-01-01T00:00:00Z",
            "score": 100,
            "mentions": [],
            "sources": [],
            "alternate_links": [],
            "cluster_id": "cluster-futo",
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            api_path = Path(temp_dir) / "feed.json"
            base_feed_path = Path(temp_dir) / "top"
            article_cache_path = Path(temp_dir) / "article_cache.json"
            try:
                os.environ["GH_MODELS_TOKEN"] = "test-token"
                with patch("pipeline.publish.GitHubModelsClient", FakeOutputCleanupClient):
                    with patch(
                        "pipeline.publish._fetch_article_with_url",
                        return_value=(
                            "https://swipe.futo.tech/",
                            "FUTO built an open-source swipe typing model from a one million swipe dataset.",
                        ),
                    ):
                        payload, _cache = publish_outputs(
                            [story],
                            str(api_path),
                            str(base_feed_path),
                            llm_cache={},
                            config={
                                "publish_top_n": 1,
                                "output_cleanup_top_n": 1,
                                "output_cleanup_model": "test-cleanup-model",
                                "importance_backfill_days": 0,
                                "llm_rate_limit_requests_per_window": 0,
                                "llm_rate_limit_min_interval_sec": 0.0,
                                "article_cache_path": str(article_cache_path),
                                "ai_keywords": ["model"],
                            },
                        )
            finally:
                os.environ.clear()
                os.environ.update(old_env)

            self.assertEqual(FakeOutputCleanupClient.seen_description_summary, "Comments")
            assert FakeOutputCleanupClient.seen_description_source_context is not None
            self.assertIn(
                "one million swipe dataset",
                FakeOutputCleanupClient.seen_description_source_context,
            )
            self.assertEqual(
                payload["items"][0]["summary"],
                "OpenAI introduced enterprise data controls for governed AI deployments.",
            )

    def test_publish_outputs_writes_feed_with_rewrites_and_importance_tags(self):
        importance = {
            "business_level": 2,
            "technical_level": 3,
            "business_impact": "[ * ]",
            "technical_impact": "[ ⬢ ]",
            "risk_impact": "R2",
            "enterprise_readiness": "ER3",
            "labor_workflow_impact": "L2",
            "confidence": "C3",
            "attention_priority": "P3",
            "development_summary": "The vendor released an enterprise AI control feature.",
            "reason_codes": ["ARCH", "GOV"],
            "recommended_action": "Plan / Pilot",
            "rationale": "The development is production-ready enough to justify architecture review.",
            "watch_items": ["Reference customer adoption"],
            "business_rationale": "It may affect planning and governance investment.",
            "technical_rationale": "It changes architecture and governance patterns.",
        }
        ai_relevance = {
            "is_ai_related": True,
            "decision": "proceed",
            "confidence": "high",
            "primary_ai_topic": "enterprise AI governance",
            "rationale": "The article covers enterprise AI controls.",
            "evidence": ["enterprise AI controls"],
        }
        output_cleanup = {
            "title": "OpenAI Adds Enterprise AI Controls for Governed Deployments",
            "description": "OpenAI introduced enterprise AI controls for teams managing governed deployments.",
            "context_hash": "test-context-hash",
            "prompt_hash": "test-prompt-hash",
            "model": "test-cleanup-model",
        }
        story = {
            "story_id": "story-combined",
            "title": "Raw OpenAI data controls headline",
            "summary": "Raw summary with uneven wording.",
            "canonical_url": "https://example.com/story",
            "url": "https://example.com/story",
            "source_name": "Example Source",
            "source_type": "rss",
            "source_category": "rss",
            "published": "2026-05-11T00:00:00Z",
            "score": 100,
            "mentions": [],
            "sources": [],
            "alternate_links": [],
            "cluster_id": "cluster-combined",
            "ai_relevance": ai_relevance,
            "importance": importance,
            "output_cleanup": output_cleanup,
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            api_path = Path(temp_dir) / "feed.json"
            base_feed_path = Path(temp_dir) / "top"
            with patch.dict(os.environ, {"GH_MODELS_TOKEN": "", "GH_Models_Token": ""}):
                payload, _cache = publish_outputs(
                    [story],
                    str(api_path),
                    str(base_feed_path),
                    llm_cache={},
                    config={
                        "publish_top_n": 1,
                        "importance_backfill_days": 0,
                        "ai_keywords": ["openai"],
                    },
                )

            item = payload["items"][0]
            self.assertEqual(item["title"], f"{output_cleanup['title']} [ * ] [ ⬢ ]")
            self.assertEqual(item["summary"], output_cleanup["description"])
            self.assertEqual(item["description"], output_cleanup["description"])
            self.assertEqual(item["originalTitle"], "Raw OpenAI data controls headline")
            self.assertEqual(item["originalSummary"], "Raw summary with uneven wording.")
            self.assertEqual(item["aiRelevance"], ai_relevance)
            self.assertEqual(item["importance"], importance)

            rss_item = ET.parse(base_feed_path.with_suffix(".xml")).getroot().find("./channel/item")
            self.assertIsNotNone(rss_item)
            assert rss_item is not None
            self.assertEqual(
                rss_item.findtext("title"),
                "OpenAI Adds Enterprise AI Controls for Governed Deployments [ * ] [ ⬢ ]",
            )
            self.assertEqual(rss_item.findtext("description"), output_cleanup["description"])

            json_feed = json.loads(base_feed_path.with_suffix(".json").read_text(encoding="utf-8"))
            self.assertEqual(
                json_feed["items"][0]["title"],
                "OpenAI Adds Enterprise AI Controls for Governed Deployments [ * ] [ ⬢ ]",
            )
            self.assertEqual(json_feed["items"][0]["content_text"], output_cleanup["description"])


if __name__ == "__main__":
    unittest.main()
