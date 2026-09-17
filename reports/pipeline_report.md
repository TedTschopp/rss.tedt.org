# Pipeline Report

- Timestamp: 2026-09-17T08:15:00.549948Z
- Sources configured: 43
- Raw items: 3733
- Stories: 2579
- Clusters: 2548
- LLM: {'status': 'ok', 'calls': 178, 'ok': 178, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 72, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'ok', 'calls': 167, 'ok': 167, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 72, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 167}, 'backlog': {'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 178
- Enrichment: 11
- Publish: 167

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.52
- normalize: 0.12
- dedupe: 0.06
- llm_enrich: 13.81
- cluster: 0.19
- score: 0.02
- write_intermediate_outputs: 0.36
- publish: 408.98
- persist_llm_cache: 0.15