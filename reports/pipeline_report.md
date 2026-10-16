# Pipeline Report

- Timestamp: 2026-10-16T00:15:51.108110Z
- Sources configured: 43
- Raw items: 2155
- Stories: 2100
- Clusters: 2070
- LLM: {'status': 'ok', 'calls': 141, 'ok': 141, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 46, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 130, 'ok': 130, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 65, 'importance': 46, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 130}, 'backlog': {'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 65, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 141
- Enrichment: 11
- Publish: 130

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.93
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 14.85
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 264.73
- persist_llm_cache: 0.23