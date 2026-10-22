# Pipeline Report

- Timestamp: 2026-10-22T00:16:52.270304Z
- Sources configured: 43
- Raw items: 2139
- Stories: 2084
- Clusters: 2056
- LLM: {'status': 'degraded', 'calls': 129, 'ok': 128, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 41, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 118, 'ok': 117, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 57, 'importance': 41, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 118}, 'backlog': {'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 57, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 129
- Enrichment: 11
- Publish: 118

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.40
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 16.09
- cluster: 0.24
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 320.44
- persist_llm_cache: 0.21