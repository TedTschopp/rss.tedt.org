# Pipeline Report

- Timestamp: 2026-09-23T08:17:53.814691Z
- Sources configured: 43
- Raw items: 4279
- Stories: 3339
- Clusters: 3310
- LLM: {'status': 'ok', 'calls': 187, 'ok': 187, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 77, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'ok', 'calls': 176, 'ok': 176, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 77, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 176}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 9}

## LLM Calls
- Total: 187
- Enrichment: 11
- Publish: 176

## Enrichment Backlog
- Remaining: 9
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.79
- normalize: 0.24
- dedupe: 0.11
- llm_enrich: 19.83
- cluster: 0.27
- score: 0.04
- write_intermediate_outputs: 0.50
- publish: 584.38
- persist_llm_cache: 0.21