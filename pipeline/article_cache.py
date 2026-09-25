"""Disposable runtime index for article history retained in Git JSON shards.

The database stores complete JSON records restored from the authoritative Git
archive. Normal publishing reads only requested URLs with a bounded SQLite page
cache; it never loads the archive into a Python dictionary. Legacy JSON import
intentionally retains every field and historical record during migration.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import sqlite3
import tempfile
from typing import Any


APPLICATION_ID = 0x52535343  # RSSC
SCHEMA_VERSION = 1
PAGE_CACHE_KIB = 8192


class ArticleCacheError(ValueError):
    """An existing article cache cannot be safely read or replaced."""


def _configure(connection: sqlite3.Connection) -> None:
    connection.execute(f"PRAGMA cache_size = -{PAGE_CACHE_KIB}")
    connection.execute("PRAGMA mmap_size = 0")
    connection.execute("PRAGMA temp_store = FILE")


def _check_schema(connection: sqlite3.Connection) -> None:
    if connection.execute("PRAGMA application_id").fetchone()[0] != APPLICATION_ID:
        raise ArticleCacheError("Not an RSS article-cache database (application_id mismatch)")
    if connection.execute("PRAGMA user_version").fetchone()[0] != SCHEMA_VERSION:
        raise ArticleCacheError("Unsupported RSS article-cache schema version")
    columns = connection.execute("PRAGMA table_info(articles)").fetchall()
    expected = [(0, "url", "TEXT", 1, None, 1), (1, "payload", "TEXT", 1, None, 0)]
    if columns != expected:
        raise ArticleCacheError("Invalid RSS article-cache articles schema")


def _decode_payload(raw: str, url: str) -> dict[str, Any]:
    try:
        payload = json.loads(raw)
    except (TypeError, ValueError) as exc:
        raise ArticleCacheError(f"Invalid article-cache JSON for {url!r}") from exc
    if not isinstance(payload, dict):
        raise ArticleCacheError(f"Article-cache record for {url!r} must be an object")
    return payload


def load_legacy_json(path: str | os.PathLike[str]) -> dict[str, dict[str, Any]]:
    """Read legacy history strictly; only a missing file represents an empty cache."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError:
        return {}
    except (OSError, UnicodeError, ValueError) as exc:
        raise ArticleCacheError(f"Cannot read article cache {path}: {exc}") from exc
    if not isinstance(payload, dict) or any(not isinstance(value, dict) for value in payload.values()):
        raise ArticleCacheError(f"Article cache {path} must map URLs to JSON objects")
    return payload


class SQLiteArticleCache:
    """Disposable URL-keyed runtime index of article history kept in Git.

    A successful context commits runtime updates; errors roll back. The archive
    command exports those records back to the authoritative JSON shards.

    ``close()`` always rolls back outstanding writes. Call ``commit()`` first when
    using this class outside a context manager. Connections stay on the publishing
    thread; article-fetch workers return results before the main thread writes.
    """

    def __init__(self, path: str | os.PathLike[str]):
        self.path = Path(path)
        existed = self.path.exists()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._connection: sqlite3.Connection | None = None
        try:
            connection = sqlite3.connect(self.path)
            self._connection = connection
            _configure(connection)
            if existed:
                _check_schema(connection)
            else:
                connection.execute(f"PRAGMA application_id = {APPLICATION_ID}")
                connection.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
                connection.execute(
                    "CREATE TABLE articles (url TEXT PRIMARY KEY NOT NULL, "
                    "payload TEXT NOT NULL) WITHOUT ROWID"
                )
                connection.commit()
            # Keep the disposable runtime database self-contained so archive
            # export and local recovery do not depend on a separate WAL file.
            connection.execute("PRAGMA journal_mode = DELETE")
            connection.execute("PRAGMA synchronous = FULL")
        except (sqlite3.Error, ArticleCacheError) as exc:
            self.close()
            raise ArticleCacheError(f"Cannot open article cache {self.path}: {exc}") from exc

    def _db(self) -> sqlite3.Connection:
        if self._connection is None:
            raise ArticleCacheError("Article cache is closed")
        return self._connection

    def get(self, url: str, default: Any = None) -> Any:
        row = self._db().execute("SELECT payload FROM articles WHERE url = ?", (url,)).fetchone()
        return default if row is None else _decode_payload(row[0], url)

    def __setitem__(self, url: str, payload: dict[str, Any]) -> None:
        if not isinstance(url, str) or not isinstance(payload, dict):
            raise ArticleCacheError("Article-cache entries require a URL string and a JSON object")
        raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
        self._db().execute(
            "INSERT INTO articles(url, payload) VALUES (?, ?) "
            "ON CONFLICT(url) DO UPDATE SET payload = excluded.payload",
            (url, raw),
        )

    def commit(self) -> None:
        self._db().commit()

    def close(self) -> None:
        if self._connection is not None:
            self._connection.close()
            self._connection = None

    def __enter__(self) -> SQLiteArticleCache:
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        try:
            if exc_type is None:
                self.commit()
        finally:
            self.close()


