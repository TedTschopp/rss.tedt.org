# Pipeline Report

- Timestamp: 2026-10-09T08:17:56.236765Z
- Sources configured: 43
- Raw items: 4613
- Stories: 2911
- Clusters: 2881
- LLM: {'status': 'degraded', 'calls': 189, 'ok': 188, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 78, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 178, 'ok': 177, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 78, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 178}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 189
- Enrichment: 11
- Publish: 178

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.93
- normalize: 0.15
- dedupe: 0.08
- llm_enrich: 16.58
- cluster: 0.19
- score: 0.02
- write_intermediate_outputs: 0.43
- publish: 512.19
- persist_llm_cache: 0.20