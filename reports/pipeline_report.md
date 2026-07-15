# Pipeline Report

- Timestamp: 2026-07-15T17:19:02.078550Z
- Sources configured: 43
- Raw items: 1947
- Stories: 1890
- Clusters: 1836
- LLM: {'status': 'degraded', 'calls': 150, 'ok': 149, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 54, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 139, 'ok': 138, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 54, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 139}, 'backlog': {'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 150
- Enrichment: 11
- Publish: 139

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.12
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 18.99
- cluster: 0.34
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 695.04
- persist_llm_cache: 0.25