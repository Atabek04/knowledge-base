---
created: 2026-06-02
aliases: [fine-tuning Whisper, Whisper fine-tune, domain adaptation STT]
tags:
  - ml/speech
  - ml/training
  - ai-engineering
---

Fine-tuning starts from a pretrained model's weights — which already encode broad language and acoustic knowledge — and continues training on a small, domain-specific dataset.

The model architecture stays the same. Only the weight values shift to better fit the new distribution.

---

### Why it works

[[Whisper transcribes audio using an encoder-decoder Transformer trained end-to-end on 680k hours|Whisper]] trained on 680k hours already knows: what speech sounds like, how phonemes map to words, how words flow in English (and 99 other languages).

Fine-tuning does not re-learn any of that. It adjusts weights for the patterns that differ in the target domain — specific vocabulary, accent, speaking pace, background noise profile.

A small dataset (hours, not hundreds of thousands of hours) is enough because the base already carries most of the signal.

---

### What changes during fine-tuning

| What stays | What changes |
|---|---|
| Model architecture (encoder-decoder Transformer) | Weight values throughout the network |
| Tokenizer vocabulary | Loss surface — now optimized for target domain |
| Learned acoustic and language patterns | Attention patterns shift toward domain-specific cues |

---

### Common fine-tuning targets

- **Language** — a base multilingual Whisper fine-tuned on Uzbek, Arabic, or a low-resource language
- **Domain** — medical, legal, customer support, podcast
- **Distillation** — a smaller, faster model that matches a larger Whisper's accuracy (`distil-whisper`)

All of these appear as separate model cards on [[Hugging Face hosts community fine-tuned Whisper variants for domain-specific transcription|Hugging Face]].

---

Read more:
- [[Whisper transcribes audio using an encoder-decoder Transformer trained end-to-end on 680k hours]]
- [[Hugging Face hosts community fine-tuned Whisper variants for domain-specific transcription]]
- [[AI Engineering MOC]]
