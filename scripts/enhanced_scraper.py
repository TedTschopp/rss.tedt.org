#!/usr/bin/env python3
"""
Enhanced RSS scraper with better error handling and configuration management.
"""

import json
import hashlib
import logging
import os
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
import xml.etree.ElementTree as ET
import urllib.request
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
import requests
import random
import time
import re
from typing import Callable
from dateutil import parser as date_parser
try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
except Exception:
    sync_playwright = None

    class PlaywrightTimeoutError(Exception):
        pass

try:
    from scripts.config import *
    from scripts.feed_generator import MultiFeedGenerator
except ModuleNotFoundError:
    from config import *
    from feed_generator import MultiFeedGenerator

try:
    from pipeline.article_content import fetch_article_markdown as _fetch_article_markdown
except ModuleNotFoundError:
    def _fetch_article_markdown(*_args: object, **_kwargs: object) -> str:
        return ''

fetch_article_markdown: Callable[..., str] = _fetch_article_markdown

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def normalize_text(text):
    """
    Normalize text to fix encoding issues and convert special characters.
    
    Handles:
    - Curly quotes → straight quotes
    - Em/en dashes → regular dashes
    - Other Unicode punctuation → ASCII equivalents
    - Mojibake patterns (double-encoded UTF-8)
    """
    if not text:
        return text
    
    # Fix common mojibake patterns (UTF-8 interpreted as Windows-1252)
    mojibake_fixes = {
        'â€™': "'",      # Right single quote
        'â€˜': "'",      # Left single quote
        'â€œ': '"',      # Left double quote
        'â€': '"',       # Right double quote (partial)
        'â€"': '—',      # Em dash
        'â€"': '–',      # En dash
        'â€¦': '...',    # Ellipsis
        'Ã©': 'é',       # e-acute
        'Ã¨': 'è',       # e-grave
        'Ã¢': 'â',       # a-circumflex
        'Ã ': 'à',       # a-grave
        'Ã§': 'ç',       # c-cedilla
    }
    
    for bad, good in mojibake_fixes.items():
        text = text.replace(bad, good)
    
    # Unicode character replacements (normalize fancy punctuation to ASCII)
    unicode_replacements = {
        '\u2018': "'",   # Left single quote
        '\u2019': "'",   # Right single quote  
        '\u201c': '"',   # Left double quote
        '\u201d': '"',   # Right double quote
        '\u2013': '-',   # En dash
        '\u2014': '-',   # Em dash
        '\u2026': '...', # Ellipsis
        '\u00a0': ' ',   # Non-breaking space
        '\u2011': '-',   # Non-breaking hyphen
        '\u2010': '-',   # Hyphen
        '\u2212': '-',   # Minus sign
    }
    
    for unicode_char, ascii_char in unicode_replacements.items():
        text = text.replace(unicode_char, ascii_char)
    
    # Normalize Unicode to NFC form for consistency
    text = unicodedata.normalize('NFC', text)
    
    return text


class RSSScraperError(Exception):
    """Custom exception for RSS scraper errors."""
    pass

class BrowserManager:
    """Context manager for a Playwright browser page (replaces Selenium WebDriver)."""

    def __init__(self, config=BROWSER_CONFIG):
        self.config = config
        self._play = None
        self._browser = None
        self._context = None
        self._page = None

    def __enter__(self):
        if sync_playwright is None:
            raise RSSScraperError(
                "Playwright is unavailable. Install browser dependencies or disable browser scraping for this run."
            )
        self._play = sync_playwright().start()
        # Use chromium; Playwright bundles compatible browsers (install via 'playwright install --with-deps chromium')
        self._browser = self._play.chromium.launch(headless=self.config.get("headless", True))
        width, height = (int(x) for x in self.config.get("window_size", "1920,1080").split(','))
        self._context = self._browser.new_context(
            user_agent=self.config.get("user_agent"),
            viewport={"width": width, "height": height},
            java_script_enabled=True,
        )
        self._page = self._context.new_page()
        return self._page

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self._context:
                self._context.close()
            if self._browser:
                self._browser.close()
        finally:
            if self._play:
                self._play.stop()

