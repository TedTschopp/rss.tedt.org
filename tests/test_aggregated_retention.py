import unittest

from scripts.config import MIN_AGGREGATED_RETENTION_DAYS, aggregate_retention_days


class AggregatedRetentionTests(unittest.TestCase):
    def test_retention_is_at_least_60_days(self):
        self.assertEqual(aggregate_retention_days(30), MIN_AGGREGATED_RETENTION_DAYS)
        self.assertEqual(aggregate_retention_days("bad-value"), MIN_AGGREGATED_RETENTION_DAYS)

    def test_retention_keeps_longer_windows(self):
        self.assertEqual(aggregate_retention_days(365), 365)


if __name__ == "__main__":
    unittest.main()
