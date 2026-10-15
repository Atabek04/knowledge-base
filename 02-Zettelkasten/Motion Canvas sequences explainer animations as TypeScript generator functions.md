---
created: 2026-10-07
aliases: [Motion Canvas, makeScene2D, yield star animation]
tags: [ai-video, code-to-video, typescript]
---

Motion Canvas is a TypeScript library for animated explainers, built around a browser editor with a live preview and a timeline. It sits between Manim's mathematics focus and Remotion's web-page focus: vector shapes, text, code blocks and diagrams that move in precise sequence.

<mark style="background: #FFF3A3A6;">In Motion Canvas a scene is a generator function, and each yield hands one finished frame to the renderer before the code continues to the next step.</mark>

---

### Generators as a timeline

A generator function pauses at every `yield` and resumes when asked for the next value, the same mechanism as [[A generator object is a suspended stack frame that resumes at yield|a Python generator's suspended frame]].

Motion Canvas turns that pause into time. The docs put it plainly: `yield` means the current frame is ready, show it and come back later.

```tsx
import { makeScene2D, Circle } from "@motion-canvas/2d";
import { all, createRef } from "@motion-canvas/core";

export default makeScene2D(function* (view) {
  const dot = createRef<Circle>();
  view.add(<Circle ref={dot} size={140} fill="#e13238" />);

  yield* dot().position.x(300, 1);                            // move right over 1 second
  yield* all(dot().fill("#e6a700", 1), dot().scale(2, 1));    // recolour and grow together
});
```

<mark style="background: #ABF7F7A6;">yield* delegates to another animation and waits until it finishes, so lines of code run in the order the viewer sees them on screen.</mark>

---

### Flow helpers

| Helper | What it does |
|---|---|
| `all()` | Runs several animations at once and waits for all of them |
| `chain()` | Runs animations one after another |
| `sequence()` | Starts animations at a fixed interval without waiting for each to finish |
| `delay()` | Starts an animation after a pause |
| `loop()` | Repeats an animation a set number of times |

---

### Time events for narration

`yield* waitUntil("replica")` pauses the scene at a named **time event**. The event appears as a marker on the editor's timeline and can be dragged to line up with the moment the narration reaches that word.

<mark style="background: #ABF7F7A6;">Time events separate what happens from when it happens, so syncing to a voiceover is done by dragging markers rather than editing durations in code.</mark>

#### Plain yield versus yield star

<mark style="background: #FF5582A6;">Writing yield instead of yield* in front of an animation does not wait for it, so the next line starts immediately and the sequence collapses into one moment.</mark>

---

### Read more
- [[A generator object is a suspended stack frame that resumes at yield]]
- [[Python generator produces values one at a time on demand]]
- [[Word timestamps from speech-to-text let animation cues sync to narration]]
- [[Choose Manim for math, Remotion for text and data, Motion Canvas for explainers and three.js for 3D video]]
- [[AI Video Production MOC]]

### External Resources
- [Motion Canvas documentation](https://motioncanvas.io/docs/)
- [Motion Canvas: flow (generators, all, chain, sequence)](https://motioncanvas.io/docs/flow)
