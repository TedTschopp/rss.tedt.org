from concurrent.futures import ThreadPoolExecutor
from threading import Barrier, Lock
import unittest

from pipeline.llm_rate_limit import RateLimitBudgetExceeded, call_with_retry, status_code_from_exception


class FakeResponse:
    def __init__(self, status_code: int, headers: dict[str, str] | None = None):
        self.status_code = status_code
        self.headers = headers or {}


class FakeHTTPError(Exception):
    def __init__(self, status_code: int, message: str = "http error", headers: dict[str, str] | None = None):
        super().__init__(message)
        self.response = FakeResponse(status_code, headers)


class LLMRateLimitTests(unittest.TestCase):
    def test_request_lock_protects_shared_state_without_serializing_calls(self):
        barrier = Barrier(2, timeout=1.0)
        request_lock = Lock()
        state = {}

        def invoke():
            def call():
                barrier.wait()
                return {"ok": True}

            return call_with_retry(
                call,
                max_attempts=1,
                base_delay_sec=0.0,
                max_delay_sec=0.0,
                rate_limit_state=state,
                request_rate_limit_max_calls=0,
                request_rate_limit_min_interval_sec=0.0,
                request_lock=request_lock,
            )

        with ThreadPoolExecutor(max_workers=2) as executor:
            results = list(executor.map(lambda _index: invoke(), range(2)))

        self.assertEqual([result[0] for result in results], [{"ok": True}, {"ok": True}])
        self.assertEqual(len(state["request_timestamps"]), 2)

    def test_call_with_retry_enforces_fixed_window_limit(self):
        current_time = [100.0]
        sleep_durations = []
        state = {}

        def fake_clock():
            return current_time[0]

        def fake_sleep(seconds):
            sleep_durations.append(seconds)
            current_time[0] += seconds

        for _index in range(3):
            result, meta = call_with_retry(
                lambda: {"ok": True},
                max_attempts=1,
                base_delay_sec=0.0,
                max_delay_sec=0.0,
                jitter_sec=0.0,
                rate_limit_state=state,
                request_rate_limit_max_calls=2,
                request_rate_limit_window_sec=10.0,
                request_rate_limit_min_interval_sec=0.0,
                sleep=fake_sleep,
                clock=fake_clock,
            )
            self.assertEqual(result, {"ok": True})
            self.assertEqual(meta["retries"], 0)

        self.assertEqual(sleep_durations, [10.0])

    def test_call_with_retry_enforces_minimum_request_interval(self):
        current_time = [50.0]
        sleep_durations = []
        state = {}

        def fake_clock():
            return current_time[0]

        def fake_sleep(seconds):
            sleep_durations.append(seconds)
            current_time[0] += seconds

        call_with_retry(
            lambda: {"ok": True},
            max_attempts=1,
            base_delay_sec=0.0,
            max_delay_sec=0.0,
            jitter_sec=0.0,
            rate_limit_state=state,
            request_rate_limit_max_calls=0,
            request_rate_limit_window_sec=60.0,
            request_rate_limit_min_interval_sec=2.5,
            sleep=fake_sleep,
            clock=fake_clock,
        )
        call_with_retry(
            lambda: {"ok": True},
            max_attempts=1,
            base_delay_sec=0.0,
            max_delay_sec=0.0,
            jitter_sec=0.0,
            rate_limit_state=state,
            request_rate_limit_max_calls=0,
            request_rate_limit_window_sec=60.0,
            request_rate_limit_min_interval_sec=2.5,
            sleep=fake_sleep,
            clock=fake_clock,
        )

        self.assertEqual(sleep_durations, [2.5])

    def test_call_with_retry_honors_retry_after_header(self):
        current_time = [100.0]
        sleep_durations = []
        attempts = [0]

        def fake_clock():
            return current_time[0]

        def fake_sleep(seconds):
            sleep_durations.append(seconds)
            current_time[0] += seconds

        def flaky_call():
            attempts[0] += 1
            if attempts[0] == 1:
                raise FakeHTTPError(429, headers={"Retry-After": "7"})
            return {"ok": True}

        result, meta = call_with_retry(
            flaky_call,
            max_attempts=2,
            base_delay_sec=1.0,
            max_delay_sec=20.0,
            jitter_sec=0.0,
            sleep=fake_sleep,
            clock=fake_clock,
        )

        self.assertEqual(result, {"ok": True})
        self.assertEqual(meta["retries"], 1)
        self.assertEqual(sleep_durations, [7.0])

    def test_call_with_retry_waits_at_least_one_minute_for_secondary_rate_limit(self):
        current_time = [100.0]
        sleep_durations = []
        attempts = [0]

        def fake_clock():
            return current_time[0]

        def fake_sleep(seconds):
            sleep_durations.append(seconds)
            current_time[0] += seconds

        def flaky_call():
            attempts[0] += 1
            if attempts[0] == 1:
                raise FakeHTTPError(403, "secondary rate limit")
            return {"ok": True}

        result, meta = call_with_retry(
            flaky_call,
            max_attempts=2,
            base_delay_sec=1.0,
            max_delay_sec=20.0,
            jitter_sec=0.0,
            sleep=fake_sleep,
            clock=fake_clock,
        )

        self.assertEqual(result, {"ok": True})
        self.assertEqual(meta["retries"], 1)
        self.assertEqual(sleep_durations, [60.0])

    def test_call_with_retry_raises_cleanly_when_daily_budget_is_exhausted(self):
        current_time = [100.0]
        daily_state = {"daily_request_count": 2, "daily_reset_at": 1000.0}
        attempts = [0]

        def fake_clock():
            return current_time[0]

        def call():
            attempts[0] += 1
            return {"ok": True}

        with self.assertRaises(RateLimitBudgetExceeded):
            call_with_retry(
                call,
                max_attempts=1,
                base_delay_sec=0.0,
                max_delay_sec=0.0,
                request_daily_max_calls=2,
                daily_rate_limit_state=daily_state,
                clock=fake_clock,
            )

        self.assertEqual(attempts[0], 0)

    def test_status_code_from_exception_checks_wrapped_cause(self):
        try:
            try:
                raise FakeHTTPError(401)
            except FakeHTTPError as exc:
                raise RuntimeError("wrapped") from exc
        except RuntimeError as wrapped:
            self.assertEqual(status_code_from_exception(wrapped), 401)


if __name__ == "__main__":
    unittest.main()
