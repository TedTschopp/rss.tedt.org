# Pipeline Report

- Timestamp: 2026-07-15T05:25:55.833858Z
- Sources configured: 43
- Raw items: 1786
- Stories: 1754
- Clusters: 1737
- LLM: {'status': 'degraded', 'calls': 988, 'ok': 987, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 235, 'output_cleanup': 250}, 'stages': {'enrichment': {'status': 'ok', 'calls': 253, 'ok': 253, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 1718, 'remaining': 1468}, 'summaries': {'before': 1697, 'remaining': 1447}}}, 'publish': {'status': 'degraded', 'calls': 735, 'ok': 734, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 250, 'importance': 235, 'output_cleanup': 250}, 'by_model': {'openai/gpt-4.1-mini': 735}, 'backlog': {'ai_relevance': {'before': 1384, 'remaining': 1134}, 'importance': {'before': 24, 'remaining': 1}, 'output_cleanup': {'before': 1477, 'remaining': 1227}}, 'backlog_remaining': 2362}}, 'backlog': {'embeddings': {'before': 1718, 'remaining': 1468}, 'summaries': {'before': 1697, 'remaining': 1447}, 'ai_relevance': {'before': 1384, 'remaining': 1134}, 'importance': {'before': 24, 'remaining': 1}, 'output_cleanup': {'before': 1477, 'remaining': 1227}}, 'backlog_remaining': 5277}

## LLM Calls
- Total: 988
- Enrichment: 253
- Publish: 735

## Enrichment Backlog
- Remaining: 5277
- embeddings: 1468
- summaries: 1447
- ai_relevance: 1134
- importance: 1
- output_cleanup: 1227

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.47
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 263.47
- cluster: 0.08
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 779.07
- persist_llm_cache: 0.11