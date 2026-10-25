# Pipeline Report

- Timestamp: 2026-10-25T03:56:52.067908Z
- Sources configured: 43
- Raw items: 2058
- Stories: 2011
- Clusters: 1983
- LLM: {'status': 'ok', 'calls': 161, 'ok': 161, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 56, 'importance': 31, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'ok', 'calls': 135, 'ok': 135, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 56, 'importance': 31, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 135}, 'backlog': {'ai_relevance': {'before': 56, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 42, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 56, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 20}

## LLM Calls
- Total: 161
- Enrichment: 26
- Publish: 135

## Enrichment Backlog
- Remaining: 20
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 43.27
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 27.61
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 519.44
- persist_llm_cache: 0.22