import unittest

from pipeline.article_content import fetch_article_markdown, html_to_markdown


class FakeResponse:
    def __init__(self, text, content_type="text/html"):
        self.text = text
        self.headers = {"content-type": content_type}

    def raise_for_status(self):
        return None


class FakeSession:
    def __init__(self, html):
        self.html = html
        self.last_url = None
        self.last_timeout = None
        self.last_headers = None

    def get(self, url, timeout=None, headers=None):
        self.last_url = url
        self.last_timeout = timeout
        self.last_headers = headers or {}
        return FakeResponse(self.html)


class ArticleContentTests(unittest.TestCase):
    def test_html_to_markdown_extracts_article_content(self):
        html = """
        <html>
          <head><title>Ignored Browser Title</title><script>bad()</script></head>
          <body>
            <nav>Navigation should not appear</nav>
            <article>
              <h1>Enterprise AI Controls Launch</h1>
              <p>The vendor released governance controls for AI systems.</p>
              <ul><li>Audit logging</li><li>Policy enforcement</li></ul>
            </article>
          </body>
        </html>
        """

        markdown = html_to_markdown(html)

        self.assertIn("# Enterprise AI Controls Launch", markdown)
        self.assertIn("The vendor released governance controls for AI systems.", markdown)
        self.assertIn("- Audit logging", markdown)
        self.assertNotIn("Navigation should not appear", markdown)
        self.assertNotIn("bad()", markdown)

    def test_fetch_article_markdown_uses_url_and_limits_output(self):
        session = FakeSession("<article><h1>Title</h1><p>" + ("word " * 40) + "</p></article>")

        markdown = fetch_article_markdown(
            "https://example.com/story",
            timeout_sec=7,
            max_chars=40,
            session=session,
        )

        self.assertEqual(session.last_url, "https://example.com/story")
        self.assertEqual(session.last_timeout, 7)
        self.assertIn("rss.tedt.org", session.last_headers.get("User-Agent", ""))
        self.assertLessEqual(len(markdown), 60)
        self.assertIn("[truncated]", markdown)

    def test_fetch_article_markdown_ignores_non_http_urls(self):
        self.assertEqual(fetch_article_markdown("mailto:test@example.com"), "")
        self.assertEqual(fetch_article_markdown(""), "")


if __name__ == "__main__":
    unittest.main()