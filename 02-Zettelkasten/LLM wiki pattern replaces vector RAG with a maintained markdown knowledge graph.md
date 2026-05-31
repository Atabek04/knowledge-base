---
created: 2026-05-31
tags:
  - ai-engineering/rag
  - ai-engineering/knowledge-management
aliases: [LLM wiki, Karpathy wiki pattern]
---

<mark style="background: yellow">**LLM wiki**</mark> is a knowledge-base architecture where an LLM continuously maintains a set of interlinked markdown files — instead of re-discovering knowledge at query time via vector search.

Proposed by Andrej Karpathy (2026) as a lightweight alternative to traditional RAG.

---

### The problem with vector RAG

Standard RAG embeds documents and retrieves by semantic similarity.
Every query re-searches the same raw sources — knowledge never accumulates.

The wiki pattern inverts this: <mark style="background: cyan">knowledge compounds as new sources are ingested</mark>, because the LLM integrates each new source into the existing graph.

---

### Three-layer architecture

- **`raw/`** — immutable input dump (articles, transcripts, PDFs). Never modified.
- **`wiki/`** — LLM-generated markdown files: summaries, entities, cross-links.
- **Schema** — a `CLAUDE.md` (or equivalent) defining structure, naming rules, and workflows.

---

### Three operations

**Ingest** — process a raw source, update or create wiki pages, auto-link to related entries.

**Query** — answer a question using wiki pages; optionally file the result as a new page.

**Lint** — periodic health check: find contradictions, stale claims, orphan pages, missing links.

---

### Why it works

Every wiki dies because <mark style="background: pink">the maintenance burden grows faster than the value</mark> — cross-referencing, deduplication, and consistency checks are tedious for humans.

LLMs handle exactly that burden cheaply.
Humans curate inputs and direct analysis; the LLM does the upkeep.

---

### Tradeoffs vs vector RAG

| | LLM wiki | Vector RAG |
|---|---|---|
| Infrastructure | None (markdown + LLM) | Vector DB + embedding model |
| Knowledge | Compounds over time | Stateless per query |
| Retrieval | Graph traversal / keyword | Semantic similarity |
| Scale | Individual / small team | Enterprise |
| Cost | LLM tokens only | Embedding + DB infra |

---

### Read more

- [[AI Engineering MOC]]
- [[LLM training uses next-token prediction on existing text to learn statistical patterns]]
