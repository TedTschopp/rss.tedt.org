import unittest

from pipeline.cluster import build_clusters
from pipeline.embedding_codec import decode_embedding, encode_embedding


class EmbeddingCodecTests(unittest.TestCase):
    def test_float32_encoding_round_trips_compactly(self):
        vector = [0.123456789, -0.25, 1.0] * 512

        encoded = encode_embedding(vector)
        decoded = decode_embedding(encoded)

        self.assertTrue(encoded.startswith("f32:"))
        self.assertLess(len(encoded), 10_000)
        self.assertEqual(len(decoded), len(vector))
        for actual, expected in zip(decoded, vector):
            self.assertAlmostEqual(actual, expected, places=6)

    def test_clusters_accept_compact_embeddings(self):
        stories = [
            {"story_id": "s1", "title": "First", "canonical_url": "https://example.com/1", "mentions": []},
            {"story_id": "s2", "title": "Second", "canonical_url": "https://example.com/2", "mentions": []},
        ]
        cache = {
            "s1": {"embedding": encode_embedding([1.0, 0.0])},
            "s2": {"embedding": encode_embedding([1.0, 0.0])},
        }

        clusters, cluster_map = build_clusters(stories, cache)

        self.assertEqual(len(clusters), 1)
        self.assertEqual(cluster_map["s1"], cluster_map["s2"])


if __name__ == "__main__":
    unittest.main()