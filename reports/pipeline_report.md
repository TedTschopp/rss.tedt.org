# Pipeline Report

- Timestamp: 2026-11-08T20:23:10.029107Z
- Sources configured: 43
- Raw items: 2142
- Stories: 2091
- Clusters: 2063
- LLM: {'status': 'degraded', 'calls': 106, 'ok': 103, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 30, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 95, 'ok': 92, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 45, 'importance': 30, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 95}, 'backlog': {'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 45, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 106
- Enrichment: 11
- Publish: 95

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.40
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 13.11
- cluster: 0.21
- score: 0.01
- write_intermediate_outputs: 0.17
- publish: 335.73
- persist_llm_cache: 0.24