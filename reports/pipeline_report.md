# Pipeline Report

- Timestamp: 2026-09-11T16:17:34.043418Z
- Sources configured: 43
- Raw items: 2087
- Stories: 2037
- Clusters: 2009
- LLM: {'status': 'degraded', 'calls': 156, 'ok': 153, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 57, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 145, 'ok': 142, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 57, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 145}, 'backlog': {'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 156
- Enrichment: 11
- Publish: 145

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.43
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 18.69
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.20
- publish: 627.58
- persist_llm_cache: 0.13