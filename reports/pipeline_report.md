# Pipeline Report

- Timestamp: 2026-09-28T00:18:54.791319Z
- Sources configured: 43
- Raw items: 2017
- Stories: 1972
- Clusters: 1943
- LLM: {'status': 'degraded', 'calls': 144, 'ok': 143, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 40, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'degraded', 'calls': 11, 'ok': 10, 'errors': 1, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 20}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 133, 'ok': 133, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 40, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 133}, 'backlog': {'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 20}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 30}

## LLM Calls
- Total: 144
- Enrichment: 11
- Publish: 133

## Enrichment Backlog
- Remaining: 30
- embeddings: 20
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.13
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 14.16
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 246.37
- persist_llm_cache: 0.21