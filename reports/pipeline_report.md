# Pipeline Report

- Timestamp: 2026-07-18T16:54:32.641409Z
- Sources configured: 43
- Raw items: 1835
- Stories: 1790
- Clusters: 1760
- LLM: {'status': 'degraded', 'calls': 112, 'ok': 110, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 33, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 101, 'ok': 99, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 33, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 101}, 'backlog': {'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 112
- Enrichment: 11
- Publish: 101

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.38
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 16.33
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 504.09
- persist_llm_cache: 0.21