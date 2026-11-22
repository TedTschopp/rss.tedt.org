# Pipeline Report

- Timestamp: 2026-11-22T16:07:40.577861Z
- Sources configured: 43
- Raw items: 2138
- Stories: 2110
- Clusters: 2082
- LLM: {'status': 'degraded', 'calls': 117, 'ok': 116, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 54, 'importance': 32, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}}}, 'publish': {'status': 'degraded', 'calls': 106, 'ok': 105, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 54, 'importance': 32, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 106}, 'backlog': {'ai_relevance': {'before': 54, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 19, 'remaining': 0}, 'summaries': {'before': 19, 'remaining': 9}, 'ai_relevance': {'before': 54, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 117
- Enrichment: 11
- Publish: 106

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 9
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.95
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 14.91
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.25
- publish: 348.76
- persist_llm_cache: 0.24