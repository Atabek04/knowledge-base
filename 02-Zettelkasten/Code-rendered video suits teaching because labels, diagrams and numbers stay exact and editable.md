---
created: 2026-10-07
aliases: [code-rendered educational video, AI explainer video, programmatic explainer]
tags: [ai-video, code-to-video, instructional-design]
---

An educational video makes claims: this arrow means a request, this number is the latency, this label names the component. Its visuals have to be correct in the way a textbook figure is correct, not merely convincing.

In [[Code-rendered video has an AI write a program that draws every frame instead of generating pixels|code-rendered video]], a program draws every frame from source code the AI wrote.

<mark style="background: #ABF7F7A6;">Code-rendered video fits teaching because every label, arrow and number is written in the source, so it is exactly what the author typed and can be corrected in one edit.</mark>

---

### Exactness: the figure says what you meant

A [[Generative video models synthesize pixels from a prompt so on-screen text and diagrams come out unreliable|generative model reproduces the look of text without its meaning]]. A program draws the string it was given.

For a diagram of a database replica, that is the difference between a box labelled "Replica" and a box labelled "Repilca".

---

### Editability: corrections stay cheap after publishing

A learner reports that a value on screen is wrong. In code, the fix is one changed constant and a re-render. In a generated clip, the fix is a new sample that may change everything else in the shot.

The same holds for a whole series: a colour scheme, a font, or an icon style defined once in code stays identical across every episode.

---

### Multimedia principles become code constraints

Several of [[Mayer's Multimedia Learning Principles reduce cognitive load through twelve evidence-based design rules|Mayer's multimedia principles]] are about *where* and *when* things appear, which is precisely what a program controls.

| Principle | What the code does |
|---|---|
| **Signaling** | Highlights exactly the element the narration names, at the moment it is named |
| **Spatial contiguity** | Places each label next to the thing it labels, by coordinates |
| **Temporal contiguity** | Shows a visual on the same frame as its spoken word, using [[Word timestamps from speech-to-text let animation cues sync to narration\|word timestamps]] |
| **Coherence** | Draws nothing that was not deliberately written |

<mark style="background: #ADCCFFA6;">Write the narration first and key every visual cue to a spoken word, so the picture and the sentence that explains it arrive together.</mark>

---

### Where code-rendered video falls short

It cannot film a real lab, a city, or a person speaking. For those shots a generated clip is the right tool, used sparingly and checked frame by frame.

<mark style="background: #FF5582A6;">Mayer's voice principle favours a natural human voice over text-to-speech, and that evidence predates current AI voices, so treat AI narration as a choice to test with learners, not a settled one.</mark>

Background music is the other trap: [[Background music in instructional video occupies the phonological loop and measurably reduces verbal learning|music under narration reduces verbal learning]], so an AI-generated soundtrack belongs in the intro and the transitions only.

---

### Read more
- [[Code-rendered video has an AI write a program that draws every frame instead of generating pixels]]
- [[Generative video models synthesize pixels from a prompt so on-screen text and diagrams come out unreliable]]
- [[Mayer's Multimedia Learning Principles reduce cognitive load through twelve evidence-based design rules]]
- [[Word timestamps from speech-to-text let animation cues sync to narration]]
- [[Background music in instructional video occupies the phonological loop and measurably reduces verbal learning]]
- [[Dual coding theory shows that pairing images with verbal explanation creates stronger memory traces]]
- [[AI Video Production MOC]]
- [[Instructional Video Design MOC]]
