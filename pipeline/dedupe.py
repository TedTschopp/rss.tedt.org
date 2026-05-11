from collections import defaultdict
import re
from typing import Any

from .text_utils import normalize_text, stable_id


SOCIAL_SOURCE_CATEGORIES = {"hn", "reddit"}
SOCIAL_SOURCE_TYPES = {"hackernews", "reddit"}
SOCIAL_DOMAINS = {
    "news.ycombinator.com",
    "hnrss.org",
    "reddit.com",
    "www.reddit.com",
    "old.reddit.com",
    "redd.it",
}

SOURCE_TYPE_PRIORITY = {
    "labs": 50,
    "arxiv": 45,
    "rss": 35,
    "hackernews": 15,
    "reddit": 10,
}

SOURCE_CATEGORY_PRIORITY = {
    "labs": 50,
    "papers": 45,
    "rss": 35,
    "ea": 34,
    "people": 33,
    "commentary": 30,
    "hn": 15,
    "reddit": 10,
}


def _as_text(value: Any) -> str:
    return str(value or "").strip()


def _title_key(title: str) -> str:
    normalized = normalize_text(title).lower()
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    return normalize_text(normalized)


def _published_day(item: dict[str, Any]) -> str:
    published = _as_text(item.get("published"))
    return published[:10] if len(published) >= 10 else ""


def _dedupe_keys(item: dict[str, Any]) -> list[str]:
    keys: list[str] = []
    canonical_url = _as_text(item.get("canonical_url"))
    if canonical_url:
        keys.append(f"url::{canonical_url}")

    title_key = _title_key(_as_text(item.get("title")))
    day = _published_day(item)
    if title_key and day:
        keys.append(f"title_day::{title_key}::{day}")
    elif title_key and not canonical_url:
        keys.append(f"title::{title_key}")

    if not keys:
        keys.append(f"item::{_as_text(item.get('item_id')) or id(item)}")
    return keys


def _find(parents: dict[str, str], node: str) -> str:
    root = node
    while parents[root] != root:
        root = parents[root]
    while node != root:
        parent = parents[node]
        parents[node] = root
        node = parent
    return root


def _union(parents: dict[str, str], left: str, right: str) -> None:
    if left not in parents:
        parents[left] = left
    if right not in parents:
        parents[right] = right
    left_root = _find(parents, left)
    right_root = _find(parents, right)
    if left_root != right_root:
        parents[right_root] = left_root


def _source_priority(entry: dict[str, Any]) -> int:
    source_type = _as_text(entry.get("source_type")).lower()
    source_category = _as_text(entry.get("source_category")).lower()
    type_priority = SOURCE_TYPE_PRIORITY.get(source_type, 25)
    category_priority = SOURCE_CATEGORY_PRIORITY.get(source_category, type_priority)
    priority = min(type_priority, category_priority)
    domain = _as_text(entry.get("domain")).lower()
    if source_type in SOCIAL_SOURCE_TYPES or source_category in SOCIAL_SOURCE_CATEGORIES:
        priority -= 20
    if domain in SOCIAL_DOMAINS:
        priority -= 10
    return priority


def _primary_sort_key(entry: dict[str, Any]) -> tuple[int, float, int, str, str]:
    try:
        authority = float(entry.get("authority_weight", 0.5) or 0.5)
    except Exception:
        authority = 0.5
    has_summary = 1 if _as_text(entry.get("summary")) else 0
    return (
        _source_priority(entry),
        authority,
        has_summary,
        _as_text(entry.get("published")),
        _as_text(entry.get("fetched_at")),
    )


