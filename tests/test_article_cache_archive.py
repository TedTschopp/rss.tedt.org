"""Offline preservation, file-boundary, and recovery tests for the Git archive."""

import json
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from pipeline.article_cache import SQLiteArticleCache, validate_database
from scripts import article_cache_archive as archive


class ArticleCacheArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.database = self.root / "article_cache.sqlite3"
        self.archive_dir = self.root / "article_archive"
        self.legacy = self.root / "article_cache.json"
        self.records = {
            "https://Example.COM:443/old": {
                "markdown": "Café 日本語\n\nLiteral control: \u001b and null: \u0000",
                "fetched_at": "2026-05-24T09:49:54.256444Z",
                "extra": {"preserved": [1, "two", None]},
            },
            "https://example.com/new": {
                "markdown": "Recent article", "fetched_at": "2026-09-23T08:08:14Z",
                "fetch_failed": False,
            },
            "https://münich.example/failed": {
                "markdown": "", "fetched_at": "2026-09-23T08:08:14Z",
                "fetch_failed": True,
            },
            "not a URL": {"markdown": "Unknown source and date", "custom": True},
        }
        self.write_database(self.database, self.records)
        self.legacy.write_text(json.dumps(self.records, ensure_ascii=False), encoding="utf-8")

    @staticmethod
    def write_database(path, records):
        with SQLiteArticleCache(path) as cache:
            for url, payload in records.items():
                cache[url] = payload

    @staticmethod
    def tree_bytes(directory):
        return {str(path.relative_to(directory)): path.read_bytes()
                for path in directory.rglob("*") if path.is_file()}

    def assert_records(self, database, records):
        self.assertEqual(validate_database(database), len(records))
        with SQLiteArticleCache(database) as cache:
            for url, expected in records.items():
                self.assertEqual(cache.get(url), expected)

    def first_part(self, directory=None):
        return sorted((directory or self.archive_dir).rglob("part-*.json"))[0]

    def test_complete_record_and_unicode_preservation(self):
        manifest = archive.export_archive(self.database, self.archive_dir)
        restored = self.root / "restored.sqlite3"
        self.assertEqual(archive.restore_archive(self.archive_dir, restored), manifest)
        self.assert_records(restored, self.records)
        self.assertEqual(manifest["records"], len(self.records))
        self.assertEqual(manifest["shards"], len(list(self.archive_dir.rglob("part-*.json"))))
        self.assertTrue(all(path.stat().st_size <= archive.MAX_FILE_BYTES
                            for path in self.archive_dir.rglob("part-*.json")))
        text = self.first_part().read_text(encoding="utf-8")
        self.assertIn("Café 日本語", text)
        self.assertTrue(self.legacy.exists())

    def test_meaningful_fetch_month_and_source_paths(self):
        archive.export_archive(self.database, self.archive_dir)
        expected = {
            "2026/05/example.com/part-0001.json",
            "2026/09/example.com/part-0001.json",
            "2026/09/xn--mnich-kva.example/part-0001.json",
            "undated/unknown-source/part-0001.json",
        }
        actual = {str(path.relative_to(self.archive_dir))
                  for path in self.archive_dir.rglob("part-*.json")}
        self.assertEqual(actual, expected)
        self.assertEqual(archive.archive_group("https://WWW.Example.com:8443/a", {
            "fetched_at": "2026-03-01T00:30:00+01:00", "published": "1999-01-01"
        }), ("2026", "02", "www.example.com"))
        self.assertEqual(archive.archive_group("https://example.com/a", {
            "fetched_at": "invalid", "published": "2026-01-01"
        }), ("undated", "example.com"))

    def test_git_attributes_keep_archive_as_ordinary_text_without_lfs(self):
        if shutil.which("git") is None:
            self.skipTest("Git is required to inspect effective repository attributes")
        repository = Path(__file__).resolve().parents[1]
        paths = [
            "derived/article_archive/2026/09/example.com/part-0001.json",
            "derived/article_archive/undated/unknown-source/part-0001.json",
            "derived/article_archive/manifest.json",
        ]
        result = subprocess.run(
            ["git", "check-attr", "-z", "filter", "diff", "merge", "text", "eol", "--", *paths],
            cwd=repository, check=True, capture_output=True,
        )
        fields = result.stdout.decode("utf-8").split("\0")
        self.assertEqual(fields.pop(), "")
        attributes = {(fields[index], fields[index + 1]): fields[index + 2]
                      for index in range(0, len(fields), 3)}
        for path in paths:
            self.assertEqual(attributes[(path, "filter")], "unset")
            self.assertEqual(attributes[(path, "diff")], "set")
            self.assertEqual(attributes[(path, "merge")], "set")
            self.assertEqual(attributes[(path, "text")], "set")
            self.assertEqual(attributes[(path, "eol")], "lf")

    def test_rollover_at_exact_utf8_byte_boundary(self):
        records = {
            "https://example.com/a": {"markdown": "日本語", "fetched_at": "2026-09-01T00:00:00Z"},
            "https://example.com/b": {"markdown": "Café", "fetched_at": "2026-09-01T00:00:00Z"},
        }
        database = self.root / "boundary.sqlite3"
        self.write_database(database, records)
        exact_bytes = len(archive.json_bytes({
            "format": archive.FORMAT, "group": "2026/09/example.com", "articles": records,
        }))
        exact_dir = self.root / "exact"
        exact = archive.export_archive(database, exact_dir, max_file_bytes=exact_bytes)
        self.assertEqual(exact["shards"], 1, "Two records exactly at the ceiling must fit")
        self.assertEqual(self.first_part(exact_dir).stat().st_size, exact_bytes)
        smaller_dir = self.root / "one-byte-less"
        smaller = archive.export_archive(database, smaller_dir, max_file_bytes=exact_bytes - 1)
        self.assertEqual(smaller["shards"], 2)
        self.assertTrue(all(path.stat().st_size <= exact_bytes - 1
                            for path in smaller_dir.rglob("part-*.json")))
        restored = self.root / "boundary-restored.sqlite3"
        archive.restore_archive(smaller_dir, restored)
        self.assert_records(restored, records)

    def test_many_records_rotate_before_the_ceiling(self):
        records = {f"https://example.com/{index:03d}": {
            "markdown": "Résumé 日本語 " * 8,
            "fetched_at": "2026-09-01T00:00:00Z",
        } for index in range(20)}
        database = self.root / "many.sqlite3"
        self.write_database(database, records)
        manifest = archive.export_archive(database, self.archive_dir, max_file_bytes=1024)
        parts = sorted(self.archive_dir.rglob("part-*.json"))
        self.assertGreater(len(parts), 1)
        self.assertEqual([part.name for part in parts],
                         [f"part-{index:04d}.json" for index in range(1, len(parts) + 1)])
        self.assertTrue(all(part.stat().st_size <= 1024 for part in parts))
        restored = self.root / "many-restored.sqlite3"
        self.assertEqual(archive.restore_archive(self.archive_dir, restored), manifest)
        self.assert_records(restored, records)

    def test_repeated_exports_and_different_insertion_orders_are_identical(self):
        first = archive.export_archive(self.database, self.archive_dir)
        before = self.tree_bytes(self.archive_dir)
        self.assertEqual(archive.export_archive(self.database, self.archive_dir), first)
        self.assertEqual(self.tree_bytes(self.archive_dir), before)
        other_database = self.root / "reverse.sqlite3"
        self.write_database(other_database, dict(reversed(list(self.records.items()))))
        other_archive = self.root / "reverse-archive"
        self.assertEqual(archive.export_archive(other_database, other_archive), first)
        self.assertEqual(self.tree_bytes(other_archive), before)

    def test_new_month_does_not_rewrite_untouched_historical_month(self):
        archive.export_archive(self.database, self.archive_dir)
        historical = self.archive_dir / "2026/05/example.com/part-0001.json"
        before = historical.read_bytes()
        with SQLiteArticleCache(self.database) as cache:
            cache["https://example.com/october"] = {
                "markdown": "New article", "fetched_at": "2026-10-01T00:00:00Z"
            }
        archive.export_archive(self.database, self.archive_dir)
        self.assertEqual(historical.read_bytes(), before)
        self.assertTrue((self.archive_dir / "2026/10/example.com/part-0001.json").exists())

    def test_refetched_url_moves_month_without_losing_other_records(self):
        archive.export_archive(self.database, self.archive_dir)
        url = "https://Example.COM:443/old"
        updated = {**self.records[url], "fetched_at": "2026-10-01T00:00:00Z"}
        with SQLiteArticleCache(self.database) as cache:
            cache[url] = updated
        archive.export_archive(self.database, self.archive_dir)
        self.assertFalse((self.archive_dir / "2026/05/example.com/part-0001.json").exists())
        restored = self.root / "moved.sqlite3"
        archive.restore_archive(self.archive_dir, restored)
        self.assert_records(restored, {**self.records, url: updated})

    def test_corrupt_missing_changed_or_oversized_shard_preserves_database(self):
        archive.export_archive(self.database, self.archive_dir)
        original = self.database.read_bytes()
        for damage in ("corrupt", "missing", "changed", "oversized"):
            with self.subTest(damage=damage):
                damaged = self.root / damage
                shutil.copytree(self.archive_dir, damaged)
                part = self.first_part(damaged)
                if damage == "corrupt":
                    part.write_text("{broken", encoding="utf-8")
                elif damage == "missing":
                    part.unlink()
                elif damage == "changed":
                    payload = json.loads(part.read_text())
                    next(iter(payload["articles"].values()))["markdown"] = "changed content"
                    part.write_bytes(archive.json_bytes(payload))
                else:
                    part.write_bytes(part.read_bytes() + b" " * archive.MAX_FILE_BYTES)
                with self.assertRaises((ValueError, FileNotFoundError)):
                    archive.restore_archive(damaged, self.database)
                self.assertEqual(self.database.read_bytes(), original)

    def test_duplicate_url_in_different_parts_is_rejected(self):
        archive.export_archive(self.database, self.archive_dir)
        part = self.first_part()
        shutil.copyfile(part, part.with_name("part-0002.json"))
        before = self.database.read_bytes()
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            archive.restore_archive(self.archive_dir, self.database)
        self.assertEqual(self.database.read_bytes(), before)

    def test_duplicate_url_keys_within_a_part_are_rejected(self):
        archive.export_archive(self.database, self.archive_dir)
        part = self.first_part()
        shard = json.loads(part.read_text())
        url, payload = next(iter(shard["articles"].items()))
        pair = json.dumps(url) + ":" + json.dumps(payload)
        duplicated = ("{\"format\":" + json.dumps(shard["format"]) + ",\"group\":"
                      + json.dumps(shard["group"]) + ",\"articles\":{" + pair + "," + pair + "}}")
        part.write_text(duplicated, encoding="utf-8")
        before = self.database.read_bytes()
        with self.assertRaises(ValueError):
            archive.restore_archive(self.archive_dir, self.database)
        self.assertEqual(self.database.read_bytes(), before)

    def test_wrong_folder_and_invalid_part_filename_are_rejected(self):
        archive.export_archive(self.database, self.archive_dir)
        original = self.database.read_bytes()
        for damage in ("folder", "filename"):
            with self.subTest(damage=damage):
                damaged = self.root / damage
                shutil.copytree(self.archive_dir, damaged)
                part = self.first_part(damaged)
                if damage == "folder":
                    wrong = part.parent.with_name("different.example") / part.name
                    wrong.parent.mkdir()
                    content = json.loads(part.read_text())
                    content["group"] = "/".join(wrong.relative_to(damaged).parts[:-1])
                    part.unlink()
                    wrong.write_bytes(archive.json_bytes(content))
                else:
                    part.rename(part.with_name("part-0001Xjson"))
                with self.assertRaises(ValueError):
                    archive.restore_archive(damaged, self.database)
                self.assertEqual(self.database.read_bytes(), original)

    def test_missing_middle_part_is_rejected(self):
        records = {f"https://example.com/{index}": {
            "markdown": "body " * 30, "fetched_at": "2026-09-01T00:00:00Z"
        } for index in range(6)}
        database = self.root / "parts.sqlite3"
        self.write_database(database, records)
        archive.export_archive(database, self.archive_dir, max_file_bytes=400)
        parts = sorted(self.archive_dir.rglob("part-*.json"))
        self.assertGreaterEqual(len(parts), 3)
        parts[1].unlink()
        with self.assertRaisesRegex(ValueError, "Missing/out-of-order"):
            archive.validate_archive(self.archive_dir)

    def test_manifest_corruption_or_missing_manifest_never_falls_back(self):
        archive.export_archive(self.database, self.archive_dir)
        original = self.database.read_bytes()
        for damage in ("corrupt", "missing", "wrong-schema"):
            with self.subTest(damage=damage):
                damaged = self.root / ("manifest-" + damage)
                shutil.copytree(self.archive_dir, damaged)
                manifest = damaged / "manifest.json"
                if damage == "missing":
                    manifest.unlink()
                elif damage == "corrupt":
                    manifest.write_text("{broken", encoding="utf-8")
                else:
                    value = json.loads(manifest.read_text())
                    value["format"] = "unsupported"
                    manifest.write_bytes(archive.json_bytes(value))
                with self.assertRaises((ValueError, FileNotFoundError)):
                    archive.restore(self.database, damaged, self.legacy)
                self.assertEqual(self.database.read_bytes(), original)
                self.assertTrue(self.legacy.exists())

    def test_missing_archive_and_legacy_never_creates_empty_history(self):
        self.legacy.unlink()
        absent = self.root / "absent.sqlite3"
        with self.assertRaisesRegex(FileNotFoundError, "refusing to create empty history"):
            archive.restore(absent, self.archive_dir, self.legacy)
        self.assertFalse(absent.exists())

    def test_legacy_migration_is_lossless_and_removes_source_only_after_export(self):
        database = self.root / "migrated.sqlite3"
        result = archive.restore(database, self.archive_dir, self.legacy)
        self.assertEqual(result["records"], len(self.records))
        self.assert_records(database, self.records)
        self.assertTrue(self.legacy.exists())
        archive.archive(database, self.archive_dir, self.legacy)
        self.assertFalse(self.legacy.exists())
        restored = self.root / "after-migration.sqlite3"
        archive.restore(restored, self.archive_dir, self.legacy)
        self.assert_records(restored, self.records)

    def test_failed_migration_export_preserves_legacy_and_prior_archive(self):
        archive.export_archive(self.database, self.archive_dir)
        original_archive = self.tree_bytes(self.archive_dir)
        legacy_bytes = self.legacy.read_bytes()
        with patch.object(archive, "export_archive", side_effect=OSError("disk full")):
            with self.assertRaisesRegex(OSError, "disk full"):
                archive.archive(self.database, self.archive_dir, self.legacy)
        self.assertEqual(self.legacy.read_bytes(), legacy_bytes)
        self.assertEqual(self.tree_bytes(self.archive_dir), original_archive)

    def test_oversized_single_record_is_not_truncated_and_keeps_prior_archive(self):
        archive.export_archive(self.database, self.archive_dir)
        before = self.tree_bytes(self.archive_dir)
        legacy_bytes = self.legacy.read_bytes()
        url = "https://example.com/oversized"
        value = {"markdown": "x" * archive.MAX_FILE_BYTES,
                 "fetched_at": "2026-09-25T00:00:00Z"}
        with SQLiteArticleCache(self.database) as cache:
            cache[url] = value
        with self.assertRaisesRegex(ValueError, "One article exceeds"):
            archive.archive(self.database, self.archive_dir, self.legacy)
        self.assertEqual(self.tree_bytes(self.archive_dir), before)
        self.assertEqual(self.legacy.read_bytes(), legacy_bytes)
        with SQLiteArticleCache(self.database) as cache:
            self.assertEqual(cache.get(url), value)

    def test_count_decrease_refuses_to_discard_previous_archive(self):
        archive.export_archive(self.database, self.archive_dir)
        before = self.tree_bytes(self.archive_dir)
        with sqlite3.connect(self.database) as connection:
            connection.execute("DELETE FROM articles WHERE url = ?", (next(iter(self.records)),))
        with self.assertRaisesRegex(ValueError, "count decreased"):
            archive.export_archive(self.database, self.archive_dir)
        self.assertEqual(self.tree_bytes(self.archive_dir), before)

    def test_failed_directory_swap_restores_previous_tree(self):
        archive.export_archive(self.database, self.archive_dir)
        before = self.tree_bytes(self.archive_dir)
        with SQLiteArticleCache(self.database) as cache:
            cache["https://example.com/added"] = {"markdown": "new"}
        original_replace = os.replace

        def fail_new_tree(source, target):
            source, target = Path(source), Path(target)
            if target == self.archive_dir and ".stage-" in source.parent.name:
                raise OSError("simulated swap failure")
            return original_replace(source, target)

        with patch.object(archive.os, "replace", side_effect=fail_new_tree):
            with self.assertRaisesRegex(OSError, "simulated swap failure"):
                archive.archive(self.database, self.archive_dir, self.legacy)
        self.assertEqual(self.tree_bytes(self.archive_dir), before)
        self.assertTrue(self.legacy.exists())
        self.assertEqual(archive.validate_archive(self.archive_dir)["records"], len(self.records))

    def test_next_operation_recovers_backup_after_interrupted_swap(self):
        archive.export_archive(self.database, self.archive_dir)
        before = self.tree_bytes(self.archive_dir)
        with SQLiteArticleCache(self.database) as cache:
            cache["https://example.com/added"] = {"markdown": "new"}
        original_replace = os.replace

        def interrupt_replacement_and_rollback(source, target):
            if Path(target) == self.archive_dir:
                raise OSError("interrupted before current tree could be restored")
            return original_replace(source, target)

        with patch.object(archive.os, "replace", side_effect=interrupt_replacement_and_rollback):
            with self.assertRaises(OSError):
                archive.archive(self.database, self.archive_dir, self.legacy)
        self.assertFalse(self.archive_dir.exists())
        self.assertTrue(self.legacy.exists())
        self.assertEqual(archive.validate_archive(self.archive_dir)["records"], len(self.records))
        self.assertEqual(self.tree_bytes(self.archive_dir), before)
        self.assertEqual(archive.export_archive(self.database, self.archive_dir)["records"], len(self.records) + 1)


if __name__ == "__main__":
    unittest.main()
