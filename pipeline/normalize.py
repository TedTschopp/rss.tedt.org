from datetime import datetime, timezone
from urllib.parse import urlparse

from .text_utils import canonicalize_url, normalize_text, parse_datetime, stable_id, to_iso


def normalize_items(raw_items: list[dict]) -> list[dict]:
    normalized = []
    now_iso = to_iso(datetime.now(timezone.utc))

    for item in raw_items:
        canonical_url = canonicalize_url(item.get("url", ""))
        parsed_url = urlparse(canonical_url)
        domain = parsed_url.netloc.lower()
        title = normalize_text(item.get("title", ""))
        summary = normalize_text(item.get("summary", ""))
        published_dt = parse_datetime(item.get("published", ""))
        published = to_iso(published_dt) if published_dt else item.get("published", "") or now_iso

        identity = canonical_url or f"{title}|{domain}|{published[:10]}"
        item_id = stable_id("itm", identity)
        normalized.append(
            {
                "item_id": item_id,
                "source_id": item.get("source_id"),
                "source_name": item.get("source_name"),
                "source_type": item.get("source_type"),
                "source_category": item.get("source_category"),
                "authority_weight": float(item.get("authority_weight", 0.5)),
                "fetched_at": item.get("fetched_at"),
                "title": title,
                "url": item.get("url", ""),
                "canonical_url": canonical_url,
                "domain": domain,
                "summary": summary,
                "published": published,
                "upvotes": item.get("upvotes"),
                "comments": item.get("comments"),
                "raw_fields": item.get("raw_fields", {}),
            }
        )

    return [item for item in normalized if item.get("title") and (item.get("canonical_url") or item.get("url"))]
