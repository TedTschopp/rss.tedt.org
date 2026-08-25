# Pipeline Report

- Timestamp: 2026-08-25T08:26:08.036684Z
- Sources configured: 43
- Raw items: 4999
- Stories: 2965
- Clusters: 2937
- LLM: {'status': 'ok', 'calls': 186, 'ok': 186, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 77, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 175, 'ok': 175, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 77, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 175}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 186
- Enrichment: 11
- Publish: 175

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 3.09
- normalize: 0.22
- dedupe: 0.10
- llm_enrich: 20.41
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.54
- publish: 654.82
- persist_llm_cache: 0.17