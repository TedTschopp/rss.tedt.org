# Pipeline Report

- Timestamp: 2026-08-14T16:28:17.945000Z
- Sources configured: 43
- Raw items: 2037
- Stories: 1984
- Clusters: 1956
- LLM: {'status': 'degraded', 'calls': 137, 'ok': 136, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 48, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 126, 'ok': 125, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 48, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 126}, 'backlog': {'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 137
- Enrichment: 11
- Publish: 126

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 5.95
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 25.19
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 609.26
- persist_llm_cache: 0.21