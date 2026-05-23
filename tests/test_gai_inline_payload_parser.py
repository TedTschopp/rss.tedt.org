import unittest
from datetime import datetime, timezone

from bs4 import BeautifulSoup

from scripts.enhanced_scraper import GAIInsightsScraper
from scripts.enhanced_scraper import RSSGenerator
from scripts.enhanced_scraper import RSSScraperError


INLINE_PAYLOAD_HTML = """
<html>
  <body>
    <script>
      const rows = [
        {date:"05/22/2026",rating:"Essential",title:`<a href=\"https://example.com/a\" target=\"_blank\">Fresh Item A</a>`,rationale:`A rationale with AI context.`},
        {date:"05/21/2026",rating:"Important",title:`<a href=\"https://example.com/b\" target=\"_blank\">Fresh Item B</a>`,rationale:`Another rationale.`}
      ];
    </script>
  </body>
</html>
"""


class GAIInlinePayloadParserTests(unittest.TestCase):
    def test_extract_inline_payload_rows_parses_expected_shape(self):
        rows = GAIInsightsScraper._extract_inline_payload_rows(INLINE_PAYLOAD_HTML)

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["Date"]["text"], "05/22/2026")
        self.assertEqual(rows[0]["Rating"]["text"], "Essential")
        self.assertEqual(rows[0]["Title"]["text"], "Fresh Item A")
        self.assertEqual(rows[0]["Title"]["links"], ["https://example.com/a"])
        self.assertIn("AI context", rows[0]["Rationale"]["text"])

    def test_extract_table_data_falls_back_when_table_missing(self):
        scraper = GAIInsightsScraper()
        soup = BeautifulSoup(INLINE_PAYLOAD_HTML, "html.parser")

        rows = scraper._extract_table_data(soup)

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[1]["Date"]["text"], "05/21/2026")
        self.assertEqual(rows[1]["Title"]["text"], "Fresh Item B")

    def test_validate_freshness_passes_for_recent_rows(self):
        rows = GAIInsightsScraper._extract_inline_payload_rows(INLINE_PAYLOAD_HTML)
        now = datetime(2026, 5, 23, tzinfo=timezone.utc)

        RSSGenerator._validate_freshness(rows, max_staleness_days=3, now=now)

    def test_validate_freshness_raises_for_stale_rows(self):
        stale_rows = [
            {
                "Date": {"text": "04/01/2026", "links": []},
                "Rating": {"text": "Essential", "links": []},
                "Title": {"text": "Old Item", "links": ["https://example.com/old"]},
                "Rationale": {"text": "Old rationale", "links": []},
            }
        ]
        now = datetime(2026, 5, 23, tzinfo=timezone.utc)

        with self.assertRaises(RSSScraperError):
          RSSGenerator._validate_freshness(stale_rows, max_staleness_days=7, now=now)


if __name__ == "__main__":
    unittest.main()
