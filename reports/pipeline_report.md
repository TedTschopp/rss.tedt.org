# Pipeline Report

- Timestamp: 2026-09-14T16:16:37.393746Z
- Sources configured: 43
- Raw items: 2106
- Stories: 2056
- Clusters: 2024
- LLM: {'status': 'degraded', 'calls': 174, 'ok': 171, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 66, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 18, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 163, 'ok': 160, 'errors': 3, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 66, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 163}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 3}}, 'backlog': {'embeddings': {'before': 18, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 3}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 174
- Enrichment: 11
- Publish: 163

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 3
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.06
- normalize: 0.09
- dedupe: 0.06
- llm_enrich: 31.00
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 580.61
- persist_llm_cache: 0.21