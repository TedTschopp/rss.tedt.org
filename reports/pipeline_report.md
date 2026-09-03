# Pipeline Report

- Timestamp: 2026-09-03T08:12:57.914803Z
- Sources configured: 43
- Raw items: 1945
- Stories: 1901
- Clusters: 1873
- LLM: {'status': 'degraded', 'calls': 92, 'ok': 91, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 38, 'importance': 24, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 81, 'ok': 80, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 38, 'importance': 24, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 81}, 'backlog': {'ai_relevance': {'before': 38, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 38, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 92
- Enrichment: 11
- Publish: 81

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.93
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 18.37
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 308.20
- persist_llm_cache: 0.20