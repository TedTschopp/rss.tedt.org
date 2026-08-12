# Pipeline Report

- Timestamp: 2026-08-12T16:38:06.878819Z
- Sources configured: 43
- Raw items: 2052
- Stories: 2005
- Clusters: 1974
- LLM: {'status': 'degraded', 'calls': 163, 'ok': 157, 'errors': 6, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 62, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 152, 'ok': 146, 'errors': 6, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 62, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 152}, 'backlog': {'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 6}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 6}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 6}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 16}

## LLM Calls
- Total: 163
- Enrichment: 11
- Publish: 152

## Enrichment Backlog
- Remaining: 16
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 6
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.40
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 20.90
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 1144.52
- persist_llm_cache: 0.21