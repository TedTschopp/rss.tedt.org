# Pipeline Report

- Timestamp: 2026-10-18T16:10:30.752827Z
- Sources configured: 43
- Raw items: 2122
- Stories: 2076
- Clusters: 2048
- LLM: {'status': 'degraded', 'calls': 118, 'ok': 117, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 39, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 107, 'ok': 106, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 39, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 107}, 'backlog': {'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 118
- Enrichment: 11
- Publish: 107

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.01
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 12.86
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 290.90
- persist_llm_cache: 0.22