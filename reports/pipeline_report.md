# Pipeline Report

- Timestamp: 2026-08-16T08:12:38.034310Z
- Sources configured: 43
- Raw items: 1873
- Stories: 1829
- Clusters: 1800
- LLM: {'status': 'degraded', 'calls': 107, 'ok': 105, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 25, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 96, 'ok': 94, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 25, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 96}, 'backlog': {'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 107
- Enrichment: 11
- Publish: 96

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 26.02
- normalize: 0.06
- dedupe: 0.04
- llm_enrich: 15.11
- cluster: 0.23
- score: 0.02
- write_intermediate_outputs: 0.21
- publish: 338.34
- persist_llm_cache: 0.19