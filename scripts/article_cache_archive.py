"""Keep the complete article corpus in small, readable, ordinary Git files."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import tempfile
from typing import Any
from urllib.parse import urlsplit

from pipeline.article_cache import SQLiteArticleCache, import_json, validate_database

MAX_FILE_BYTES = 1024 * 1024
DEFAULT_DATABASE = Path("derived/article_cache.sqlite3")
DEFAULT_ARCHIVE = Path("derived/article_archive")
DEFAULT_LEGACY = Path("derived/article_cache.json")
FORMAT = "rss-article-archive-v1"
README = """# Article Archive

Every cached article lives in ordinary Git as readable JSON. No Git LFS,
release assets, external storage, expiry, or article deletion is used.

## Folder Layout

`YYYY/MM/source-host/part-NNNN.json`

- Year and month come from `fetched_at`, not the article's publication date.
- Source is the URL hostname in lowercase ASCII (IDNA); ports are omitted.
- Invalid dates use `undated`; invalid hostnames use `unknown-source`.
- Parts contain URL-keyed records sorted by URL. Each file is at most 1 MiB.
  Additional parts are created automatically before that limit is reached.
- A refetched URL moves to its new fetch month; older versions remain in Git
  history. The current archive retains the latest record for every URL.
- `manifest.json` defines the format, counts, size ceiling, and a SHA-256 of
  every URL and complete record in URL order. It is not an unbounded URL index.

