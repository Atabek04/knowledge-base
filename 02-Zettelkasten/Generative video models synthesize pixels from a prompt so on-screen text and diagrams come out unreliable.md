---
created: 2026-10-07
aliases: [generative video, text-to-video, AI video generation, video diffusion]
tags: [ai-video, generative-video]
---

Veo, Kling, Runway and Seedance are generative video models. You describe a shot in words, optionally attach a reference image, and the model returns a short clip with no program behind it.

<mark style="background: #FFF3A3A6;">A generative video model synthesizes the pixels of a clip directly from a prompt, so there is no editable source, only the sampled result.</mark>

---

### How the pixels are made

Most of these models are diffusion models. Generation starts from random noise shaped like a short video and removes noise step by step, steered at each step toward something that matches the prompt.

The model learned what videos *look like* from millions of examples. It never learned the rules that produced them: spelling, arithmetic, or which arrow in a diagram points where.

---

### Why text and diagrams break

<mark style="background: #ABF7F7A6;">The model reproduces the visual texture of letters and labels without their meaning, so text comes out misspelled, numbers change between frames, and diagram arrows connect the wrong boxes.</mark>

A chart is a precise claim. A generated chart is a picture of a chart.

#### No small edits

A generated clip cannot be nudged. "Move the label ten pixels up" is not an operation; the only option is to prompt again and hope the new sample keeps everything else.

---

### The plausibility trap

Generated footage looks finished even when it is wrong, the same way [[AI-generated code is harder to review because it looks clean even when the logic is wrong|AI-generated code looks clean while the logic is wrong]].

<mark style="background: #FF5582A6;">Polished output lowers the viewer's guard, so a wrong label in a beautiful generated shot is more likely to be believed than one in a rough sketch.</mark>

---

### Where generative video is the right tool

It is strong exactly where code is weak: realistic people, places, weather, camera moves, and physical motion that nobody would hand-animate.

Keeping a character recognisable across several clips needs extra technique, covered by [[Character reference sheets keep an AI character consistent across separately generated shots|character reference sheets]] and [[Image-to-video anchors each generated shot to an approved still frame|image-to-video anchoring]].

#### Tools as of October 2026

- **Google Veo 3.1**: native audio, clips up to about a minute.
- **Kling 3.0**: strong human motion, native 4K.
- **Runway Gen-4.5**: fine motion and camera control, with an API.
- **Wan 2.2**: open weights, runs locally (see [[Wan 2.2 runs open-weight video generation locally by trading GPU memory for render time|Wan 2.2 on a local GPU]]).

Model names and versions change every few months. OpenAI shut down its Sora app in April 2026, so tutorials built around it are out of date.

---

### Read more
- [[Code-rendered video has an AI write a program that draws every frame instead of generating pixels]]
- [[AI-generated code is harder to review because it looks clean even when the logic is wrong]]
- [[Character reference sheets keep an AI character consistent across separately generated shots]]
- [[Image-to-video anchors each generated shot to an approved still frame]]
- [[Wan 2.2 runs open-weight video generation locally by trading GPU memory for render time]]
- [[AI Video Production MOC]]

### External Resources
- [Google Veo](https://deepmind.google/models/veo/)
- [Kling AI](https://klingai.com)
- [Runway](https://runway.com)
- [Runway API documentation](https://docs.dev.runwayml.com)
- [Best AI video generation tools 2026: Sora, Runway, Kling, Veo (FreeAcademy)](https://freeacademy.ai/blog/best-ai-video-generation-tools-2026)
