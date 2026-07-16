# Pipeline Report

- Timestamp: 2026-07-16T17:22:58.204870Z
- Sources configured: 43
- Raw items: 1876
- Stories: 1819
- Clusters: 1775
- LLM: {'status': 'degraded', 'calls': 159, 'ok': 157, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 71, 'importance': 57, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 148, 'ok': 146, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 71, 'importance': 57, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 148}, 'backlog': {'ai_relevance': {'before': 71, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 71, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 2}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 12}

## LLM Calls
- Total: 159
- Enrichment: 11
- Publish: 148

## Enrichment Backlog
- Remaining: 12
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.68
- normalize: 0.05
- dedupe: 0.04
- llm_enrich: 23.51
- cluster: 0.23
- score: 0.01
- write_intermediate_outputs: 0.22
- publish: 1059.15
- persist_llm_cache: 0.25