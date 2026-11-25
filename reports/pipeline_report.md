# Pipeline Report

- Timestamp: 2026-11-25T00:37:23.973941Z
- Sources configured: 43
- Raw items: 2290
- Stories: 2259
- Clusters: 2227
- LLM: {'status': 'ok', 'calls': 173, 'ok': 173, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 67, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 162, 'ok': 162, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 75, 'importance': 67, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 162}, 'backlog': {'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 75, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 173
- Enrichment: 11
- Publish: 162

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.27
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 16.20
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.29
- publish: 572.57
- persist_llm_cache: 0.28