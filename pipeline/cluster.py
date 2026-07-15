from collections import defaultdict
from math import sqrt
from typing import Any, cast

try:
    import numpy as np
except ImportError:
    np = None

from .embedding_codec import decode_embedding
from .text_utils import normalize_text, stable_id


def _cosine(a: list[float], b: list[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(left * right for left, right in zip(a, b))
    norm_a = sqrt(sum(value * value for value in a))
    norm_b = sqrt(sum(value * value for value in b))
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


def _union_similar_embeddings(
    parents: dict[str, str],
    vectors: dict[str, list[float]],
    similarity_threshold: float,
    block_size: int = 256,
) -> None:
    if np is None:
        embedded_ids = list(vectors)
        for index, left_id in enumerate(embedded_ids):
            for right_id in embedded_ids[index + 1 :]:
                if _cosine(vectors[left_id], vectors[right_id]) >= similarity_threshold:
                    _union(parents, left_id, right_id)
        return

    ids_by_dimension: dict[int, list[str]] = defaultdict(list)
    for story_id, vector in vectors.items():
        if vector:
            ids_by_dimension[len(vector)].append(story_id)

    for dimension, story_ids in ids_by_dimension.items():
        if dimension <= 0 or len(story_ids) < 2:
            continue
        matrix = np.asarray([vectors[story_id] for story_id in story_ids], dtype=np.float32)
        norms = np.linalg.norm(matrix, axis=1)
        valid = norms > 0
        matrix[valid] /= norms[valid, np.newaxis]
        matrix[~valid] = 0

        for start in range(0, len(story_ids), block_size):
            end = min(start + block_size, len(story_ids))
            with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
                similarities = matrix[start:end] @ matrix.T
            left_offsets, right_indexes = np.nonzero(similarities >= similarity_threshold)
            for left_offset, right_index in zip(left_offsets.tolist(), right_indexes.tolist()):
                left_index = start + left_offset
                if right_index > left_index:
                    _union(parents, story_ids[left_index], story_ids[right_index])


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
        embedding = decode_embedding(cache_map.get("embedding"))
        if embedding:
            vectors[story_id] = embedding

    # hard links by canonical URL
    for ids in by_url.values():
        if len(ids) < 2:
            continue
        anchor = ids[0]
        for candidate_id in ids[1:]:
            _union(parents, anchor, candidate_id)

    # embedding-first links across all embedded stories
    _union_similar_embeddings(parents, vectors, similarity_threshold)

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
