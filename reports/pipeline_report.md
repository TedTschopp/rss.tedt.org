# Pipeline Report

- Timestamp: 2026-08-30T16:15:39.718096Z
- Sources configured: 43
- Raw items: 1708
- Stories: 1656
- Clusters: 1629
- LLM: {'status': 'degraded', 'calls': 131, 'ok': 130, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 52, 'importance': 48, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 120, 'ok': 119, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 52, 'importance': 48, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 120}, 'backlog': {'ai_relevance': {'before': 52, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 52, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 131
- Enrichment: 11
- Publish: 120

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 10.63
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 16.87
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 480.55
- persist_llm_cache: 0.20