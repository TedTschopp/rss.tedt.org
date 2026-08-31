# Pipeline Report

- Timestamp: 2026-08-31T08:20:08.108020Z
- Sources configured: 43
- Raw items: 3093
- Stories: 2376
- Clusters: 2348
- LLM: {'status': 'ok', 'calls': 187, 'ok': 187, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 77, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 176, 'ok': 176, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 77, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 176}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 187
- Enrichment: 11
- Publish: 176

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.15
- normalize: 0.17
- dedupe: 0.09
- llm_enrich: 14.36
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.36
- publish: 698.17
- persist_llm_cache: 0.21