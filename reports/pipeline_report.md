# Pipeline Report

- Timestamp: 2026-10-17T00:19:08.791585Z
- Sources configured: 43
- Raw items: 2150
- Stories: 2096
- Clusters: 2068
- LLM: {'status': 'degraded', 'calls': 123, 'ok': 121, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 53, 'importance': 39, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 112, 'ok': 110, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 53, 'importance': 39, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 112}, 'backlog': {'ai_relevance': {'before': 53, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 53, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 123
- Enrichment: 11
- Publish: 112

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.90
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 13.43
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 411.93
- persist_llm_cache: 0.22