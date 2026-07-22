# Pipeline Report

- Timestamp: 2026-07-22T10:25:47.284876Z
- Sources configured: 43
- Raw items: 1767
- Stories: 1730
- Clusters: 1702
- LLM: {'status': 'degraded', 'calls': 111, 'ok': 108, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 34, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 100, 'ok': 97, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 34, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 100}, 'backlog': {'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 111
- Enrichment: 11
- Publish: 100

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.63
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 17.35
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 542.48
- persist_llm_cache: 0.21