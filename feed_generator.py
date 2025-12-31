#!/usr/bin/env python3
"""
Multi-format feed generator supporting RSS 2.0, RSS 1.0, Atom 1.0, and JSON Feed.
"""

import json
import hashlib
import unicodedata
from datetime import datetime, timezone
from xml.etree import ElementTree as ET
from xml.dom import minidom


def normalize_text(text):
    """
    Normalize text to fix encoding issues and convert special characters.
    """
    if not text:
        return text
    
    # Fix common mojibake patterns (UTF-8 interpreted as Windows-1252)
    mojibake_fixes = {
        'â€™': "'",
        'â€˜': "'",
        'â€œ': '"',
        'â€': '"',
        'â€"': '—',
        'â€"': '–',
        'â€¦': '...',
        'Ã©': 'é',
        'Ã¨': 'è',
        'Ã¢': 'â',
        'Ã ': 'à',
        'Ã§': 'ç',
    }
    
    for bad, good in mojibake_fixes.items():
        text = text.replace(bad, good)
    
    # Unicode character replacements
    unicode_replacements = {
        '\u2018': "'",
        '\u2019': "'",
        '\u201c': '"',
        '\u201d': '"',
        '\u2013': '-',
        '\u2014': '-',
        '\u2026': '...',
        '\u00a0': ' ',
        '\u2011': '-',
        '\u2010': '-',
        '\u2212': '-',
    }
    
    for unicode_char, ascii_char in unicode_replacements.items():
        text = text.replace(unicode_char, ascii_char)
    
    text = unicodedata.normalize('NFC', text)
    return text


class FeedEntry:
    """Represents a single feed entry/item."""
    
    def __init__(self, title, link, description, pub_date=None, guid=None, author=None):
        self.title = normalize_text(title) if title else ''
        self.link = link or ''
        self.description = normalize_text(description) if description else ''
        self.pub_date = pub_date or datetime.now(timezone.utc)
        self.guid = guid or hashlib.md5(f"{title}|{link}".encode()).hexdigest()
        self.author = author or ''
    
    def to_dict(self):
        """Convert entry to dictionary for JSON serialization."""
        return {
            'id': self.guid,
            'url': self.link,
            'title': self.title,
            'content_text': self.description,
            'date_published': self.pub_date.isoformat() if isinstance(self.pub_date, datetime) else self.pub_date,
            'author': {'name': self.author} if self.author else None
        }


