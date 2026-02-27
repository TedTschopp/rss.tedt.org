from collections import defaultdict

from .text_utils import story_fingerprint, stable_id


def dedupe_to_stories(items: list[dict]) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)

    for item in items:
        if item.get("canonical_url"):
            key = f"url::{item['canonical_url']}"
        else:
            key = f"fp::{story_fingerprint(item.get('title', ''), item.get('domain', ''), item.get('published', '')[:10])}"
        grouped[key].append(item)

    stories = []
    for key, group in grouped.items():
        sorted_group = sorted(group, key=lambda entry: entry.get("published", ""), reverse=True)
        representative = sorted_group[0]
        first_seen = min(entry.get("fetched_at", "") for entry in group)
        last_seen = max(entry.get("fetched_at", "") for entry in group)
        mentions = []
        for entry in group:
            mentions.append(
                {
                    "item_id": entry.get("item_id"),
                    "source_id": entry.get("source_id"),
                    "source_name": entry.get("source_name"),
                    "source_type": entry.get("source_type"),
                    "published": entry.get("published"),
                    "upvotes": entry.get("upvotes"),
                    "comments": entry.get("comments"),
                }
            )

        story_id = stable_id("sty", key)
        stories.append(
            {
                "story_id": story_id,
                "canonical_url": representative.get("canonical_url") or representative.get("url"),
                "url": representative.get("url"),
                "title": representative.get("title"),
                "summary": representative.get("summary", ""),
                "published": representative.get("published"),
                "first_seen_at": first_seen,
                "last_seen_at": last_seen,
                "primary_source_id": representative.get("source_id"),
                "source_name": representative.get("source_name"),
                "source_type": representative.get("source_type"),
                "authority_weight": representative.get("authority_weight", 0.5),
                "domain": representative.get("domain", ""),
                "mentions": mentions,
            }
        )

    return sorted(stories, key=lambda story: story.get("published", ""), reverse=True)
