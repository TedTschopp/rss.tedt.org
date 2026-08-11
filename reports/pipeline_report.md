# Pipeline Report

- Timestamp: 2026-08-11T04:39:47.399204Z
- Sources configured: 43
- Raw items: 5457
- Stories: 3035
- Clusters: 3008
- LLM: {'status': 'ok', 'calls': 462, 'ok': 462, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 194, 'importance': 192, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 436, 'ok': 436, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 194, 'importance': 192, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 436}, 'backlog': {'ai_relevance': {'before': 194, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 194, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 462
- Enrichment: 26
- Publish: 436

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.34
- normalize: 0.35
- dedupe: 0.15
- llm_enrich: 79.96
- cluster: 0.26
- score: 0.03
- write_intermediate_outputs: 0.59
- publish: 2115.75
- persist_llm_cache: 0.23