# Pipeline Report

- Timestamp: 2026-08-13T16:44:33.558576Z
- Sources configured: 43
- Raw items: 1978
- Stories: 1932
- Clusters: 1904
- LLM: {'status': 'degraded', 'calls': 142, 'ok': 132, 'errors': 10, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 50, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 131, 'ok': 121, 'errors': 10, 'skipped': 0, 'by_kind': {'ai_relevance': 61, 'importance': 50, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 131}, 'backlog': {'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 10}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 61, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 10}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 142
- Enrichment: 11
- Publish: 131

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 10
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.23
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 25.35
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 1556.71
- persist_llm_cache: 0.20