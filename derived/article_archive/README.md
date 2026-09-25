# Article Archive

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
