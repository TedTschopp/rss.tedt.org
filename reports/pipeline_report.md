# Pipeline Report

- Timestamp: 2026-11-18T06:31:39.218034Z
- Sources configured: 43
- Raw items: 4173
- Stories: 2874
- Clusters: 2846
- LLM: {'status': 'ok', 'calls': 185, 'ok': 185, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 75, 'output_cleanup': 20}, 'stages': {'enrichment': {'status': 'ok', 'calls': 11, 'ok': 11, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}}}, 'publish': {'status': 'ok', 'calls': 174, 'ok': 174, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 79, 'importance': 75, 'output_cleanup': 20}, 'by_model': {'openai/gpt-4.1-mini': 174}, 'backlog': {'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 20, 'remaining': 0}, 'summaries': {'before': 20, 'remaining': 10}, 'ai_relevance': {'before': 79, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 20, 'remaining': 0}}, 'backlog_remaining': 10}

## LLM Calls
- Total: 185
- Enrichment: 11
- Publish: 174

## Enrichment Backlog
- Remaining: 10
- embeddings: 0
- summaries: 10
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.01
- ingestion: 2.32
- normalize: 0.13
- dedupe: 0.07
- llm_enrich: 13.50
- cluster: 0.16
- score: 0.02
- write_intermediate_outputs: 0.37
- publish: 602.47
- persist_llm_cache: 0.20