---
created: 2026-06-02
aliases: [HMM STT, classical STT, HMM-GMM speech recognition]
tags:
  - ml/speech
  - ai-engineering
---

Classical STT, used before deep learning, was built on two stacked models: a **Gaussian Mixture Model (GMM)** for acoustics and a **Hidden Markov Model (HMM)** for sequences.

No neural networks — pure probability.

---

### The pipeline

Raw audio → **MFCC features** → GMM → HMM → language model → text.

| Stage | What it does |
|---|---|
| MFCC extraction | Converts raw waveform into a compact spectral fingerprint per time frame |
| GMM (acoustic model) | For each phoneme (`/p/`, `/b/`, `/æ/`…), scores how likely the current MFCC frame belongs to it |
| HMM (sequence model) | Treats phonemes as hidden states; finds the most probable phoneme sequence over time using Viterbi |
| Language model (n-gram) | Re-ranks word sequences based on how natural they are in the language |

---

### Why HMMs fit speech

Speech is a time-series: the same word can be spoken fast or slow, with varying pauses between phonemes.

HMMs model this naturally — each state can "stay" (emit multiple frames) or "transition" to the next, absorbing variable-duration speech into a fixed phoneme sequence.

---

### The core limitation

GMMs model each phoneme in isolation. They cannot capture context: the `/t/` in *"top"* sounds different from the `/t/` in *"stop"*, but a GMM treats both identically.

This forced engineers to hand-craft context-dependent phoneme models (triphones), making the system brittle and labor-intensive.

[[Whisper transcribes audio using an encoder-decoder Transformer trained end-to-end on 680k hours|Whisper]] eliminates all of this — no phonemes, no GMMs, no HMMs.

---

Read more:
- [[Whisper transcribes audio using an encoder-decoder Transformer trained end-to-end on 680k hours]]
- [[AI Engineering MOC]]
