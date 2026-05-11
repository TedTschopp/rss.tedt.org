from datetime import timedelta
from typing import Any

RAW_DIR = "raw"
DATA_DIR = "data"
DERIVED_DIR = "derived"
API_DIR = "api"
FEEDS_DIR = "feeds"
REPORTS_DIR = "reports"

SOURCE_STATE_FILE = f"{DERIVED_DIR}/source_state.json"
FETCH_LOG_FILE = f"{DERIVED_DIR}/fetch_log.jsonl"
LLM_CACHE_FILE = f"{DERIVED_DIR}/llm_cache.json"
LLM_CALL_LOG_FILE = f"{DERIVED_DIR}/llm_call_log.jsonl"

DEFAULT_PIPELINE_CONFIG: dict[str, Any] = {
    "schema_version": "1.0.0",
    "publish_top_n": 200,
    "llm_top_n": 50,
    "score_weight_authority": 100.0,
    "score_weight_freshness": 120.0,
    "score_weight_engagement": 80.0,
    "score_weight_velocity": 40.0,
    "score_weight_coverage": 30.0,
    "score_weight_novelty_penalty": 50.0,
    "llm_chat_max_calls": 25,
    "llm_retry_max_attempts": 4,
    "llm_retry_base_delay_sec": 1.5,
    "llm_retry_max_delay_sec": 20.0,
    "llm_retry_jitter_sec": 0.8,
    # If we see a burst of HTTP 429 responses, treat it as a signal to back off harder
    # than simple per-call exponential retry.
    "llm_429_window_sec": 60,
    "llm_429_threshold": 5,
    "llm_429_cooldown_base_sec": 45.0,
    "llm_429_cooldown_max_sec": 300.0,
    "half_life_hours": 36,
    "request_timeout_sec": 25,
    "article_fetch_timeout_sec": 15,
    "article_max_chars": 12000,
    "importance_backfill_days": 7,
    "ai_relevance_model": "openai/gpt-4.1-mini",
    "importance_model": "openai/gpt-5",
    "output_cleanup_enabled": True,
    "output_cleanup_top_n": 200,
    "output_cleanup_model": "openai/gpt-4.1-mini",
    "user_agent": "rss.tedt.org-pipeline/1.0 (+https://rss.tedt.org)",
    "reddit_user_agent": "rss.tedt.org-bot/1.0 by TedTschopp",
    "etag_ttl": str(timedelta(days=3)),
    "ai_keywords": [
        "ai",
        "artificial intelligence",
        "machine learning",
        "ml",
        "llm",
        "model",
        "models",
        "agent",
        "agents",
        "openai",
        "anthropic",
        "claude",
        "chatgpt",
        "gpt",
        "gemini",
        "copilot",
        "deepmind",
        "inference",
        "neural",
        "transformer",
        "rag",
        "prompt",
        "fine-tuning",
        "embeddings",
        "multimodal",
        "arxiv",
    ],
}
