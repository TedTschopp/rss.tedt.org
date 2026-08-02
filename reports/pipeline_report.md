# Pipeline Report

- Timestamp: 2026-08-02T16:30:43.320260Z
- Sources configured: 43
- Raw items: 1955
- Stories: 1905
- Clusters: 1877
- LLM: {'status': 'degraded', 'calls': 120, 'ok': 117, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 39, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 109, 'ok': 106, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 39, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 109}, 'backlog': {'ai_relevance': {'before': 50, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 50, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 120
- Enrichment: 11
- Publish: 109

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.05
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 14.97
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 585.48
- persist_llm_cache: 0.21