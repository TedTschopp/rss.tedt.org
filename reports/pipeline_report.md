# Pipeline Report

- Timestamp: 2026-09-02T08:18:22.460597Z
- Sources configured: 43
- Raw items: 4308
- Stories: 2733
- Clusters: 2704
- LLM: {'status': 'ok', 'calls': 173, 'ok': 173, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 68, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 162, 'ok': 162, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 68, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 162}, 'backlog': {'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 173
- Enrichment: 11
- Publish: 162

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 3.03
- normalize: 0.23
- dedupe: 0.12
- llm_enrich: 14.40
- cluster: 0.28
- score: 0.03
- write_intermediate_outputs: 0.47
- publish: 624.58
- persist_llm_cache: 0.22