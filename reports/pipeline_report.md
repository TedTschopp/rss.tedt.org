# Pipeline Report

- Timestamp: 2026-10-24T00:23:28.408072Z
- Sources configured: 43
- Raw items: 2442
- Stories: 2386
- Clusters: 2356
- LLM: {'status': 'degraded', 'calls': 169, 'ok': 165, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 66, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 158, 'ok': 154, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 72, 'importance': 66, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 158}, 'backlog': {'ai_relevance': {'before': 72, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 72, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 169
- Enrichment: 11
- Publish: 158

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.12
- normalize: 0.11
- dedupe: 0.07
- llm_enrich: 14.17
- cluster: 0.26
- score: 0.03
- write_intermediate_outputs: 0.32
- publish: 658.07
- persist_llm_cache: 0.23