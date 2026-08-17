# Pipeline Report

- Timestamp: 2026-08-17T04:02:32.419173Z
- Sources configured: 43
- Raw items: 1905
- Stories: 1862
- Clusters: 1830
- LLM: {'status': 'degraded', 'calls': 172, 'ok': 170, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 35, 'output_cleanup': 47}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 35, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}}}, 'publish': {'status': 'degraded', 'calls': 146, 'ok': 144, 'errors': 2, 'skipped': 0, 'by_kind': {'ai_relevance': 64, 'importance': 35, 'output_cleanup': 47}, 'by_model': {'openai/gpt-4.1-mini': 146}, 'backlog': {'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 2}}, 'backlog': {'embeddings': {'before': 35, 'remaining': 0}, 'summaries': {'before': 41, 'remaining': 16}, 'ai_relevance': {'before': 64, 'remaining': 0}, 'importance': {'before': 2, 'remaining': 2}, 'output_cleanup': {'before': 47, 'remaining': 0}}, 'backlog_remaining': 18}

## LLM Calls
- Total: 172
- Enrichment: 26
- Publish: 146

## Enrichment Backlog
- Remaining: 18
- embeddings: 0
- summaries: 16
- ai_relevance: 0
- importance: 2
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.58
- normalize: 0.04
- dedupe: 0.03
- llm_enrich: 35.88
- cluster: 0.20
- score: 0.01
- write_intermediate_outputs: 0.16
- publish: 764.90
- persist_llm_cache: 0.14