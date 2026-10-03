import hashlib
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import Mock, patch
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

import requests

from scripts.enhanced_scraper import RSSGenerator, RSSScraperError
from scripts.gai_briefings import (
    HistoricalRatingEstimator, add_briefing, briefing_rows, canonical_url,
    merge_rows, parse_briefing, save_briefings, supplement_rows,
    published_rating,
)


def rated_row(day='09/25/2026', title='Enterprise agent safety', url='https://example.com/safety'):
    return {'Date': {'text': day, 'links': []},
            'Rating': {'text': 'Essential', 'links': []},
            'Title': {'text': title, 'links': [url]},
            'Rationale': {'text': 'Practical agent oversight for enterprise deployments.', 'links': []}}


def page(heading='In Today’s News Briefing — September 29, 2026', links=None):
    links = links or [('https://example.com/new?utm_source=email', 'Enterprise agent safety upgrade')]
    anchors = ''.join(f'<tr><td><a href="{url}">{title}</a></td></tr>' for url, title in links)
    return (f'<a href="https://example.com/promo">Promotion</a><div class="hhs-rich-text">'
            f'<h1>{heading}</h1><table>{anchors}</table></div>')


class BriefingRecoveryTests(unittest.TestCase):
    def test_dated_section_excludes_promotions_and_fragment_links(self):
        briefing = parse_briefing(page(links=[('https://example.com/a', 'Story'), ('#', 'Placeholder')]))
        self.assertEqual(briefing['date'], '2026-09-29')
        self.assertEqual(briefing['items'], [{'title': 'Story', 'url': 'https://example.com/a'}])

    def test_undated_capture_never_uses_archive_timestamp_as_publication_date(self):
        with self.assertRaisesRegex(ValueError, 'capture date is not a publication date'):
            parse_briefing(page(heading="In Today's News Briefing"), capture_timestamp='20260929120000')

    def test_undated_capture_can_use_agreeing_published_dates(self):
        rows = [rated_row(url='https://example.com/a'), rated_row(url='https://example.com/b')]
        briefing = parse_briefing(page(heading="In Today's News Briefing", links=[
            ('https://example.com/a', 'A'), ('https://example.com/b', 'B')]), rated_rows=rows)
        self.assertEqual(briefing['date'], '2026-09-25')
        self.assertEqual(briefing['date_basis'], 'matching published GAI rating dates')

    def test_future_heading_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'future'):
            parse_briefing(page(), now=datetime(2026, 9, 28, tzinfo=timezone.utc))

    def test_dedup_preserves_distinct_headlines_with_reused_publisher_link(self):
        first = rated_row()
        second = rated_row(title='A different story with a mistaken shared link')
        self.assertEqual(len(merge_rows([first, first, second])), 2)

    def test_tracking_cleanup_retains_article_identifier(self):
        self.assertEqual(canonical_url('http://www.example.com/story/?id=2&utm_source=mail&mod=alert#x'),
                         'https://example.com/story?id=2')

    def test_conflicting_original_ratings_are_preserved_as_publisher_versions(self):
        first = rated_row()
        second = json.loads(json.dumps(first))
        second['Rating']['text'] = 'Important'
        self.assertEqual(len(merge_rows([first, second, first])), 2)

    def test_publisher_specialty_qualification_is_preserved(self):
        row = rated_row()
        row['Rating']['text'] = 'Optional, Essential for Bioscience'
        self.assertTrue(published_rating(row))
        estimate = HistoricalRatingEstimator([row]).estimate(row['Title']['text'])
        self.assertEqual(estimate['rating'], 'Optional')
        self.assertEqual(merge_rows([row])[0]['Rating']['text'], 'Optional, Essential for Bioscience')

    def test_original_rating_wins_over_estimate_and_archive_url_alias(self):
        original = rated_row(day='09/29/2026', title='Enterprise agent safety upgrade')
        data = {'briefings': [parse_briefing(page())], 'rating_overrides': {}}
        estimate = briefing_rows(data, [rated_row()])[0]
        estimate['Title']['links'] = original['Title']['links']
        self.assertEqual(merge_rows([estimate], [original]), [original])
        original['Title']['links'] = ['https://archive.is/abc']
        self.assertEqual(briefing_rows(data, [original]), [])

    def test_estimator_uses_published_examples_only(self):
        estimated = rated_row(title='Something else')
        estimated['Rating']['estimated'] = True
        model = HistoricalRatingEstimator([rated_row(), estimated])
        result = model.estimate('Enterprise agent safety upgrade')
        self.assertEqual(result['rating'], 'Essential')
        self.assertEqual(len(result['examples']), 1)
        self.assertEqual(result['examples'][0]['url'], 'https://example.com/safety')

    def test_refresh_retains_prior_versions_and_freshness_guard(self):
        with TemporaryDirectory() as tmp:
            history = Path(tmp)/'briefings.json'
            report = Path(tmp)/'report.json'
            data = {'schema_version': 1, 'briefings': [], 'rating_overrides': {}}
            self.assertTrue(add_briefing(data, parse_briefing(page())))
            self.assertFalse(add_briefing(data, parse_briefing(page())))
            save_briefings(data, history)
            now = datetime(2026, 10, 3, tzinfo=timezone.utc)
            with patch('scripts.gai_briefings.requests.get', side_effect=requests.ConnectionError('offline')):
                rows = supplement_rows([rated_row()], path=history, report_path=report, now=now)
            RSSGenerator._validate_freshness(rows, 7, now=now)
            with self.assertRaises(RSSScraperError):
                RSSGenerator._validate_freshness(rows, 7, now=datetime(2026, 10, 7, tzinfo=timezone.utc))
            payload = json.loads(report.read_text())
            self.assertEqual(payload['status'], 'supplemented')
            self.assertEqual(payload['estimated_ratings'], 1)
            self.assertIn('offline', payload['briefing_lookup_error'])

    def test_fresh_publisher_rating_replaces_prior_estimate(self):
        with TemporaryDirectory() as tmp:
            history = Path(tmp)/'briefings.json'
            report = Path(tmp)/'report.json'
            data = {'schema_version': 1, 'briefings': [parse_briefing(page())], 'rating_overrides': {}}
            save_briefings(data, history)
            estimated = briefing_rows(data, [rated_row()])
            original = rated_row(day='09/29/2026', title='Enterprise agent safety upgrade', url='https://archive.is/new')
            response = Mock(content=page().encode())
            with patch('scripts.gai_briefings.requests.get', return_value=response):
                rows = supplement_rows([original], estimated, path=history, report_path=report)
            self.assertEqual(rows, [original])
            self.assertEqual(json.loads(report.read_text())['estimated_ratings'], 0)

    def test_estimate_label_all_formats_archive_and_publisher_guid(self):
        with TemporaryDirectory() as tmp:
            previous = Path.cwd()
            os.chdir(tmp)
            try:
                now = datetime.now(timezone.utc)
                original = rated_row(day=now.strftime('%m/%d/%Y'))
                data = {'briefings': [parse_briefing(page(heading=f"In Today's News Briefing — {now:%B %d, %Y}"))],
                        'rating_overrides': {}}
                estimated = briefing_rows(data, [original])[0]
                old = json.loads(json.dumps(estimated))
                old['Date']['text'] = '01/01/2024'
                old['Title']['text'] = 'An older estimated story'
                RSSGenerator.generate_gai_feed([estimated, original, old])
                main = ET.parse('ai_rss_feed.xml').findall('.//item')
                self.assertIn('(Estimated)', main[0].findtext('title'))
                content = '|'.join([original['Date']['text'], original['Rating']['text'],
                                    original['Title']['text'], original['Rationale']['text']])
                self.assertEqual(main[1].findtext('guid'), hashlib.md5(content.encode()).hexdigest())
                for filename in ('ai_rss_feed.atom', 'ai_rss_feed_rss1.xml', 'ai_rss_feed.json'):
                    self.assertIn('(Estimated)', Path(filename).read_text())
                archive = ET.parse('ai_rss_feed_archive.xml').findall('.//item')
                self.assertEqual(len(archive), 1)
                self.assertIn('(Estimated)', archive[0].findtext('title'))
                RSSGenerator.generate_gai_feed([estimated, original, old])
                self.assertEqual(len(ET.parse('ai_rss_feed_archive.xml').findall('.//item')), 1)
            finally:
                os.chdir(previous)


if __name__ == '__main__':
    unittest.main()
