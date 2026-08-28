# Pipeline Report

- Timestamp: 2026-08-28T02:51:22.889256Z
- Sources configured: 43
- Raw items: 3416
- Stories: 2510
- Clusters: 2482
- LLM: {'status': 'degraded', 'calls': 162, 'ok': 160, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 62, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 151, 'ok': 149, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 69, 'importance': 62, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 151}, 'backlog': {'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 69, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 162
- Enrichment: 11
- Publish: 151

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.71
- normalize: 0.19
- dedupe: 0.09
- llm_enrich: 18.18
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.39
- publish: 671.42
- persist_llm_cache: 0.20