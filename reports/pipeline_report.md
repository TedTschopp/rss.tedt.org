# Pipeline Report

- Timestamp: 2026-10-18T03:52:45.368223Z
- Sources configured: 43
- Raw items: 2051
- Stories: 2011
- Clusters: 1983
- LLM: {'status': 'degraded', 'calls': 169, 'ok': 168, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 36, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}}}, 'publish': {'status': 'degraded', 'calls': 143, 'ok': 142, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 60, 'importance': 36, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 143}, 'backlog': {'ai_relevance': {'before': 60, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 43, 'remaining': 0}, 'summaries': {'before': 43, 'remaining': 18}, 'ai_relevance': {'before': 60, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 19}

## LLM Calls
- Total: 169
- Enrichment: 26
- Publish: 143

## Enrichment Backlog
- Remaining: 19
- embeddings: 0
- summaries: 18
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 1.70
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 29.59
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.20
- publish: 510.97
- persist_llm_cache: 0.26