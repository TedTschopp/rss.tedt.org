# Pipeline Report

- Timestamp: 2026-10-10T00:19:13.865163Z
- Sources configured: 43
- Raw items: 2147
- Stories: 2091
- Clusters: 2062
- LLM: {'status': 'ok', 'calls': 141, 'ok': 141, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 51, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 130, 'ok': 130, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 51, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 130}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 141
- Enrichment: 11
- Publish: 130

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.93
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 12.96
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 330.13
- persist_llm_cache: 0.22