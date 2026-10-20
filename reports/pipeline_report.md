# Pipeline Report

- Timestamp: 2026-10-20T00:21:28.833438Z
- Sources configured: 43
- Raw items: 2129
- Stories: 2074
- Clusters: 2045
- LLM: {'status': 'degraded', 'calls': 153, 'ok': 150, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 53, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 142, 'ok': 139, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 53, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 142}, 'backlog': {'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 13}

## LLM Calls
- Total: 153
- Enrichment: 11
- Publish: 142

## Enrichment Backlog
- Remaining: 13
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 3.46
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 16.94
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 554.06
- persist_llm_cache: 0.27