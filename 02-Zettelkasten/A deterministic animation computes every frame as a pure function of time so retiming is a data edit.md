---
created: 2026-10-07
aliases: [deterministic animation, seek function, frame as a function of time, time-driven animation]
tags: [ai-video, code-to-video, animation]
---

A browser animation usually runs on a loop: every time the screen refreshes, it nudges each object a little further. That works for a live page and fails the moment the animation has to be rendered into a video file.

<mark style="background: #FFF3A3A6;">A deterministic animation computes the whole picture from the time value alone, so asking for second 12.4 always returns the same frame no matter what was drawn before.</mark>

---

### Pure function of time

A **pure function** returns a result that depends only on its arguments and changes nothing outside itself. Called twice with the same input, it gives the same output.

Applied to animation, the input is the time $t$ and the output is the frame. Code-to-video harnesses expose this as a single entry point such as `seek(t)`.

```js
window.__anim = {
  duration: 60, fps: 30,
  seek(t) {
    const x = 100 + 400 * Math.min(t / 2, 1);   // slide in over the first 2 seconds
    ctx.clearRect(0, 0, W, H);
    ctx.fillRect(x, 300, 80, 80);
  }
};
```

---

### Accumulated state breaks rendering

The live-page style keeps state between frames:

```js
function tick(dt) { x += velocity * dt; draw(); }   // frame 900 depends on frames 0 to 899
```

<mark style="background: #ABF7F7A6;">When each frame adds to the previous one, frame 900 can only be reached by replaying frames 0 to 899, and any skipped or slowed frame changes everything after it.</mark>

A renderer that captures slower than real time, or jumps straight to a later frame, gets a different video from the one seen in the browser.

#### Hidden sources of non-determinism

- `Math.random()` without a fixed seed gives new values on every run.
- `Date.now()` and `performance.now()` read the wall clock, not $t$.
- Physics that integrates step by step is accumulated state in disguise; precompute it or use a closed-form formula of $t$.

<mark style="background: #ADCCFFA6;">Never read the wall clock or an unseeded random generator inside an animation that will be rendered to video.</mark>

---

### What determinism buys

#### Random access

Any frame can be rendered first, which lets you inspect frame 1420 without playing the 1419 before it.

#### Parallel rendering

Workers can each take a range of frames and render them at the same time, because no frame waits for another.

#### Retiming as a data edit

When every scene's start and length live in a table, moving a scene two seconds later is a change to one number. Nothing has to be re-animated by hand, and every frame after it lands on its new time automatically.

---

### Read more
- [[Headless browser capture turns a web animation into MP4 by seeking each frame and piping it to FFmpeg]]
- [[Code-rendered video has an AI write a program that draws every frame instead of generating pixels]]
- [[Remotion builds video as React components driven by the current frame number]]
- [[Frame-anchored review notes turn vague video feedback into precise fix requests for an AI agent]]
- [[AI Video Production MOC]]

### External Resources
- [code-animations: the seek(t) contract and determinism checks](https://github.com/beriki770-ship-it/code-animations)
- [Remotion: the fundamentals (a video as a function of images over time)](https://www.remotion.dev/docs/the-fundamentals)