def _sorted_group(group: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(group, key=_primary_sort_key, reverse=True)


def _mention(entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "item_id": entry.get("item_id"),
        "source_id": entry.get("source_id"),
        "source_name": entry.get("source_name"),
        "source_type": entry.get("source_type"),
        "source_category": entry.get("source_category"),
        "authority_weight": entry.get("authority_weight"),
        "title": entry.get("title"),
        "url": entry.get("url"),
        "canonical_url": entry.get("canonical_url"),
        "discussion_url": entry.get("discussion_url"),
        "domain": entry.get("domain"),
        "published": entry.get("published"),
        "upvotes": entry.get("upvotes"),
        "comments": entry.get("comments"),
    }


def _source_row(entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "source_id": entry.get("source_id"),
        "source_name": entry.get("source_name"),
        "source_type": entry.get("source_type"),
        "source_category": entry.get("source_category"),
        "authority_weight": entry.get("authority_weight"),
        "url": entry.get("url"),
        "canonical_url": entry.get("canonical_url"),
        "discussion_url": entry.get("discussion_url"),
        "domain": entry.get("domain"),
        "published": entry.get("published"),
        "upvotes": entry.get("upvotes"),
        "comments": entry.get("comments"),
    }


def _alternate_link(entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "url": entry.get("url"),
        "canonical_url": entry.get("canonical_url"),
        "discussion_url": entry.get("discussion_url"),
        "source_id": entry.get("source_id"),
        "source_name": entry.get("source_name"),
        "source_type": entry.get("source_type"),
        "source_category": entry.get("source_category"),
        "domain": entry.get("domain"),
    }


def _unique_sources(group: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_source: dict[str, dict[str, Any]] = {}
    for entry in _sorted_group(group):
        source_id = _as_text(entry.get("source_id"))
        if source_id and source_id not in by_source:
            by_source[source_id] = _source_row(entry)
    return list(by_source.values())


def _unique_alternate_links(group: list[dict[str, Any]]) -> list[dict[str, Any]]:
    links: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for entry in _sorted_group(group):
        row = _alternate_link(entry)
        key = (_as_text(row.get("source_id")), _as_text(row.get("url")), _as_text(row.get("discussion_url")))
        if key in seen:
            continue
        seen.add(key)
        links.append(row)
    return links


def _story_identity(representative: dict[str, Any], group: list[dict[str, Any]]) -> str:
    canonical_url = _as_text(representative.get("canonical_url")) or _as_text(representative.get("url"))
    if canonical_url:
        return f"url::{canonical_url}"
    title_key = _title_key(_as_text(representative.get("title")))
    day = _published_day(representative)
    if title_key and day:
        return f"title_day::{title_key}::{day}"
    return "|".join(sorted(_as_text(entry.get("item_id")) for entry in group))


def _group_items(items: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    parents: dict[str, str] = {}
    item_nodes: list[str] = []

    for index, item in enumerate(items):
        item_node = f"item::{index}"
        parents[item_node] = item_node
        item_nodes.append(item_node)
        for key in _dedupe_keys(item):
            _union(parents, item_node, f"key::{key}")

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item_node, item in zip(item_nodes, items):
        grouped[_find(parents, item_node)].append(item)
    return list(grouped.values())


def dedupe_to_stories(items: list[dict]) -> list[dict]:
    typed_items = [dict(item) for item in items]
    stories: list[dict[str, Any]] = []

    for group in _group_items(typed_items):
        sorted_group = _sorted_group(group)
        representative = sorted_group[0]
        first_seen = min((_as_text(entry.get("fetched_at")) for entry in group if _as_text(entry.get("fetched_at"))), default="")
        last_seen = max((_as_text(entry.get("fetched_at")) for entry in group if _as_text(entry.get("fetched_at"))), default="")
        mentions = [_mention(entry) for entry in sorted_group]
        sources = _unique_sources(group)
        alternate_links = _unique_alternate_links(group)
        source_ids = {_as_text(entry.get("source_id")) for entry in group if _as_text(entry.get("source_id"))}
        story_key = _story_identity(representative, group)

        primary_source = _source_row(representative)
        stories.append(
            {
                "story_id": stable_id("sty", story_key),
                "canonical_url": representative.get("canonical_url") or representative.get("url"),
                "url": representative.get("url"),
                "title": representative.get("title"),
                "summary": representative.get("summary", ""),
                "published": representative.get("published"),
                "first_seen_at": first_seen,
                "last_seen_at": last_seen,
                "primary_source_id": representative.get("source_id"),
                "primary_source": primary_source,
                "source_name": representative.get("source_name"),
                "source_type": representative.get("source_type"),
                "source_category": representative.get("source_category"),
                "authority_weight": representative.get("authority_weight", 0.5),
                "domain": representative.get("domain", ""),
                "is_duplicate": len(source_ids) > 1,
                "duplicate_count": max(0, len(group) - 1),
                "duplicate_source_count": len(source_ids),
                "sources": sources,
                "alternate_links": alternate_links,
                "mentions": mentions,
            }
        )

    return sorted(stories, key=lambda story: story.get("published", ""), reverse=True)