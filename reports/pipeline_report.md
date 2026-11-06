# Pipeline Report

- Timestamp: 2026-11-06T05:42:17.753646Z
- Sources configured: 43
- Raw items: 4188
- Stories: 2991
- Clusters: 2963
- LLM: {'status': 'degraded', 'calls': 188, 'ok': 186, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 77, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 177, 'ok': 175, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 80, 'importance': 77, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 177}, 'backlog': {'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 80, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 188
- Enrichment: 11
- Publish: 177

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.89
- normalize: 0.22
- dedupe: 0.11
- llm_enrich: 15.77
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.48
- publish: 506.26
- persist_llm_cache: 0.27