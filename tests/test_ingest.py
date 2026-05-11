import unittest
import tempfile
from unittest.mock import patch

from pipeline.ingest import run_ingestion


RSS_BODY = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Example Feed</title>
    <item>
      <title>Example Item</title>
      <link>https://example.com/item</link>
      <description>Example summary</description>
      <pubDate>Mon, 11 May 2026 00:00:00 GMT</pubDate>
    </item>
  </channel>
</rss>
"""


class FakeResponse:
    def __init__(self, status_code, text="", content_type="application/rss+xml"):
        self.status_code = status_code
        self.text = text
        self.headers = {"content-type": content_type}

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")


class CookiePreflightSession:
    def __init__(self):
        self.headers = {}
        self.get_calls = 0
        self.head_called = False

    def get(self, url, timeout=None, headers=None):
        self.get_calls += 1
        if self.get_calls == 1:
            return FakeResponse(403, "Forbidden", "text/html")
        return FakeResponse(200, RSS_BODY)

    def head(self, url, timeout=None, headers=None, allow_redirects=False):
        self.head_called = allow_redirects
        return FakeResponse(200, "", "application/rss+xml")


class IngestTests(unittest.TestCase):
    def test_ingestion_retries_after_cookie_preflight_on_403(self):
        session = CookiePreflightSession()
        source = {
            "id": "rss_cookie_feed",
            "type": "rss",
            "name": "Cookie Feed",
            "url": "https://example.com/feed",
            "category": "rss",
            "authority_weight": 0.5,
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            with patch("pipeline.ingest.requests.Session", return_value=session):
                raw_items, fetch_rows, _state = run_ingestion([source], {}, temp_dir, config={"request_timeout_sec": 5})

        self.assertTrue(session.head_called)
        self.assertEqual(session.get_calls, 2)
        self.assertEqual(fetch_rows[0]["http_status"], 200)
        self.assertEqual(fetch_rows[0]["item_count"], 1)
        self.assertEqual(raw_items[0]["title"], "Example Item")


if __name__ == "__main__":
    unittest.main()
