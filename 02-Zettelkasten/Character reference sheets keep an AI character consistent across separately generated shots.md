---
created: 2026-10-07
aliases: [character reference sheet, character turnaround, character consistency, style block]
tags: [ai-video, generative-video]
---

A short film generated with AI is assembled from many separate clips. In each one the main character should be the same person, with the same face, hair and coat, and by default that is exactly what goes wrong.

<mark style="background: #ABF7F7A6;">Each generated clip is sampled independently, and the model keeps no memory of the previous shot, so a character described only in words drifts a little in every clip.</mark>

---

### The reference sheet

<mark style="background: #FFF3A3A6;">A character reference sheet is a set of approved images of one character from fixed angles, attached to every generation so the model copies the character instead of reinventing it.</mark>

The pattern documented across AI short films:

- A **turnaround**: front, three-quarter, side and back views, in high resolution.
- A **face close-up**, so features survive when the camera moves in.
- A **mid-angle close-up** for clothing and props.

The sheet is generated first, several candidates are compared, and one is locked before any video is made.

---

### Locking the rest of the world

A character is one of five things to fix before generating:

| Locked asset | Example |
|---|---|
| Character | The turnaround sheet |
| Wardrobe and props | The same scarf, the same bag |
| World | Reference stills of the main locations |
| Style | One fixed paragraph of style wording pasted into every prompt, called a **style block** |
| Motion | How the camera is allowed to move |

<mark style="background: #ADCCFFA6;">Attach the same reference images and the same style block to every shot prompt, and change only the action of the shot.</mark>

This works without training a custom model: documented productions held two characters across a 70-second film and four across a 3-minute episode with references alone.

---

### What references cannot guarantee

<mark style="background: #FF5582A6;">References reduce drift but do not remove it, so the finished cut still needs a shot-by-shot audit for a changed face, hand or costume.</mark>

A [[Contact sheets show a whole video's frames at a glance so drift is caught before playback|contact sheet of the cut]] puts every shot side by side and makes the audit fast.

---

### Read more
- [[Image-to-video anchors each generated shot to an approved still frame]]
- [[Generative video models synthesize pixels from a prompt so on-screen text and diagrams come out unreliable]]
- [[Contact sheets show a whole video's frames at a glance so drift is caught before playback]]
- [[AI Video Production MOC]]

### External Resources
- [Character consistency in AI video workflows (FilmDaft)](https://filmdaft.com/character-consistency-in-ai-video-workflows/)
- [Using a character reference sheet to keep AI characters consistent (invideo)](https://invideo.io/faq/how-do-you-use-a-character-reference-sheet-to-keep-ai/)
