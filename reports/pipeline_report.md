# Pipeline Report

- Timestamp: 2026-07-21T10:25:28.098867Z
- Sources configured: 43
- Raw items: 1821
- Stories: 1773
- Clusters: 1744
- LLM: {'status': 'degraded', 'calls': 112, 'ok': 109, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 38, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 101, 'ok': 98, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 38, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 101}, 'backlog': {'ai_relevance': {'before': 43, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 43, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 112
- Enrichment: 11
- Publish: 101

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.75
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 18.68
- cluster: 0.16
- score: 0.01
- write_intermediate_outputs: 0.21
- publish: 512.31
- persist_llm_cache: 0.15