import json
from contextlib import closing
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from pipeline.article_cache import (
    ArticleCacheError,
    PAGE_CACHE_KIB,
    SQLiteArticleCache,
    import_json,
    load_legacy_json,
    validate_database,
)


class ArticleCacheTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.database = self.root / "articles.sqlite3"

    def test_migration_preserves_all_history_and_optional_fields(self):
        records = {
            "https://example.com/old": {
                "markdown": "# Märchen\n\nExact  spaces.\n\t◻ 😀\n",
                "fetched_at": "1999-01-01T00:00:00Z",
                "extra": {"list": [1, None, True], "source": "原文"},
            },
            "https://example.com/failed": {
                "markdown": "", "fetched_at": "2000-01-01T00:00:00Z", "fetch_failed": True,
            },
        }
        source = self.root / "article_cache.json"
        source.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")
        original_bytes = source.read_bytes()
        self.assertEqual(import_json(source, self.database), 2)
        self.assertEqual(validate_database(self.database), 2)
        with SQLiteArticleCache(self.database) as cache:
            for url, record in records.items():
                self.assertEqual(cache.get(url), record)
            self.assertEqual(cache.get("missing", "default"), "default")
        self.assertEqual(source.read_bytes(), original_bytes)

    def test_committed_updates_replace_only_the_requested_url(self):
        with SQLiteArticleCache(self.database) as cache:
            cache["old"] = {"markdown": "history"}
            cache["current"] = {"markdown": "before"}
        with SQLiteArticleCache(self.database) as cache:
            cache["current"] = {"markdown": "after"}
        with SQLiteArticleCache(self.database) as cache:
            self.assertEqual(cache.get("old"), {"markdown": "history"})
            self.assertEqual(cache.get("current"), {"markdown": "after"})
        self.assertEqual(validate_database(self.database), 2)

    def test_failure_rolls_back_and_releases_connection(self):
        with SQLiteArticleCache(self.database) as cache:
            cache["saved"] = {"markdown": "before"}
        with self.assertRaisesRegex(RuntimeError, "publication failed"):
            with SQLiteArticleCache(self.database) as cache:
                cache["saved"] = {"markdown": "after"}
                cache["new"] = {"markdown": "uncommitted"}
                raise RuntimeError("publication failed")
        with SQLiteArticleCache(self.database) as cache:
            self.assertEqual(cache.get("saved"), {"markdown": "before"})
            self.assertIsNone(cache.get("new"))
            cache["new"] = {"markdown": "can write again"}

    def test_plain_close_rolls_back_uncommitted_changes(self):
        cache = SQLiteArticleCache(self.database)
        cache["unsaved"] = {"markdown": "uncommitted"}
        cache.close()
        self.assertEqual(validate_database(self.database), 0)
        with self.assertRaisesRegex(ArticleCacheError, "closed"):
            cache.get("unsaved")

    def test_lookup_is_indexed_and_uses_bounded_page_cache(self):
        with SQLiteArticleCache(self.database) as cache:
            for number in range(1000):
                cache[f"https://example.com/{number}"] = {"markdown": f"Article {number}"}
        with SQLiteArticleCache(self.database) as cache:
            connection = cache._db()
            self.assertEqual(connection.execute("PRAGMA cache_size").fetchone()[0], -PAGE_CACHE_KIB)
            self.assertEqual(connection.execute("PRAGMA mmap_size").fetchone()[0], 0)
            plan = connection.execute(
                "EXPLAIN QUERY PLAN SELECT payload FROM articles WHERE url = ?", ("requested",)
            ).fetchone()[3]
            self.assertIn("SEARCH articles USING PRIMARY KEY", plan)
            statements = []
            connection.set_trace_callback(statements.append)
            self.assertEqual(cache.get("https://example.com/17"), {"markdown": "Article 17"})
            self.assertEqual(len(statements), 1)
            self.assertIn("WHERE url =", statements[0])

    def test_legacy_missing_is_empty_but_corruption_fails(self):
        source = self.root / "legacy.json"
        self.assertEqual(load_legacy_json(source), {})
        for content in ("{truncated", "[]", '{"url": "not an object"}'):
            with self.subTest(content=content):
                source.write_text(content, encoding="utf-8")
                with self.assertRaises(ArticleCacheError):
                    load_legacy_json(source)

    def test_missing_validation_does_not_create_database(self):
        with self.assertRaises(ArticleCacheError):
            validate_database(self.database)
        self.assertFalse(self.database.exists())

    def test_existing_corrupt_or_foreign_sqlite_is_rejected_unchanged(self):
        for content in (b"", b"not a database", b"SQLite format 3\0truncated"):
            with self.subTest(content=content):
                self.database.write_bytes(content)
                with self.assertRaises(ArticleCacheError):
                    SQLiteArticleCache(self.database)
                with self.assertRaises(ArticleCacheError):
                    validate_database(self.database)
                self.assertEqual(self.database.read_bytes(), content)
        self.database.unlink()
        with closing(sqlite3.connect(self.database)) as connection:
            connection.execute("CREATE TABLE unrelated(value TEXT)")
        with self.assertRaisesRegex(ArticleCacheError, "application_id"):
            validate_database(self.database)

    def test_schema_version_and_corrupt_payload_are_rejected(self):
        with SQLiteArticleCache(self.database) as cache:
            cache["url"] = {"markdown": "text"}
        with closing(sqlite3.connect(self.database)) as connection:
            connection.execute("PRAGMA user_version = 999")
        with self.assertRaisesRegex(ArticleCacheError, "schema version"):
            validate_database(self.database)
        with closing(sqlite3.connect(self.database)) as connection:
            connection.execute("PRAGMA user_version = 1")
            connection.execute("UPDATE articles SET payload = '{broken'")
            connection.commit()
        with self.assertRaisesRegex(ArticleCacheError, "JSON"):
            validate_database(self.database)
        with SQLiteArticleCache(self.database) as cache:
            with self.assertRaisesRegex(ArticleCacheError, "JSON"):
                cache.get("url")

    def test_migration_failure_preserves_previous_database(self):
        with SQLiteArticleCache(self.database) as cache:
            cache["existing"] = {"markdown": "keep me"}
        original_bytes = self.database.read_bytes()
        source = self.root / "legacy.json"
        source.write_text('{"new": {"markdown": "new text"}}', encoding="utf-8")
        with patch("pipeline.article_cache.validate_database", side_effect=ArticleCacheError("bad snapshot")):
            with self.assertRaisesRegex(ArticleCacheError, "bad snapshot"):
                import_json(source, self.database)
        self.assertEqual(self.database.read_bytes(), original_bytes)
        self.assertEqual(list(self.root.glob("*.tmp*")), [])

    def test_missing_or_corrupt_migration_source_preserves_database(self):
        with SQLiteArticleCache(self.database) as cache:
            cache["existing"] = {"markdown": "keep me"}
        original_bytes = self.database.read_bytes()
        source = self.root / "legacy.json"
        with self.assertRaises(ArticleCacheError):
            import_json(source, self.database)
        source.write_text("broken", encoding="utf-8")
        with self.assertRaises(ArticleCacheError):
            import_json(source, self.database)
        self.assertEqual(self.database.read_bytes(), original_bytes)

    def test_migration_refuses_active_sqlite_sidecars(self):
        with SQLiteArticleCache(self.database) as cache:
            cache["existing"] = {"markdown": "keep me"}
        original_bytes = self.database.read_bytes()
        source = self.root / "legacy.json"
        source.write_text('{"new": {"markdown": "new text"}}', encoding="utf-8")
        for suffix in ("-journal", "-wal", "-shm"):
            with self.subTest(sidecar=suffix):
                sidecar = Path(str(self.database) + suffix)
                sidecar.write_bytes(b"active")
                with self.assertRaisesRegex(ArticleCacheError, "active or unrecovered"):
                    import_json(source, self.database)
                self.assertEqual(self.database.read_bytes(), original_bytes)
                self.assertEqual(sidecar.read_bytes(), b"active")
                sidecar.unlink()


if __name__ == "__main__":
    unittest.main()
