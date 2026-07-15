# Pipeline Report

- Timestamp: 2026-07-15T10:01:22.559665Z
- Sources configured: 43
- Raw items: 1731
- Stories: 1691
- Clusters: 1632
- LLM: {'status': 'degraded', 'calls': 121, 'ok': 119, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 71, 'importance': 23, 'output_cleanup': 17}, 'stages': {'enrichment': {'status': 'ok', 'calls': 10, 'ok': 10, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 9, 'remaining': 0}, 'summaries': {'before': 9, 'remaining': 0}}}, 'publish': {'status': 'degraded', 'calls': 111, 'ok': 109, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 71, 'importance': 23, 'output_cleanup': 17}, 'by_model': {'openai/gpt-4.1-mini': 111}, 'backlog': {'ai_relevance': {'before': 71, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 17, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 9, 'remaining': 0}, 'summaries': {'before': 9, 'remaining': 0}, 'ai_relevance': {'before': 71, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 17, 'remaining': 0}}, 'backlog_remaining': 2}

## LLM Calls
- Total: 121
- Enrichment: 10
- Publish: 111

## Enrichment Backlog
- Remaining: 2
- embeddings: 0
- summaries: 0
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.07
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 15.76
- cluster: 0.34
- score: 0.02
- write_intermediate_outputs: 0.22
- publish: 522.09
- persist_llm_cache: 0.26