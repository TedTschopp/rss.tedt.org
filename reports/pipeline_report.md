# Pipeline Report

- Timestamp: 2026-08-29T03:51:45.541475Z
- Sources configured: 43
- Raw items: 1852
- Stories: 1822
- Clusters: 1792
- LLM: {'status': 'degraded', 'calls': 218, 'ok': 217, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 94, 'importance': 51, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}}}, 'publish': {'status': 'degraded', 'calls': 192, 'ok': 191, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 94, 'importance': 51, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 192}, 'backlog': {'ai_relevance': {'before': 94, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 44, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}, 'ai_relevance': {'before': 94, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 19}

## LLM Calls
- Total: 218
- Enrichment: 26
- Publish: 192

## Enrichment Backlog
- Remaining: 19
- embeddings: 0
- summaries: 18
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.74
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 32.61
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.23
- publish: 737.47
- persist_llm_cache: 0.21