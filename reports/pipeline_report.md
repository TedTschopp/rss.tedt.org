# Pipeline Report

- Timestamp: 2026-11-05T16:24:22.982294Z
- Sources configured: 43
- Raw items: 2232
- Stories: 2174
- Clusters: 2146
- LLM: {'status': 'degraded', 'calls': 121, 'ok': 118, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 41, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 110, 'ok': 107, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 41, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 110}, 'backlog': {'ai_relevance': {'before': 49, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 49, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 121
- Enrichment: 11
- Publish: 110

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.41
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 15.55
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 419.14
- persist_llm_cache: 0.30