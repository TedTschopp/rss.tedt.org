# Pipeline Report

- Timestamp: 2026-07-24T16:42:44.522157Z
- Sources configured: 43
- Raw items: 1927
- Stories: 1877
- Clusters: 1848
- LLM: {'status': 'degraded', 'calls': 130, 'ok': 128, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 55, 'importance': 44, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 119, 'ok': 117, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 55, 'importance': 44, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 119}, 'backlog': {'ai_relevance': {'before': 55, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 55, 'remaining': 1}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 130
- Enrichment: 11
- Publish: 119

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.27
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 17.46
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 594.51
- persist_llm_cache: 0.20