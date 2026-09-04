# Pipeline Report

- Timestamp: 2026-09-04T16:16:15.211887Z
- Sources configured: 43
- Raw items: 2598
- Stories: 2543
- Clusters: 2515
- LLM: {'status': 'degraded', 'calls': 161, 'ok': 160, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 64, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 150, 'ok': 149, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 66, 'importance': 64, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 150}, 'backlog': {'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 66, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 161
- Enrichment: 11
- Publish: 150

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.42
- normalize: 0.12
- dedupe: 0.08
- llm_enrich: 17.95
- cluster: 0.24
- score: 0.03
- write_intermediate_outputs: 0.33
- publish: 583.20
- persist_llm_cache: 0.21