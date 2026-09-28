# Pipeline Report

- Timestamp: 2026-09-28T08:22:40.776128Z
- Sources configured: 43
- Raw items: 3780
- Stories: 2627
- Clusters: 2592
- LLM: {'status': 'ok', 'calls': 188, 'ok': 188, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 78, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 177, 'ok': 177, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 78, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 177}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 188
- Enrichment: 11
- Publish: 177

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.29
- normalize: 0.23
- dedupe: 0.11
- llm_enrich: 14.55
- cluster: 0.27
- score: 0.03
- write_intermediate_outputs: 0.42
- publish: 503.18
- persist_llm_cache: 0.22