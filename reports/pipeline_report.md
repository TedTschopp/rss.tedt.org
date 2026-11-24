# Pipeline Report

- Timestamp: 2026-11-24T14:25:24.841622Z
- Sources configured: 43
- Raw items: 2154
- Stories: 2124
- Clusters: 2092
- LLM: {'status': 'degraded', 'calls': 225, 'ok': 223, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 89, 'importance': 62, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 48, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 23}}}, 'publish': {'status': 'degraded', 'calls': 199, 'ok': 197, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 89, 'importance': 62, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 199}, 'backlog': {'ai_relevance': {'before': 89, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 48, 'remaining': 0}, 'summaries': {'before': 48, 'remaining': 23}, 'ai_relevance': {'before': 89, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 225
- Enrichment: 26
- Publish: 199

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 23
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.71
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 34.33
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 982.28
- persist_llm_cache: 0.27