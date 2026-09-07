---
aliases: [AI speaking scoring limits, transcript pronunciation]
created: 2026-09-04
tags: [ielts, speaking, ai, research]
---

Pronunciation is a quarter of the Speaking band, and it is the one criterion an LLM working from text has no access to.

Measured: assessing pronunciation from a transcript alone reaches <mark style="background: #FFB8EBA6;">accuracy 0.404</mark>, rising to 0.728 only when the model is fed engineered phonetic and acoustic features. Prosody correlation stays at 0.243 even with those cues.

The obvious workaround does not work either. Writing pause markers into the transcript changes nothing — three different pause encodings produced effect sizes whose confidence intervals cross zero. <mark style="background: #ADCCFFA6;">The fluency signal lives in measured speech timing, not in how a pause is typed.</mark>

Holistic speaking scores from text look deceptively good, but only because a single overall label is dominated by grammar, vocabulary and coherence — the criteria that *are* in the transcript. <mark style="background: #FFF3A3A6;">A good-looking overall number is not evidence that the pronunciation component was assessed at all.</mark>

Source: [Transcript-only pronunciation assessment (arXiv 2509.14187)](https://arxiv.org/html/2509.14187) · [Pause encoding and fluency signal (arXiv 2608.26137)](https://arxiv.org/html/2608.26137)

### Read more
- [[Ask an LLM what rule a sentence breaks rather than what band the essay is]]
- [[Prosodic pronunciation training transfers to spontaneous speech while segmental training does not]]
- [[LLM essay scoring matches examiners on average but varies by over a band on any single essay]]
