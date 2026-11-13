# Pipeline Report

- Timestamp: 2026-11-13T05:44:04.006279Z
- Sources configured: 43
- Raw items: 2240
- Stories: 2182
- Clusters: 2152
- LLM: {'status': 'degraded', 'calls': 157, 'ok': 153, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 58, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 146, 'ok': 142, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 68, 'importance': 58, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 146}, 'backlog': {'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 68, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 157
- Enrichment: 11
- Publish: 146

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.36
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 14.55
- cluster: 0.15
- score: 0.01
- write_intermediate_outputs: 0.21
- publish: 696.98
- persist_llm_cache: 0.24