# Pipeline Report

- Timestamp: 2026-09-08T08:15:37.420176Z
- Sources configured: 43
- Raw items: 1955
- Stories: 1907
- Clusters: 1876
- LLM: {'status': 'ok', 'calls': 127, 'ok': 127, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 45, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 116, 'ok': 116, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 45, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 116}, 'backlog': {'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 51, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 127
- Enrichment: 11
- Publish: 116

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.08
- normalize: 0.06
- dedupe: 0.06
- llm_enrich: 26.41
- cluster: 0.28
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 449.82
- persist_llm_cache: 0.21