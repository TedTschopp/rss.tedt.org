# Pipeline Report

- Timestamp: 2026-10-28T08:14:22.921895Z
- Sources configured: 43
- Raw items: 4388
- Stories: 2910
- Clusters: 2883
- LLM: {'status': 'degraded', 'calls': 180, 'ok': 179, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 74, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 169, 'ok': 168, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 74, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 169}, 'backlog': {'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 180
- Enrichment: 11
- Publish: 169

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 4.60
- normalize: 0.18
- dedupe: 0.10
- llm_enrich: 16.05
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.47
- publish: 476.63
- persist_llm_cache: 0.26