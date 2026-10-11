# Pipeline Report

- Timestamp: 2026-10-11T00:18:01.264642Z
- Sources configured: 43
- Raw items: 2132
- Stories: 2085
- Clusters: 2054
- LLM: {'status': 'ok', 'calls': 104, 'ok': 104, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 25, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 93, 'ok': 93, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 48, 'importance': 25, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 93}, 'backlog': {'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 48, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 104
- Enrichment: 11
- Publish: 93

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.86
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 14.33
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 185.25
- persist_llm_cache: 0.23