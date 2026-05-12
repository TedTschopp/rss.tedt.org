import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline.constants import DEFAULT_PIPELINE_CONFIG
from pipeline.llm_client import GitHubModelsClient
from pipeline.publish import publish_outputs


REQUIRED_IMPORTANCE_FIELDS = {
    "business_level",
    "technical_level",
    "business_impact",
    "technical_impact",
    "risk_impact",
    "enterprise_readiness",
    "labor_workflow_impact",
    "confidence",
    "attention_priority",
    "development_summary",
    "reason_codes",
    "recommended_action",
    "rationale",
    "watch_items",
    "business_rationale",
    "technical_rationale",
}

REQUIRED_AI_RELEVANCE_FIELDS = {
    "is_ai_related",
    "decision",
    "confidence",
    "primary_ai_topic",
    "rationale",
    "evidence",
}


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


class FakeSession:
    def __init__(self, response_content):
        self.headers = {}
        self.response_content = response_content
        self.last_payload = None

    def post(self, url, json=None, timeout=None):
        self.last_payload = json
        return FakeResponse(
            {
                "choices": [
                    {
                        "message": {
                            "content": self.response_content,
                        }
                    }
                ],
                "usage": {"total_tokens": 123},
            }
        )


class ImportanceGradingContractTests(unittest.TestCase):
    def test_importance_schema_requires_expanded_rubric_fields(self):
        with open("prompts/importance_schema.json", encoding="utf-8") as handle:
            schema = json.load(handle)

        contract = schema["json_schema"]["schema"]
        properties = set(contract["properties"])
        required = set(contract["required"])

        self.assertTrue(REQUIRED_IMPORTANCE_FIELDS.issubset(properties))
        self.assertTrue(REQUIRED_IMPORTANCE_FIELDS.issubset(required))

    def test_ai_relevance_schema_requires_gate_fields(self):
        with open("prompts/ai_relevance_schema.json", encoding="utf-8") as handle:
            schema = json.load(handle)

        contract = schema["json_schema"]["schema"]
        properties = set(contract["properties"])
        required = set(contract["required"])

        self.assertTrue(REQUIRED_AI_RELEVANCE_FIELDS.issubset(properties))
        self.assertTrue(REQUIRED_AI_RELEVANCE_FIELDS.issubset(required))

    def test_check_ai_relevance_uses_rubric_title_summary_and_article(self):
        response_content = json.dumps(
            {
                "is_ai_related": True,
                "decision": "proceed",
                "confidence": "high",
                "primary_ai_topic": "enterprise AI governance",
                "rationale": "The article is about enterprise AI controls and model governance.",
                "evidence": ["Mentions AI governance", "Discusses model controls"],
            }
        )
        client = GitHubModelsClient(token="test-token")
        fake_session = FakeSession(response_content)
        client.session = fake_session

        result = client.check_ai_relevance(
            "Title",
            "Context",
            "AI relevance rubric text",
            model="test-model",
            article="Article body text",
        )

        self.assertTrue(result["is_ai_related"])
        self.assertEqual(result["decision"], "proceed")
        self.assertEqual(result["evidence"], ["Mentions AI governance", "Discusses model controls"])
        self.assertIn("AI relevance rubric text", fake_session.last_payload["messages"][1]["content"])
        self.assertIn("Title", fake_session.last_payload["messages"][1]["content"])
        self.assertIn("Context", fake_session.last_payload["messages"][1]["content"])
        self.assertIn("Article body text", fake_session.last_payload["messages"][1]["content"])

    def test_grade_importance_returns_expanded_rubric_payload(self):
        response_content = json.dumps(
            {
                "business_level": 2,
                "technical_level": 3,
                "business_impact": "[ * ]",
                "technical_impact": "[ ⬢ ]",
                "risk_impact": "R2",
                "enterprise_readiness": "ER3",
                "labor_workflow_impact": "L2",
                "confidence": "C3",
                "attention_priority": "P3",
                "development_summary": "The vendor released an enterprise AI control feature. It changes governance workflows. Teams should evaluate adoption.",
                "reason_codes": ["ARCH", "GOV"],
                "recommended_action": "Plan / Pilot",
                "rationale": "The development is production-ready enough to justify architecture review.",
                "watch_items": ["Reference customer adoption", "Policy integration details"],
                "business_rationale": "It may affect planning and governance investment.",
                "technical_rationale": "It changes architecture and governance patterns.",
            }
        )
        client = GitHubModelsClient(token="test-token")
        fake_session = FakeSession(response_content)
        client.session = fake_session

        result = client.grade_importance("Title", "Context", "Rubric text", model="test-model", article="Article body text")

        self.assertTrue(REQUIRED_IMPORTANCE_FIELDS.issubset(result))
        self.assertEqual(result["risk_impact"], "R2")
        self.assertEqual(result["enterprise_readiness"], "ER3")
        self.assertEqual(result["labor_workflow_impact"], "L2")
        self.assertEqual(result["confidence"], "C3")
        self.assertEqual(result["attention_priority"], "P3")
        self.assertEqual(result["reason_codes"], ["ARCH", "GOV"])
        self.assertEqual(result["watch_items"], ["Reference customer adoption", "Policy integration details"])
        self.assertIn("Rubric text", fake_session.last_payload["messages"][1]["content"])
        self.assertIn("Article body text", fake_session.last_payload["messages"][1]["content"])

    def test_publish_outputs_preserves_expanded_importance_payload(self):
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
            "development_summary": "The vendor released an enterprise AI control feature. It changes governance workflows. Teams should evaluate adoption.",
            "reason_codes": ["ARCH", "GOV"],
            "recommended_action": "Plan / Pilot",
            "rationale": "The development is production-ready enough to justify architecture review.",
            "watch_items": ["Reference customer adoption"],
            "business_rationale": "It may affect planning and governance investment.",
            "technical_rationale": "It changes architecture and governance patterns.",
            "rubric_hash": "abc123",
        }
        story = {
            "story_id": "story-1",
            "title": "Enterprise AI governance platform launches",
            "summary": "An AI platform vendor launched governance features for enterprise AI operations.",
            "canonical_url": "https://example.com/story",
            "source_name": "Example Source",
            "source_type": "rss",
            "published": "2026-05-10T00:00:00Z",
            "score": 100,
            "mentions": [],
            "cluster_id": "cluster-1",
            "importance": importance,
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            api_path = Path(temp_dir) / "feed.json"
            base_feed_path = Path(temp_dir) / "top"
            with patch.dict(os.environ, {"GH_MODELS_TOKEN": "", "GH_Models_Token": ""}):
                payload, _cache = publish_outputs(
                    [story],
                    str(api_path),
                    str(base_feed_path),
                    llm_cache={"story-1": {"importance": importance}},
                    config={"publish_top_n": 1},
                )

            self.assertEqual(payload["items"][0]["importance"], importance)
            saved_payload = json.loads(api_path.read_text(encoding="utf-8"))
            self.assertEqual(saved_payload["items"][0]["importance"]["attention_priority"], "P3")

    def test_publish_outputs_uses_default_importance_model_constant(self):
        class FakeImportanceClient:
            seen_model = None
            seen_article = None
            seen_relevance_model = None

            def __init__(self, token, timeout_sec):
                self.token = token
                self.timeout_sec = timeout_sec

            def check_ai_relevance(self, title, summary, rubric_markdown, model, article=""):
                FakeImportanceClient.seen_relevance_model = model
                return {
                    "is_ai_related": True,
                    "decision": "proceed",
                    "confidence": "high",
                    "primary_ai_topic": "enterprise AI governance",
                    "rationale": "The story is about AI governance.",
                    "evidence": ["AI governance"],
                    "model": model,
                    "input_hash": "test-relevance-input-hash",
                }

            def grade_importance(self, title, summary, rubric_markdown, model, article=""):
                FakeImportanceClient.seen_model = model
                FakeImportanceClient.seen_article = article
                return {
                    "business_level": 2,
                    "technical_level": 3,
                    "business_impact": "[ * ]",
                    "technical_impact": "[ ⬢ ]",
                    "risk_impact": "R2",
                    "enterprise_readiness": "ER3",
                    "labor_workflow_impact": "L2",
                    "confidence": "C3",
                    "attention_priority": "P3",
                    "development_summary": "The vendor released an enterprise AI control feature. It changes governance workflows. Teams should evaluate adoption.",
                    "reason_codes": ["ARCH", "GOV"],
                    "recommended_action": "Plan / Pilot",
                    "rationale": "The development is production-ready enough to justify architecture review.",
                    "watch_items": ["Reference customer adoption"],
                    "business_rationale": "It may affect planning and governance investment.",
                    "technical_rationale": "It changes architecture and governance patterns.",
                    "model": model,
                    "input_hash": "test-input-hash",
                }

        story = {
            "story_id": "story-model",
            "title": "Enterprise AI governance platform launches",
            "summary": "An AI platform vendor launched governance features for enterprise AI operations.",
            "canonical_url": "https://example.com/model-story",
            "source_name": "Example Source",
            "source_type": "rss",
            "published": "2026-05-10T00:00:00Z",
            "score": 100,
            "mentions": [],
            "cluster_id": "cluster-model",
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            api_path = Path(temp_dir) / "feed.json"
            base_feed_path = Path(temp_dir) / "top"
            with patch.dict(os.environ, {"GH_MODELS_TOKEN": "test-token"}):
                with patch("pipeline.publish.GitHubModelsClient", FakeImportanceClient):
                    with patch("pipeline.publish.fetch_article_markdown", return_value="Fetched article markdown"):
                        payload, _cache = publish_outputs(
                            [story],
                            str(api_path),
                            str(base_feed_path),
                            llm_cache={},
                            config={
                                "publish_top_n": 1,
                                "llm_rate_limit_requests_per_window": 0,
                                "llm_rate_limit_min_interval_sec": 0.0,
                            },
                        )

        expected_model = DEFAULT_PIPELINE_CONFIG["importance_model"]
        self.assertEqual(FakeImportanceClient.seen_model, expected_model)
        self.assertEqual(FakeImportanceClient.seen_relevance_model, DEFAULT_PIPELINE_CONFIG["ai_relevance_model"])
        self.assertEqual(FakeImportanceClient.seen_article, "Fetched article markdown")
        self.assertEqual(payload["items"][0]["importance"]["model"], expected_model)

    def test_publish_outputs_skips_importance_grading_when_relevance_gate_fails(self):
        class FakeImportanceClient:
            relevance_calls = 0
            importance_calls = 0

            def __init__(self, token, timeout_sec):
                self.token = token
                self.timeout_sec = timeout_sec

            def check_ai_relevance(self, title, summary, rubric_markdown, model, article=""):
                FakeImportanceClient.relevance_calls += 1
                return {
                    "is_ai_related": False,
                    "decision": "skip",
                    "confidence": "high",
                    "primary_ai_topic": "",
                    "rationale": "The article uses AI as a marketing label, but the substance is cookware logistics.",
                    "evidence": ["No AI system, model, data, or automation development is described."],
                    "model": model,
                    "input_hash": "not-ai-input-hash",
                }

            def grade_importance(self, title, summary, rubric_markdown, model, article=""):
                FakeImportanceClient.importance_calls += 1
                return {}

        story = {
            "story_id": "story-not-ai",
            "title": "AI-branded coffee mug launches",
            "summary": "A retailer launched an AI-themed mug, but no AI system or technology is involved.",
            "canonical_url": "https://example.com/not-ai",
            "source_name": "Example Source",
            "source_type": "rss",
            "published": "2026-05-10T00:00:00Z",
            "score": 100,
            "mentions": [],
            "cluster_id": "cluster-not-ai",
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            api_path = Path(temp_dir) / "feed.json"
            base_feed_path = Path(temp_dir) / "top"
            with patch.dict(os.environ, {"GH_MODELS_TOKEN": "test-token"}):
                with patch("pipeline.publish.GitHubModelsClient", FakeImportanceClient):
                    with patch("pipeline.publish.fetch_article_markdown", return_value="Coffee mug article body"):
                        payload, cache = publish_outputs(
                            [story],
                            str(api_path),
                            str(base_feed_path),
                            llm_cache={},
                            config={
                                "publish_top_n": 1,
                                "llm_rate_limit_requests_per_window": 0,
                                "llm_rate_limit_min_interval_sec": 0.0,
                            },
                        )

        self.assertEqual(FakeImportanceClient.relevance_calls, 1)
        self.assertEqual(FakeImportanceClient.importance_calls, 0)
        self.assertFalse(payload["items"][0]["aiRelevance"]["is_ai_related"])
        self.assertIsNone(payload["items"][0]["importance"])
        self.assertIn("ai_relevance", cache["story-not-ai"])


if __name__ == "__main__":
    unittest.main()