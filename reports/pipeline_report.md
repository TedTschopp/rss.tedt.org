# Pipeline Report

- Timestamp: 2026-08-04T00:34:31.262657Z
- Sources configured: 43
- Raw items: 1937
- Stories: 1885
- Clusters: 1856
- LLM: {'status': 'degraded', 'calls': 124, 'ok': 122, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 53, 'importance': 40, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 113, 'ok': 111, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 53, 'importance': 40, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 113}, 'backlog': {'ai_relevance': {'before': 53, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 53, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 124
- Enrichment: 11
- Publish: 113

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.71
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 18.43
- cluster: 0.19
- score: 0.02
- write_intermediate_outputs: 0.20
- publish: 494.47
- persist_llm_cache: 0.17