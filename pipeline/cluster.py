from collections import defaultdict
from math import sqrt
from typing import Any, cast

from .text_utils import normalize_text, stable_id


def _cosine(a: list[float], b: list[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sqrt(sum(x * x for x in a))
    norm_b = sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


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
    left_root = _find(parents, left)
    right_root = _find(parents, right)
    if left_root != right_root:
        parents[right_root] = left_root


def build_clusters(
    stories: list[dict[str, Any]],
    llm_cache: dict[str, Any],
    similarity_threshold: float = 0.86,
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    if not stories:
        return [], {}

    parents = {story["story_id"]: story["story_id"] for story in stories}

    by_url: dict[str, list[str]] = defaultdict(list)
    by_title: dict[str, list[str]] = defaultdict(list)
    vectors: dict[str, list[float]] = {}
    for story in stories:
        story_id = str(story["story_id"])
        canonical_url = str(story.get("canonical_url") or "")
        if canonical_url:
            by_url[canonical_url].append(story_id)

        title_key = normalize_text(str(story.get("title", ""))).lower()
        if title_key:
            by_title[title_key].append(story_id)

        cache_entry = llm_cache.get(story_id)
        cache_map: dict[str, Any] = {}
        if isinstance(cache_entry, dict):
            typed_entry = cast(dict[str, Any], cache_entry)
            cache_map = {str(key): value for key, value in typed_entry.items()}
        embedding = cache_map.get("embedding", [])
        if isinstance(embedding, list) and embedding:
            vectors[story_id] = embedding

    # hard links by canonical URL
    for ids in by_url.values():
        if len(ids) < 2:
            continue
        anchor = ids[0]
        for candidate_id in ids[1:]:
            _union(parents, anchor, candidate_id)

    # embedding-first links across all embedded stories
    embedded_ids = list(vectors.keys())
    for index, left_id in enumerate(embedded_ids):
        left_vec = vectors[left_id]
        for right_id in embedded_ids[index + 1 :]:
            right_vec = vectors[right_id]
            if _cosine(left_vec, right_vec) >= similarity_threshold:
                _union(parents, left_id, right_id)

    # fallback: exact-title links only for stories without embeddings
    for ids in by_title.values():
        ids_without_vectors = [story_id for story_id in ids if story_id not in vectors]
        if len(ids_without_vectors) < 2:
            continue
        anchor = ids_without_vectors[0]
        for candidate_id in ids_without_vectors[1:]:
            _union(parents, anchor, candidate_id)

    clusters_by_root: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for story in stories:
        root = _find(parents, str(story["story_id"]))
        clusters_by_root[root].append(story)

    all_clusters = list(clusters_by_root.values())

    cluster_rows: list[dict[str, Any]] = []
    story_to_cluster: dict[str, str] = {}
    for cluster in all_clusters:
        story_ids = sorted(str(story["story_id"]) for story in cluster)
        representative = sorted(cluster, key=lambda row: (row.get("authority_weight", 0), row.get("published", "")), reverse=True)[0]
        cluster_id = stable_id("clu", "|".join(story_ids))
        source_count = len({mention.get("source_id") for story in cluster for mention in story.get("mentions", []) if mention.get("source_id")})
        for story_id in story_ids:
            story_to_cluster[story_id] = cluster_id

        cluster_rows.append(
            {
                "cluster_id": cluster_id,
                "label": representative.get("title", "")[0:120],
                "story_ids": story_ids,
                "source_count": source_count,
                "representative_story_id": representative.get("story_id"),
                "updated_at": representative.get("last_seen_at"),
            }
        )

    return cluster_rows, story_to_cluster
