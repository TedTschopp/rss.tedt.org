from pathlib import Path
import yaml

from .text_utils import stable_id


def _load_sources_payload(path: str) -> dict:
    file_path = Path(path)
    if not file_path.exists():
        return {}

    with file_path.open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle) or {}

    return payload if isinstance(payload, dict) else {}


def _from_sources_yaml(path: str) -> list[dict]:
    payload = _load_sources_payload(path)
    sources = payload.get("sources", [])
    normalized = []
    for source in sources:
        if not isinstance(source, dict):
            continue
        source_id = source.get("id") or stable_id("src", source.get("url", source.get("name", "unknown")))
        normalized.append(
            {
                "id": source_id,
                "type": source.get("type", "rss"),
                "name": source.get("name", source_id),
                "url": source.get("url", ""),
                "category": source.get("category", source.get("type", "rss")),
                "authority_weight": float(source.get("authority_weight", 0.5)),
                "enabled": source.get("enabled", True),
            }
        )

    return [source for source in normalized if source.get("enabled") and source.get("url")]


def load_pipeline_settings(path: str = "sources.yml") -> dict:
    payload = _load_sources_payload(path)
    ranking = payload.get("ranking", {})
    if not isinstance(ranking, dict):
        return {}

    weights = ranking.get("weights", {})
    if not isinstance(weights, dict):
        weights = {}

    settings = {}

    half_life_hours = ranking.get("half_life_hours")
    if half_life_hours is not None:
        settings["half_life_hours"] = float(half_life_hours)

    mapping = {
        "authority": "score_weight_authority",
        "freshness": "score_weight_freshness",
        "engagement": "score_weight_engagement",
        "velocity": "score_weight_velocity",
        "coverage": "score_weight_coverage",
        "novelty_penalty": "score_weight_novelty_penalty",
    }
    for source_key, setting_key in mapping.items():
        value = weights.get(source_key)
        if value is not None:
            settings[setting_key] = float(value)

    return settings


def _from_jekyll_config(path: str) -> list[dict]:
    file_path = Path(path)
    if not file_path.exists():
        return []

    with file_path.open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle) or {}

    feeds = payload.get("feeds", [])
    sources = []
    for feed in feeds:
        if not isinstance(feed, dict) or not feed.get("aggregated"):
            continue
        if feed.get("enabled") is False:
            continue
        for feed_url in feed.get("sources", []):
            source_id = stable_id("rss", feed_url)
            sources.append(
                {
                    "id": source_id,
                    "type": "rss",
                    "name": feed.get("name", source_id),
                    "url": feed_url,
                    "category": feed.get("key", "rss"),
                    "authority_weight": 0.55,
                    "enabled": True,
                }
            )

    unique = {}
    for source in sources:
        unique[source["id"]] = source
    return list(unique.values())


def load_sources(sources_file: str = "sources.yml", jekyll_file: str = "_config.yml") -> list[dict]:
    sources = _from_sources_yaml(sources_file)
    if sources:
        return sources
    return _from_jekyll_config(jekyll_file)
