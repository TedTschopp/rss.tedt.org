# Pipeline Report

- Timestamp: 2026-11-14T05:32:02.581970Z
- Sources configured: 43
- Raw items: 2769
- Stories: 2717
- Clusters: 2689
- LLM: {'status': 'degraded', 'calls': 185, 'ok': 184, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 76, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'degraded', 'calls': 174, 'ok': 173, 'errors': 1, 'skipped': 0, 'by_kind': {'ai_relevance': 78, 'importance': 76, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 174}, 'backlog': {'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 1}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 78, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 1}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 11}

## LLM Calls
- Total: 185
- Enrichment: 11
- Publish: 174

## Enrichment Backlog
- Remaining: 11
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 1
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.33
- normalize: 0.09
- dedupe: 0.07
- llm_enrich: 20.95
- cluster: 0.19
- score: 0.02
- write_intermediate_outputs: 0.33
- publish: 482.65
- persist_llm_cache: 0.30