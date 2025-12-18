# Aggregated Feed Health Report: aggregated_ea.xml

Generated: 2025-12-18T00:57:07.797712+00:00 UTC

- Total sources: 7
- Attempted: 7  Skipped: 0  Failures: 1  With Items: 3  Recovered: 0
- Prune threshold: 3 consecutive failures (permanent classes: ssl_error,dns_error)

## Recommended Prune Candidates

- https://bizzdesign.com/blog/feed (cf=5, class=other_failure, last_error=not well-formed (invalid token): line 3, column 42)

## Source Details (first 100)

| URL | Status | Class | CF | Items | Last Status | Error Excerpt |
|-----|--------|-------|----|-------|-------------|---------------|
| https://www.forrester.com/blogs/category/enterprise-architecture/feed/ | ok | success | 0 | 10 | 200 |  |
| https://blog.opengroup.org/feed | empty | not_modified | 0 | 0 | 304 |  |
| https://www.leanix.net/en/blog/rss.xml | ok | success | 0 | 8 | 200 |  |
| https://feed.infoq.com/enterprise-architecture | ok | success | 0 | 1 | 200 |  |
| https://eapj.org/feed | empty | not_modified | 0 | 0 | 304 |  |
| https://bizzdesign.com/blog/feed | failed | other_failure | 5 | 0 | exception | not well-formed (invalid token): line 3, column 42 |
| https://www.architectureandgovernance.com/elevating-ea/feed/ | empty | not_modified | 0 | 0 | 304 |  |
