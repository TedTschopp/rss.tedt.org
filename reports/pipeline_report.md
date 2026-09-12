# Pipeline Report

- Timestamp: 2026-09-12T03:51:04.441582Z
- Sources configured: 43
- Raw items: 2074
- Stories: 2022
- Clusters: 1992
- LLM: {'status': 'degraded', 'calls': 191, 'ok': 190, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 44, 'output_cleanup': 44}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 40, 'remaining': 15}}}, 'publish': {'status': 'degraded', 'calls': 165, 'ok': 164, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 77, 'importance': 44, 'output_cleanup': 44}, 'by_model': {'openai/gpt-4.1-mini': 165}, 'backlog': {'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 40, 'remaining': 15}, 'ai_relevance': {'before': 77, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 1}, 'output_cleanup': {'before': 44, 'remaining': 0}}, 'backlog_remaining': 16}

## LLM Calls
- Total: 191
- Enrichment: 26
- Publish: 165

## Enrichment Backlog
- Remaining: 16
- embeddings: 0
- summaries: 15
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.39
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 30.60
- cluster: 0.17
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 571.45
- persist_llm_cache: 0.14