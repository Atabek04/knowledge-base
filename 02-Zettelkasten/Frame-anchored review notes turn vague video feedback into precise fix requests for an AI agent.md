---
created: 2026-10-07
aliases: [frame-anchored review, video review notes, frame annotation, review editor]
tags: [ai-video, review, agentic-engineering]
---

"The middle part feels off" is honest feedback and useless to a coding agent. The agent cannot watch the video the way a person does, and it cannot tell which of 5,000 frames the person meant.

<mark style="background: #FFF3A3A6;">A frame-anchored review note ties each requested change to a frame range, optionally a region of the screen, and one concrete instruction.</mark>

---

### Vague versus anchored

| Vague | Anchored |
|---|---|
| The diagram part is confusing | Frames 1420 to 1510: the "Replica" label overlaps the arrow; move it above the box |
| The ending drags | Frames 4800 to 5100: hold is 10 s; cut to 3 s |
| Colours feel off | Frames 900 to 960, top-left: leader box is red, use the palette's blue |

```json
{ "from": 1420, "to": 1510, "region": [640, 200, 900, 320],
  "fix": "Label overlaps the arrow; place it above the box" }
```

<mark style="background: #ABF7F7A6;">In a deterministic animation a frame number maps to a single state of the program, so an anchored note points the agent straight at the code that produced the problem.</mark>

That mapping exists only because the video is [[A deterministic animation computes every frame as a pure function of time so retiming is a data edit|a pure function of time]].

---

### Build the review tool too

The creator of the music video "LGTM" (2026) described doing exactly this: they had Claude build a small video editor, then used it to mark segments and frames with fix requests, over several rounds.

A minimal version is a player with a frame counter, a box-drawing tool, a comment field, and an export to JSON that the agent reads. A coding agent can build it in an afternoon, and every later round of review runs on it.

<mark style="background: #ADCCFFA6;">Review in rounds: export all notes for a pass at once, let the agent fix them together, re-render, and review the new render before writing more notes.</mark>

[[Contact sheets show a whole video's frames at a glance so drift is caught before playback|Contact sheets]] help pick which ranges deserve a closer look.

---

### The tool does not replace looking

<mark style="background: #FF5582A6;">A review tool only makes feedback precise; if the reviewer approves a render without actually watching it, the loop becomes rubber-stamping.</mark>

The LGTM creator was candid that even they "LGTM'd it" in the end: [[You cannot review what you cannot understand so AI oversight collapses into rubber-stamping|human review only protects anything when the reviewer genuinely evaluates the output]].

---

### Read more
- [[A deterministic animation computes every frame as a pure function of time so retiming is a data edit]]
- [[Contact sheets show a whole video's frames at a glance so drift is caught before playback]]
- [[You cannot review what you cannot understand so AI oversight collapses into rubber-stamping]]
- [[Verification becomes the scarce engineering skill as AI makes generating code cheap]]
- [[Story-first direction separates memorable AI video from generic one-shot output]]
- [[AI Video Production MOC]]

### External Resources
- [LGTM (YouTube): the video and the creator's comment on the review editor](https://youtu.be/3TNpOD6bov8)
