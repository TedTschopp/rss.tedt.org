# Pipeline Report

- Timestamp: 2026-09-29T08:16:05.314790Z
- Sources configured: 43
- Raw items: 7931
- Stories: 4970
- Clusters: 4942
- LLM: {'status': 'degraded', 'calls': 178, 'ok': 177, 'errors': 1, 'skipped': 0, 'by_kind': {'importance': 74, 'ai_relevance': 73, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 167, 'ok': 166, 'errors': 1, 'skipped': 0, 'by_kind': {'importance': 74, 'ai_relevance': 73, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 167}, 'backlog': {'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 178
- Enrichment: 11
- Publish: 167

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.89
- normalize: 0.46
- dedupe: 0.20
- llm_enrich: 14.25
- cluster: 0.27
- score: 0.04
- write_intermediate_outputs: 1.07
- publish: 419.77
- persist_llm_cache: 0.25