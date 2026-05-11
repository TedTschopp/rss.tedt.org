import json
import unittest
from datetime import datetime, timezone
from xml.etree import ElementTree as ET

from scripts.feed_generator import FeedEntry, MultiFeedGenerator


class FeedGeneratorDescriptionTests(unittest.TestCase):
    def test_feed_entry_strips_html_and_xml_from_description(self):
        entry = FeedEntry(
            title="Test",
            link="https://example.com/article",
            description=(
                "<p>First <strong>sentence</strong> &amp; second.</p>"
                "<script>alert('no')</script>"
                "<?xml version='1.0'?><note><body>XML text</body></note>"
                "<!-- hidden -->"
            ),
            pub_date=datetime(2026, 5, 11, tzinfo=timezone.utc),
            guid="test-guid",
        )

        self.assertEqual(entry.description, "First sentence & second. XML text")

    def test_generated_formats_use_plain_text_descriptions(self):
        generator = MultiFeedGenerator(
            title="Test Feed",
            link="https://example.com/feed.xml",
            description="A test feed",
        )
        generator.add_item(
            title="Test Item",
            link="https://example.com/item",
            description="&lt;p&gt;Encoded <em>and raw</em> markup&lt;/p&gt;",
            pub_date=datetime(2026, 5, 11, tzinfo=timezone.utc),
            guid="item-guid",
        )

        rss = ET.fromstring(generator.generate_rss2(include_stylesheet=False))
        rss_description = rss.find("./channel/item/description")
        self.assertIsNotNone(rss_description)
        self.assertEqual(rss_description.text, "Encoded and raw markup")

        atom = ET.fromstring(generator.generate_atom(include_stylesheet=False))
        atom_summary = atom.find("{http://www.w3.org/2005/Atom}entry/{http://www.w3.org/2005/Atom}summary")
        self.assertIsNotNone(atom_summary)
        self.assertEqual(atom_summary.text, "Encoded and raw markup")

        json_feed = json.loads(generator.generate_json_feed())
        self.assertEqual(json_feed["items"][0]["content_text"], "Encoded and raw markup")

    def test_atom_generation_does_not_namespace_later_rss2_output(self):
        generator = MultiFeedGenerator(
            title="Test Feed",
            link="https://example.com/feed.xml",
            description="A test feed",
        )
        generator.add_item(
            title="Test Item",
            link="https://example.com/item",
            description="Test description",
            pub_date=datetime(2026, 5, 11, tzinfo=timezone.utc),
            guid="item-guid",
        )

        generator.generate_atom(include_stylesheet=False)
        rss_text = generator.generate_rss2(include_stylesheet=False)
        rss = ET.fromstring(rss_text)

        self.assertEqual(rss.tag, "rss")
        self.assertIsNotNone(rss.find("./channel/item"))
        self.assertNotIn('xmlns="http://www.w3.org/2005/Atom"', rss_text)


if __name__ == "__main__":
    unittest.main()