# Pipeline Report

- Timestamp: 2026-09-05T16:13:50.716587Z
- Sources configured: 43
- Raw items: 1959
- Stories: 1918
- Clusters: 1887
- LLM: {'status': 'ok', 'calls': 130, 'ok': 130, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 37, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 119, 'ok': 119, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 62, 'importance': 37, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 119}, 'backlog': {'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 62, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 130
- Enrichment: 11
- Publish: 119

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.19
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 19.09
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 468.40
- persist_llm_cache: 0.20