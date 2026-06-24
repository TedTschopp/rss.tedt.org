from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class GitHubModelsCallLimits:
    model: str
    category: str
    plan: str
    requests_per_minute: int
    requests_per_day: int
    concurrent_requests: int
    min_interval_sec: float


_PLAN_ALIASES = {
    "free": "free",
    "copilot_free": "free",
    "pro": "pro",
    "copilot_pro": "pro",
    "business": "business",
    "copilot_business": "business",
    "enterprise": "enterprise",
    "copilot_enterprise": "enterprise",
}

_LIMITS_BY_CATEGORY: dict[str, dict[str, tuple[int, int, int]]] = {
    "low": {
        "free": (15, 150, 5),
        "pro": (15, 150, 5),
        "business": (15, 300, 5),
        "enterprise": (20, 450, 8),
    },
    "high": {
        "free": (10, 50, 2),
        "pro": (10, 50, 2),
        "business": (10, 100, 2),
        "enterprise": (15, 150, 4),
    },
    "embedding": {
        "free": (15, 150, 5),
        "pro": (15, 150, 5),
        "business": (15, 300, 5),
        "enterprise": (20, 450, 8),
    },
    "gpt5_reasoning": {
        "pro": (1, 8, 1),
        "business": (2, 10, 1),
        "enterprise": (2, 12, 1),
    },
    "mini_reasoning": {
        "pro": (2, 12, 1),
        "business": (3, 15, 1),
        "enterprise": (3, 20, 1),
    },
    "deepseek": {
        "free": (1, 8, 1),
        "pro": (1, 8, 1),
        "business": (2, 10, 1),
        "enterprise": (2, 12, 1),
    },
    "grok3": {
        "pro": (1, 8, 1),
        "business": (2, 10, 1),
        "enterprise": (2, 12, 1),
    },
    "grok3_mini": {
        "pro": (2, 12, 1),
        "business": (3, 15, 1),
        "enterprise": (3, 20, 1),
    },
}


def normalize_copilot_plan(plan: Any) -> str:
    value = str(plan or "copilot_enterprise").strip().lower().replace("-", "_")
    return _PLAN_ALIASES.get(value, "enterprise")


def normalize_llm_provider(provider: Any) -> str:
    value = str(provider or "github_models").strip().lower().replace("-", "_")
    if value in {"openai", "openai_api", "openai_wif"}:
        return "openai"
    if value in {"github", "github_models", "gh_models", "models"}:
        return "github_models"
    return value or "github_models"


def model_limit_category(model: str) -> str:
    normalized = str(model or "").strip().lower()
    compact = normalized.replace("_", "-")

    if "embedding" in compact or "embed" in compact:
        return "embedding"
    if "deepseek" in compact or "mai-ds-r1" in compact:
        return "deepseek"
    if "grok-3-mini" in compact:
        return "grok3_mini"
    if "grok-3" in compact:
        return "grok3"
    if any(name in compact for name in ("gpt-5-mini", "gpt-5-nano", "gpt-5-chat", "o1-mini", "o3-mini", "o4-mini")):
        return "mini_reasoning"
    if "/o1" in compact or "/o3" in compact or compact.endswith("o1") or compact.endswith("o3") or "gpt-5" in compact:
        return "gpt5_reasoning"
    if any(name in compact for name in ("mini", "nano")):
        return "low"
    return "high"


def _positive_int(value: Any, default: int = 0) -> int:
    try:
        return max(0, int(value))
    except Exception:
        return default


def _positive_float(value: Any, default: float = 0.0) -> float:
    try:
        return max(0.0, float(value))
    except Exception:
        return default


def _daily_budget_enabled(config: dict[str, Any]) -> bool:
    value = config.get("github_models_daily_budget_enabled", True)
    return str(value).strip().lower() not in {"0", "false", "no", "off"}


