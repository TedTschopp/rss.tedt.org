# Pipeline Report

- Timestamp: 2026-09-01T04:11:32.778036Z
- Sources configured: 43
- Raw items: 3057
- Stories: 2340
- Clusters: 2312
- LLM: {'status': 'ok', 'calls': 419, 'ok': 419, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 176, 'importance': 169, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 34, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}}}, 'publish': {'status': 'ok', 'calls': 393, 'ok': 393, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 176, 'importance': 169, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 393}, 'backlog': {'ai_relevance': {'before': 176, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 34, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}, 'ai_relevance': {'before': 176, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 16}

## LLM Calls
- Total: 419
- Enrichment: 26
- Publish: 393

## Enrichment Backlog
- Remaining: 16
- embeddings: 0
- summaries: 16
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.61
- normalize: 0.11
- dedupe: 0.06
- llm_enrich: 41.64
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.33
- publish: 1660.41
- persist_llm_cache: 0.18