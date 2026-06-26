# Aggregated Feed Health Report: aggregated_ea.xml

Generated: 2026-06-26T02:28:44.421554+00:00 UTC

- Total sources: 7
- Attempted: 6  Skipped: 1  Failures: 1  With Items: 3  Recovered: 1
- Prune threshold: 3 consecutive failures (permanent classes: ssl_error,dns_error)

## Recommended Prune Candidates

- https://eapj.org/feed (cf=3, class=other_failure, last_error=HTTP 403)

## Source Details (first 100)

| URL | Category | Status | Class | CF | Items | Last Status | Error Excerpt |
|-----|----------|--------|-------|----|-------|-------------|---------------|
| https://feed.infoq.com/enterprise-architecture |  | empty | success | 0 | 0 | 200 |  |
| https://www.leanix.net/en/blog/rss.xml |  | ok | success | 0 | 8 | 200 |  |
| https://eapj.org/feed |  | failed | other_failure | 3 | 0 | exception | HTTP 403 |
| https://blog.opengroup.org/feed |  | ok | success | 0 | 30 | 200 |  |
| https://bizzdesign.com/blog/feed |  | skipped | skipped | 5 | 0 | exception | not well-formed (invalid token): line 3, column 42 |
| https://www.architectureandgovernance.com/elevating-ea/feed/ |  | empty | not_modified | 0 | 0 | 304 |  |
| https://www.forrester.com/blogs/category/enterprise-architecture/feed/ |  | ok | success | 0 | 10 | 200 |  |
