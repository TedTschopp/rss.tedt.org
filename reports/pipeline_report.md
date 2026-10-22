# Pipeline Report

- Timestamp: 2026-10-22T16:15:32.216209Z
- Sources configured: 43
- Raw items: 2227
- Stories: 2177
- Clusters: 2148
- LLM: {'status': 'degraded', 'calls': 157, 'ok': 155, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 56, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 146, 'ok': 144, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 56, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 146}, 'backlog': {'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 157
- Enrichment: 11
- Publish: 146

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.26
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 14.48
- cluster: 0.16
- score: 0.01
- write_intermediate_outputs: 0.21
- publish: 527.18
- persist_llm_cache: 0.22