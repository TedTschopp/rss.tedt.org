# Pipeline Report

- Timestamp: 2026-09-04T00:20:06.541441Z
- Sources configured: 43
- Raw items: 2030
- Stories: 1980
- Clusters: 1952
- LLM: {'status': 'ok', 'calls': 150, 'ok': 150, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 49, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 139, 'ok': 139, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 49, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 139}, 'backlog': {'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 150
- Enrichment: 11
- Publish: 139

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.97
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 21.60
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 456.31
- persist_llm_cache: 0.21