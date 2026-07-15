import json
import tempfile
import unittest
from pathlib import Path

from pipeline.embedding_codec import decode_embedding
from pipeline.run_all import _apply_env_overrides, _combine_llm_status, _prune_llm_cache, _write_report


class RunAllConfigTests(unittest.TestCase):
    def test_prune_llm_cache_removes_stale_entries(self):
        cache = {
            "active": {"summary": "Current"},
            "stale": {"summary": "Expired"},
        }

        result = _prune_llm_cache(cache, ["active"], max_bytes=10_000)

        self.assertEqual(result, {"active": cache["active"]})

    def test_prune_llm_cache_compacts_numeric_embeddings(self):
        cache = {"active": {"embedding": [0.1, 0.2, 0.3]}}

        result = _prune_llm_cache(cache, ["active"], max_bytes=10_000)

        self.assertIsInstance(result["active"]["embedding"], str)
        self.assertEqual(len(decode_embedding(result["active"]["embedding"])), 3)

    def test_prune_llm_cache_prioritizes_active_entries_within_byte_budget(self):
        cache = {
            "lower-priority": {"embedding": ["x" * 80]},
            "highest-priority": {"embedding": ["y" * 80]},
            "stale": {"embedding": ["z"]},
        }
        highest_priority_size = len(
            json.dumps(
                {"highest-priority": cache["highest-priority"]},
                indent=2,
                ensure_ascii=False,
            ).encode("utf-8")
        )
        max_bytes = highest_priority_size + 2

        result = _prune_llm_cache(
            cache,
            ["highest-priority", "lower-priority"],
            max_bytes=max_bytes,
        )

        self.assertEqual(result, {"highest-priority": cache["highest-priority"]})
        self.assertLessEqual(
            len(json.dumps(result, indent=2, ensure_ascii=False).encode("utf-8")),
            max_bytes,
        )

    def test_apply_env_overrides_supports_runtime_cost_controls(self):
        config = {}
        env = {
            "PIPELINE_LLM_TOP_N": "20",
            "PIPELINE_LLM_EMBEDDING_BATCH_SIZE": "100",
            "PIPELINE_LLM_EMBEDDING_MAX_STORIES": "500",
            "PIPELINE_LLM_CHAT_MAX_CALLS": "10",
            "PIPELINE_PUBLISH_TOP_N": "80",
            "PIPELINE_LLM_RATE_LIMIT_REQUESTS_PER_WINDOW": "12",
            "PIPELINE_LLM_RATE_LIMIT_WINDOW_SEC": "30",
            "PIPELINE_LLM_RATE_LIMIT_MIN_INTERVAL_SEC": "0.5",
            "PIPELINE_LLM_PROVIDER": "openai",
            "PIPELINE_GITHUB_MODELS_COPILOT_PLAN": "copilot_enterprise",
            "PIPELINE_GITHUB_MODELS_DAILY_BUDGET_ENABLED": "true",
            "PIPELINE_GITHUB_MODELS_DAILY_REQUEST_CAP": "12",
            "PIPELINE_GITHUB_MODELS_GLOBAL_DAILY_REQUEST_CAP": "0",
            "PIPELINE_GITHUB_MODELS_FAIL_FAST_AUTH": "true",
            "PIPELINE_OPENAI_BASE_URL": "https://api.openai.com/v1",
            "PIPELINE_OPENAI_RATE_LIMIT_REQUESTS_PER_MINUTE": "60",
            "PIPELINE_OPENAI_DAILY_REQUEST_CAP": "0",
            "PIPELINE_OPENAI_GLOBAL_DAILY_REQUEST_CAP": "0",
            "PIPELINE_LLM_RETRY_MAX_ATTEMPTS": "2",
            "PIPELINE_LLM_RETRY_BASE_DELAY_SEC": "1.0",
            "PIPELINE_LLM_RETRY_MAX_DELAY_SEC": "8",
            "PIPELINE_LLM_RETRY_JITTER_SEC": "0.3",
            "PIPELINE_LLM_429_WINDOW_SEC": "30",
            "PIPELINE_LLM_429_THRESHOLD": "3",
            "PIPELINE_LLM_429_COOLDOWN_BASE_SEC": "10",
            "PIPELINE_LLM_429_COOLDOWN_MAX_SEC": "60",
            "PIPELINE_SUMMARY_MODEL": "openai/gpt-4.1-mini",
            "PIPELINE_AI_RELEVANCE_MODEL": "openai/gpt-4.1-mini",
            "PIPELINE_IMPORTANCE_MODEL": "openai/gpt-5",
            "PIPELINE_OUTPUT_CLEANUP_MODEL": "openai/gpt-4.1-mini",
            "PIPELINE_OUTPUT_CLEANUP_TOP_N": "0",
            "PIPELINE_AI_RELEVANCE_MAX_CALLS": "500",
            "PIPELINE_IMPORTANCE_MAX_CALLS": "500",
            "PIPELINE_OUTPUT_CLEANUP_MAX_CALLS": "500",
            "PIPELINE_IMPORTANCE_BACKFILL_DAYS": "2",
            "PIPELINE_BACKFILL_MODE": "true",
            "PIPELINE_OUTPUT_CLEANUP_ENABLED": "false",
            "PIPELINE_ARTICLE_FETCH_WORKERS": "4",
            "PIPELINE_ARTICLE_FETCH_MAX_URLS": "500",
            "PIPELINE_ARTICLE_CACHE_ENABLED": "true",
            "PIPELINE_ARTICLE_CACHE_TTL_HOURS": "24",
            "PIPELINE_ARTICLE_CACHE_PATH": "derived/article_cache.json",
        }

        result = _apply_env_overrides(config, env)

        self.assertEqual(result["llm_top_n"], 20)
        self.assertEqual(result["llm_embedding_batch_size"], 100)
        self.assertEqual(result["llm_embedding_max_stories"], 500)
        self.assertEqual(result["llm_chat_max_calls"], 10)
        self.assertEqual(result["publish_top_n"], 80)
        self.assertEqual(result["llm_rate_limit_requests_per_window"], 12)
        self.assertEqual(result["llm_rate_limit_window_sec"], 30.0)
        self.assertEqual(result["llm_rate_limit_min_interval_sec"], 0.5)
        self.assertEqual(result["llm_provider"], "openai")
        self.assertEqual(result["github_models_copilot_plan"], "copilot_enterprise")
        self.assertTrue(result["github_models_daily_budget_enabled"])
        self.assertEqual(result["github_models_daily_request_cap"], 12)
        self.assertEqual(result["github_models_global_daily_request_cap"], 0)
        self.assertTrue(result["github_models_fail_fast_auth"])
        self.assertEqual(result["openai_base_url"], "https://api.openai.com/v1")
        self.assertEqual(result["openai_rate_limit_requests_per_minute"], 60)
        self.assertEqual(result["openai_daily_request_cap"], 0)
        self.assertEqual(result["openai_global_daily_request_cap"], 0)
        self.assertEqual(result["llm_retry_max_attempts"], 2)
        self.assertEqual(result["llm_retry_base_delay_sec"], 1.0)
        self.assertEqual(result["llm_retry_max_delay_sec"], 8.0)
        self.assertEqual(result["llm_retry_jitter_sec"], 0.3)
        self.assertEqual(result["llm_429_window_sec"], 30.0)
        self.assertEqual(result["llm_429_threshold"], 3)
        self.assertEqual(result["llm_429_cooldown_base_sec"], 10.0)
        self.assertEqual(result["llm_429_cooldown_max_sec"], 60.0)
        self.assertEqual(result["summary_model"], "openai/gpt-4.1-mini")
        self.assertEqual(result["ai_relevance_model"], "openai/gpt-4.1-mini")
        self.assertEqual(result["importance_model"], "openai/gpt-5")
        self.assertEqual(result["output_cleanup_model"], "openai/gpt-4.1-mini")
        self.assertEqual(result["output_cleanup_top_n"], 0)
        self.assertEqual(result["ai_relevance_max_calls"], 500)
        self.assertEqual(result["importance_max_calls"], 500)
        self.assertEqual(result["output_cleanup_max_calls"], 500)
        self.assertEqual(result["importance_backfill_days"], 2)
        self.assertTrue(result["backfill_mode"])
        self.assertFalse(result["output_cleanup_enabled"])
        self.assertEqual(result["article_fetch_workers"], 4)
        self.assertEqual(result["article_fetch_max_urls"], 500)
        self.assertTrue(result["article_cache_enabled"])
        self.assertEqual(result["article_cache_ttl_hours"], 24)
        self.assertEqual(result["article_cache_path"], "derived/article_cache.json")

    def test_apply_env_overrides_parses_true_values_for_cleanup_flag(self):
        config = {"output_cleanup_enabled": False}

        result = _apply_env_overrides(config, {"PIPELINE_OUTPUT_CLEANUP_ENABLED": "yes"})

        self.assertTrue(result["output_cleanup_enabled"])


