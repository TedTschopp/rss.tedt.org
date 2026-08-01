# Pipeline Report

- Timestamp: 2026-08-01T00:32:24.110729Z
- Sources configured: 43
- Raw items: 1935
- Stories: 1901
- Clusters: 1873
- LLM: {'status': 'ok', 'calls': 148, 'ok': 148, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 53, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 137, 'ok': 137, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 53, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 137}, 'backlog': {'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 148
- Enrichment: 11
- Publish: 137

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.94
- normalize: 0.08
- dedupe: 0.06
- llm_enrich: 14.00
- cluster: 0.26
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 446.45
- persist_llm_cache: 0.22