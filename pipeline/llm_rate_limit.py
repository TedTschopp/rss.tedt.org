from collections.abc import Callable
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import random
import time
from typing import Any


class RateLimitBudgetExceeded(RuntimeError):
    """Raised when the local daily model-call budget is exhausted."""


def _response_from_exception(exc: Exception) -> Any | None:
    response = getattr(exc, "response", None)
    if response is not None:
        return response
    cause = getattr(exc, "__cause__", None)
    if isinstance(cause, Exception):
        return _response_from_exception(cause)
    return None


def status_code_from_exception(exc: Exception) -> int | None:
    response = _response_from_exception(exc)
    if response is None:
        return None
    status = getattr(response, "status_code", None)
    if isinstance(status, int):
        return status
    return None


def _headers_from_exception(exc: Exception) -> Any | None:
    response = _response_from_exception(exc)
    if response is None:
        return None
    headers = getattr(response, "headers", None)
    if not headers:
        return None
    return headers


def retry_after_seconds(exc: Exception, clock: Callable[[], float] | None = None) -> float | None:
    headers = _headers_from_exception(exc)
    if not headers:
        return None
    retry_after = headers.get("Retry-After")
    if retry_after is None:
        return None
    try:
        return float(retry_after)
    except Exception:
        try:
            parsed = parsedate_to_datetime(str(retry_after))
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return max(0.0, parsed.timestamp() - (clock or time.time)())
        except Exception:
            return None


def rate_limit_reset_seconds(exc: Exception, clock: Callable[[], float] | None = None) -> float | None:
    headers = _headers_from_exception(exc)
    if not headers:
        return None
    reset_at = headers.get("x-ratelimit-reset") or headers.get("X-RateLimit-Reset")
    if reset_at is None:
        return None
    try:
        return max(0.0, float(reset_at) - (clock or time.time)())
    except Exception:
        return None


def rate_limit_remaining(exc: Exception) -> int | None:
    headers = _headers_from_exception(exc)
    if not headers:
        return None
    remaining = headers.get("x-ratelimit-remaining") or headers.get("X-RateLimit-Remaining")
    if remaining is None:
        return None
    try:
        return int(str(remaining))
    except Exception:
        return None


def is_rate_limit_exception(exc: Exception) -> bool:
    status_code = status_code_from_exception(exc)
    text = str(exc).lower()
    if status_code == 429:
        return True
    if status_code == 403:
        if retry_after_seconds(exc) is not None:
            return True
        remaining = rate_limit_remaining(exc)
        return remaining == 0 or "rate limit" in text or "secondary rate limit" in text
    return "too many requests" in text or "rate limit" in text


def is_auth_or_permission_exception(exc: Exception) -> bool:
    status_code = status_code_from_exception(exc)
    if status_code == 401:
        return True
    return status_code == 403 and not is_rate_limit_exception(exc)


def is_retryable_exception(exc: Exception) -> bool:
    status_code = status_code_from_exception(exc)
    if status_code in {500, 502, 503, 504}:
        return True
    if is_rate_limit_exception(exc):
        return True
    text = str(exc).lower()
    return "timed out" in text or "timeout" in text


def _numeric_list(value: Any) -> list[float]:
    if not isinstance(value, list):
        return []
    return [float(item) for item in value if isinstance(item, (int, float))]


def _wait_for_request_budget(
    state: dict[str, Any],
    *,
    request_rate_limit_window_sec: float,
    request_rate_limit_max_calls: int,
    request_rate_limit_min_interval_sec: float,
    sleep: Callable[[float], None],
    clock: Callable[[], float],
) -> float:
    total_sleep = 0.0
    max_calls = int(max(0, request_rate_limit_max_calls))
    window_sec = float(max(1.0, request_rate_limit_window_sec))
    min_interval_sec = float(max(0.0, request_rate_limit_min_interval_sec))

    while True:
        now = clock()
        cooldown_remaining = max(0.0, float(state.get("cooldown_until", 0.0) or 0.0) - now)

        min_interval_remaining = 0.0
        last_request_at = float(state.get("last_request_at", 0.0) or 0.0)
        if min_interval_sec > 0 and last_request_at > 0:
            min_interval_remaining = max(0.0, last_request_at + min_interval_sec - now)

        window_remaining = 0.0
        if max_calls > 0:
            recent = _numeric_list(state.get("request_timestamps"))
            cutoff = now - window_sec
            recent = [timestamp for timestamp in recent if timestamp > cutoff]
            state["request_timestamps"] = recent
            if len(recent) >= max_calls:
                window_remaining = max(0.0, min(recent) + window_sec - now)

        sleep_for = max(cooldown_remaining, min_interval_remaining, window_remaining)
        if sleep_for <= 0:
            return total_sleep

        sleep(sleep_for)
        total_sleep += sleep_for


