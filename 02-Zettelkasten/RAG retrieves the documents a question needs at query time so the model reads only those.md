---
aliases: [RAG, retrieval-augmented generation]
created: 2026-09-20
---

A model knows only its training data and whatever is in the prompt. A company's internal docs, a codebase, last week's tickets: none of that is in either. Pasting it all into the prompt does not scale past a few pages.

<mark style="background: #FFF3A3A6;">Retrieval-augmented generation splits the job in two: a retriever finds the handful of passages relevant to the question, and the generator (the LLM) answers with those passages placed in its prompt.</mark> The name says it: generation, augmented by retrieval. Introduced by Lewis et al. at Facebook AI in 2020, it became the default way to connect an LLM to private data after 2023.

---

### The pipeline

1. **Index**: documents are chunked and each chunk is turned into an embedding vector, stored in a vector database.
2. **Retrieve**: the user's question is embedded the same way; the nearest chunks by vector similarity are pulled.
3. **Generate**: those chunks are inserted into the prompt alongside the question, and the model answers.

<mark style="background: #ABF7F7A6;">The model never sees the whole corpus; it sees a query-shaped slice of it, chosen by similarity, on every call.</mark> That is what makes RAG a context-engineering technique: it decides what goes into the window, per question, at run time.

---

### What it does and does not fix

RAG fixes staleness (index the new document, no retraining) and scale (millions of documents behind a 4k or 200k window). <mark style="background: #FF5582A6;">It does not fix retrieval quality: if the right chunk is not among the top hits, the model answers from the wrong ones with full confidence.</mark> Chunking, embedding choice and re-ranking are where RAG systems succeed or fail.

---

### Read more

- [[Context engineering curates everything in the window and not the wording of one message]]
- [[Word embeddings map tokens to high-dimensional vectors that encode meaning through context]]
- [[LLM wiki pattern replaces vector RAG with a maintained markdown knowledge graph]]
- [[AI Engineering MOC]]
