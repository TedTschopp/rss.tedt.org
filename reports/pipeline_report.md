# Pipeline Report

- Timestamp: 2026-11-09T12:21:07.559837Z
- Sources configured: 43
- Raw items: 2179
- Stories: 2132
- Clusters: 2103
- LLM: {'status': 'degraded', 'calls': 225, 'ok': 221, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 81, 'importance': 68, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'degraded', 'calls': 199, 'ok': 195, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 81, 'importance': 68, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 199}, 'backlog': {'ai_relevance': {'before': 81, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 4}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 81, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 4}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 29}

## LLM Calls
- Total: 225
- Enrichment: 26
- Publish: 199

## Enrichment Backlog
- Remaining: 29
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.41
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 30.57
- cluster: 0.14
- score: 0.01
- write_intermediate_outputs: 0.19
- publish: 1258.89
- persist_llm_cache: 0.23