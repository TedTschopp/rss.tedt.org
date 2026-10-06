# Pipeline Report

- Timestamp: 2026-10-06T00:19:19.700124Z
- Sources configured: 43
- Raw items: 2894
- Stories: 2842
- Clusters: 2813
- LLM: {'status': 'degraded', 'calls': 145, 'ok': 144, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 51, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 134, 'ok': 133, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 51, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 134}, 'backlog': {'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 145
- Enrichment: 11
- Publish: 134

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.74
- normalize: 0.14
- dedupe: 0.08
- llm_enrich: 17.22
- cluster: 0.27
- score: 0.03
- write_intermediate_outputs: 0.37
- publish: 331.41
- persist_llm_cache: 0.22