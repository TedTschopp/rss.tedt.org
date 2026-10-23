# Pipeline Report

- Timestamp: 2026-10-23T08:20:48.307563Z
- Sources configured: 43
- Raw items: 4017
- Stories: 3069
- Clusters: 3039
- LLM: {'status': 'degraded', 'calls': 181, 'ok': 177, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 74, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 170, 'ok': 166, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 76, 'importance': 74, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 170}, 'backlog': {'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 76, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 181
- Enrichment: 11
- Publish: 170

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.43
- normalize: 0.19
- dedupe: 0.10
- llm_enrich: 14.72
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.57
- publish: 783.51
- persist_llm_cache: 0.28