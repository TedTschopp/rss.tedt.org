# Pipeline Report

- Timestamp: 2026-09-21T03:54:36.211597Z
- Sources configured: 43
- Raw items: 1943
- Stories: 1902
- Clusters: 1874
- LLM: {'status': 'degraded', 'calls': 216, 'ok': 215, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 85, 'importance': 56, 'output_cleanup': 49}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}}}, 'publish': {'status': 'degraded', 'calls': 190, 'ok': 189, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 85, 'importance': 56, 'output_cleanup': 49}, 'by_model': {'openai/gpt-4.1-mini': 190}, 'backlog': {'ai_relevance': {'before': 85, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 42, 'remaining': 17}, 'ai_relevance': {'before': 85, 'remaining': 0}, 'importance': {'before': 1, 'remaining': 1}, 'output_cleanup': {'before': 49, 'remaining': 0}}, 'backlog_remaining': 18}

## LLM Calls
- Total: 216
- Enrichment: 26
- Publish: 190

## Enrichment Backlog
- Remaining: 18
- embeddings: 0
- summaries: 17
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 3.19
- normalize: 0.03
- dedupe: 0.03
- llm_enrich: 29.00
- cluster: 0.18
- score: 0.01
- write_intermediate_outputs: 0.18
- publish: 528.17
- persist_llm_cache: 0.14