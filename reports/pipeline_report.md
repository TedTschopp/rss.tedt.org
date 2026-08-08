# Pipeline Report

- Timestamp: 2026-08-08T00:19:51.497470Z
- Sources configured: 43
- Raw items: 1964
- Stories: 1914
- Clusters: 1886
- LLM: {'status': 'ok', 'calls': 118, 'ok': 118, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 38, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 107, 'ok': 107, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 49, 'importance': 38, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 107}, 'backlog': {'ai_relevance': {'before': 49, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 49, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 118
- Enrichment: 11
- Publish: 107

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.80
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 19.74
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 430.53
- persist_llm_cache: 0.21