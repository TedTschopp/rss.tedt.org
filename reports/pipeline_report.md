# Pipeline Report

- Timestamp: 2026-11-08T05:02:39.278546Z
- Sources configured: 43
- Raw items: 2159
- Stories: 2109
- Clusters: 2081
- LLM: {'status': 'degraded', 'calls': 94, 'ok': 91, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 20, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 18, 'remaining': 8}}}, 'publish': {'status': 'degraded', 'calls': 83, 'ok': 80, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 20, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 83}, 'backlog': {'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 18, 'remaining': 8}, 'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 94
- Enrichment: 11
- Publish: 83

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 8
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.07
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 11.99
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 345.13
- persist_llm_cache: 0.23