# Pipeline Report

- Timestamp: 2026-11-22T05:36:20.794088Z
- Sources configured: 43
- Raw items: 2161
- Stories: 2130
- Clusters: 2101
- LLM: {'status': 'ok', 'calls': 81, 'ok': 81, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 32, 'importance': 18, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 70, 'ok': 70, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 32, 'importance': 18, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 70}, 'backlog': {'ai_relevance': {'before': 32, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 32, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 81
- Enrichment: 11
- Publish: 70

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.71
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 12.16
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 127.43
- persist_llm_cache: 0.26