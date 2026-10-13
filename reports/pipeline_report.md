# Pipeline Report

- Timestamp: 2026-10-13T16:15:28.303215Z
- Sources configured: 43
- Raw items: 2182
- Stories: 2131
- Clusters: 2104
- LLM: {'status': 'degraded', 'calls': 154, 'ok': 153, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 53, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 143, 'ok': 142, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 70, 'importance': 53, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 143}, 'backlog': {'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 70, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 154
- Enrichment: 11
- Publish: 143

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.76
- normalize: 0.06
- dedupe: 0.05
- llm_enrich: 17.52
- cluster: 0.22
- score: 0.02
- write_intermediate_outputs: 0.27
- publish: 502.30
- persist_llm_cache: 0.25