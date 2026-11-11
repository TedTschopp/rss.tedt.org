# Pipeline Report

- Timestamp: 2026-11-11T05:15:29.817419Z
- Sources configured: 43
- Raw items: 4315
- Stories: 2929
- Clusters: 2903
- LLM: {'status': 'degraded', 'calls': 189, 'ok': 188, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 79, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 178, 'ok': 177, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 79, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 178}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 189
- Enrichment: 11
- Publish: 178

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.38
- normalize: 0.23
- dedupe: 0.11
- llm_enrich: 23.74
- cluster: 0.25
- score: 0.03
- write_intermediate_outputs: 0.49
- publish: 531.81
- persist_llm_cache: 0.26