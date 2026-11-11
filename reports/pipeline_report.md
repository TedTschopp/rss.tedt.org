# Pipeline Report

- Timestamp: 2026-11-11T16:07:56.137570Z
- Sources configured: 43
- Raw items: 3016
- Stories: 2958
- Clusters: 2927
- LLM: {'status': 'degraded', 'calls': 179, 'ok': 178, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 73, 'output_cleanup': 18}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 168, 'ok': 167, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 73, 'output_cleanup': 18}, 'by_model': {'openai/gpt-4.1-mini': 168}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 18, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 18, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 179
- Enrichment: 11
- Publish: 168

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 5.23
- normalize: 0.10
- dedupe: 0.07
- llm_enrich: 15.11
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.34
- publish: 633.56
- persist_llm_cache: 0.27