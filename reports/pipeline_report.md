# Pipeline Report

- Timestamp: 2026-10-13T04:00:10.629574Z
- Sources configured: 43
- Raw items: 2012
- Stories: 1970
- Clusters: 1941
- LLM: {'status': 'ok', 'calls': 161, 'ok': 161, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 55, 'importance': 32, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}}}, 'publish': {'status': 'ok', 'calls': 135, 'ok': 135, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 55, 'importance': 32, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 135}, 'backlog': {'ai_relevance': {'before': 55, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 46, 'remaining': 0}, 'summaries': {'before': 46, 'remaining': 21}, 'ai_relevance': {'before': 55, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 161
- Enrichment: 26
- Publish: 135

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 21
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.14
- normalize: 0.04
- dedupe: 0.04
- llm_enrich: 27.54
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 350.54
- persist_llm_cache: 0.20