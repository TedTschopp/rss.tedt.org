# Pipeline Report

- Timestamp: 2026-11-27T13:15:00.428032Z
- Sources configured: 43
- Raw items: 2230
- Stories: 2200
- Clusters: 2165
- LLM: {'status': 'ok', 'calls': 236, 'ok': 236, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 91, 'importance': 70, 'output_cleanup': 49}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}}}, 'publish': {'status': 'ok', 'calls': 210, 'ok': 210, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 91, 'importance': 70, 'output_cleanup': 49}, 'by_model': {'openai/gpt-4.1-mini': 210}, 'backlog': {'ai_relevance': {'before': 91, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 45, 'remaining': 0}, 'summaries': {'before': 47, 'remaining': 22}, 'ai_relevance': {'before': 91, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 236
- Enrichment: 26
- Publish: 210

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 22
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.91
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 36.85
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 955.39
- persist_llm_cache: 0.30