def _wait_for_daily_budget(
    state: dict[str, Any],
    *,
    request_daily_max_calls: int,
    clock: Callable[[], float],
) -> None:
    daily_max_calls = int(max(0, request_daily_max_calls))
    if daily_max_calls <= 0:
        return

    now = clock()
    reset_at = float(state.get("daily_reset_at", 0.0) or 0.0)
    if reset_at <= now:
        next_reset = datetime.fromtimestamp(now, tz=timezone.utc).replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0,
        ).timestamp() + 86400.0
        state["daily_request_count"] = 0
        state["daily_reset_at"] = next_reset
    if int(state.get("daily_request_count", 0) or 0) >= daily_max_calls:
        reset_at = float(state.get("daily_reset_at", 0.0) or 0.0)
        raise RateLimitBudgetExceeded(
            f"github_models_daily_budget_exhausted limit={daily_max_calls} reset_at={int(reset_at)}"
        )


def _note_request_attempt(state: dict[str, Any], clock: Callable[[], float]) -> None:
    now = clock()
    state["last_request_at"] = now
    recent = _numeric_list(state.get("request_timestamps"))
    recent.append(now)
    state["request_timestamps"] = recent


def _note_daily_request_attempt(state: dict[str, Any], request_daily_max_calls: int) -> None:
    if int(max(0, request_daily_max_calls)) > 0:
        state["daily_request_count"] = int(state.get("daily_request_count", 0) or 0) + 1


def _note_429(
    state: dict[str, Any],
    *,
    window_sec: float,
    threshold: int,
    cooldown_base_sec: float,
    cooldown_max_sec: float,
    retry_after_sec: float | None,
    clock: Callable[[], float],
) -> None:
    now = clock()
    recent = _numeric_list(state.get("recent_429"))
    recent.append(now)
    cutoff = now - float(max(1.0, window_sec))
    recent = [timestamp for timestamp in recent if timestamp >= cutoff]
    state["recent_429"] = recent

    if len(recent) < int(max(1, threshold)):
        return

    strikes = int(state.get("cooldown_strikes", 0) or 0) + 1
    state["cooldown_strikes"] = strikes
    cooldown = min(float(cooldown_max_sec), float(cooldown_base_sec) * (2 ** (strikes - 1)))
    if retry_after_sec is not None:
        cooldown = max(cooldown, float(retry_after_sec))
    cooldown = min(float(cooldown_max_sec), cooldown + (0.1 * cooldown))
    state["cooldown_until"] = max(float(state.get("cooldown_until", 0.0) or 0.0), now + cooldown)