class RunAllReportTests(unittest.TestCase):
    def test_combine_llm_status_sums_enrichment_and_publish_calls(self):
        combined = _combine_llm_status(
            {
                "status": "ok",
                "calls": 11,
                "ok": 11,
                "errors": 0,
                "skipped": 0,
                "backlog": {
                    "embeddings": {"before": 20, "remaining": 10},
                    "summaries": {"before": 15, "remaining": 5},
                },
            },
            {
                "status": "ok",
                "calls": 229,
                "ok": 229,
                "errors": 0,
                "skipped": 0,
                "by_kind": {"output_cleanup": 80, "ai_relevance": 38, "importance": 31},
                "backlog": {
                    "ai_relevance": {"before": 12, "remaining": 4},
                    "importance": {"before": 3, "remaining": 2},
                    "output_cleanup": {"before": 8, "remaining": 1},
                },
            },
        )

        self.assertEqual(combined["calls"], 240)
        self.assertEqual(combined["ok"], 240)
        self.assertEqual(combined["stages"]["enrichment"]["calls"], 11)
        self.assertEqual(combined["stages"]["publish"]["calls"], 229)
        self.assertEqual(combined["by_kind"]["output_cleanup"], 80)
        self.assertEqual(combined["backlog_remaining"], 22)
        self.assertEqual(combined["backlog"]["summaries"]["remaining"], 5)
        self.assertEqual(combined["backlog"]["output_cleanup"]["remaining"], 1)

    def test_write_report_includes_stage_timing_section(self):
        report = {
            "timestamp": "2026-05-22T12:00:00Z",
            "sources_configured": 1,
            "raw_items": 2,
            "stories": 2,
            "clusters": 1,
            "llm_status": {"status": "ok", "calls": 0},
            "stage_timings_sec": {
                "ingestion": 1.2345,
                "publish": 2.0,
            },
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            json_path = base / "report.json"
            md_path = base / "report.md"
            _write_report(str(json_path), str(md_path), report)

            md = md_path.read_text(encoding="utf-8")
            self.assertIn("## Stage Timings (seconds)", md)
            self.assertIn("- ingestion: 1.23", md)
            self.assertIn("- publish: 2.00", md)

    def test_write_report_includes_llm_stage_breakdown_when_present(self):
        report = {
            "timestamp": "2026-05-22T12:00:00Z",
            "sources_configured": 1,
            "raw_items": 2,
            "stories": 2,
            "clusters": 1,
            "llm_status": {
                "status": "ok",
                "calls": 240,
                "stages": {
                    "enrichment": {"calls": 11},
                    "publish": {"calls": 229},
                },
                "backlog_remaining": 22,
                "backlog": {
                    "embeddings": {"before": 20, "remaining": 10},
                    "summaries": {"before": 15, "remaining": 5},
                    "ai_relevance": {"before": 12, "remaining": 4},
                    "importance": {"before": 3, "remaining": 2},
                    "output_cleanup": {"before": 8, "remaining": 1},
                },
            },
            "stage_timings_sec": {},
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            json_path = base / "report.json"
            md_path = base / "report.md"
            _write_report(str(json_path), str(md_path), report)

            md = md_path.read_text(encoding="utf-8")
            self.assertIn("## LLM Calls", md)
            self.assertIn("- Total: 240", md)
            self.assertIn("- Enrichment: 11", md)
            self.assertIn("- Publish: 229", md)
            self.assertIn("## Enrichment Backlog", md)
            self.assertIn("- Remaining: 22", md)
            self.assertIn("- summaries: 5", md)


if __name__ == "__main__":
    unittest.main()