class DataPersistence:
    """Handle data persistence and change detection."""
    
    @staticmethod
    def load_previous_data(filename=PREVIOUS_DATA_FILE):
        """Load previously scraped data."""
        try:
            if Path(filename).exists():
                with open(filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Error loading previous data: {e}")
        return {}
    
    @staticmethod
    def save_current_data(data, filename=PREVIOUS_DATA_FILE):
        """Save current data for future comparison."""
        try:
            Path(filename).parent.mkdir(parents=True, exist_ok=True)
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Error saving current data: {e}")
    
    @staticmethod
    def has_data_changed(current_data, previous_data, key='data'):
        """Check if data has changed since last run."""
        return current_data != previous_data.get(key, [])

class GAIInsightsScraper:
    """Scraper for GAI Insights table data."""
    
    def __init__(self):
        self.url = GAI_INSIGHTS_URL
        self.table_id = GAI_TABLE_ID
        self.config = SCRAPING_CONFIG
    
    def scrape(self):
        """Scrape table data from GAI Insights."""
        logger.info(f"Starting GAI Insights scraping from {self.url}")
        
        with BrowserManager() as page:
            return self._scrape_with_page(page)
    
    def _scrape_with_page(self, page):
        """Internal method to scrape with a Playwright page."""
        try:
            logger.info("Navigating to page via Playwright")
            page.goto(self.url, timeout=self.config["page_load_timeout"] * 1000, wait_until="domcontentloaded")

            # Allow additional JS-driven population
            time.sleep(self.config["dynamic_content_wait"])

            # Try waiting specifically for table rows
            try:
                page.wait_for_selector(f"#{self.table_id} tbody tr", timeout=45_000)
                time.sleep(2)
            except PlaywrightTimeoutError:
                logger.warning("Table rows not immediately found, proceeding with current DOM...")

            html = page.content()
            soup = BeautifulSoup(html, 'html.parser')
            try:
                return self._extract_table_data(soup)
            except RSSScraperError as e:
                # Save snapshot for debugging if expected table not found or parsing fails
                try:
                    snapshot_path = 'gaiinsights_snapshot.html'
                    with open(snapshot_path, 'w', encoding='utf-8') as snap:
                        snap.write(html)
                    logger.warning(f"Saved HTML snapshot to {snapshot_path} for diagnostics")
                except Exception as snap_err:
                    logger.warning(f"Failed to write HTML snapshot: {snap_err}")
                raise
        except Exception as e:
            logger.error(f"Error during GAI scraping: {e}")
            raise RSSScraperError(f"GAI scraping failed: {e}")
    
    def _extract_table_data(self, soup):
        """Extract data from the HTML table.

        Primary: find table by configured ID.
        Fallback: heuristically choose a table with headers likely matching the GAI ratings table.
        """
        table = soup.find('table', id=self.table_id)
        if not table:
            logger.warning(f"Table with ID '{self.table_id}' not found; attempting heuristic fallback")
            candidates = soup.find_all('table')
            best = None
            best_score = 0
            # Keywords typical to the GAI table headers
            keywords = {'date', 'rating', 'score', 'title', 'headline', 'news'}
            for t in candidates:
                try:
                    # Prefer header row within thead, else first row
                    headers_row = t.find('thead')
                    if headers_row:
                        hdrs = [th.get_text(strip=True).lower() for th in headers_row.find_all(['th','td'])]
                    else:
                        first_row = t.find('tr')
                        hdrs = [th.get_text(strip=True).lower() for th in first_row.find_all(['th','td'])] if first_row else []
                    score = sum(1 for h in hdrs for kw in keywords if kw in h)
                    # Bonus if there are at least 3+ columns
                    if len(hdrs) >= 3:
                        score += 1
                    if score > best_score:
                        best_score = score
                        best = t
                except Exception:
                    continue
            # Require a minimal score to avoid picking arbitrary layout tables
            if best and best_score >= 2:
                logger.info(f"Using heuristic table match (score={best_score})")
                table = best
            else:
                raise RSSScraperError(f"Table with ID '{self.table_id}' not found and no suitable fallback table detected")
        
        # Extract headers
        headers_row = table.find('thead')
        if headers_row:
            headers = [th.get_text(strip=True) for th in headers_row.find_all(['th', 'td'])]
        else:
            first_row = table.find('tr')
            headers = [th.get_text(strip=True) for th in first_row.find_all(['th', 'td'])] if first_row else []
        
        # Extract rows
        tbody = table.find('tbody')
        rows = tbody.find_all('tr') if tbody else table.find_all('tr')[1:]
        
        table_data = []
        for row in rows:
            cells = row.find_all(['td', 'th'])
            if not cells:
                continue
            
            row_data = {}
            for i, cell in enumerate(cells):
                header = headers[i] if i < len(headers) else f"Column_{i+1}"
                cell_text = normalize_text(cell.get_text(strip=True))
                links = [a.get('href') for a in cell.find_all('a', href=True)]
                
                row_data[header] = {
                    'text': cell_text,
                    'links': links
                }
            
            # Only add rows with content
            if any(data['text'] or data['links'] for data in row_data.values()):
                table_data.append(row_data)
        
        logger.info(f"Successfully extracted {len(table_data)} rows from GAI table")
        return table_data

class RSSGenerator:
    """Generate RSS feeds from scraped data."""
    
    @staticmethod
    def generate_gai_feed(table_data):
        """Generate RSS feed for GAI Insights data with 60-day retention and archiving.

        Behaviour:
        - Keep all rows that are within last 60 days inside primary feed.
        - Move older rows into an archive feed file (appended, de-duplicated by GUID).
        - If dates are unparsable, treat as current run (remain in main feed).
        """
        metadata = RSS_METADATA["gai"]
        main_filename = RSS_FEED_FILES["gai"]
        archive_filename = RSS_FEED_FILES.get("gai_archive", "ai_rss_feed_archive.xml")

        cutoff = datetime.now(timezone.utc).date().toordinal() - 60  # ordinal comparison for speed
        recent_rows = []
        archive_rows = []

        # First pass: classify rows by date (if parseable)
        for row in table_data:
            date_val, rating_val, title_val, title_url, desc_val = RSSGenerator._extract_row_data(row)
            parsed_dt = RSSGenerator._parse_date(date_val)
            if parsed_dt:
                if parsed_dt.date().toordinal() >= cutoff:
                    recent_rows.append(row)
                else:
                    archive_rows.append(row)
            else:
                # Keep in recent if date unknown
                recent_rows.append(row)

        logger.info(f"Retention split: {len(recent_rows)} recent rows, {len(archive_rows)} to archive (from {len(table_data)} total)")

        # Generate main feed
        try:
            fg = FeedGenerator()
            fg.title(metadata["title"])
            fg.link(href=metadata["link"], rel='alternate')
            fg.description(metadata["description"])
            fg.language('en')
            fg.lastBuildDate(datetime.now(timezone.utc))
            fg.generator('GitHub Action RSS Scraper v2.1 (retention)')

            for i, row_data in enumerate(recent_rows):
                try:
                    fe = fg.add_entry()
                    date_val, rating_val, title_val, title_url, desc_val = RSSGenerator._extract_row_data(row_data)
                    # Normalize text to fix encoding issues
                    title_val = normalize_text(title_val)
                    desc_val = normalize_text(desc_val)
                    rss_title = title_val or f"Entry {i+1}"
                    if rating_val and rating_val.lower() in RATING_TAGS:
                        rss_title += RATING_TAGS[rating_val.lower()]
                    content_for_id = f"{date_val}|{rating_val}|{title_val}|{desc_val}"
                    entry_id = hashlib.md5(content_for_id.encode()).hexdigest()
                    fe.id(entry_id)
                    fe.title(rss_title)
                    fe.description(desc_val or title_val)
                    fe.link(href=title_url or metadata["link"])
                    pub_date = RSSGenerator._parse_date(date_val) or datetime.now(timezone.utc)
                    fe.pubDate(pub_date)
                except Exception as e:
                    logger.error(f"Error processing recent GAI entry {i+1}: {e}")
            
            # Write RSS 2.0 with XSL stylesheet
            rss_str = fg.rss_str(pretty=True).decode('utf-8')
            if '<?xml-stylesheet' not in rss_str:
                # Insert stylesheet AFTER the XML declaration (must come after <?xml version...?>)
                rss_str = rss_str.replace(
                    "?>\n<rss",
                    '?>\n<?xml-stylesheet type="text/xsl" href="/feed-style.xsl"?>\n<rss'
                )
            with open(main_filename, 'w', encoding='utf-8') as f:
                f.write(rss_str)
            logger.info(f"GAI RSS 2.0 feed written: {main_filename} ({len(recent_rows)} entries)")
            
            # Generate additional formats using MultiFeedGenerator
            try:
                multi_gen = MultiFeedGenerator(
                    title=metadata["title"],
                    link=metadata["link"],
                    description=metadata["description"],
                    language='en',
                    author='Ted Tschopp'
                )
                
                for row_data in recent_rows:
                    try:
                        date_val, rating_val, title_val, title_url, desc_val = RSSGenerator._extract_row_data(row_data)
                        title_val = normalize_text(title_val)
                        desc_val = normalize_text(desc_val)
                        rss_title = title_val or "Entry"
                        if rating_val and rating_val.lower() in RATING_TAGS:
                            rss_title += RATING_TAGS[rating_val.lower()]
                        content_for_id = f"{date_val}|{rating_val}|{title_val}|{desc_val}"
                        entry_id = hashlib.md5(content_for_id.encode()).hexdigest()
                        pub_date = RSSGenerator._parse_date(date_val) or datetime.now(timezone.utc)
                        
                        multi_gen.add_item(
                            title=rss_title,
                            link=title_url or metadata["link"],
                            description=desc_val or title_val,
                            pub_date=pub_date,
                            guid=entry_id
                        )
                    except Exception as e:
                        logger.error(f"Error adding entry to multi-format generator: {e}")
                
                # Write additional formats
                base_name = main_filename.replace('.xml', '')
                
                with open(f'{base_name}_rss1.xml', 'w', encoding='utf-8') as f:
                    f.write(multi_gen.generate_rss1())
                logger.info(f"GAI RSS 1.0 feed written: {base_name}_rss1.xml")
                
                with open(f'{base_name}.atom', 'w', encoding='utf-8') as f:
                    f.write(multi_gen.generate_atom())
                logger.info(f"GAI Atom feed written: {base_name}.atom")
                
                with open(f'{base_name}.json', 'w', encoding='utf-8') as f:
                    f.write(multi_gen.generate_json_feed())
                logger.info(f"GAI JSON Feed written: {base_name}.json")
                
            except Exception as e:
                logger.warning(f"Could not generate additional feed formats: {e}")
                
        except Exception as e:
            logger.error(f"Error generating main GAI RSS feed: {e}")
            raise RSSScraperError(f"GAI RSS generation failed: {e}")

        # Archive handling: load existing archive entries (if file exists) then append new ones and write out
        if archive_rows:
            try:
                existing_archive = []
                if Path(archive_filename).exists():
                    try:
                        # Lightweight parse: collect existing GUIDs to prevent duplication
                        from xml.etree import ElementTree as ET
                        tree = ET.parse(archive_filename)
                        root = tree.getroot()
                        for item in root.findall('.//item'):
                            guid_el = item.find('guid')
                            title_el = item.find('title')
                            link_el = item.find('link')
                            desc_el = item.find('description')
                            pub_el = item.find('pubDate')
                            existing_archive.append({
                                'guid': guid_el.text if guid_el is not None else '',
                                'title': title_el.text if title_el is not None else '',
                                'link': link_el.text if link_el is not None else metadata['link'],
                                'description': desc_el.text if desc_el is not None else '',
                                'pubDate': pub_el.text if pub_el is not None else ''
                            })
                    except Exception as parse_err:
                        logger.warning(f"Could not parse existing archive (will recreate): {parse_err}")

                existing_guids = {a['guid'] for a in existing_archive if a.get('guid')}

                archive_fg = FeedGenerator()
                archive_fg.title(metadata["title"] + " (Archive)")
                archive_fg.link(href=metadata["link"], rel='alternate')
                archive_fg.description("Archived items older than 60 days from GAI Insights feed")
                archive_fg.language('en')
                archive_fg.lastBuildDate(datetime.now(timezone.utc))
                archive_fg.generator('GitHub Action RSS Scraper v2.1 (archive)')

                # Re-add existing archive entries first (preserve history)
                for a in existing_archive:
                    try:
                        fe = archive_fg.add_entry()
                        fe.id(a['guid'])
                        fe.title(normalize_text(a['title']))
                        fe.description(normalize_text(a['description']))
                        fe.link(href=a['link'])
                        if a['pubDate']:
                            fe.pubDate(a['pubDate'])
                    except Exception:
                        continue

                # Append new archive rows
                for row_data in archive_rows:
                    try:
                        date_val, rating_val, title_val, title_url, desc_val = RSSGenerator._extract_row_data(row_data)
                        # Normalize text to fix encoding issues
                        title_val = normalize_text(title_val)
                        desc_val = normalize_text(desc_val)
                        content_for_id = f"{date_val}|{rating_val}|{title_val}|{desc_val}"
                        entry_id = hashlib.md5(content_for_id.encode()).hexdigest()
                        if entry_id in existing_guids:
                            continue
                        fe = archive_fg.add_entry()
                        rss_title = title_val or "Archived Entry"
                        if rating_val and rating_val.lower() in RATING_TAGS:
                            rss_title += RATING_TAGS[rating_val.lower()]
                        fe.id(entry_id)
                        fe.title(rss_title)
                        fe.description(desc_val or title_val)
                        fe.link(href=title_url or metadata['link'])
                        pub_date = RSSGenerator._parse_date(date_val) or datetime.now(timezone.utc)
                        fe.pubDate(pub_date)
                    except Exception as e:
                        logger.error(f"Error archiving row: {e}")
                        continue

                with open(archive_filename, 'wb') as f:
                    f.write(archive_fg.rss_str(pretty=True))
                logger.info(f"Archive RSS updated: {archive_filename} (total entries: {len(existing_archive) + len(archive_rows)})")
            except Exception as e:
                logger.error(f"Error updating archive feed: {e}")
        else:
            logger.info("No rows exceeded 60-day retention; archive unchanged.")
    
    @staticmethod
    def _extract_row_data(row_data):
        """Extract structured data from a table row."""
        columns = list(row_data.items())
        
        date_value = ""
        rating_value = ""
        title_value = ""
        title_url = ""
        description_value = ""
        
        for col_name, col_data in columns:
            col_text = col_data.get('text', '').strip()
            col_links = col_data.get('links', [])
            
            # Identify columns by content
            if not date_value and (col_name.lower() in ['date', 'published', 'time'] or 
                                 any(char.isdigit() for char in col_text[:10])):
                date_value = col_text
            elif not rating_value and (col_name.lower() in ['rating', 'score'] or 
                                      col_text.lower() in ['essential', 'important', 'optional']):
                rating_value = col_text
            elif not title_value and (col_links or (len(col_text) > 10 and 
                                                   col_name.lower() not in ['rating', 'score'])):
                title_value = col_text
                if col_links:
                    title_url = col_links[0]
            elif len(col_text) > len(description_value):
                description_value = col_text
        
        return date_value, rating_value, title_value, title_url, description_value
    
    @staticmethod
    def _parse_date(date_str):
        """Parse date string to datetime object."""
        if not date_str:
            return None
        
        try:
            for date_format in ['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y']:
                try:
                    return datetime.strptime(date_str, date_format).replace(tzinfo=timezone.utc)
                except ValueError:
                    continue
        except:
            pass
        
        return None

# ---------------- Aggregator Utilities ---------------- #

def load_aggregator_configs():
    """Load aggregation settings from unified 'feeds' list in _config.yml.

    We now treat any entry in feeds with aggregated: true (and enabled != false)
    as an aggregation config. Backward compatibility: if legacy aggregated_feeds
    block still exists, include those too (but unified list takes precedence
    for matching keys).
    """
    results = []
    try:
        site_yaml = Path('_config.yml')
        if not site_yaml.exists():
            return results
        try:
            import yaml
        except ImportError:
            logger.warning("PyYAML not installed; skipping aggregation config load")
            return results
        with open(site_yaml, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}

        # Unified list
        unified = data.get('feeds') or []
        if isinstance(unified, list):
            for raw in unified:
                if not isinstance(raw, dict):
                    continue
                if not raw.get('aggregated'):
                    continue
                if raw.get('enabled') is False:
                    continue
                cfg = dict(AGGREGATED_DEFAULT)
                for k,v in raw.items():
                    cfg[k] = v
                cfg['output'] = (cfg.get('output') or cfg.get('url') or 'aggregated_external.xml').lstrip('/')
                cfg['key'] = raw.get('key') or Path(cfg['output']).stem
                results.append(cfg)

        # Legacy block fallback (only add keys not already present)
        legacy = data.get('aggregated_feeds')
        legacy_list = []
        if isinstance(legacy, dict):
            legacy_list = [legacy]
        elif isinstance(legacy, list):
            legacy_list = legacy
        if legacy_list:
            existing_keys = {r['key'] for r in results if 'key' in r}
            for raw in legacy_list:
                if not isinstance(raw, dict):
                    continue
                temp = dict(AGGREGATED_DEFAULT)
                for k,v in raw.items():
                    temp[k] = v
                temp['output'] = (temp.get('output') or 'aggregated_external.xml').lstrip('/')
                temp['key'] = raw.get('key') or Path(temp['output']).stem
                if temp['key'] not in existing_keys:
                    results.append(temp)
    except Exception as e:
        logger.warning(f"Error loading aggregated feed configs: {e}")
    return results

# Backward compatibility helper (returns first config or default)
def load_aggregator_config():
    configs = load_aggregator_configs()
    return configs[0] if configs else dict(AGGREGATED_DEFAULT)

AGG_CACHE_FILE = AGGREGATOR_CACHE_FILE
_USER_AGENTS = [
    # A small rotating pool of realistic desktop browser UA strings
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'
]

# Importance grading (EA aggregated feed)
IMPORTANCE_RUBRIC_PATH = 'Docs/reference/business-and-technical-importance-rubric.md'
AI_RELEVANCE_RUBRIC_PATH = 'Docs/reference/ai-relevance-rubric.md'
BUSINESS_TAGS = {1: '[ ~ ]', 2: '[ * ]', 3: '[ ! ]'}
TECHNICAL_TAGS = {1: '[ ◻ ]', 2: '[ ◼ ]', 3: '[ ⬢ ]'}
_ALL_IMPORTANCE_TAGS = set(list(BUSINESS_TAGS.values()) + list(TECHNICAL_TAGS.values()))


def _resolve_models_token() -> str:
    return (os.environ.get('GH_MODELS_TOKEN', '').strip() or os.environ.get('GH_Models_Token', '').strip())


def _read_text_file(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as handle:
            return handle.read().strip()
    except Exception:
        return ''


def _rubric_hash(markdown: str) -> str:
    return hashlib.sha1((markdown or '').encode('utf-8')).hexdigest()


def _ai_relevance_context_hash(title: str, summary: str, article: str, rubric_hash: str, model: str) -> str:
    raw = json.dumps(
        {
            'title': title,
            'summary': summary,
            'article': article,
            'rubric_hash': rubric_hash,
            'model': model,
        },
        sort_keys=True,
        ensure_ascii=False,
    )
    return hashlib.sha1(raw.encode('utf-8')).hexdigest()


def _ai_relevance_allows_grading(relevance: dict | None) -> bool:
    if not relevance:
        return False
    decision = str(relevance.get('decision') or '').strip().lower()
    return bool(relevance.get('is_ai_related')) and decision == 'proceed'


def _strip_trailing_importance_tags(title: str) -> str:
    if not title:
        return ''
    cleaned = str(title)
    while True:
        stripped = cleaned.rstrip()
        removed = False
        for tag in _ALL_IMPORTANCE_TAGS:
            if stripped.endswith(tag):
                cleaned = stripped[: -len(tag)].rstrip()
                removed = True
                break
        if not removed:
            return cleaned


def _count_trailing_importance_tags(title: str) -> int:
    if not title:
        return 0
    cleaned = str(title)
    count = 0
    while True:
        stripped = cleaned.rstrip()
        removed = False
        for tag in _ALL_IMPORTANCE_TAGS:
            if stripped.endswith(tag):
                cleaned = stripped[: -len(tag)].rstrip()
                count += 1
                removed = True
                break
        if not removed:
            return count


def _importance_cache(cache: dict) -> dict:
    return cache.setdefault('importance', {})


def _importance_key_for_entry(cfg: dict, entry: dict) -> str:
    # Stable enough for aggregation: prefer link; fallback to GUID.
    link = str(entry.get('link') or '').strip()
    guid = str(entry.get('guid') or '').strip()
    basis = link or guid or (entry.get('title') or '')
    key_hash = hashlib.sha1(str(basis).encode('utf-8')).hexdigest()[:16]
    feed_key = str(cfg.get('key') or 'aggregated').strip() or 'aggregated'
    return f"{feed_key}_{key_hash}"


def _status_code_from_exception(exc: Exception) -> int | None:
    response = getattr(exc, 'response', None)
    if response is None:
        return None
    status = getattr(response, 'status_code', None)
    if isinstance(status, int):
        return status
    return None


def _retry_after_seconds(exc: Exception) -> float | None:
    response = getattr(exc, 'response', None)
    if response is None:
        return None
    headers = getattr(response, 'headers', None)
    if not headers:
        return None
    retry_after = headers.get('Retry-After')
    if retry_after is None:
        return None
    try:
        return float(retry_after)
    except Exception:
        return None


def _call_with_retry(
    call,
    max_attempts: int = 4,
    base_delay_sec: float = 1.5,
    max_delay_sec: float = 20.0,
    rate_limit_state: dict | None = None,
    rate_limit_window_sec: float = 60.0,
    rate_limit_threshold: int = 5,
    rate_limit_cooldown_base_sec: float = 45.0,
    rate_limit_cooldown_max_sec: float = 300.0,
) -> tuple[dict, dict]:
    retries = 0
    state = rate_limit_state if isinstance(rate_limit_state, dict) else None

    for attempt in range(1, max_attempts + 1):
        try:
            if state is not None:
                now = time.time()
                cooldown_until = float(state.get('cooldown_until', 0.0) or 0.0)
                if now < cooldown_until:
                    sleep_for = max(0.0, cooldown_until - now)
                    logger.warning(f'LLM 429 cooldown active: sleeping {sleep_for:.1f}s')
                    time.sleep(sleep_for)

            result = call()
            if state is not None:
                state['recent_429'] = []
                state['cooldown_strikes'] = 0
            return result, {'attempt': attempt, 'retries': retries}
        except Exception as exc:
            msg = str(exc).lower()
            status_code = _status_code_from_exception(exc)
            retryable = status_code in {429, 500, 502, 503, 504} or 'too many requests' in msg or 'timed out' in msg or 'timeout' in msg
            if attempt >= max_attempts or not retryable:
                raise

            retry_after = _retry_after_seconds(exc)
            if state is not None and status_code == 429:
                now = time.time()
                recent = state.setdefault('recent_429', [])
                if not isinstance(recent, list):
                    recent = []
                    state['recent_429'] = recent
                recent.append(now)
                cutoff = now - float(max(1.0, rate_limit_window_sec))
                state['recent_429'] = [t for t in recent if isinstance(t, (int, float)) and t >= cutoff]
                if len(state['recent_429']) >= int(max(1, rate_limit_threshold)):
                    strikes = int(state.get('cooldown_strikes', 0) or 0) + 1
                    state['cooldown_strikes'] = strikes
                    cooldown = min(float(rate_limit_cooldown_max_sec), float(rate_limit_cooldown_base_sec) * (2 ** (strikes - 1)))
                    if retry_after is not None:
                        cooldown = max(cooldown, float(retry_after))
                    cooldown = min(float(rate_limit_cooldown_max_sec), cooldown + (0.1 * cooldown))
                    state['cooldown_until'] = max(float(state.get('cooldown_until', 0.0) or 0.0), now + cooldown)
                    logger.warning(
                        f"Sustained 429s detected (count={len(state['recent_429'])} window={rate_limit_window_sec}s); "
                        f"cooling down for ~{cooldown:.1f}s"
                    )

            if retry_after is not None:
                delay = min(max_delay_sec, max(0.0, retry_after))
            else:
                delay = min(max_delay_sec, base_delay_sec * (2 ** (attempt - 1)))

            if state is not None:
                cooldown_until = float(state.get('cooldown_until', 0.0) or 0.0)
                cooldown_remaining = max(0.0, cooldown_until - time.time())
                delay = max(float(delay), cooldown_remaining)

            time.sleep(delay)
            retries += 1

    raise RuntimeError('importance_call_failed')

def _load_agg_cache():
    try:
        if Path(AGG_CACHE_FILE).exists():
            with open(AGG_CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        logger.warning(f"Failed to load aggregator cache: {e}")
    return { 'sources': {}, 'domain_last_fetch': {} }

def _save_agg_cache(cache):
    try:
        Path(AGG_CACHE_FILE).parent.mkdir(parents=True, exist_ok=True)
        with open(AGG_CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(cache, f, indent=2)
    except Exception as e:
        logger.warning(f"Failed to save aggregator cache: {e}")

def polite_delay(policy, domain, cache):
    now = time.time()
    domain_times = cache.setdefault('domain_last_fetch', {})
    last = domain_times.get(domain, 0)
    min_interval = policy.get('per_domain_min_interval', 10)
    wait_needed = last + min_interval - now
    if wait_needed > 0:
        sleep_time = min(wait_needed, min_interval)
        logger.info(f"Respecting per-domain interval for {domain}: sleeping {sleep_time:.2f}s")
        time.sleep(sleep_time)
    # Random base inter-request delay
    base_delay = random.uniform(policy.get('min_delay', 1.0), policy.get('max_delay', 3.0))
    time.sleep(base_delay)
    domain_times[domain] = time.time()

def fetch_rss(url, policy, cache):
    """Fetch RSS politely with rotating UA, conditional requests, retries, backoff, and pacing.

    Returns list of items (dict) or empty list on failure/304.
    """
    src_meta = cache.setdefault('sources', {}).setdefault(url, {})
    # Failure tracking (persisted in cache file):
    #   consecutive_failures: int
    #   last_status: HTTP status code or 'exception'
    #   last_error: string summary of last failure
    #   last_success_ts: epoch seconds of last successful fetch
    # Allow configurable skip threshold (default 5) to avoid wasting time on dead feeds.
    skip_threshold = policy.get('skip_after_failures', 5)
    if src_meta.get('consecutive_failures', 0) >= skip_threshold and not src_meta.get('recent_success_grace'):
        logger.warning(f"Skipping {url} (consecutive failures >= {skip_threshold})")
        src_meta['skipped'] = True
        src_meta['last_classification'] = 'skipped'
        return []
    src_meta.pop('skipped', None)
    headers = {
        'User-Agent': random.choice(_USER_AGENTS),
        'Accept': 'application/rss+xml, application/xml;q=0.9, text/xml;q=0.8, */*;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close',
        'Cache-Control': 'no-cache'
    }
    # Conditional headers
    if 'etag' in src_meta:
        headers['If-None-Match'] = src_meta['etag']
    if 'last_modified' in src_meta:
        headers['If-Modified-Since'] = src_meta['last_modified']

    attempts = policy.get('retry_attempts', 3)
    back_base = policy.get('retry_backoff_base', 2)
    jitter = policy.get('retry_jitter', 0.5)
    timeout = policy.get('timeout', 25)
    domain = urlparse(url).hostname or 'unknown'

    polite_delay(policy, domain, cache)

    last_err = None
    session = requests.Session()
    for attempt in range(1, attempts + 1):
        try:
            resp = session.get(url, headers=headers, timeout=timeout)
            status = resp.status_code
            if status == 304:
                logger.info(f"Not modified (304): {url}")
                src_meta['last_status'] = 304
                src_meta['last_error'] = None
                src_meta['last_classification'] = 'not_modified'
                return []
            if status >= 400:
                raise RuntimeError(f"HTTP {status}")
            # Update caching headers
            if 'ETag' in resp.headers:
                src_meta['etag'] = resp.headers['ETag']
            if 'Last-Modified' in resp.headers:
                src_meta['last_modified'] = resp.headers['Last-Modified']
            content = resp.content
            root = ET.fromstring(content)
            channel = root.find('channel') or root
            items = []
            for item in channel.findall('.//item'):
                def _text(tag):
                    el = item.find(tag)
                    return el.text.strip() if el is not None and el.text else ''
                items.append({
                    'title': _text('title'),
                    'link': _text('link'),
                    'description': _text('description') or _text('summary'),
                    'pubDate': _text('pubDate')
                })
            # Success bookkeeping
            src_meta['consecutive_failures'] = 0
            src_meta['last_status'] = status
            src_meta['last_error'] = None
            src_meta['last_success_ts'] = time.time()
            # Provide a one-run grace after recovery so we don't immediately skip again.
            src_meta['recent_success_grace'] = True
            src_meta['last_classification'] = 'success'
            return items
        except Exception as e:
            last_err = e
            logger.warning(f"Fetch attempt {attempt}/{attempts} failed for {url}: {e}")
            if attempt < attempts:
                delay = (back_base ** (attempt - 1)) + random.uniform(0, jitter)
                logger.info(f"Backing off {delay:.2f}s before retry")
                time.sleep(delay)
    # Failure after all attempts
    fail_count = src_meta.get('consecutive_failures', 0) + 1
    src_meta['consecutive_failures'] = fail_count
    src_meta['last_status'] = getattr(last_err, 'status', 'exception') if last_err else 'unknown'
    src_meta['last_error'] = str(last_err) if last_err else 'Unknown failure'
    # Remove grace once we have a failure
    src_meta.pop('recent_success_grace', None)
    # Classification heuristics
    err_l = (src_meta.get('last_error') or '').lower()
    classification = 'other_failure'
    if 'ssl' in err_l:
        classification = 'ssl_error'
    elif 'name or service not known' in err_l or 'nxdomain' in err_l or 'temporary failure in name resolution' in err_l or 'nodename nor servname' in err_l:
        classification = 'dns_error'
    elif isinstance(src_meta.get('last_status'), int):
        try:
            code = int(src_meta['last_status'])
            if 400 <= code < 500:
                classification = 'http_4xx'
            elif 500 <= code < 600:
                classification = 'http_5xx'
        except Exception:
            pass
    if 'parse' in err_l or 'xml' in err_l:
        classification = 'xml_error'
    src_meta['last_classification'] = classification
    logger.error(f"All attempts failed for {url}: {last_err}")
    return []

def parse_pub_date(date_str):
    if not date_str:
        return None
    try:
        return date_parser.parse(date_str)
    except Exception:
        return None

def normalize_aggregated_sources(raw_sources):
    """Normalize aggregated feed sources to a list of {url, category} objects.

    Backward compatible with legacy list[str] source format.
    """
    normalized = []
    for src in raw_sources or []:
        if isinstance(src, str):
            url = src.strip()
            if not url:
                continue
            normalized.append({'url': url, 'category': None})
            continue

        if isinstance(src, dict):
            url_value = src.get('url')
            url = str(url_value).strip() if url_value is not None else ''
            if not url:
                logger.warning(f"Skipping malformed aggregated source object without url: {src}")
                continue
            category_value = src.get('category')
            category = str(category_value).strip() if category_value is not None else None
            if category == '':
                category = None
            normalized.append({'url': url, 'category': category})
            continue

        logger.warning(f"Skipping unsupported aggregated source entry: {src}")

    seen_categories = {}
    for src in normalized:
        if src['url'] in seen_categories and seen_categories[src['url']] != src.get('category'):
            logger.warning(
                "Duplicate aggregated source URL with different categories: "
                f"{src['url']} ({seen_categories[src['url']]} vs {src.get('category')})"
            )
        else:
            seen_categories[src['url']] = src.get('category')

    return normalized

def aggregate_external_feeds(cfg):
    sources = normalize_aggregated_sources(cfg.get('sources', []))
    max_items = int(cfg.get('max_items', 150))
    retention_days = int(cfg.get('retention_days', 60))
    source_attr = (cfg.get('source_attribution') or 'title').lower()
    output_file = cfg.get('output', 'aggregated_external.xml')
    archive_file = cfg.get('archive_output') or output_file.replace('.xml', '_archive.xml')
    if not sources:
        logger.info("No sources configured for aggregation")
        return
    logger.info(f"Aggregating {len(sources)} sources -> {output_file} (retention {retention_days} days) [polite mode]")
    collected = []
    # Shuffle sources to avoid same ordering every run
    shuffled = list(sources)
    random.shuffle(shuffled)
    cache = _load_agg_cache()
    policy = AGGREGATED_FETCH_POLICY
    policy.setdefault('skip_after_failures', 5)
    # Optional fast mode for testing (reduces delays). Activate with FAST_AGGREGATE=1
    if os.getenv('FAST_AGGREGATE'):
        logger.info("FAST_AGGREGATE enabled: using minimal polite delays for test run")
        policy = dict(policy)
        policy['min_delay'] = 0.05
        policy['max_delay'] = 0.15
        policy['per_domain_min_interval'] = 0.2
    health = {
        'total_sources': len(shuffled),
        'attempted': 0,
        'skipped': 0,
        'with_items': 0,
        'failures': 0,
        'recovered': 0,
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'details': []
    }
    prune_threshold = int(os.getenv('PRUNE_CONSECUTIVE_THRESHOLD', '3'))
    permanent_classes = {'ssl_error','dns_error'}
    recommended_prune = []
    for src in shuffled:
        src_url = src.get('url')
        src_category = src.get('category')
        logger.info(f"Fetching source: {src_url}" + (f" [category: {src_category}]" if src_category else ""))
        pre_failures = cache.get('sources', {}).get(src_url, {}).get('consecutive_failures', 0)
        items = fetch_rss(src_url, policy, cache)
        meta = cache.get('sources', {}).get(src_url, {})
        if meta.get('skipped'):
            health['skipped'] += 1
            health['details'].append({
                'url': src_url,
                'category': src_category,
                'status': 'skipped',
                'items': 0,
                'consecutive_failures': meta.get('consecutive_failures', 0),
                'last_error': meta.get('last_error'),
                'last_status': meta.get('last_status'),
                'classification': meta.get('last_classification') or 'skipped'
            })
            continue
        health['attempted'] += 1
        if items:
            health['with_items'] += 1
            if pre_failures and meta.get('consecutive_failures', 0) == 0:
                health['recovered'] += 1
            logger.info(f"  Retrieved {len(items)} items")
        else:
            if meta.get('consecutive_failures', 0) > 0:
                health['failures'] += 1
            logger.info("  No items returned")
        classification = meta.get('last_classification') or ('ok' if items else 'empty')
        cf = meta.get('consecutive_failures', 0)
        if (classification in permanent_classes and cf >= 1) or cf >= prune_threshold:
            recommended_prune.append(src_url)
        health['details'].append({
            'url': src_url,
            'category': src_category,
            'status': 'ok' if items else ('failed' if meta.get('consecutive_failures', 0) > 0 else 'empty'),
            'items': len(items),
            'consecutive_failures': meta.get('consecutive_failures', 0),
            'last_error': meta.get('last_error'),
            'last_status': meta.get('last_status'),
            'classification': classification
        })
        src_host = urlparse(src_url).hostname or 'source'
        attribution = f"Source: {src_host}"
        if src_category:
            attribution += f" | Category: {src_category}"
        for it in items:
            dt = parse_pub_date(it.get('pubDate')) or datetime.now(timezone.utc)
            guid_basis = f"{it.get('title')}|{it.get('link')}|{dt.isoformat()}"
            guid = hashlib.md5(guid_basis.encode()).hexdigest()
            title_text = it.get('title') or 'Untitled'
            description_text = it.get('description') or ''
            if source_attr == 'title':
                title_text += f" ({attribution})"
            elif source_attr == 'description':
                description_text = f"[{attribution}]\n\n{description_text}" if description_text else f"[{attribution}]"
            collected.append({
                'title': title_text,
                'link': it.get('link') or cfg.get('link'),
                'description': description_text,
                'pubDate': dt,
                'guid': guid
            })
        time.sleep(1)  # polite throttle

    # Deduplicate by GUID
    unique = {c['guid']: c for c in collected}.values()
    # Split by retention
    cutoff_ord = (datetime.now(timezone.utc).date().toordinal() - retention_days)
    recent = []
    archive_additions = []
    for entry in unique:
        if entry['pubDate'].date().toordinal() >= cutoff_ord:
            recent.append(entry)
        else:
            archive_additions.append(entry)

    # Sort & trim recent
    recent_sorted = sorted(recent, key=lambda x: x['pubDate'], reverse=True)[:max_items]

    # Optional: LLM importance grading + tags for selected aggregated feeds
    feed_key_norm = str(cfg.get('key') or '').strip().lower()
    importance_feed_keys = {'aggregated_ea', 'aggregated_broad_ai_news'}
    importance_enabled = feed_key_norm in importance_feed_keys
    importance_client = None
    importance_rubric = ''
    importance_rubric_hash = ''
    ai_relevance_rubric = ''
    ai_relevance_rubric_hash = ''
    importance_store = None

    if importance_enabled:
        token = _resolve_models_token()
        importance_rubric = _read_text_file(IMPORTANCE_RUBRIC_PATH)
        importance_rubric_hash = _rubric_hash(importance_rubric) if importance_rubric else ''
        ai_relevance_rubric = _read_text_file(AI_RELEVANCE_RUBRIC_PATH)
        ai_relevance_rubric_hash = _rubric_hash(ai_relevance_rubric) if ai_relevance_rubric else ''
        if not token:
            logger.warning(
                f"{feed_key_norm} aggregated importance tagging skipped: missing GH_MODELS_TOKEN / GH_Models_Token"
            )
        elif not importance_rubric_hash:
            logger.warning(
                f"{feed_key_norm} aggregated importance tagging skipped: missing rubric file {IMPORTANCE_RUBRIC_PATH}"
            )
        elif not ai_relevance_rubric_hash:
            logger.warning(
                f"{feed_key_norm} aggregated importance tagging skipped: missing rubric file {AI_RELEVANCE_RUBRIC_PATH}"
            )
        else:
            try:
                from pipeline.llm_client import GitHubModelsClient
            except Exception as import_err:
                GitHubModelsClient = None
                logger.warning(
                    f"{feed_key_norm} aggregated importance tagging skipped: could not import pipeline.llm_client ({import_err})"
                )

            if GitHubModelsClient is not None:
                importance_client = GitHubModelsClient(token=token, timeout_sec=int(cfg.get('request_timeout_sec', 25)))
                importance_store = _importance_cache(cache)

    rate_limit_state: dict = {}
    rate_limit_window_sec = float(cfg.get('llm_429_window_sec', 60))
    rate_limit_threshold = int(cfg.get('llm_429_threshold', 5))
    rate_limit_cooldown_base_sec = float(cfg.get('llm_429_cooldown_base_sec', 45.0))
    rate_limit_cooldown_max_sec = float(cfg.get('llm_429_cooldown_max_sec', 300.0))
    article_fetch_timeout_sec = int(cfg.get('article_fetch_timeout_sec', cfg.get('request_timeout_sec', 25)))
    article_max_chars = int(cfg.get('article_max_chars', 12000))

    def _tag_entries_with_importance(entries: list[dict], label: str) -> None:
        if not entries:
            return
        if not importance_enabled or importance_client is None or importance_store is None or not importance_rubric_hash or not ai_relevance_rubric_hash:
            return

        graded = 0
        reused = 0
        total = len(entries)

        for entry in entries:
            cache_key = _importance_key_for_entry(cfg, entry)
            existing = importance_store.get(cache_key)
            if isinstance(existing, dict) and str(existing.get('rubric_hash') or '') == importance_rubric_hash:
                existing_relevance = existing.get('ai_relevance') if isinstance(existing.get('ai_relevance'), dict) else None
                if isinstance(existing_relevance, dict) and not _ai_relevance_allows_grading(existing_relevance):
                    continue
                business_level = existing.get('business_level')
                technical_level = existing.get('technical_level')
                try:
                    b_tag = BUSINESS_TAGS.get(int(business_level))
                    t_tag = TECHNICAL_TAGS.get(int(technical_level))
                except Exception:
                    b_tag = None
                    t_tag = None
                if b_tag and t_tag:
                    base_title = _strip_trailing_importance_tags(entry.get('title') or '')
                    entry['title'] = f"{base_title} {b_tag} {t_tag}".strip()
                    reused += 1
                continue

            title_for_grading = str(entry.get('title') or '')
            title_for_grading = _strip_trailing_importance_tags(title_for_grading)
            # Reduce noise from source attribution in title (if present)
            title_for_grading = re.sub(r"\s*\(Source:.*\)\s*$", "", title_for_grading).strip()
            context_for_grading = str(entry.get('description') or '')
            article_for_grading = fetch_article_markdown(
                str(entry.get('link') or ''),
                timeout_sec=article_fetch_timeout_sec,
                max_chars=article_max_chars,
            )
            relevance_model = str(cfg.get('ai_relevance_model') or 'openai/gpt-4.1-mini')
            relevance_context_hash = _ai_relevance_context_hash(
                title_for_grading,
                context_for_grading,
                article_for_grading,
                ai_relevance_rubric_hash,
                relevance_model,
            )
            existing_relevance = existing.get('ai_relevance') if isinstance(existing, dict) and isinstance(existing.get('ai_relevance'), dict) else None
            relevance_payload = existing_relevance
            if not isinstance(relevance_payload, dict) or str(relevance_payload.get('context_hash') or '') != relevance_context_hash:
                try:
                    relevance_result, _relevance_meta = _call_with_retry(
                        lambda: importance_client.check_ai_relevance(
                            title_for_grading,
                            context_for_grading,
                            ai_relevance_rubric,
                            model=relevance_model,
                            article=article_for_grading,
                        ),
                        max_attempts=int(cfg.get('llm_retry_max_attempts', 4)),
                        base_delay_sec=float(cfg.get('llm_retry_base_delay_sec', 1.5)),
                        max_delay_sec=float(cfg.get('llm_retry_max_delay_sec', 20.0)),
                        rate_limit_state=rate_limit_state,
                        rate_limit_window_sec=rate_limit_window_sec,
                        rate_limit_threshold=rate_limit_threshold,
                        rate_limit_cooldown_base_sec=rate_limit_cooldown_base_sec,
                        rate_limit_cooldown_max_sec=rate_limit_cooldown_max_sec,
                    )
                    relevance_payload = {
                        'is_ai_related': bool(relevance_result.get('is_ai_related')),
                        'decision': relevance_result.get('decision', ''),
                        'confidence': relevance_result.get('confidence', ''),
                        'primary_ai_topic': relevance_result.get('primary_ai_topic', ''),
                        'rationale': relevance_result.get('rationale', ''),
                        'evidence': relevance_result.get('evidence', []),
                        'rubric_hash': ai_relevance_rubric_hash,
                        'context_hash': relevance_context_hash,
                        'checked_at': datetime.now(timezone.utc).isoformat(),
                        'model': relevance_result.get('model'),
                        'input_hash': relevance_result.get('input_hash'),
                    }
                    existing_record = existing if isinstance(existing, dict) else {}
                    existing_record['ai_relevance'] = relevance_payload
                    importance_store[cache_key] = existing_record
                except Exception as relevance_err:
                    logger.warning(f"{feed_key_norm} aggregated AI relevance check failed for entry: {relevance_err}")
                    continue

            if not _ai_relevance_allows_grading(relevance_payload):
                continue

            try:
                result, _meta = _call_with_retry(
                    lambda: importance_client.grade_importance(
                        title_for_grading,
                        context_for_grading,
                        importance_rubric,
                        model=str(cfg.get('importance_model') or 'openai/gpt-4.1-mini'),
                        article=article_for_grading,
                    ),
                    max_attempts=int(cfg.get('llm_retry_max_attempts', 4)),
                    base_delay_sec=float(cfg.get('llm_retry_base_delay_sec', 1.5)),
                    max_delay_sec=float(cfg.get('llm_retry_max_delay_sec', 20.0)),
                            rate_limit_state=rate_limit_state,
                            rate_limit_window_sec=rate_limit_window_sec,
                            rate_limit_threshold=rate_limit_threshold,
                            rate_limit_cooldown_base_sec=rate_limit_cooldown_base_sec,
                            rate_limit_cooldown_max_sec=rate_limit_cooldown_max_sec,
                )
                importance_store[cache_key] = {
                    'ai_relevance': relevance_payload,
                    'business_level': result.get('business_level'),
                    'technical_level': result.get('technical_level'),
                    'business_impact': result.get('business_impact', ''),
                    'technical_impact': result.get('technical_impact', ''),
                    'risk_impact': result.get('risk_impact', ''),
                    'enterprise_readiness': result.get('enterprise_readiness', ''),
                    'labor_workflow_impact': result.get('labor_workflow_impact', ''),
                    'confidence': result.get('confidence', ''),
                    'attention_priority': result.get('attention_priority', ''),
                    'development_summary': result.get('development_summary', ''),
                    'reason_codes': result.get('reason_codes', []),
                    'recommended_action': result.get('recommended_action', ''),
                    'rationale': result.get('rationale', ''),
                    'watch_items': result.get('watch_items', []),
                    'business_rationale': result.get('business_rationale', ''),
                    'technical_rationale': result.get('technical_rationale', ''),
                    'rubric_hash': importance_rubric_hash,
                    'graded_at': datetime.now(timezone.utc).isoformat(),
                    'model': result.get('model'),
                    'input_hash': result.get('input_hash'),
                }
                try:
                    b_tag = BUSINESS_TAGS.get(int(result.get('business_level')))
                    t_tag = TECHNICAL_TAGS.get(int(result.get('technical_level')))
                except Exception:
                    b_tag = None
                    t_tag = None
                if b_tag and t_tag:
                    base_title = _strip_trailing_importance_tags(entry.get('title') or '')
                    entry['title'] = f"{base_title} {b_tag} {t_tag}".strip()
                    graded += 1
            except Exception as grade_err:
                logger.warning(f"{feed_key_norm} aggregated importance grading failed for entry: {grade_err}")

        logger.info(f"{feed_key_norm} aggregated importance tagging complete ({label}): graded={graded} reused={reused} total={total}")

    # Apply importance tagging to current items
    _tag_entries_with_importance(recent_sorted, label='recent')

    logger.info(f"Writing {len(recent_sorted)} recent aggregated items; {len(archive_additions)} to archive")
    fg = FeedGenerator()
    fg.title(cfg.get('title'))
    fg.link(href=cfg.get('link'), rel='alternate')
    fg.description(cfg.get('description'))
    fg.language('en')
    fg.lastBuildDate(datetime.now(timezone.utc))
    fg.generator('GitHub Action RSS Aggregator v2 (retention)')
    for entry in recent_sorted:
        fe = fg.add_entry()
        fe.id(entry['guid'])
        fe.title(normalize_text(entry['title']))
        fe.description(normalize_text(entry['description']))
        fe.link(href=entry['link'])
        fe.pubDate(entry['pubDate'])
    with open(output_file, 'wb') as f:
        f.write(fg.rss_str(pretty=True))
    logger.info(f"Aggregated feed written: {output_file}")

    # Generate additional feed formats (RSS 1.0, Atom, JSON Feed)
    try:
        multi_gen = MultiFeedGenerator(
            title=cfg.get('title'),
            link=cfg.get('link'),
            description=cfg.get('description'),
            language='en',
            author='Ted Tschopp'
        )
        for entry in recent_sorted:
            multi_gen.add_item(
                title=normalize_text(entry['title']),
                link=entry['link'],
                description=normalize_text(entry['description']),
                pub_date=entry['pubDate'],
                guid=entry['guid']
            )

        base_name = output_file[:-4] if output_file.endswith('.xml') else output_file
        with open(f'{base_name}_rss1.xml', 'w', encoding='utf-8') as f:
            f.write(multi_gen.generate_rss1())
        with open(f'{base_name}.atom', 'w', encoding='utf-8') as f:
            f.write(multi_gen.generate_atom())
        with open(f'{base_name}.json', 'w', encoding='utf-8') as f:
            f.write(multi_gen.generate_json_feed())
        logger.info(f"Aggregated alternate formats written: {base_name}_rss1.xml, {base_name}.atom, {base_name}.json")
    except Exception as e:
        logger.warning(f"Could not generate additional formats for aggregated feed {output_file}: {e}")

    # Archive update
    should_update_archive = bool(archive_additions) or (feed_key_norm == 'aggregated_ea' and Path(archive_file).exists())
    if should_update_archive:
        try:
            existing = []
            existing_guids = set()
            if Path(archive_file).exists():
                try:
                    tree = ET.parse(archive_file)
                    root = tree.getroot()
                    for item in root.findall('.//item'):
                        guid_el = item.find('guid')
                        title_el = item.find('title')
                        link_el = item.find('link')
                        desc_el = item.find('description')
                        pub_el = item.find('pubDate')
                        guid_val = guid_el.text if guid_el is not None else ''
                        existing_guids.add(guid_val)
                        existing.append({
                            'guid': guid_val,
                            'title': title_el.text if title_el is not None else '',
                            'link': link_el.text if link_el is not None else cfg.get('link'),
                            'description': desc_el.text if desc_el is not None else '',
                            'pubDate': pub_el.text if pub_el is not None else ''
                        })
                except Exception as parse_err:
                    logger.warning(f"Could not parse existing aggregated archive; recreating: {parse_err}")

            # Tag EA archive entries as well (reuse cache where possible)
            if feed_key_norm == 'aggregated_ea':
                _tag_entries_with_importance(existing, label='archive existing')
                _tag_entries_with_importance(archive_additions, label='archive additions')

            archive_fg = FeedGenerator()
            archive_fg.title(cfg.get('title') + ' (Archive)')
            archive_fg.link(href=cfg.get('link'), rel='alternate')
            archive_fg.description('Archived aggregated items older than retention window')
            archive_fg.language('en')
            archive_fg.lastBuildDate(datetime.now(timezone.utc))
            archive_fg.generator('GitHub Action RSS Aggregator v2 (archive)')
            # Re-add existing
            for e in existing:
                if not e.get('guid'):
                    continue
                fe = archive_fg.add_entry()
                fe.id(e['guid'])
                fe.title(normalize_text(e['title']))
                fe.description(normalize_text(e['description']))
                fe.link(href=e['link'])
                if e['pubDate']:
                    fe.pubDate(e['pubDate'])
            # Add new
            added = 0
            for entry in archive_additions:
                if entry['guid'] in existing_guids:
                    continue
                fe = archive_fg.add_entry()
                fe.id(entry['guid'])
                fe.title(normalize_text(entry['title']))
                fe.description(normalize_text(entry['description']))
                fe.link(href=entry['link'])
                fe.pubDate(entry['pubDate'])
                added += 1
            with open(archive_file, 'wb') as f:
                f.write(archive_fg.rss_str(pretty=True))
            logger.info(f"Aggregated archive updated: {archive_file} (added {added}, total {len(existing) + added})")
        except Exception as e:
            logger.error(f"Error updating aggregated archive: {e}")
    # Persist cache updates
    _save_agg_cache(cache)
    # Write health and report artifacts under reports/aggregation; public feed
    # files remain at the repository root.
    try:
        report_dir = Path(AGGREGATION_REPORTS_DIR)
        report_dir.mkdir(parents=True, exist_ok=True)
        output_stem = Path(output_file).stem
        health_file = report_dir / f'{output_stem}_health.json'
        with open(health_file, 'w', encoding='utf-8') as hf:
            json.dump(health, hf, indent=2)
        logger.info(f"Health summary written: {health_file} (attempted {health['attempted']}, skipped {health['skipped']}, failures {health['failures']}, recovered {health['recovered']})")
        # Markdown report
        report_file = report_dir / f'{output_stem}_report.md'
        with open(report_file, 'w', encoding='utf-8') as rf:
            rf.write(f"# Aggregated Feed Health Report: {output_file}\n\n")
            rf.write(f"Generated: {health['timestamp']} UTC\n\n")
            rf.write(f"- Total sources: {health['total_sources']}\n")
            rf.write(f"- Attempted: {health['attempted']}  Skipped: {health['skipped']}  Failures: {health['failures']}  With Items: {health['with_items']}  Recovered: {health['recovered']}\n")
            rf.write(f"- Prune threshold: {prune_threshold} consecutive failures (permanent classes: ssl_error,dns_error)\n\n")
            if recommended_prune:
                rf.write("## Recommended Prune Candidates\n\n")
                for u in recommended_prune:
                    meta = cache['sources'].get(u, {})
                    rf.write(f"- {u} (cf={meta.get('consecutive_failures',0)}, class={meta.get('last_classification')}, last_error={ (meta.get('last_error') or '')[:100] })\n")
                rf.write('\n')
            rf.write("## Source Details (first 100)\n\n")
            rf.write("| URL | Category | Status | Class | CF | Items | Last Status | Error Excerpt |\n")
            rf.write("|-----|----------|--------|-------|----|-------|-------------|---------------|\n")
            for d in health['details'][:100]:
                err_excerpt = (d.get('last_error') or '')[:60].replace('\n',' ')
                rf.write(f"| {d['url']} | {d.get('category') or ''} | {d['status']} | {d.get('classification','')} | {d['consecutive_failures']} | {d['items']} | {d.get('last_status')} | {err_excerpt} |\n")
        logger.info(f"Markdown report written: {report_file}")
        # Skipped sources summary
        skipped_sources = [u for u,m in cache.get('sources',{}).items() if m.get('skipped')]
        skipped_path = Path(SKIPPED_SOURCES_FILE)
        skipped_path.parent.mkdir(parents=True, exist_ok=True)
        with open(skipped_path,'w',encoding='utf-8') as sf:
            json.dump({ 'generated': health['timestamp'], 'skip_threshold': policy.get('skip_after_failures'), 'sources': skipped_sources }, sf, indent=2)
        logger.info(f"Skipped sources summary written: {skipped_path}")
    except Exception as he:
        logger.warning(f"Failed to write health summary: {he}")

def main():
    """Main execution function."""
    logger.info("Starting enhanced RSS scraper")
    
    try:
        # Initialize components
        persistence = DataPersistence()
        gai_scraper = GAIInsightsScraper()
        
        # Load previous data
        previous_data = persistence.load_previous_data()
        
        current_gai_data = previous_data.get('gai_data', [])
        gai_enabled = str(os.environ.get("GAI_SCRAPE_ENABLED", "true")).strip().lower() in {
            "1",
            "true",
            "yes",
            "on",
        }

        # Scrape GAI Insights
        logger.info("=" * 60)
        logger.info("SCRAPING GAI INSIGHTS")
        logger.info("=" * 60)

        if not gai_enabled:
            logger.info("GAI scraping disabled for this run; reusing previous data and skipping browser-dependent scrape")
            if current_gai_data:
                RSSGenerator.generate_gai_feed(current_gai_data)
        else:
            try:
                current_gai_data = gai_scraper.scrape()
                # Check for changes
                if persistence.has_data_changed(current_gai_data, previous_data, 'gai_data'):
                    logger.info("Changes detected in GAI data")
                else:
                    logger.info("No changes detected in GAI data")
                # Generate primary GAI feed
                RSSGenerator.generate_gai_feed(current_gai_data)
            except Exception as gai_err:
                logger.error(f"GAI scraping failed; skipping GAI feed and continuing: {gai_err}")

        # Aggregated external feeds (multi-feed support)
        try:
            aggregator_cfgs = load_aggregator_configs()
            if not aggregator_cfgs:
                logger.info("No aggregated feeds configured")
            else:
                for cfg in aggregator_cfgs:
                    if not cfg.get('enabled', True):
                        logger.info(f"Aggregator '{cfg.get('key')}' disabled")
                        continue
                    logger.info("=" * 60)
                    logger.info(f"AGGREGATING SOURCES FOR FEED: {cfg.get('key')} -> {cfg.get('output')}")
                    logger.info("=" * 60)
                    aggregate_external_feeds(cfg)
        except Exception as agg_err:
            logger.error(f"Aggregator(s) failed: {agg_err}")
        
        # Save current data
        current_data = {
            'gai_data': current_gai_data,
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
        persistence.save_current_data(current_data)
        
        logger.info("RSS scraper completed successfully")
        
    except Exception as e:
        logger.error(f"Fatal error in RSS scraper: {e}")
        import traceback
        traceback.print_exc()
        exit(1)

if __name__ == "__main__":
    main()
