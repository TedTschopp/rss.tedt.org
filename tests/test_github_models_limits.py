import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from pipeline.github_models_limits import (
    github_models_call_limits,
    llm_call_limits,
    model_limit_category,
    seed_global_daily_state_from_call_log,
    seed_model_daily_states_from_call_log,
)


class GitHubModelsLimitsTests(unittest.TestCase):
    def test_enterprise_gpt5_uses_twelve_request_daily_limit(self):
        limits = github_models_call_limits(
            {
                "github_models_copilot_plan": "copilot_enterprise",
                "github_models_daily_request_cap": 12,
                "llm_rate_limit_requests_per_window": 20,
                "llm_rate_limit_min_interval_sec": 1.0,
            },
            "openai/gpt-5",
        )

        self.assertEqual(limits.category, "gpt5_reasoning")
        self.assertEqual(limits.plan, "enterprise")
        self.assertEqual(limits.requests_per_minute, 2)
        self.assertEqual(limits.requests_per_day, 12)
        self.assertEqual(limits.concurrent_requests, 1)
        self.assertEqual(limits.min_interval_sec, 30.0)

    def test_daily_request_cap_clamps_cheaper_model_classes(self):
        limits = github_models_call_limits(
            {
                "github_models_copilot_plan": "copilot_enterprise",
                "github_models_daily_request_cap": 12,
                "llm_rate_limit_requests_per_window": 20,
                "llm_rate_limit_min_interval_sec": 1.0,
            },
            "openai/gpt-4.1-mini",
        )

        self.assertEqual(limits.category, "low")
        self.assertEqual(limits.requests_per_minute, 20)
        self.assertEqual(limits.requests_per_day, 12)
        self.assertEqual(limits.min_interval_sec, 3.0)

    def test_model_classification_handles_embeddings(self):
        self.assertEqual(model_limit_category("openai/text-embedding-3-small"), "embedding")

    def test_openai_provider_uses_configurable_minute_limit_without_daily_cap_by_default(self):
        limits = llm_call_limits(
            {
                "llm_provider": "openai",
                "openai_rate_limit_requests_per_minute": 120,
                "openai_daily_request_cap": 0,
                "llm_rate_limit_min_interval_sec": 0.0,
            },
            "openai/gpt-5",
        )

        self.assertEqual(limits.category, "openai")
        self.assertEqual(limits.plan, "openai_api")
        self.assertEqual(limits.requests_per_minute, 120)
        self.assertEqual(limits.requests_per_day, 0)
        self.assertEqual(limits.min_interval_sec, 0.5)

    def test_seed_global_daily_state_counts_only_real_attempts_for_current_day(self):
        now = datetime(2026, 6, 24, 12, 0, tzinfo=timezone.utc)
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "llm_call_log.jsonl"
            rows = [
                {"ts": "2026-06-24T01:00:00Z", "model": "openai/gpt-5", "status": "ok"},
                {"ts": "2026-06-24T02:00:00Z", "model": "openai/gpt-5", "status": "error"},
                {"ts": "2026-06-24T03:00:00Z", "model": "openai/gpt-5", "status": "skipped"},
                {"ts": "2026-06-23T23:00:00Z", "model": "openai/gpt-5", "status": "ok"},
            ]
            path.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")

            state = seed_global_daily_state_from_call_log(str(path), now=now)
            model_states = seed_model_daily_states_from_call_log(str(path), now=now)

        self.assertEqual(state["daily_request_count"], 2)
        self.assertEqual(model_states["openai/gpt-5"]["daily_request_count"], 2)


if __name__ == "__main__":
    unittest.main()