class MultiFeedGenerator:
    """
    Generates feeds in multiple formats: RSS 2.0, RSS 1.0, Atom 1.0, JSON Feed.
    """
    
    def __init__(self, title, link, description, language='en', author=None):
        self.title = title
        self.link = link
        self.description = description
        self.language = language
        self.author = author
        self.entries = []
        self.last_build_date = datetime.now(timezone.utc)
        self.stylesheet_url = '/feed-style.xsl'
    
    def add_entry(self, entry):
        """Add a FeedEntry to the feed."""
        self.entries.append(entry)
    
    def add_item(self, title, link, description, pub_date=None, guid=None, author=None):
        """Convenience method to add an entry directly."""
        entry = FeedEntry(title, link, description, pub_date, guid, author)
        self.entries.append(entry)
        return entry
    
    def _format_rfc822_date(self, dt):
        """Format datetime as RFC 822 for RSS 2.0."""
        if isinstance(dt, str):
            return dt
        return dt.strftime('%a, %d %b %Y %H:%M:%S +0000')
    
    def _format_iso8601_date(self, dt):
        """Format datetime as ISO 8601 for Atom."""
        if isinstance(dt, str):
            return dt
        return dt.isoformat()
    
    def _prettify_xml(self, elem, include_declaration=True):
        """Return a pretty-printed XML string."""
        rough_string = ET.tostring(elem, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        pretty = reparsed.toprettyxml(indent="  ", encoding=None)
        # Remove extra blank lines
        lines = [line for line in pretty.split('\n') if line.strip()]
        if include_declaration:
            return '\n'.join(lines)
        else:
            # Skip XML declaration
            return '\n'.join(lines[1:])
    
    def generate_rss2(self, include_stylesheet=True):
        """
        Generate RSS 2.0 feed.
        Returns XML string with optional XSL stylesheet reference.
        """
        # Build XML manually to include processing instruction
        lines = ['<?xml version="1.0" encoding="UTF-8"?>']
        
        if include_stylesheet:
            lines.append(f'<?xml-stylesheet type="text/xsl" href="{self.stylesheet_url}"?>')
        
        rss = ET.Element('rss', {
            'version': '2.0',
            'xmlns:atom': 'http://www.w3.org/2005/Atom',
            'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
        })
        
        channel = ET.SubElement(rss, 'channel')
        ET.SubElement(channel, 'title').text = self.title
        ET.SubElement(channel, 'link').text = self.link
        ET.SubElement(channel, 'description').text = self.description
        ET.SubElement(channel, 'language').text = self.language
        ET.SubElement(channel, 'lastBuildDate').text = self._format_rfc822_date(self.last_build_date)
        ET.SubElement(channel, 'generator').text = 'MultiFeedGenerator v1.0'
        ET.SubElement(channel, 'docs').text = 'http://www.rssboard.org/rss-specification'
        
        # Atom self link
        atom_link = ET.SubElement(channel, '{http://www.w3.org/2005/Atom}link')
        atom_link.set('href', self.link.rstrip('/') + '/feed.xml')
        atom_link.set('rel', 'self')
        atom_link.set('type', 'application/rss+xml')
        
        for entry in self.entries:
            item = ET.SubElement(channel, 'item')
            ET.SubElement(item, 'title').text = entry.title
            ET.SubElement(item, 'link').text = entry.link
            ET.SubElement(item, 'description').text = entry.description
            guid = ET.SubElement(item, 'guid')
            guid.text = entry.guid
            guid.set('isPermaLink', 'false')
            ET.SubElement(item, 'pubDate').text = self._format_rfc822_date(entry.pub_date)
        
        # Pretty print and prepend declarations
        rough_string = ET.tostring(rss, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        xml_content = reparsed.toprettyxml(indent="  ", encoding=None)
        # Remove the XML declaration from minidom output (we add our own)
        xml_lines = xml_content.split('\n')
        xml_body = '\n'.join(line for line in xml_lines[1:] if line.strip())
        
        lines.append(xml_body)
        return '\n'.join(lines)
    
    def generate_rss1(self, include_stylesheet=True):
        """
        Generate RSS 1.0 (RDF) feed.
        """
        RDF_NS = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
        RSS_NS = 'http://purl.org/rss/1.0/'
        DC_NS = 'http://purl.org/dc/elements/1.1/'
        
        lines = ['<?xml version="1.0" encoding="UTF-8"?>']
        if include_stylesheet:
            lines.append(f'<?xml-stylesheet type="text/xsl" href="{self.stylesheet_url}"?>')
        
        # Register namespaces
        ET.register_namespace('rdf', RDF_NS)
        ET.register_namespace('', RSS_NS)
        ET.register_namespace('dc', DC_NS)
        
        rdf = ET.Element(f'{{{RDF_NS}}}RDF', {
            f'xmlns': RSS_NS,
            f'xmlns:rdf': RDF_NS,
            f'xmlns:dc': DC_NS
        })
        
        # Channel
        channel = ET.SubElement(rdf, 'channel', {f'{{{RDF_NS}}}about': self.link})
        ET.SubElement(channel, 'title').text = self.title
        ET.SubElement(channel, 'link').text = self.link
        ET.SubElement(channel, 'description').text = self.description
        ET.SubElement(channel, f'{{{DC_NS}}}language').text = self.language
        ET.SubElement(channel, f'{{{DC_NS}}}date').text = self._format_iso8601_date(self.last_build_date)
        
        # Items sequence
        items_seq = ET.SubElement(ET.SubElement(channel, 'items'), f'{{{RDF_NS}}}Seq')
        for entry in self.entries:
            li = ET.SubElement(items_seq, f'{{{RDF_NS}}}li')
            li.set(f'{{{RDF_NS}}}resource', entry.link)
        
        # Item elements
        for entry in self.entries:
            item = ET.SubElement(rdf, 'item', {f'{{{RDF_NS}}}about': entry.link})
            ET.SubElement(item, 'title').text = entry.title
            ET.SubElement(item, 'link').text = entry.link
            ET.SubElement(item, 'description').text = entry.description
            ET.SubElement(item, f'{{{DC_NS}}}date').text = self._format_iso8601_date(entry.pub_date)
        
        rough_string = ET.tostring(rdf, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        xml_content = reparsed.toprettyxml(indent="  ", encoding=None)
        xml_lines = xml_content.split('\n')
        xml_body = '\n'.join(line for line in xml_lines[1:] if line.strip())
        
        lines.append(xml_body)
        return '\n'.join(lines)
    
    def generate_atom(self, include_stylesheet=True):
        """
        Generate Atom 1.0 feed.
        """
        ATOM_NS = 'http://www.w3.org/2005/Atom'
        
        lines = ['<?xml version="1.0" encoding="UTF-8"?>']
        if include_stylesheet:
            lines.append(f'<?xml-stylesheet type="text/xsl" href="{self.stylesheet_url}"?>')
        
        ET.register_namespace('', ATOM_NS)
        
        feed = ET.Element('feed', {'xmlns': ATOM_NS})
        
        ET.SubElement(feed, 'title').text = self.title
        ET.SubElement(feed, 'subtitle').text = self.description
        
        link_alt = ET.SubElement(feed, 'link')
        link_alt.set('href', self.link)
        link_alt.set('rel', 'alternate')
        
        link_self = ET.SubElement(feed, 'link')
        link_self.set('href', self.link.rstrip('/') + '/feed.atom')
        link_self.set('rel', 'self')
        link_self.set('type', 'application/atom+xml')
        
        ET.SubElement(feed, 'id').text = self.link
        ET.SubElement(feed, 'updated').text = self._format_iso8601_date(self.last_build_date)
        ET.SubElement(feed, 'generator').text = 'MultiFeedGenerator v1.0'
        
        if self.author:
            author_elem = ET.SubElement(feed, 'author')
            ET.SubElement(author_elem, 'name').text = self.author
        
        for entry in self.entries:
            entry_elem = ET.SubElement(feed, 'entry')
            ET.SubElement(entry_elem, 'title').text = entry.title
            
            link = ET.SubElement(entry_elem, 'link')
            link.set('href', entry.link)
            link.set('rel', 'alternate')
            
            ET.SubElement(entry_elem, 'id').text = f'urn:uuid:{entry.guid}'
            ET.SubElement(entry_elem, 'published').text = self._format_iso8601_date(entry.pub_date)
            ET.SubElement(entry_elem, 'updated').text = self._format_iso8601_date(entry.pub_date)
            
            summary = ET.SubElement(entry_elem, 'summary')
            summary.set('type', 'text')
            summary.text = entry.description
            
            if entry.author:
                author_elem = ET.SubElement(entry_elem, 'author')
                ET.SubElement(author_elem, 'name').text = entry.author
        
        rough_string = ET.tostring(feed, encoding='unicode')
        reparsed = minidom.parseString(rough_string)
        xml_content = reparsed.toprettyxml(indent="  ", encoding=None)
        xml_lines = xml_content.split('\n')
        xml_body = '\n'.join(line for line in xml_lines[1:] if line.strip())
        
        lines.append(xml_body)
        return '\n'.join(lines)
    
    def generate_json_feed(self):
        """
        Generate JSON Feed 1.1.
        https://jsonfeed.org/version/1.1
        """
        feed = {
            'version': 'https://jsonfeed.org/version/1.1',
            'title': self.title,
            'home_page_url': self.link,
            'feed_url': self.link.rstrip('/') + '/feed.json',
            'description': self.description,
            'language': self.language,
            'items': []
        }
        
        if self.author:
            feed['authors'] = [{'name': self.author}]
        
        for entry in self.entries:
            item = {
                'id': entry.guid,
                'url': entry.link,
                'title': entry.title,
                'content_text': entry.description,
                'date_published': self._format_iso8601_date(entry.pub_date)
            }
            if entry.author:
                item['authors'] = [{'name': entry.author}]
            feed['items'].append(item)
        
        return json.dumps(feed, indent=2, ensure_ascii=False)
    
    def write_all_formats(self, base_filename, include_stylesheet=True):
        """
        Write feed in all supported formats.
        
        Args:
            base_filename: Base name without extension (e.g., 'ai_rss_feed')
            include_stylesheet: Whether to include XSL stylesheet reference
        
        Returns:
            dict: Mapping of format name to filename
        """
        files_written = {}
        
        # RSS 2.0
        rss2_file = f'{base_filename}.xml'
        with open(rss2_file, 'w', encoding='utf-8') as f:
            f.write(self.generate_rss2(include_stylesheet))
        files_written['rss2'] = rss2_file
        
        # RSS 1.0
        rss1_file = f'{base_filename}_rss1.xml'
        with open(rss1_file, 'w', encoding='utf-8') as f:
            f.write(self.generate_rss1(include_stylesheet))
        files_written['rss1'] = rss1_file
        
        # Atom
        atom_file = f'{base_filename}.atom'
        with open(atom_file, 'w', encoding='utf-8') as f:
            f.write(self.generate_atom(include_stylesheet))
        files_written['atom'] = atom_file
        
        # JSON Feed
        json_file = f'{base_filename}.json'
        with open(json_file, 'w', encoding='utf-8') as f:
            f.write(self.generate_json_feed())
        files_written['json'] = json_file
        
        return files_written


# Convenience function for backward compatibility
def create_multi_format_feed(title, link, description, entries, base_filename, 
                              language='en', author=None, include_stylesheet=True):
    """
    Create feeds in all formats from a list of entry dictionaries.
    
    Args:
        title: Feed title
        link: Feed link
        description: Feed description
        entries: List of dicts with keys: title, link, description, pub_date (optional), guid (optional)
        base_filename: Base filename without extension
        language: Feed language (default: 'en')
        author: Feed author (optional)
        include_stylesheet: Whether to include XSL stylesheet
    
    Returns:
        dict: Mapping of format name to filename
    """
    generator = MultiFeedGenerator(title, link, description, language, author)
    
    for entry_data in entries:
        generator.add_item(
            title=entry_data.get('title', ''),
            link=entry_data.get('link', ''),
            description=entry_data.get('description', ''),
            pub_date=entry_data.get('pub_date'),
            guid=entry_data.get('guid'),
            author=entry_data.get('author')
        )
    
    return generator.write_all_formats(base_filename, include_stylesheet)


if __name__ == '__main__':
    # Test the generator
    gen = MultiFeedGenerator(
        title="Test Feed",
        link="https://example.com",
        description="A test feed",
        author="Test Author"
    )
    
    gen.add_item(
        title="Test Article [ ! ]",
        link="https://example.com/article1",
        description="This is a test article description.",
        pub_date=datetime.now(timezone.utc)
    )
    
    gen.add_item(
        title="Another Article [ * ]",
        link="https://example.com/article2",
        description="Another test description.",
        pub_date=datetime.now(timezone.utc)
    )
    
    print("RSS 2.0:")
    print(gen.generate_rss2()[:500], "...")
    print("\nAtom:")
    print(gen.generate_atom()[:500], "...")
    print("\nJSON Feed:")
    print(gen.generate_json_feed()[:500], "...")
