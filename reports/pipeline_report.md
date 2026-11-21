# Pipeline Report

- Timestamp: 2026-11-21T16:08:02.461152Z
- Sources configured: 43
- Raw items: 2203
- Stories: 2175
- Clusters: 2146
- LLM: {'status': 'degraded', 'calls': 107, 'ok': 102, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 33, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 96, 'ok': 91, 'errors': 5, 'skipped': 0, 'by_kind': {'ai_relevance': 43, 'importance': 33, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 96}, 'backlog': {'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 5}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 43, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 5}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 15}

## LLM Calls
- Total: 107
- Enrichment: 11
- Publish: 96

## Enrichment Backlog
- Remaining: 15
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 5
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.03
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 16.49
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 554.31
- persist_llm_cache: 0.26