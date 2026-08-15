# Pipeline Report

- Timestamp: 2026-08-15T04:00:17.017169Z
- Sources configured: 43
- Raw items: 1912
- Stories: 1875
- Clusters: 1845
- LLM: {'status': 'ok', 'calls': 216, 'ok': 216, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 94, 'importance': 48, 'output_cleanup': 48}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}}}, 'publish': {'status': 'ok', 'calls': 190, 'ok': 190, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 94, 'importance': 48, 'output_cleanup': 48}, 'by_model': {'openai/gpt-4.1-mini': 190}, 'backlog': {'ai_relevance': {'before': 94, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 37, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}, 'ai_relevance': {'before': 94, 'remaining': 0}, 'importance': {'before': 3, 'remaining': 0}, 'output_cleanup': {'before': 48, 'remaining': 0}}, 'backlog_remaining': 18}

## LLM Calls
- Total: 216
- Enrichment: 26
- Publish: 190

## Enrichment Backlog
- Remaining: 18
- embeddings: 0
- summaries: 18
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.95
- normalize: 0.07
- dedupe: 0.05
- llm_enrich: 35.17
- cluster: 0.27
- score: 0.02
- write_intermediate_outputs: 0.24
- publish: 697.04
- persist_llm_cache: 0.21