def github_models_call_limits(config: dict[str, Any], model: str) -> GitHubModelsCallLimits:
    plan = normalize_copilot_plan(config.get("github_models_copilot_plan", "copilot_enterprise"))
    category = model_limit_category(model)
    plan_limits = _LIMITS_BY_CATEGORY.get(category, _LIMITS_BY_CATEGORY["high"])
    rpm, rpd, concurrency = plan_limits.get(plan) or plan_limits.get("enterprise") or (1, 1, 1)

    configured_rpm = _positive_int(config.get("llm_rate_limit_requests_per_window"), 0)
    if configured_rpm > 0:
        rpm = min(rpm, configured_rpm)

    configured_daily_cap = _positive_int(config.get("github_models_daily_request_cap"), 0)
    if configured_daily_cap > 0:
        rpd = min(rpd, configured_daily_cap)

    if not _daily_budget_enabled(config):
        rpd = 0

    configured_min_interval = _positive_float(config.get("llm_rate_limit_min_interval_sec"), 0.0)
    doc_min_interval = 60.0 / max(1, rpm)
    min_interval_sec = max(configured_min_interval, doc_min_interval)

    return GitHubModelsCallLimits(
        model=model,
        category=category,
        plan=plan,
        requests_per_minute=rpm,
        requests_per_day=rpd,
        concurrent_requests=concurrency,
        min_interval_sec=min_interval_sec,
    )


def openai_call_limits(config: dict[str, Any], model: str) -> GitHubModelsCallLimits:
    rpm = _positive_int(config.get("openai_rate_limit_requests_per_minute"), 0)
    if rpm <= 0:
        rpm = _positive_int(config.get("llm_rate_limit_requests_per_window"), 60) or 60

    rpd = _positive_int(config.get("openai_daily_request_cap"), 0)
    configured_min_interval = _positive_float(config.get("llm_rate_limit_min_interval_sec"), 0.0)
    doc_min_interval = 60.0 / max(1, rpm)
    min_interval_sec = max(configured_min_interval, doc_min_interval)

    return GitHubModelsCallLimits(
        model=model,
        category="openai",
        plan="openai_api",
        requests_per_minute=rpm,
        requests_per_day=rpd,
        concurrent_requests=1,
        min_interval_sec=min_interval_sec,
    )


def llm_call_limits(config: dict[str, Any], model: str) -> GitHubModelsCallLimits:
    if normalize_llm_provider(config.get("llm_provider", "github_models")) == "openai":
        return openai_call_limits(config, model)
    return github_models_call_limits(config, model)


def llm_global_daily_request_cap(config: dict[str, Any]) -> int:
    if normalize_llm_provider(config.get("llm_provider", "github_models")) == "openai":
        return _positive_int(config.get("openai_global_daily_request_cap"), 0)
    return _positive_int(config.get("github_models_global_daily_request_cap"), 0)


def _next_utc_midnight(now: datetime) -> float:
    tomorrow = now.astimezone(timezone.utc).date() + timedelta(days=1)
    return datetime.combine(tomorrow, datetime.min.time(), tzinfo=timezone.utc).timestamp()


def seed_global_daily_state_from_call_log(path: str | None, now: datetime | None = None) -> dict[str, Any]:
    now_dt = now or datetime.now(timezone.utc)
    state = {"daily_request_count": 0, "daily_reset_at": _next_utc_midnight(now_dt)}
    if not path:
        return state

    state["daily_request_count"] = sum(_current_day_model_counts(path, now_dt).values())
    return state


def seed_model_daily_states_from_call_log(path: str | None, now: datetime | None = None) -> dict[str, dict[str, Any]]:
    now_dt = now or datetime.now(timezone.utc)
    reset_at = _next_utc_midnight(now_dt)
    counts = _current_day_model_counts(path, now_dt)
    return {
        model: {
            "daily_request_count": count,
            "daily_reset_at": reset_at,
        }
        for model, count in counts.items()
    }


def _current_day_model_counts(path: str | None, now: datetime) -> dict[str, int]:
    if not path:
        return {}

    log_path = Path(path)
    if not log_path.exists():
        return {}

    current_day = now.astimezone(timezone.utc).date()
    counts: dict[str, int] = {}
    try:
        with log_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                try:
                    row = json.loads(line)
                except Exception:
                    continue
                if not isinstance(row, dict) or not row.get("model") or row.get("status") == "skipped":
                    continue
                model = str(row.get("model") or "")
                ts_raw = str(row.get("ts") or "")
                try:
                    ts = datetime.fromisoformat(ts_raw.replace("Z", "+00:00")).astimezone(timezone.utc)
                except Exception:
                    continue
                if ts.date() == current_day:
                    counts[model] = counts.get(model, 0) + 1
    except Exception:
        return {}

    return counts


def rate_limit_state_for_model(states: dict[str, dict[str, Any]], model: str) -> dict[str, Any]:
    return states.setdefault(str(model or "unknown"), {})
