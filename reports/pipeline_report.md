# Pipeline Report

- Timestamp: 2026-11-04T05:25:54.820094Z
- Sources configured: 43
- Raw items: 4031
- Stories: 2953
- Clusters: 2925
- LLM: {'status': 'degraded', 'calls': 186, 'ok': 184, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 77, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 175, 'ok': 173, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 77, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 175}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 186
- Enrichment: 11
- Publish: 175

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.64
- normalize: 0.22
- dedupe: 0.11
- llm_enrich: 21.30
- cluster: 0.28
- score: 0.04
- write_intermediate_outputs: 0.46
- publish: 613.48
- persist_llm_cache: 0.23