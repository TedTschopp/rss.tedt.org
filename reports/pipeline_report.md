# Pipeline Report

- Timestamp: 2026-10-31T08:14:23.412245Z
- Sources configured: 43
- Raw items: 3283
- Stories: 2634
- Clusters: 2608
- LLM: {'status': 'ok', 'calls': 184, 'ok': 184, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 75, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 173, 'ok': 173, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 75, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 173}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 184
- Enrichment: 11
- Publish: 173

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.69
- normalize: 0.16
- dedupe: 0.09
- llm_enrich: 13.35
- cluster: 0.26
- score: 0.03
- write_intermediate_outputs: 0.38
- publish: 514.28
- persist_llm_cache: 0.23