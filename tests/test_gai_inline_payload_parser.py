import unittest

from bs4 import BeautifulSoup

from scripts.enhanced_scraper import GAIInsightsScraper


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


if __name__ == "__main__":
    unittest.main()
