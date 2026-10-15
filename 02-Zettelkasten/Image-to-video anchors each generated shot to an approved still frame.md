---
created: 2026-10-07
aliases: [image-to-video, I2V, first-frame anchoring, keyframe-first]
tags: [ai-video, generative-video]
---

Text-to-video asks a model to invent everything in a shot at once: the composition, the character, the lighting and the motion. When any one of them is wrong, the whole clip is regenerated and the other three change too.

<mark style="background: #FFF3A3A6;">Image-to-video generates a clip that starts from a given still image, so the model only invents the motion and the first frame is exactly the picture you approved.</mark>

---

### Keyframe first, motion second

1. Generate or draw the still for the shot, using the [[Character reference sheets keep an AI character consistent across separately generated shots|character reference sheet]].
2. Iterate on the still until composition and character are right.
3. Animate the approved still with an image-to-video model.

<mark style="background: #ABF7F7A6;">Stills are cheap and fast to regenerate compared with clips, so moving the decisions about composition onto stills cuts the number of expensive video generations.</mark>

#### First and last frame

Some models take two images, the first and the last frame, and generate the motion between them. ComfyUI exposes this for Wan 2.2 as a first-last-frame workflow. Chaining shots this way, the last frame of one clip becomes the first frame of the next.

---

### What the anchor does not hold

<mark style="background: #FF5582A6;">The anchor fixes only the first frame, so the longer a clip runs, the further the character and scene can drift away from the approved still.</mark>

Short clips, cut together, stay closer to the references than one long clip.

---

### Read more
- [[Character reference sheets keep an AI character consistent across separately generated shots]]
- [[Generative video models synthesize pixels from a prompt so on-screen text and diagrams come out unreliable]]
- [[Wan 2.2 runs open-weight video generation locally by trading GPU memory for render time]]
- [[AI Video Production MOC]]

### External Resources
- [ComfyUI: Wan 2.2 video tutorial (text, image, and first-last-frame to video)](https://docs.comfy.org/tutorials/video/wan/wan2_2)
- [Keeping AI video shots visually consistent (invideo)](https://invideo.io/faq/how-do-you-keep-ai-generated-video-shots-visually/)