def call_with_retry(
    call: Callable[[], Any],
    max_attempts: int,
    base_delay_sec: float,
    max_delay_sec: float,
    jitter_sec: float = 0.0,
    rate_limit_state: dict[str, Any] | None = None,
    rate_limit_window_sec: float = 60.0,
    rate_limit_threshold: int = 5,
    rate_limit_cooldown_base_sec: float = 45.0,
    rate_limit_cooldown_max_sec: float = 300.0,
    request_rate_limit_window_sec: float = 60.0,
    request_rate_limit_max_calls: int = 0,
    request_rate_limit_min_interval_sec: float = 0.0,
    request_daily_max_calls: int = 0,
    daily_rate_limit_state: dict[str, Any] | None = None,
    global_daily_max_calls: int = 0,
    global_daily_rate_limit_state: dict[str, Any] | None = None,
    sleep: Callable[[float], None] | None = None,
    clock: Callable[[], float] | None = None,
) -> tuple[Any, dict[str, Any]]:
    retries = 0
    total_rate_limit_sleep = 0.0
    total_retry_sleep = 0.0
    state = rate_limit_state if isinstance(rate_limit_state, dict) else None
    daily_state = daily_rate_limit_state if isinstance(daily_rate_limit_state, dict) else state
    global_daily_state = (
        global_daily_rate_limit_state if isinstance(global_daily_rate_limit_state, dict) else None
    )
    sleep_fn = sleep or time.sleep
    clock_fn = clock or time.time

    for attempt in range(1, max_attempts + 1):
        try:
            if global_daily_state is not None:
                _wait_for_daily_budget(
                    global_daily_state,
                    request_daily_max_calls=global_daily_max_calls,
                    clock=clock_fn,
                )

            if daily_state is not None:
                _wait_for_daily_budget(
                    daily_state,
                    request_daily_max_calls=request_daily_max_calls,
                    clock=clock_fn,
                )

            if state is not None:
                total_rate_limit_sleep += _wait_for_request_budget(
                    state,
                    request_rate_limit_window_sec=request_rate_limit_window_sec,
                    request_rate_limit_max_calls=request_rate_limit_max_calls,
                    request_rate_limit_min_interval_sec=request_rate_limit_min_interval_sec,
                    sleep=sleep_fn,
                    clock=clock_fn,
                )
                _note_request_attempt(state, clock_fn)

            if daily_state is not None:
                _note_daily_request_attempt(daily_state, request_daily_max_calls)
            if global_daily_state is not None:
                _note_daily_request_attempt(global_daily_state, global_daily_max_calls)

            result = call()
            if state is not None:
                state["recent_429"] = []
                state["cooldown_strikes"] = 0
            return result, {
                "attempt": attempt,
                "retries": retries,
                "rate_limit_sleep_sec": total_rate_limit_sleep,
                "retry_sleep_sec": total_retry_sleep,
            }
        except RateLimitBudgetExceeded:
            raise
        except Exception as exc:
            retryable = is_retryable_exception(exc)
            if attempt >= max_attempts or not retryable:
                status_code = status_code_from_exception(exc)
                raise RuntimeError(
                    f"llm_call_failed attempt={attempt} retries={retries} status={status_code} error={exc}"
                ) from exc

            status_code = status_code_from_exception(exc)
            retry_after = retry_after_seconds(exc, clock_fn)
            if state is not None and status_code == 429:
                _note_429(
                    state,
                    window_sec=rate_limit_window_sec,
                    threshold=rate_limit_threshold,
                    cooldown_base_sec=rate_limit_cooldown_base_sec,
                    cooldown_max_sec=rate_limit_cooldown_max_sec,
                    retry_after_sec=retry_after,
                    clock=clock_fn,
                )

            if retry_after is not None:
                delay = min(rate_limit_cooldown_max_sec, max(0.0, retry_after))
            elif status_code in {403, 429} and is_rate_limit_exception(exc):
                reset_delay = rate_limit_reset_seconds(exc, clock_fn)
                if rate_limit_remaining(exc) == 0 and reset_delay is not None:
                    delay = min(rate_limit_cooldown_max_sec, reset_delay)
                else:
                    delay = min(
                        rate_limit_cooldown_max_sec,
                        max(60.0, base_delay_sec * (2 ** (attempt - 1))),
                    )
            else:
                jitter = random.uniform(0.0, max(0.0, float(jitter_sec))) if jitter_sec > 0 else 0.0
                delay = min(max_delay_sec, base_delay_sec * (2 ** (attempt - 1)) + jitter)

            if state is not None:
                cooldown_until = float(state.get("cooldown_until", 0.0) or 0.0)
                cooldown_remaining = max(0.0, cooldown_until - clock_fn())
                delay = max(float(delay), cooldown_remaining)

            sleep_fn(delay)
            total_retry_sleep += delay
            retries += 1

    raise RuntimeError("llm_call_failed exhausted retries")
