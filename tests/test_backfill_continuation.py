import unittest
import tempfile
from pathlib import Path

from scripts.backfill_continuation import continuation_status, continuation_status_from_path


class BackfillContinuationTests(unittest.TestCase):
    def test_continues_when_backlog_shrinks_and_runs_remain(self):
        report = {
            "llm_status": {
                "backlog": {
                    "embeddings": {"before": 100, "remaining": 50},
                    "summaries": {"before": 80, "remaining": 30},
                },
                "backlog_remaining": 80,
            }
        }

        status = continuation_status(report, runs_remaining=4)

        self.assertTrue(status["should_continue"])
        self.assertEqual(status["next_runs_remaining"], 3)
        self.assertEqual(status["reason"], "progress")

    def test_stops_when_backlog_is_complete(self):
        report = {
            "llm_status": {
                "backlog": {"summaries": {"before": 20, "remaining": 0}},
                "backlog_remaining": 0,
            }
        }

        status = continuation_status(report, runs_remaining=4)

        self.assertFalse(status["should_continue"])
        self.assertEqual(status["reason"], "complete")

    def test_stops_when_batch_makes_no_progress(self):
        report = {
            "llm_status": {
                "backlog": {"summaries": {"before": 20, "remaining": 20}},
                "backlog_remaining": 20,
            }
        }

        status = continuation_status(report, runs_remaining=4)

        self.assertFalse(status["should_continue"])
        self.assertEqual(status["reason"], "stalled")

    def test_stops_when_run_budget_is_exhausted(self):
        report = {
            "llm_status": {
                "backlog": {"summaries": {"before": 20, "remaining": 10}},
                "backlog_remaining": 10,
            }
        }

        status = continuation_status(report, runs_remaining=1)

        self.assertFalse(status["should_continue"])
        self.assertEqual(status["reason"], "run_limit")

    def test_missing_backlog_is_not_treated_as_complete(self):
        status = continuation_status({"llm_status": {}}, runs_remaining=4)

        self.assertFalse(status["should_continue"])
        self.assertEqual(status["reason"], "invalid_report")

    def test_missing_report_file_stops_as_invalid(self):
        status = continuation_status_from_path(Path("missing-report.json"), runs_remaining=4)

        self.assertFalse(status["should_continue"])
        self.assertEqual(status["reason"], "invalid_report")

    def test_malformed_report_file_stops_as_invalid(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = Path(temp_dir) / "pipeline-report.json"
            report_path.write_text("{", encoding="utf-8")

            status = continuation_status_from_path(report_path, runs_remaining=4)

        self.assertFalse(status["should_continue"])
        self.assertEqual(status["reason"], "invalid_report")


if __name__ == "__main__":
    unittest.main()