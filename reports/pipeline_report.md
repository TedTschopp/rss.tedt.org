# Pipeline Report

- Timestamp: 2026-09-10T16:16:20.882201Z
- Sources configured: 43
- Raw items: 2009
- Stories: 1954
- Clusters: 1924
- LLM: {'status': 'degraded', 'calls': 171, 'ok': 170, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 67, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 160, 'ok': 159, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 67, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 160}, 'backlog': {'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 171
- Enrichment: 11
- Publish: 160

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.43
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 16.01
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 581.65
- persist_llm_cache: 0.21