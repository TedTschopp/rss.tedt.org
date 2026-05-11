import unittest

from pipeline.dedupe import dedupe_to_stories
from pipeline.normalize import normalize_items


class DedupeCleanupTests(unittest.TestCase):
    def test_normalize_derives_hacker_news_discussion_url(self):
        normalized = normalize_items(
            [
                {
                    "source_id": "hn_front_page",
                    "source_name": "Hacker News Front Page",
                    "source_type": "hackernews",
                    "source_category": "hn",
                    "authority_weight": 0.7,
                    "fetched_at": "2026-05-11T01:00:00Z",
                    "title": "OpenAI releases enterprise controls",
                    "url": "https://www.wired.com/story/openai-enterprise-controls/",
                    "summary": "",
                    "published": "2026-05-11T01:00:00Z",
                    "raw_fields": {"hn_item_id": "123"},
                }
            ]
        )

        self.assertEqual(normalized[0]["discussion_url"], "https://news.ycombinator.com/item?id=123")

    def test_duplicate_sources_prefer_original_publisher_and_track_links(self):
        items = [
            {
                "item_id": "hn-1",
                "source_id": "hn_front_page",
                "source_name": "Hacker News Front Page",
                "source_type": "hackernews",
                "source_category": "hn",
                "authority_weight": 0.7,
                "fetched_at": "2026-05-11T01:00:00Z",
                "title": "OpenAI releases enterprise controls",
                "url": "https://www.wired.com/story/openai-enterprise-controls/",
                "canonical_url": "https://www.wired.com/story/openai-enterprise-controls/",
                "discussion_url": "https://news.ycombinator.com/item?id=123",
                "domain": "www.wired.com",
                "summary": "HN discussion of the Wired article.",
                "published": "2026-05-11T01:00:00Z",
                "upvotes": 200,
                "comments": 40,
            },
            {
                "item_id": "wired-1",
                "source_id": "rss_wired_ai",
                "source_name": "WIRED AI",
                "source_type": "rss",
                "source_category": "rss",
                "authority_weight": 0.78,
                "fetched_at": "2026-05-11T00:30:00Z",
                "title": "OpenAI releases enterprise controls",
                "url": "https://www.wired.com/story/openai-enterprise-controls/",
                "canonical_url": "https://www.wired.com/story/openai-enterprise-controls/",
                "domain": "www.wired.com",
                "summary": "Original WIRED article summary.",
                "published": "2026-05-11T00:30:00Z",
                "upvotes": None,
                "comments": None,
            },
        ]

        stories = dedupe_to_stories(items)

        self.assertEqual(len(stories), 1)
        story = stories[0]
        self.assertEqual(story["primary_source_id"], "rss_wired_ai")
        self.assertEqual(story["source_name"], "WIRED AI")
        self.assertEqual(story["summary"], "Original WIRED article summary.")
        self.assertTrue(story["is_duplicate"])
        self.assertEqual(story["duplicate_count"], 1)
        self.assertEqual(story["duplicate_source_count"], 2)

        self.assertEqual(len(story["mentions"]), 2)
        hn_mention = next(mention for mention in story["mentions"] if mention["source_id"] == "hn_front_page")
        self.assertEqual(hn_mention["url"], "https://www.wired.com/story/openai-enterprise-controls/")
        self.assertEqual(hn_mention["discussion_url"], "https://news.ycombinator.com/item?id=123")

        sources = story["sources"]
        self.assertEqual([source["source_id"] for source in sources], ["rss_wired_ai", "hn_front_page"])
        alternate_links = story["alternate_links"]
        self.assertIn(
            {
                "url": "https://www.wired.com/story/openai-enterprise-controls/",
                "canonical_url": "https://www.wired.com/story/openai-enterprise-controls/",
                "discussion_url": "https://news.ycombinator.com/item?id=123",
                "source_id": "hn_front_page",
                "source_name": "Hacker News Front Page",
                "source_type": "hackernews",
                "source_category": "hn",
                "domain": "www.wired.com",
            },
            alternate_links,
        )

    def test_exact_title_same_day_groups_cross_source_articles(self):
        items = [
            {
                "item_id": "a",
                "source_id": "source_a",
                "source_name": "Source A",
                "source_type": "rss",
                "source_category": "rss",
                "authority_weight": 0.6,
                "fetched_at": "2026-05-11T00:00:00Z",
                "title": "OpenAI announces new data controls",
                "url": "https://example.com/openai-data-controls",
                "canonical_url": "https://example.com/openai-data-controls",
                "domain": "example.com",
                "summary": "First summary.",
                "published": "2026-05-11T00:00:00Z",
            },
            {
                "item_id": "b",
                "source_id": "source_b",
                "source_name": "Source B",
                "source_type": "rss",
                "source_category": "rss",
                "authority_weight": 0.7,
                "fetched_at": "2026-05-11T00:05:00Z",
                "title": "OpenAI announces new data controls",
                "url": "https://mirror.example.net/story/42",
                "canonical_url": "https://mirror.example.net/story/42",
                "domain": "mirror.example.net",
                "summary": "Second summary.",
                "published": "2026-05-11T00:05:00Z",
            },
        ]

        stories = dedupe_to_stories(items)

        self.assertEqual(len(stories), 1)
        self.assertEqual(stories[0]["duplicate_source_count"], 2)
        self.assertEqual(len(stories[0]["alternate_links"]), 2)


if __name__ == "__main__":
    unittest.main()