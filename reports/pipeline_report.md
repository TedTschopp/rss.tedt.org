# Pipeline Report

- Timestamp: 2026-10-19T03:59:32.376947Z
- Sources configured: 43
- Raw items: 2063
- Stories: 2019
- Clusters: 1986
- LLM: {'status': 'degraded', 'calls': 183, 'ok': 182, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 54, 'output_cleanup': 43}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'degraded', 'calls': 157, 'ok': 156, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 54, 'output_cleanup': 43}, 'by_model': {'openai/gpt-4.1-mini': 157}, 'backlog': {'ai_relevance': {'before': 60, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 43, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 60, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 43, 'remaining': 0}}, 'backlog_remaining': 21}

## LLM Calls
- Total: 183
- Enrichment: 26
- Publish: 157

## Enrichment Backlog
- Remaining: 21
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.78
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 27.49
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 665.80
- persist_llm_cache: 0.23