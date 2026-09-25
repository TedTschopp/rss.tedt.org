# Article Archive in Git

Every cached article stays in the repository as ordinary, readable JSON. There
is no Git LFS, external archive, release storage, retention expiry, or deletion
of old articles. Git stores historical revisions; the current archive contains
the latest fetched record for every URL, matching the original cache semantics.

## Folder Structure

```text
derived/
  article_archive/
    README.md                     # Human and machine navigation instructions
    manifest.json                 # Format, counts, ceiling, full-corpus checksum
    2026/
      09/
        example.com/
          part-0001.json           # First <=1 MiB group of complete records
          part-0002.json           # Created automatically as the group grows
    undated/
      unknown-source/
        part-0001.json             # Preserved records without usable date/host
  article_cache.sqlite3           # Ignored, disposable runtime lookup index
```

Dates are the UTC **fetch month**, not a claim about publication dates. Source
folders use a lowercase, filename-safe hostname (IDNA encoded; ports omitted).
Each part identifies its format and folder, then maps full article URLs to their
complete records. The original Markdown, timestamps, optional fields, and
failed-fetch markers survive migration unchanged. A refetch can move a URL to a
new month; its prior version remains in Git history.

## Automatic Growth and Cost Controls

The exporter sorts by fetch month, source, and URL. It starts a new numbered part
**before adding a record would exceed 1,048,576 bytes (1 MiB)**. There is no large
central URL index: the manifest has fixed-size metadata and one full-corpus hash.
Unchanged archives are byte-for-byte stable. Plain JSON lets Git compress objects
and delta repeated edits efficiently, unlike repeatedly replacing a giant gzip
blob. Historical months and unrelated sources normally stay unchanged.

`.gitattributes` explicitly disables filters, including LFS, for this archive.
The workflow separately checks both the 1 MiB file ceiling and the effective Git
filter attribute before committing. These files therefore consume ordinary Git
storage, not Git LFS storage/bandwidth. GitHub's warning threshold is 50 MiB and
its enforced ordinary-file limit is 100 MiB; this archive's cap is much smaller.
Sources: [large-file limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github),
[LFS configuration](https://docs.github.com/en/repositories/working-with-files/managing-large-files/configuring-git-large-file-storage),
[LFS billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs).

A single serialized record larger than 1 MiB fails with an explicit error; it is
never truncated or sent to LFS. The pipeline normally limits fetched article
text to 12,000 characters, far below this ceiling. If that contract changes,
introduce explicit per-article text fragments before raising the file cap.

Total repository history still grows as articles are retained. Small files solve
the recurring per-file failure and avoid LFS billing; they do not make unlimited
Git storage free of all capacity limits. Standard Actions usage remains governed
by the account's existing plan. No billing settings are changed.

## Publication and Recovery

1. Rebuild the disposable SQLite index from the committed archive. Verify every
   shard's size, schema, date/source placement, part sequence, URL uniqueness,
   total count, and aggregate checksum before replacing the local index.
2. Publishing performs indexed lookups with an 8 MiB SQLite page cache. TTL,
   historical backfill reuse, grading inputs, public feed URLs, and feed formats
   retain their existing behavior. Transactions roll back on publication errors.
3. Export a complete new archive into a temporary sibling directory. Stream SQL
   records into bounded parts, then restore and verify the staged archive.
4. Swap the verified archive into place, with a local backup for interrupted
   directory swaps. Only after full verification remove the legacy JSON.
5. Stage archive additions, changes, and deletions with generated feeds, enforce
   the small-file/no-LFS guards, and commit once. A failed job leaves remote Git
   unchanged. All writers use one fixed concurrency group and run only on main.
6. Deploy only when generation and commit succeed. A failed run leaves the last
   successfully deployed site available.

Read-only validation and local reconstruction require no GitHub API or AI calls:

```sh
python -m scripts.article_cache_archive validate
python -m scripts.article_cache_archive restore
```

After merging, the workflow can verify the migration without scraping or model
calls:

```sh
gh workflow run scrape-and-generate-rss.yml \
  --repo TedTschopp/rss.tedt.org --ref main -f archive_only=true
```

To recover, check out the desired Git commit in a clean directory and run the
restore command. The records travel with Git; no expiring backup or external
credential is needed. Do not combine shard files from different revisions.
Missing/corrupt archives fail rather than silently creating empty history.
A missing runtime database with an existing archive instructs local callers to
restore first. Legacy-only local checkouts can migrate their adjacent JSON.

Before running the offline suite in a fresh checkout, reconstruct its disposable
index with `python -m scripts.article_cache_archive restore`, then run
`python -m unittest discover -s tests -v`. CI performs both steps and therefore
also verifies every committed shard before running the tests.
