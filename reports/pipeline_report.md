# Pipeline Report

- Timestamp: 2026-07-17T02:01:05.597416Z
- Sources configured: 43
- Raw items: 1570
- Stories: 1521
- Clusters: 1494
- LLM: {'status': 'degraded', 'calls': 123, 'ok': 121, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 42, 'output_cleanup': 19}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 112, 'ok': 110, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 51, 'importance': 42, 'output_cleanup': 19}, 'by_model': {'openai/gpt-4.1-mini': 112}, 'backlog': {'ai_relevance': {'before': 51, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 51, 'remaining': 1}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 19, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 123
- Enrichment: 11
- Publish: 112

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 1
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 10.40
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 17.38
- cluster: 0.20
- score: 0.01
- write_intermediate_outputs: 0.16
- publish: 546.71
- persist_llm_cache: 0.16