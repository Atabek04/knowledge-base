---
created: 2026-10-07
aliases: [Wan 2.2, Wan2.2, local video generation, open-weight video model]
tags: [ai-video, generative-video, local-ai]
---

Hosted video models such as Veo and Kling charge per clip and run on someone else's servers. Wan 2.2, released by Alibaba in July 2025, is the strongest video model whose weights anyone can download and run on their own GPU.

<mark style="background: #FFF3A3A6;">An open-weight model publishes its trained parameters for download, so it runs on your own hardware with no per-clip fee and no upload of your material.</mark>

Wan 2.2 is released under the Apache 2.0 licence, which allows commercial use.

---

### The model family

| Model | Task | Size | Official memory guidance |
|---|---|---|---|
| **TI2V-5B** | Text or image to video, 720p at 24 fps | 5B, dense | Runs on a 24 GB consumer card such as an RTX 4090; a 5-second 720p clip in under 9 minutes |
| **T2V-A14B** | Text to video, 480p and 720p | 27B total, 14B active | About 80 GB on a single GPU |
| **I2V-A14B** | Image to video, 480p and 720p | 27B total, 14B active | About 80 GB on a single GPU |

#### Two experts split by noise level

The A14B models are a **mixture of experts**: two 14B networks, of which only one runs at each denoising step. A high-noise expert handles the early steps and decides the overall layout; a low-noise expert handles the late steps and refines detail.

---

### Memory traded for time

<mark style="background: #ABF7F7A6;">Offloading keeps most of the model in ordinary system RAM and moves each part onto the GPU only while it computes, so it fits a smaller card at the cost of constant copying that slows every clip.</mark>

The same 5B model the official repository sizes for a 24 GB card is described by ComfyUI's documentation as fitting in 8 GB with ComfyUI's native offloading. Lower-precision weights (fp8 or quantized files) shrink it further, at some cost in quality.

<mark style="background: #ADCCFFA6;">On a small GPU, draft at low resolution and short length, and render the final shots at full settings only once the composition is approved.</mark>

---

### ComfyUI

**ComfyUI** is the usual way to run Wan locally: a node editor in the browser where a workflow is a graph of boxes (load model, encode prompt, sample, decode, save video) wired together. Official workflow templates for Wan 2.2 load with one click.

<mark style="background: #FF5582A6;">Newer Wan versions are not guaranteed to stay open: Wan 2.5, released in September 2025, was offered through hosted APIs only.</mark>

---

### Read more
- [[Generative video models synthesize pixels from a prompt so on-screen text and diagrams come out unreliable]]
- [[Image-to-video anchors each generated shot to an approved still frame]]
- [[AI Video Production MOC]]

### External Resources
- [Wan 2.2 (GitHub): models, requirements, licence](https://github.com/Wan-Video/Wan2.2)
- [ComfyUI documentation](https://docs.comfy.org)
- [ComfyUI: Wan 2.2 video tutorial](https://docs.comfy.org/tutorials/video/wan/wan2_2)
