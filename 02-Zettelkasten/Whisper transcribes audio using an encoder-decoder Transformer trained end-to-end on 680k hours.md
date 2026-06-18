---
created: 2026-06-02
aliases: [Whisper, OpenAI Whisper, Whisper STT]
tags:
  - ml/speech
  - ai-engineering
---

Whisper is OpenAI's speech-to-text model. Instead of a hand-crafted phoneme pipeline, it is a single **encoder-decoder Transformer** trained end-to-end on 680,000 hours of audio scraped from the web.

---

### Architecture

| Step | What happens |
|---|---|
| Audio → mel spectrogram | 30-second audio chunk is converted into a 2D frequency-time representation |
| Encoder | A stack of Transformer encoder layers compresses the spectrogram into a contextual representation |
| Decoder | Autoregressively generates text tokens, attending to the encoder output at each step |

The decoder works like a text LLM: given all tokens produced so far, predict the next one — except it also attends to the encoded audio at every step.

---

### How it differs from [[HMM-GMM STT models speech as a sequence of hidden phoneme states over acoustic features|HMM-GMM]]

[[HMM-GMM STT models speech as a sequence of hidden phoneme states over acoustic features|HMM-GMM]] is a pipeline of independently trained components. Whisper is trained all at once — the loss signal flows from the final text output back through every layer simultaneously.

This lets the model learn what acoustic patterns are useful for transcription, rather than relying on hand-designed phoneme categories.

---

### What "680k hours of web audio" buys

Diversity. Whisper heard accents, background noise, music, multiple languages, poor microphones, and technical jargon — all during training. This breadth makes the base model robust, but also means it is not optimized for any specific domain.

---

### Why base Whisper lags behind paid tools

Paid transcription services fine-tune Whisper on curated domain data, add speaker diarization, and apply post-processing (punctuation, formatting).

[[Fine-tuning adapts a pretrained Whisper checkpoint to a new domain without training from scratch|Fine-tuning on domain data]] is the main lever — even small amounts of high-quality in-domain audio shift accuracy significantly.

---

Read more:
- [[HMM-GMM STT models speech as a sequence of hidden phoneme states over acoustic features]]
- [[Fine-tuning adapts a pretrained Whisper checkpoint to a new domain without training from scratch]]
- [[Hugging Face hosts community fine-tuned Whisper variants for domain-specific transcription]]
- [[AI Engineering MOC]]
