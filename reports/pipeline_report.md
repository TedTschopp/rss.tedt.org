# Pipeline Report

- Timestamp: 2026-09-03T00:23:53.399884Z
- Sources configured: 43
- Raw items: 2020
- Stories: 1961
- Clusters: 1932
- LLM: {'status': 'degraded', 'calls': 136, 'ok': 133, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 43, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}}}, 'publish': {'status': 'degraded', 'calls': 125, 'ok': 122, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 43, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 125}, 'backlog': {'ai_relevance': {'before': 62, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 11}, 'ai_relevance': {'before': 62, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 136
- Enrichment: 11
- Publish: 125

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 11
- ai_relevance: 1
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 25.93
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 18.78
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 601.50
- persist_llm_cache: 0.20