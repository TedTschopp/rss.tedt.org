# Pipeline Report

- Timestamp: 2026-10-14T03:54:03.629139Z
- Sources configured: 43
- Raw items: 2023
- Stories: 1975
- Clusters: 1948
- LLM: {'status': 'degraded', 'calls': 137, 'ok': 135, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 36, 'importance': 29, 'output_cleanup': 46}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}}}, 'publish': {'status': 'degraded', 'calls': 111, 'ok': 109, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 36, 'importance': 29, 'output_cleanup': 46}, 'by_model': {'openai/gpt-4.1-mini': 111}, 'backlog': {'ai_relevance': {'before': 36, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 41, 'remaining': 0}, 'summaries': {'before': 45, 'remaining': 20}, 'ai_relevance': {'before': 36, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 2}, 'output_cleanup': {'before': 46, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 137
- Enrichment: 26
- Publish: 111

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.65
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 27.99
- cluster: 0.21
- score: 0.01
- write_intermediate_outputs: 0.20
- publish: 565.34
- persist_llm_cache: 0.24