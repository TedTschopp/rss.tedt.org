from datetime import datetime, timezone
import re
from typing import Any

from feed_generator import MultiFeedGenerator

from .constants import DEFAULT_PIPELINE_CONFIG
from .io_utils import write_json


def _is_ai_story(story: dict[str, Any], ai_keywords: list[str]) -> bool:
    def keyword_match(text: str) -> bool:
        lowered_text = text.lower()
        for keyword in ai_keywords:
            escaped = re.escape(keyword)
            if re.search(rf"(?<![a-z0-9]){escaped}(?![a-z0-9])", lowered_text):
                return True
        return False

    llm_topics = story.get("llm", {}).get("topics", []) if isinstance(story.get("llm"), dict) else []
    if isinstance(llm_topics, list):
        if any(keyword_match(str(topic)) for topic in llm_topics):
            return True

    title = str(story.get("title", "")).lower()
    summary = str(story.get("summary", "")).lower()
    domain = str(story.get("domain", "")).lower()
    haystack = f"{title}\n{summary}\n{domain}"
    return keyword_match(haystack)


def _to_feed_entry(story: dict) -> dict:
    return {
        "title": story.get("title", ""),
        "link": story.get("canonical_url") or story.get("url", ""),
        "description": story.get("llm", {}).get("summary") or story.get("summary", ""),
        "pub_date": story.get("published"),
        "guid": story.get("story_id"),
    }


def publish_outputs(ranked_stories: list[dict], api_path: str, base_feed_path: str, config: dict | None = None):
    cfg = {**DEFAULT_PIPELINE_CONFIG, **(config or {})}
    publish_top_n = int(cfg.get("publish_top_n", 200))
    ai_keywords = [str(keyword).lower() for keyword in cfg.get("ai_keywords", [])]
    ai_only_stories = [story for story in ranked_stories if _is_ai_story(story, ai_keywords)]
    top_stories = ai_only_stories[:publish_top_n]

    payload = {
        "schema_version": cfg.get("schema_version", "1.0.0"),
        "generated": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "count": len(top_stories),
        "items": [
            {
                "title": story.get("title"),
                "url": story.get("canonical_url") or story.get("url"),
                "source": story.get("source_name"),
                "sourceType": story.get("source_type"),
                "published": story.get("published"),
                "summary": story.get("llm", {}).get("summary") or story.get("summary"),
                "score": story.get("score"),
                "upvotes": sum(int(m.get("upvotes") or 0) for m in story.get("mentions", [])) or None,
                "comments": sum(int(m.get("comments") or 0) for m in story.get("mentions", [])) or None,
                "clusterId": story.get("cluster_id"),
            }
            for story in top_stories
        ],
    }
    write_json(api_path, payload)

    feed = MultiFeedGenerator(
        title="TedTschopp News Graph - Top Stories",
        link="https://rss.tedt.org/feeds/top.xml",
        description="Natural20-style ranked stories across configured sources",
    )

    for story in top_stories:
        feed.add_item(**_to_feed_entry(story))

    feed.write_all_formats(base_feed_path)
    return payload
