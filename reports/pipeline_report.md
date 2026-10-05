# Pipeline Report

- Timestamp: 2026-10-05T08:23:11.380547Z
- Sources configured: 43
- Raw items: 4272
- Stories: 2780
- Clusters: 2751
- LLM: {'status': 'ok', 'calls': 191, 'ok': 191, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 80, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 180, 'ok': 180, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 80, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 180}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 191
- Enrichment: 11
- Publish: 180

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.14
- normalize: 0.17
- dedupe: 0.09
- llm_enrich: 14.27
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.39
- publish: 451.84
- persist_llm_cache: 0.25