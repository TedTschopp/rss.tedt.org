# Pipeline Report

- Timestamp: 2026-10-21T16:13:49.911547Z
- Sources configured: 43
- Raw items: 2193
- Stories: 2138
- Clusters: 2110
- LLM: {'status': 'ok', 'calls': 164, 'ok': 164, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 59, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 153, 'ok': 153, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 74, 'importance': 59, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 153}, 'backlog': {'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 74, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 164
- Enrichment: 11
- Publish: 153

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 17.72
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 15.62
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 433.59
- persist_llm_cache: 0.23