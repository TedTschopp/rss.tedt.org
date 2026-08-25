# Pipeline Report

- Timestamp: 2026-08-25T16:27:16.299460Z
- Sources configured: 43
- Raw items: 2374
- Stories: 2316
- Clusters: 2288
- LLM: {'status': 'degraded', 'calls': 183, 'ok': 181, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 75, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 172, 'ok': 170, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 75, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 172}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 183
- Enrichment: 11
- Publish: 172

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.51
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 17.78
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 748.02
- persist_llm_cache: 0.17