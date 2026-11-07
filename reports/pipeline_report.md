# Pipeline Report

- Timestamp: 2026-11-07T20:05:45.001097Z
- Sources configured: 43
- Raw items: 2158
- Stories: 2104
- Clusters: 2075
- LLM: {'status': 'degraded', 'calls': 104, 'ok': 102, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 31, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 93, 'ok': 91, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 42, 'importance': 31, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 93}, 'backlog': {'ai_relevance': {'before': 42, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 42, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 104
- Enrichment: 11
- Publish: 93

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.49
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 12.22
- cluster: 0.21
- score: 0.02
- write_intermediate_outputs: 0.29
- publish: 365.92
- persist_llm_cache: 0.27