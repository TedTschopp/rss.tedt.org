# Pipeline Report

- Timestamp: 2026-10-10T03:56:06.051326Z
- Sources configured: 43
- Raw items: 2094
- Stories: 2040
- Clusters: 2010
- LLM: {'status': 'degraded', 'calls': 175, 'ok': 174, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 30, 'output_cleanup': 46}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}}}, 'publish': {'status': 'degraded', 'calls': 149, 'ok': 148, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 73, 'importance': 30, 'output_cleanup': 46}, 'by_model': {'openai/gpt-4.1-mini': 149}, 'backlog': {'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}, 'ai_relevance': {'before': 73, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 18}

## LLM Calls
- Total: 175
- Enrichment: 26
- Publish: 149

## Enrichment Backlog
- Remaining: 18
- embeddings: 0
- summaries: 17
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.97
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 28.60
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.32
- publish: 413.92
- persist_llm_cache: 0.24