def validate_database(path: str | os.PathLike[str]) -> int:
    """Validate the runtime index read-only, including every record; return its count."""
    source = Path(path).resolve()
    if not source.is_file():
        raise ArticleCacheError(f"Article-cache database does not exist: {source}")
    connection: sqlite3.Connection | None = None
    try:
        connection = sqlite3.connect(source.as_uri() + "?mode=ro", uri=True)
        _configure(connection)
        _check_schema(connection)
        integrity = connection.execute("PRAGMA integrity_check").fetchall()
        if integrity != [("ok",)]:
            raise ArticleCacheError(f"Article-cache integrity check failed: {integrity}")
        count = 0
        for url, payload in connection.execute("SELECT url, payload FROM articles"):
            if not isinstance(url, str):
                raise ArticleCacheError("Article-cache URL must be text")
            _decode_payload(payload, url)
            count += 1
        return count
    except sqlite3.Error as exc:
        raise ArticleCacheError(f"Invalid article-cache database {source}: {exc}") from exc
    finally:
        if connection is not None:
            connection.close()


def import_json(source: str | os.PathLike[str], destination: str | os.PathLike[str]) -> int:
    """Atomically migrate all legacy records; preserve any destination on failure."""
    source_path = Path(source)
    destination_path = Path(destination)
    if not source_path.is_file():
        raise ArticleCacheError(f"Legacy article cache does not exist: {source_path}")
    if source_path.resolve() == destination_path.resolve():
        raise ArticleCacheError("Legacy source and SQLite destination must differ")
    _reject_sqlite_sidecars(destination_path)
    records = load_legacy_json(source_path)
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=destination_path.name + ".", suffix=".tmp", dir=destination_path.parent
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    # SQLiteArticleCache intentionally rejects existing empty/corrupt databases.
    temporary.unlink()
    try:
        with SQLiteArticleCache(temporary) as cache:
            for url, payload in records.items():
                cache[url] = payload
        count = validate_database(temporary)
        if count != len(records):
            raise ArticleCacheError("Article-cache migration record count changed")
        # Compare decoded payloads so optional fields and exact Markdown survive.
        with SQLiteArticleCache(temporary) as cache:
            for url, payload in records.items():
                if cache.get(url) != payload:
                    raise ArticleCacheError(f"Article-cache migration changed {url!r}")
        _reject_sqlite_sidecars(destination_path)
        os.replace(temporary, destination_path)
        return count
    finally:
        temporary.unlink(missing_ok=True)
        Path(str(temporary) + "-journal").unlink(missing_ok=True)


def _reject_sqlite_sidecars(path: Path) -> None:
    for suffix in ("-journal", "-wal", "-shm"):
        if Path(str(path) + suffix).exists():
            raise ArticleCacheError(
                f"Cannot replace active or unrecovered SQLite database {path}: {suffix} exists"
            )
