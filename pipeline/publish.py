from datetime import datetime, timezone

from feed_generator import MultiFeedGenerator

from .constants import DEFAULT_PIPELINE_CONFIG
from .io_utils import write_json


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
    top_stories = ranked_stories[:publish_top_n]

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
