import unittest
from datetime import timezone

from pipeline.score import score_stories
from pipeline.text_utils import parse_datetime


class DateParsingTests(unittest.TestCase):
    def test_parse_datetime_accepts_rss_rfc822_dates(self):
        parsed = parse_datetime("Wed, 28 Jun 2017 07:00:00 GMT")

        self.assertIsNotNone(parsed)
        self.assertEqual(parsed.year, 2017)
        self.assertEqual(parsed.month, 6)
        self.assertEqual(parsed.day, 28)
        self.assertEqual(parsed.hour, 7)
        self.assertEqual(parsed.tzinfo, timezone.utc)

    def test_score_stories_does_not_treat_old_rss_dates_as_freshish(self):
        stories = [
            {
                "story_id": "old-openai",
                "authority_weight": 0.95,
                "published": "Wed, 28 Jun 2017 07:00:00 GMT",
                "mentions": [{"source_id": "rss_openai_blog"}],
            }
        ]

        ranked = score_stories(stories, {"old-openai": "cluster-1"})

        self.assertLess(ranked[0]["score_breakdown"]["freshness_score"], 0.01)
        self.assertLess(ranked[0]["score"], 102)


if __name__ == "__main__":
    unittest.main()
