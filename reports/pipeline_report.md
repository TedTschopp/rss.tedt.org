# Pipeline Report

- Timestamp: 2026-10-08T00:19:32.737032Z
- Sources configured: 43
- Raw items: 2061
- Stories: 1998
- Clusters: 1970
- LLM: {'status': 'ok', 'calls': 138, 'ok': 138, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 48, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 127, 'ok': 127, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 59, 'importance': 48, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 127}, 'backlog': {'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 59, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 138
- Enrichment: 11
- Publish: 127

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.37
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 14.72
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 377.92
- persist_llm_cache: 0.25