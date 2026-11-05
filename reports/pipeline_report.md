# Pipeline Report

- Timestamp: 2026-11-05T05:43:36.384627Z
- Sources configured: 43
- Raw items: 4182
- Stories: 3239
- Clusters: 3211
- LLM: {'status': 'degraded', 'calls': 177, 'ok': 176, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 72, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 166, 'ok': 165, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 72, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 166}, 'backlog': {'ai_relevance': {'before': 74, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 74, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 177
- Enrichment: 11
- Publish: 166

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.44
- normalize: 0.23
- dedupe: 0.11
- llm_enrich: 16.01
- cluster: 0.25
- score: 0.04
- write_intermediate_outputs: 0.51
- publish: 418.57
- persist_llm_cache: 0.27