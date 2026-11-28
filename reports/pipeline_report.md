# Pipeline Report

- Timestamp: 2026-11-28T12:27:15.166980Z
- Sources configured: 43
- Raw items: 2101
- Stories: 2073
- Clusters: 2043
- LLM: {'status': 'ok', 'calls': 242, 'ok': 242, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 103, 'importance': 63, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 216, 'ok': 216, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 103, 'importance': 63, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 216}, 'backlog': {'ai_relevance': {'before': 103, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 49, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 103, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 242
- Enrichment: 26
- Publish: 216

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 1.45
- normalize: 0.07
- dedupe: 0.06
- llm_enrich: 35.93
- cluster: 0.25
- score: 0.02
- write_intermediate_outputs: 0.26
- publish: 911.13
- persist_llm_cache: 0.27