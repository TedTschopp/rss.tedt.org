# Pipeline Report

- Timestamp: 2026-08-30T03:54:52.817621Z
- Sources configured: 43
- Raw items: 1898
- Stories: 1857
- Clusters: 1829
- LLM: {'status': 'degraded', 'calls': 219, 'ok': 217, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 87, 'importance': 56, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 20}}}, 'publish': {'status': 'degraded', 'calls': 193, 'ok': 191, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 87, 'importance': 56, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 193}, 'backlog': {'ai_relevance': {'before': 87, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 2}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 44, 'remaining': 20}, 'ai_relevance': {'before': 87, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 2}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 22}

## LLM Calls
- Total: 219
- Enrichment: 26
- Publish: 193

## Enrichment Backlog
- Remaining: 22
- embeddings: 0
- summaries: 20
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.95
- normalize: 0.08
- dedupe: 0.05
- llm_enrich: 31.08
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 818.23
- persist_llm_cache: 0.20