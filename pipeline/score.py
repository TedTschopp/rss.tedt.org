import math
from datetime import datetime, timezone
from typing import Any

from .constants import DEFAULT_PIPELINE_CONFIG
from .text_utils import parse_datetime


def _freshness_score(published: str, half_life_hours: float) -> float:
    published_dt = parse_datetime(published)
    if not published_dt:
        return 0.2
    now = datetime.now(timezone.utc)
    age_hours = max(0.0, (now - published_dt).total_seconds() / 3600.0)
    return math.exp(-math.log(2) * age_hours / max(1e-6, half_life_hours))


def _engagement_score(story: dict[str, Any]) -> float:
    upvotes = 0
    comments = 0
    for mention in story.get("mentions", []):
        upvotes += max(0, int(mention.get("upvotes") or 0))
        comments += max(0, int(mention.get("comments") or 0))
    raw = math.log1p(upvotes) * 0.7 + math.log1p(comments) * 0.3
    return min(1.0, raw / 6.0)


def _coverage_score(story: dict[str, Any]) -> float:
    sources = {mention.get("source_id") for mention in story.get("mentions", []) if mention.get("source_id")}
    return min(1.0, len(sources) / 5.0)


def score_stories(
    stories: list[dict[str, Any]],
    cluster_map: dict[str, str],
    config: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    cfg = {**DEFAULT_PIPELINE_CONFIG, **(config or {})}
    half_life = float(cfg.get("half_life_hours", 36))
    authority_weight = float(cfg.get("score_weight_authority", 100.0))
    freshness_weight = float(cfg.get("score_weight_freshness", 120.0))
    engagement_weight = float(cfg.get("score_weight_engagement", 80.0))
    velocity_weight = float(cfg.get("score_weight_velocity", 40.0))
    coverage_weight = float(cfg.get("score_weight_coverage", 30.0))
    novelty_penalty_weight = float(cfg.get("score_weight_novelty_penalty", 50.0))

    for story in stories:
        authority = max(0.0, min(1.0, float(story.get("authority_weight", 0.5))))
        freshness = _freshness_score(story.get("published", ""), half_life)
        engagement = _engagement_score(story)
        coverage = _coverage_score(story)
        velocity = 0.0
        novelty_penalty = 0.0

        score = (
            authority_weight * authority
            + freshness_weight * freshness
            + engagement_weight * engagement
            + velocity_weight * velocity
            + coverage_weight * coverage
            - novelty_penalty_weight * novelty_penalty
        )

        story["cluster_id"] = cluster_map.get(story["story_id"])
        story["score_breakdown"] = {
            "authority_score": round(authority, 4),
            "freshness_score": round(freshness, 4),
            "engagement_score": round(engagement, 4),
            "coverage_score": round(coverage, 4),
            "velocity_score": round(velocity, 4),
            "novelty_penalty": round(novelty_penalty, 4),
        }
        story["score"] = round(score, 2)

    ranked = sorted(stories, key=lambda row: row.get("score", 0), reverse=True)
    for index, story in enumerate(ranked, start=1):
        story["rank"] = index

    return ranked
