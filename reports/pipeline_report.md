# Pipeline Report

- Timestamp: 2026-11-10T16:25:38.693824Z
- Sources configured: 43
- Raw items: 2149
- Stories: 2090
- Clusters: 2063
- LLM: {'status': 'degraded', 'calls': 173, 'ok': 169, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 64, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 162, 'ok': 158, 'errors': 4, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 64, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 162}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 4}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 4}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 14}

## LLM Calls
- Total: 173
- Enrichment: 11
- Publish: 162

## Enrichment Backlog
- Remaining: 14
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 4
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.76
- normalize: 0.05
- dedupe: 0.05
- llm_enrich: 16.13
- cluster: 0.20
- score: 0.02
- write_intermediate_outputs: 0.32
- publish: 704.37
- persist_llm_cache: 0.26