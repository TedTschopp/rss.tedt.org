import unittest

from pipeline.source_registry import load_sources


REQUIRED_TOP_SOURCE_URLS = {
    "https://natural20.com/feed.xml",
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://arstechnica.com/ai/feed/",
    "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
    "https://www.wired.com/feed/tag/ai/latest/rss",
    "https://futurism.com/categories/ai-artificial-intelligence/feed",
    "https://www.technologyreview.com/topic/artificial-intelligence/feed/",
    "https://www.technologyreview.com/feed/",
    "https://venturebeat.com/category/ai/feed/",
    "https://the-decoder.com/feed/",
    "https://www.artificialintelligence-news.com/feed/rss/",
    "https://www.sciencedaily.com/rss/computers_math/artificial_intelligence.xml",
    "https://openai.com/news/rss.xml",
    "https://deepmind.google/blog/rss.xml",
    "https://blog.google/rss/",
    "https://news.google.com/rss/search?q=site%3Aanthropic.com%20Anthropic&hl=en-US&gl=US&ceid=US%3Aen",
    "https://news.google.com/rss/search?q=%22xAI%22&hl=en-US&gl=US&ceid=US%3Aen",
    "https://blog.samaltman.com/posts.atom",
    "https://news.google.com/rss/search?q=%22Dario%20Amodei%22&hl=en-US&gl=US&ceid=US%3Aen",
    "https://news.ycombinator.com/rss",
    "https://hn.algolia.com/api/v1/search_by_date?tags=story&query=AI",
    "https://www.reddit.com/r/MachineLearning/new/.rss",
    "https://www.reddit.com/r/artificial/new/.rss",
    "https://www.reddit.com/r/LocalLLaMA/new/.rss",
    "https://www.reddit.com/r/singularity/new/.rss",
    "https://www.reddit.com/r/ChatGPT/new/.rss",
    "https://rss.arxiv.org/rss/cs.AI",
    "https://rss.arxiv.org/rss/cs.CL",
    "https://rss.arxiv.org/rss/cs.LG",
    "https://rss.arxiv.org/rss/cs.AI+cs.CL+cs.LG",
    "https://magazine.sebastianraschka.com/feed",
    "https://aisnakeoil.substack.com/feed",
    "https://www.normaltech.ai/feed",
    "https://www.oneusefulthing.org/feed",
    "https://www.theinformation.com/feed",
    "https://garymarcus.substack.com/feed",
    "https://simonwillison.net/atom/everything/",
}


class SourcesConfigTests(unittest.TestCase):
    def test_required_top_source_urls_are_configured(self):
        configured_urls = {source["url"] for source in load_sources("sources.yml")}

        self.assertEqual(set(), REQUIRED_TOP_SOURCE_URLS - configured_urls)

    def test_source_ids_and_urls_are_unique(self):
        sources = load_sources("sources.yml")
        source_ids = [source["id"] for source in sources]
        urls = [source["url"] for source in sources]

        self.assertEqual(len(source_ids), len(set(source_ids)))
        self.assertEqual(len(urls), len(set(urls)))


if __name__ == "__main__":
    unittest.main()
