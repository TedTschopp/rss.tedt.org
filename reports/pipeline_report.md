# Pipeline Report

- Timestamp: 2026-08-07T16:27:20.076866Z
- Sources configured: 43
- Raw items: 1981
- Stories: 1937
- Clusters: 1910
- LLM: {'status': 'ok', 'calls': 121, 'ok': 121, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 40, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 110, 'ok': 110, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 50, 'importance': 40, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 110}, 'backlog': {'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 50, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 121
- Enrichment: 11
- Publish: 110

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.77
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 22.68
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 550.04
- persist_llm_cache: 0.21