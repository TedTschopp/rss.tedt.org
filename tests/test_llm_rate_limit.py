import unittest

from pipeline.llm_rate_limit import call_with_retry


class LLMRateLimitTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()