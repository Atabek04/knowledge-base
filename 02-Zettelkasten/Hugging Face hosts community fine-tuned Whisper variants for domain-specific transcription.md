---
created: 2026-06-02
aliases: [Hugging Face Whisper, HF fine-tuned models, HF model hub STT]
tags:
  - ml/speech
  - ai-engineering
---

Hugging Face is a model repository and community platform. Anyone can publish a model — including fine-tuned variants built on top of existing checkpoints like [[Whisper transcribes audio using an encoder-decoder Transformer trained end-to-end on 680k hours|Whisper]].

---

### What the community actually does

Researchers and engineers [[Fine-tuning adapts a pretrained Whisper checkpoint to a new domain without training from scratch|fine-tune]] base Whisper on specialized data, then publish the resulting weights as a new model card.

Examples:
- `openai/whisper-large-v3` → base model from OpenAI
- `distil-whisper/distil-large-v3` → same architecture, distilled to be 6× faster with minimal accuracy loss
- `tarteel-ai/whisper-large-v2-arabic-egyptian` → fine-tuned on Egyptian Arabic recitation
- Domain-specific variants for medical dictation, court transcription, customer call centers

---

### How to choose

If your audio matches a fine-tuned model's training distribution, it will outperform base Whisper — often significantly — at zero cost.

Check the model card for:
- Training dataset and domain
- Word Error Rate (WER) benchmarks
- Language coverage
- Model size (affects inference speed)

---

### Distillation vs fine-tuning

| Approach | Goal |
|---|---|
| Fine-tuning | Better accuracy on target domain |
| Distillation | Same accuracy, smaller/faster model |

Distilled models like `distil-whisper` are worth considering for real-time or resource-constrained use cases.

---

Read more:
- [[Whisper transcribes audio using an encoder-decoder Transformer trained end-to-end on 680k hours]]
- [[Fine-tuning adapts a pretrained Whisper checkpoint to a new domain without training from scratch]]
- [[AI Engineering MOC]]
