# Pipeline Report

- Timestamp: 2026-08-10T08:42:27.479379Z
- Sources configured: 43
- Raw items: 1849
- Stories: 1811
- Clusters: 1783
- LLM: {'status': 'degraded', 'calls': 127, 'ok': 125, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 55, 'importance': 41, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 116, 'ok': 114, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 55, 'importance': 41, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 116}, 'backlog': {'ai_relevance': {'before': 55, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 55, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 127
- Enrichment: 11
- Publish: 116

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.58
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 21.88
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.21
- publish: 604.19
- persist_llm_cache: 0.19