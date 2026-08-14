# Pipeline Report

- Timestamp: 2026-08-14T04:46:25.072504Z
- Sources configured: 43
- Raw items: 3476
- Stories: 2782
- Clusters: 2752
- LLM: {'status': 'ok', 'calls': 466, 'ok': 466, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 195, 'importance': 195, 'output_cleanup': 50}, 'stages': {'enrichment': {'status': 'ok', 'calls': 26, 'ok': 26, 'errors': 0, 'skipped': 0, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}}}, 'publish': {'status': 'ok', 'calls': 440, 'ok': 440, 'errors': 0, 'skipped': 0, 'by_kind': {'ai_relevance': 195, 'importance': 195, 'output_cleanup': 50}, 'by_model': {'openai/gpt-4.1-mini': 440}, 'backlog': {'ai_relevance': {'before': 195, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 0}}, 'backlog': {'embeddings': {'before': 50, 'remaining': 0}, 'summaries': {'before': 50, 'remaining': 25}, 'ai_relevance': {'before': 195, 'remaining': 0}, 'importance': {'before': 0, 'remaining': 0}, 'output_cleanup': {'before': 50, 'remaining': 0}}, 'backlog_remaining': 25}

## LLM Calls
- Total: 466
- Enrichment: 26
- Publish: 440

## Enrichment Backlog
- Remaining: 25
- embeddings: 0
- summaries: 25
- ai_relevance: 0
- importance: 0
- output_cleanup: 0

## Stage Timings (seconds)
- load_sources_and_state: 0.02
- ingestion: 2.54
- normalize: 0.17
- dedupe: 0.09
- llm_enrich: 82.37
- cluster: 0.28
- score: 0.03
- write_intermediate_outputs: 0.41
- publish: 1656.13
- persist_llm_cache: 0.24