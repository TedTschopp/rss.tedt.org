# Pipeline Report

- Timestamp: 2026-08-10T16:30:53.115666Z
- Sources configured: 43
- Raw items: 1999
- Stories: 1951
- Clusters: 1923
- LLM: {'status': 'degraded', 'calls': 165, 'ok': 164, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 61, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 154, 'ok': 153, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 61, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 154}, 'backlog': {'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 165
- Enrichment: 11
- Publish: 154

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.91
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 19.58
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 780.50
- persist_llm_cache: 0.21