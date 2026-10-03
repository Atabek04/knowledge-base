---
aliases: [context rot, long-context degradation]
created: 2026-10-03
---

A model's context window has an advertised size: 200k tokens, 1M tokens. The natural assumption is that anything inside that limit is read equally well, so a bigger window means more can be handed over safely.

<mark style="background: #FFF3A3A6;">Context rot is the measurable drop in an LLM's output quality as the number of input tokens grows, even when the input is far below the window limit.</mark> The name fits: the context does not run out, it decays, and the longer it sits and grows, the less reliably the model uses it.

The term comes from Chroma's July 2025 technical report, which tested 18 frontier models (GPT-4.1, Claude 4, Gemini 2.5, Qwen3) on deliberately simple tasks such as finding one fact in a long text or copying a list of repeated words.

---

### What the experiments showed

#### Degradation at every length

Accuracy fell with each length increment, not only near the limit. A model with a 1M-token window already showed context rot at 50k tokens.

<mark style="background: #FF5582A6;">A context window's size is how much a model accepts, not how much it reads reliably.</mark>

#### Simple tasks fail too

The tasks needed no reasoning: retrieve a sentence, replicate text. Models still made more errors as input grew, so the cause is length itself, not task difficulty.

#### Distractors hurt more than length alone

A distractor is a passage that looks relevant to the question but does not answer it. Adding even one lowered accuracy beyond what the extra tokens explained, and several compounded.

<mark style="background: #ABF7F7A6;">Attention spreads over every token in the window, so each irrelevant but similar-looking passage competes with the right one for the model's focus.</mark> How [[Attention allows each token to directly reference any other token regardless of distance|attention links every token to every other]] is what makes this competition possible.

---

### Avoiding context rot

<mark style="background: #ADCCFFA6;">Give the model the smallest set of tokens that holds what the current step needs; relevance beats volume.</mark> A tight 20k window outperforms a 200k window stuffed with everything.

Every fix is a [[Context engineering curates everything in the window and not the wording of one message#The core techniques|context engineering technique]] applied with that goal:

- **Just-in-time loading**: the model [[Tool calling lets a model fetch what it needs during a task instead of being handed everything upfront|fetches files and docs through tools]] when a step needs them.
- **Compaction**: summarise a long history and continue from the summary.
- **Fresh sessions**: one task per session; clear the window when the topic changes.
- **Sub-agents**: each worker gets a clean window and returns only a summary.
- **External notes**: state lives in a file the agent re-reads, not in the growing transcript.
- **Pruning**: drop stale tool output, failed attempts and look-alike documents, since those are exactly the distractors.

---

### Read more

- [[Context engineering curates everything in the window and not the wording of one message]]
- [[Tool calling lets a model fetch what it needs during a task instead of being handed everything upfront]]
- [[Attention allows each token to directly reference any other token regardless of distance]]
- [[AI Engineering MOC]]
- [[Agentic Engineering MOC]]
- Source: [Context Rot: How Increasing Input Tokens Impacts LLM Performance, Chroma](https://www.trychroma.com/research/context-rot)
