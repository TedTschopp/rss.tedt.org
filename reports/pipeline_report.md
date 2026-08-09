# Pipeline Report

- Timestamp: 2026-08-09T16:20:19.560283Z
- Sources configured: 43
- Raw items: 1984
- Stories: 1935
- Clusters: 1907
- LLM: {'status': 'degraded', 'calls': 135, 'ok': 134, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 56, 'importance': 48, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 124, 'ok': 123, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 56, 'importance': 48, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 124}, 'backlog': {'ai_relevance': {'before': 56, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 56, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 135
- Enrichment: 11
- Publish: 124

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.79
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 18.68
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 684.78
- persist_llm_cache: 0.21