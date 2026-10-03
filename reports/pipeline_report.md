# Pipeline Report

- Timestamp: 2026-10-03T17:24:59.760444Z
- Sources configured: 43
- Raw items: 2000
- Stories: 1953
- Clusters: 1926
- LLM: {'status': 'ok', 'calls': 94, 'ok': 94, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 17, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 83, 'ok': 83, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 46, 'importance': 17, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 83}, 'backlog': {'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 46, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 94
- Enrichment: 11
- Publish: 83

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.89
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 15.02
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 182.09
- persist_llm_cache: 0.27