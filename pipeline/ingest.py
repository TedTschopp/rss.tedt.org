import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET
from typing import Any, cast

import requests

from .constants import DEFAULT_PIPELINE_CONFIG
from .text_utils import normalize_text, parse_datetime, to_iso


def _as_str(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def _as_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return default


def _classify_error(status_code: int | None, error_text: str | None) -> str:
    if status_code is not None and 400 <= status_code < 500:
        return "http_4xx"
    if status_code is not None and status_code >= 500:
        return "http_5xx"
    if not error_text:
        return "unknown"
    message = error_text.lower()
    if "name or service not known" in message or "temporary failure" in message:
        return "dns_error"
    if "ssl" in message or "certificate" in message:
        return "ssl_error"
    if "timed out" in message:
        return "timeout"
    if "xml" in message or "parse" in message:
        return "parse_error"
    return "network_error"


def _parse_rss_items(xml_text: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    root = ET.fromstring(xml_text)

    channels = root.findall(".//channel")
    if channels:
        for node in root.findall(".//item"):
            items.append(
                {
                    "title": normalize_text(node.findtext("title", "")),
                    "url": normalize_text(node.findtext("link", "")),
                    "summary": normalize_text(node.findtext("description", "")),
                    "published": node.findtext("pubDate", "") or node.findtext("published", "") or "",
                    "author": normalize_text(node.findtext("author", "")),
                    "categories": [c.text for c in node.findall("category") if c.text],
                    "raw_type": "rss",
                }
            )
        return items

    for node in root.findall(".//{http://www.w3.org/2005/Atom}entry"):
        link = ""
        for link_node in node.findall("{http://www.w3.org/2005/Atom}link"):
            href = link_node.attrib.get("href")
            rel = link_node.attrib.get("rel", "alternate")
            if href and rel == "alternate":
                link = href
                break
        if not link:
            id_node = node.findtext("{http://www.w3.org/2005/Atom}id", "")
            link = id_node

        items.append(
            {
                "title": normalize_text(node.findtext("{http://www.w3.org/2005/Atom}title", "")),
                "url": normalize_text(link),
                "summary": normalize_text(
                    node.findtext("{http://www.w3.org/2005/Atom}summary", "")
                    or node.findtext("{http://www.w3.org/2005/Atom}content", "")
                ),
                "published": node.findtext("{http://www.w3.org/2005/Atom}published", "")
                or node.findtext("{http://www.w3.org/2005/Atom}updated", ""),
                "author": normalize_text(node.findtext("{http://www.w3.org/2005/Atom}author/{http://www.w3.org/2005/Atom}name", "")),
                "categories": [],
                "raw_type": "atom",
            }
        )
    return items


def _parse_hn_items(payload: dict[str, Any]) -> list[dict[str, Any]]:
    hits = payload.get("hits", [])
    items: list[dict[str, Any]] = []
    for hit in hits:
        if not isinstance(hit, dict):
            continue
        hit_map = cast(dict[str, Any], hit)
        title = _as_str(hit_map.get("title") or hit_map.get("story_title") or "")
        object_id = _as_str(hit_map.get("objectID", ""))
        url = _as_str(hit_map.get("url") or hit_map.get("story_url") or f"https://news.ycombinator.com/item?id={object_id}")
        discussion_url = f"https://news.ycombinator.com/item?id={object_id}" if object_id else ""
        items.append(
            {
                "title": normalize_text(title),
                "url": normalize_text(url),
            "discussion_url": discussion_url,
                "summary": "",
                "published": _as_str(hit_map.get("created_at", "")),
                "upvotes": _as_int(hit_map.get("points", 0)),
                "comments": _as_int(hit_map.get("num_comments", 0)),
                "author": normalize_text(_as_str(hit_map.get("author", ""))),
                "hn_item_id": object_id,
                "raw_type": "hackernews",
            }
        )
    return items


def _parse_reddit_items(payload: dict[str, Any]) -> list[dict[str, Any]]:
    root_data = payload.get("data", {})
    children: list[Any] = []
    if isinstance(root_data, dict):
        root_map = cast(dict[str, Any], root_data)
        maybe_children = root_map.get("children", [])
        if isinstance(maybe_children, list):
            children = cast(list[Any], maybe_children)

    items: list[dict[str, Any]] = []
    for child in children:
        if not isinstance(child, dict):
            continue
        child_map = cast(dict[str, Any], child)
        data = child_map.get("data", {})
        if not isinstance(data, dict):
            continue
        data_map = cast(dict[str, Any], data)
        permalink = _as_str(data_map.get("permalink", ""))
        url = _as_str(data_map.get("url_overridden_by_dest") or data_map.get("url") or (f"https://www.reddit.com{permalink}" if permalink else ""))
        discussion_url = f"https://www.reddit.com{permalink}" if permalink else ""
        created_utc = data_map.get("created_utc")
        published = ""
        if created_utc is not None:
            published = datetime.fromtimestamp(float(created_utc), tz=timezone.utc).isoformat().replace("+00:00", "Z")

        items.append(
            {
                "title": normalize_text(_as_str(data_map.get("title", ""))),
                "url": normalize_text(url),
                "discussion_url": discussion_url,
                "summary": normalize_text(_as_str(data_map.get("selftext", "")))[:700],
                "published": published,
                "upvotes": _as_int(data_map.get("ups", data_map.get("score", 0))),
                "comments": _as_int(data_map.get("num_comments", 0)),
                "subreddit": _as_str(data_map.get("subreddit", "")),
                "author": normalize_text(_as_str(data_map.get("author", ""))),
                "reddit_post_id": _as_str(data_map.get("id", "")),
                "raw_type": "reddit",
            }
        )
    return items


def _parse_source_items(source_type: str, text_body: str, json_payload: dict[str, Any] | None) -> list[dict[str, Any]]:
    if source_type in {"rss", "arxiv", "labs"}:
        return _parse_rss_items(text_body)
    if source_type == "hackernews":
        return _parse_hn_items(json_payload or {})
    if source_type == "reddit":
        return _parse_reddit_items(json_payload or {})
    return []


def _get_source_response(session: requests.Session, url: str, timeout: int, headers: dict[str, str]) -> requests.Response:
    response = session.get(url, timeout=timeout, headers=headers)
    if response.status_code != 403:
        return response

    try:
        session.head(url, timeout=timeout, headers=headers, allow_redirects=True)
        return session.get(url, timeout=timeout, headers=headers)
    except Exception:
        return response


def _fetch_source_worker(
    source: dict[str, Any],
    state: dict[str, Any],
    session: requests.Session,
    timeout: int,
    raw_daily_dir: Path,
    cfg: dict[str, Any],
) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    """Worker function for parallel source fetching."""
    source_id = source["id"]
    source_state = state.get(source_id, {})
    headers: dict[str, str] = {}
    if source_state.get("etag"):
        headers["If-None-Match"] = source_state["etag"]
    if source_state.get("last_modified"):
        headers["If-Modified-Since"] = source_state["last_modified"]

    if source.get("type") == "reddit":
        headers["User-Agent"] = str(cfg.get("reddit_user_agent", "rss.tedt.org-bot/1.0"))

    started = time.perf_counter()
    fetched_at = to_iso(datetime.now(timezone.utc))
    status_code = None
    error = ""
    parsed = []
    raw_items: list[dict[str, Any]] = []

    try:
        response = _get_source_response(session, source["url"], timeout, headers)
        status_code = response.status_code
        response.raise_for_status()
        content_type = (response.headers.get("content-type") or "").lower()

        if status_code == 304:
            parsed = []
        else:
            text_body = response.text
            payload: dict[str, Any] | None = response.json() if "json" in content_type else None
            parsed = _parse_source_items(source.get("type", "rss"), text_body, payload)
            snapshot: dict[str, Any] = {
                "source": source,
                "fetched_at": fetched_at,
                "item_count": len(parsed),
                "items": parsed,
            }
            with (raw_daily_dir / f"{source_id}.json").open("w", encoding="utf-8") as handle:
                json.dump(snapshot, handle, indent=2, ensure_ascii=False)

        state_update = {
            "etag": response.headers.get("etag"),
            "last_modified": response.headers.get("last-modified"),
            "consecutive_failures": 0,
            "last_success_ts": fetched_at,
            "last_status": status_code,
        }

    except Exception as exc:
        error = str(exc)
        prev_failures = int(source_state.get("consecutive_failures", 0))
        state_update = {
            **source_state,
            "consecutive_failures": prev_failures + 1,
            "last_error": error,
            "last_status": status_code,
        }

    latency_ms = int((time.perf_counter() - started) * 1000)
    fetch_row = {
        "fetch_id": f"{source_id}_{fetched_at}",
        "source_id": source_id,
        "source_type": source.get("type"),
        "fetched_at": fetched_at,
        "http_status": status_code,
        "latency_ms": latency_ms,
        "item_count": len(parsed),
        "error": error,
        "error_class": _classify_error(status_code, error),
    }

    for item in parsed:
        published_dt = parse_datetime(item.get("published", ""))
        raw_items.append(
            {
                "source_id": source_id,
                "source_name": source.get("name"),
                "source_type": source.get("type"),
                "source_category": source.get("category"),
                "authority_weight": source.get("authority_weight", 0.5),
                "fetched_at": fetched_at,
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "discussion_url": item.get("discussion_url", ""),
                "summary": item.get("summary", ""),
                "author": item.get("author", ""),
                "published": to_iso(published_dt) if published_dt else item.get("published", ""),
                "upvotes": item.get("upvotes"),
                "comments": item.get("comments"),
                "raw_fields": item,
            }
        )

    return fetch_row, raw_items, (source_id, state_update)



def run_ingestion(
    sources: list[dict[str, Any]],
    state: dict[str, Any],
    raw_dir: str,
    config: dict[str, Any] | None = None,
):
    cfg = {**DEFAULT_PIPELINE_CONFIG, **(config or {})}
    timeout = int(cfg.get("request_timeout_sec", 25))

    fetch_rows: list[dict[str, Any]] = []
    raw_items: list[dict[str, Any]] = []
    next_state: dict[str, Any] = dict(state)
    run_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    raw_daily_dir = Path(raw_dir) / run_date
    raw_daily_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": str(cfg.get("user_agent", "rss.tedt.org-pipeline/1.0"))})

    # Parallel source fetching with ThreadPoolExecutor
    max_workers = min(5, len(sources))  # Use up to 5 concurrent workers
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(_fetch_source_worker, source, next_state, session, timeout, raw_daily_dir, cfg): source
            for source in sources
        }

        for future in as_completed(futures):
            try:
                fetch_row, items, (source_id, state_update) = future.result()
                fetch_rows.append(fetch_row)
                raw_items.extend(items)
                next_state[source_id] = state_update
            except Exception as exc:
                source = futures[future]
                source_id = source["id"]
                error = str(exc)
                prev_failures = int(next_state.get(source_id, {}).get("consecutive_failures", 0))
                next_state[source_id] = {
                    **next_state.get(source_id, {}),
                    "consecutive_failures": prev_failures + 1,
                    "last_error": error,
                }
                fetch_rows.append({
                    "fetch_id": f"{source_id}_{to_iso(datetime.now(timezone.utc))}",
                    "source_id": source_id,
                    "source_type": source.get("type"),
                    "fetched_at": to_iso(datetime.now(timezone.utc)),
                    "http_status": None,
                    "latency_ms": 0,
                    "item_count": 0,
                    "error": error,
                    "error_class": _classify_error(None, error),
                })

    return raw_items, fetch_rows, next_state
