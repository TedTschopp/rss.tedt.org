# Pipeline Report

- Timestamp: 2026-11-20T16:57:05.349747Z
- Sources configured: 43
- Raw items: 2275
- Stories: 2245
- Clusters: 2217
- LLM: {'status': 'degraded', 'calls': 129, 'ok': 128, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 40, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 118, 'ok': 117, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 58, 'importance': 40, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 118}, 'backlog': {'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 58, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 129
- Enrichment: 11
- Publish: 118

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.77
- normalize: 0.09
- dedupe: 0.07
- llm_enrich: 18.15
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.29
- publish: 486.66
- persist_llm_cache: 0.27