The runtime SQLite database is a disposable index rebuilt from these files.
The archive is authoritative. See `Docs/operations/article-cache-archive.md`
for migration, verification, and recovery commands.
"""


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")


def _read_json(path: Path) -> Any:
    def unique_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        value = {}
        for key, item in pairs:
            if key in value:
                raise ValueError(f"Duplicate JSON key in article archive: {key}")
            value[key] = item
        return value

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)


def archive_group(url: str, payload: dict[str, Any]) -> tuple[str, ...]:
    try:
        fetched = datetime.fromisoformat(str(payload.get("fetched_at", "")).replace("Z", "+00:00"))
        if fetched.tzinfo is None:
            fetched = fetched.replace(tzinfo=timezone.utc)
        fetched = fetched.astimezone(timezone.utc)
        date_parts = (f"{fetched.year:04d}", f"{fetched.month:02d}")
    except (ValueError, TypeError, OverflowError):
        date_parts = ("undated",)
    try:
        host = (urlsplit(url).hostname or "").encode("idna").decode("ascii").lower().rstrip(".")
        host = re.sub(r"[^a-z0-9.-]", "_", host).strip(".")
        if not host or len(host) > 200:
            host = "unknown-source"
    except (ValueError, UnicodeError):
        host = "unknown-source"
    return (*date_parts, host)


def _connect(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)
    connection.execute("PRAGMA cache_size = -8192")
    connection.execute("PRAGMA mmap_size = 0")
    connection.execute("PRAGMA temp_store = FILE")
    return connection


def _record_digest(connection: sqlite3.Connection) -> tuple[int, str]:
    digest = hashlib.sha256()
    count = 0
    for url, raw in connection.execute("SELECT url, payload FROM articles ORDER BY url"):
        digest.update(json.dumps([url, json.loads(raw)], sort_keys=True, ensure_ascii=False,
                                 separators=(",", ":"), allow_nan=False).encode("utf-8") + b"\n")
        count += 1
    return count, digest.hexdigest()


def _backup_path(archive_dir: Path) -> Path:
    return archive_dir.with_name("." + archive_dir.name + ".previous")


def _recover_interrupted_swap(archive_dir: Path) -> None:
    backup = _backup_path(archive_dir)
    if backup.exists() and not archive_dir.exists():
        os.replace(backup, archive_dir)


def _read_manifest(archive_dir: Path) -> dict[str, Any]:
    if archive_dir.is_symlink():
        raise ValueError("Archive directory cannot be a symlink")
    path = archive_dir / "manifest.json"
    if path.is_symlink() or path.stat().st_size > MAX_FILE_BYTES:
        raise ValueError("Invalid archive manifest file")
    manifest = _read_json(path)
    if manifest.get("format") != FORMAT:
        raise ValueError("Unsupported article archive format")
    for key in ("records", "shards", "max_file_bytes"):
        if type(manifest.get(key)) is not int or manifest[key] < 0:
            raise ValueError(f"Invalid article archive {key}")
    if not 128 <= manifest["max_file_bytes"] <= MAX_FILE_BYTES:
        raise ValueError("Archive file ceiling exceeds 1 MiB")
    if not isinstance(manifest.get("records_sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", manifest["records_sha256"]):
        raise ValueError("Invalid archive content hash")
    return manifest


def restore_archive(archive_dir: Path, database: Path) -> dict[str, Any]:
    """Validate every tracked record before atomically replacing the runtime DB."""
    _recover_interrupted_swap(archive_dir)
    manifest = _read_manifest(archive_dir)
    database.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".article-restore-", dir=database.parent) as name:
        restored = Path(name) / "restored.sqlite3"
        shards = 0
        part_numbers: dict[tuple[str, ...], int] = {}
        with SQLiteArticleCache(restored) as cache:
            def path_order(path: Path) -> tuple[str, int, str]:
                match = re.fullmatch(r"part-([0-9]{4,})\.json", path.name)
                return str(path.parent), int(match[1]) if match else -1, path.name

            for path in sorted(archive_dir.rglob("*"), key=path_order):
                if path.is_symlink():
                    raise ValueError("Archive symlinks are not permitted")
                if path.is_dir():
                    continue
                if path.parent == archive_dir and path.name in {"manifest.json", "README.md"}:
                    continue
                if path.stat().st_size > manifest["max_file_bytes"]:
                    raise ValueError(f"Archive shard exceeds file limit: {path}")
                relative = path.relative_to(archive_dir)
                match = re.fullmatch(r"part-([0-9]{4,})\.json", path.name)
                if not match:
                    raise ValueError(f"Unexpected archive file: {relative}")
                group = tuple(relative.parts[:-1])
                part_numbers[group] = part_numbers.get(group, 0) + 1
                if int(match[1]) != part_numbers[group]:
                    raise ValueError(f"Missing/out-of-order archive part: {relative}")
                shard = _read_json(path)
                records = shard.get("articles")
                if (shard.get("format") != FORMAT or shard.get("group") != "/".join(group)
                        or not isinstance(records, dict) or not records):
                    raise ValueError(f"Invalid archive shard: {relative}")
                for url, payload in records.items():
                    if not isinstance(payload, dict) or archive_group(url, payload) != group:
                        raise ValueError(f"Article is in the wrong date/source folder: {relative}")
                    if cache.get(url) is not None:
                        raise ValueError(f"Duplicate archived URL: {url}")
                    cache[url] = payload
                shards += 1
        validate_database(restored)
        connection = _connect(restored)
        try:
            count, digest = _record_digest(connection)
        finally:
            connection.close()
        if count != manifest["records"] or digest != manifest["records_sha256"] or shards != manifest["shards"]:
            raise ValueError("Archive count/content checksum mismatch (missing or changed records)")
        if any(Path(str(database) + suffix).exists() for suffix in ("-journal", "-wal", "-shm")):
            raise ValueError("Refusing to replace a runtime database with active SQLite sidecars")
        os.replace(restored, database)
    return manifest


def validate_archive(archive_dir: Path) -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as temporary:
        return restore_archive(archive_dir, Path(temporary) / "verify.sqlite3")


def export_archive(database: Path, archive_dir: Path, max_file_bytes: int = MAX_FILE_BYTES) -> dict[str, Any]:
    """Export deterministic bounded shards, verify them, then swap the full tree."""
    if not 128 <= max_file_bytes <= MAX_FILE_BYTES:
        raise ValueError("Shard size must be between 128 bytes and 1 MiB")
    validate_database(database)
    _recover_interrupted_swap(archive_dir)
    old = validate_archive(archive_dir) if archive_dir.exists() else None
    connection = _connect(database)
    archive_dir.parent.mkdir(parents=True, exist_ok=True)
    try:
        count, digest = _record_digest(connection)
        if old and count < old["records"]:
            raise ValueError("Article count decreased; refusing to discard archived history")
        if old and old["records_sha256"] == digest and old["max_file_bytes"] == max_file_bytes:
            return old
        # Sorting may spill to disk; neither the complete corpus nor a large
        # source/month group is accumulated in Python memory.
        connection.create_function("archive_group", 2, lambda url, raw: "/".join(archive_group(url, json.loads(raw))))
        with tempfile.TemporaryDirectory(prefix="." + archive_dir.name + ".stage-", dir=archive_dir.parent) as temporary:
            stage = Path(temporary) / "archive"
            stage.mkdir()
            shard_count = 0
            group = None
            part = 0
            records: dict[str, Any] = {}
            size = 0

            def payload_bytes(values: dict[str, Any], group_name: str) -> bytes:
                return json_bytes({"format": FORMAT, "group": group_name, "articles": values})

            def write_part() -> None:
                nonlocal shard_count, part
                if not records:
                    return
                part += 1
                path = stage.joinpath(*group.split("/"), f"part-{part:04d}.json")
                encoded = payload_bytes(records, group)
                if len(encoded) > max_file_bytes:
                    raise ValueError("Archive writer exceeded shard size ceiling")
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(encoded)
                shard_count += 1

            rows = connection.execute("SELECT url, payload, archive_group(url, payload) AS folder FROM articles ORDER BY folder, url")
            for url, raw, folder in rows:
                value = json.loads(raw)
                if folder != group:
                    write_part()
                    group, part, records = folder, 0, {}
                    size = len(payload_bytes({}, group))
                # Exact size increment under indent=2 serialization, including
                # separators/indentation. Avoid repeatedly serializing a full shard.
                single_size = len(payload_bytes({url: value}, group))
                base_size = len(payload_bytes({}, group))
                increment = single_size - base_size
                candidate_size = size + increment + (0 if not records else -2)
                if records and candidate_size > max_file_bytes:
                    write_part()
                    records, size = {}, base_size
                    candidate_size = single_size
                if candidate_size > max_file_bytes:
                    raise ValueError(f"One article exceeds the 1 MiB archive ceiling: {url}")
                records[url] = value
                size = candidate_size
            write_part()
            manifest = {"format": FORMAT, "records": count, "shards": shard_count,
                        "max_file_bytes": max_file_bytes, "records_sha256": digest,
                        "layout": "YYYY/MM/source-host/part-NNNN.json; invalid dates use undated"}
            (stage / "manifest.json").write_bytes(json_bytes(manifest))
            (stage / "README.md").write_text(README, encoding="utf-8")
            if validate_archive(stage) != manifest:
                raise ValueError("Archive export verification failed")
            backup = _backup_path(archive_dir)
            if backup.exists():
                # The current tree was validated above, so a leftover old backup
                # from a completed swap can now be discarded locally.
                shutil.rmtree(backup)
            if archive_dir.exists():
                os.replace(archive_dir, backup)
            try:
                os.replace(stage, archive_dir)
            except BaseException:
                if backup.exists() and not archive_dir.exists():
                    os.replace(backup, archive_dir)
                raise
            if backup.exists():
                shutil.rmtree(backup)
            return manifest
    finally:
        connection.close()


def restore(database: Path, archive_dir: Path, legacy: Path) -> dict[str, Any]:
    _recover_interrupted_swap(archive_dir)
    if archive_dir.exists():
        return restore_archive(archive_dir, database)
    if not legacy.is_file():
        raise FileNotFoundError("No Git article archive or legacy cache; refusing to create empty history")
    count = import_json(legacy, database)
    return {"operation": "legacy_migration", "records": count}


def archive(database: Path, archive_dir: Path, legacy: Path) -> dict[str, Any]:
    manifest = export_archive(database, archive_dir)
    # Full record/content verification completed before the original is removed.
    legacy.unlink(missing_ok=True)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("restore", "archive", "validate"))
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--archive-dir", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument("--legacy", type=Path, default=DEFAULT_LEGACY)
    args = parser.parse_args()
    if args.operation == "restore":
        result = restore(args.database, args.archive_dir, args.legacy)
    elif args.operation == "archive":
        result = archive(args.database, args.archive_dir, args.legacy)
    else:
        result = validate_archive(args.archive_dir)
    print(json.dumps(result, sort_keys=True))
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as output:
            output.write("\n### Article Archive in Git\n\n")
            for key, value in result.items():
                output.write(f"- {key}: {value}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
