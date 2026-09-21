# Pipeline Report

- Timestamp: 2026-09-21T08:19:13.299640Z
- Sources configured: 43
- Raw items: 3234
- Stories: 2386
- Clusters: 2357
- LLM: {'status': 'degraded', 'calls': 189, 'ok': 187, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 79, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 178, 'ok': 176, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 79, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 178}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 189
- Enrichment: 11
- Publish: 178

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.01
- normalize: 0.17
- dedupe: 0.09
- llm_enrich: 15.47
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.37
- publish: 651.43
- persist_llm_cache: 0.22