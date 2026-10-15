---
created: 2026-10-07
aliases: [Remotion, React video, useCurrentFrame]
tags: [ai-video, code-to-video, react]
---

Remotion is a framework for making videos with React, the JavaScript library for building user interfaces from components. Anything a web page can show (text, charts, SVG, images, CSS) can become a frame of a video.

<mark style="background: #FFF3A3A6;">In Remotion a video is a React component that reads the current frame number and returns what the screen should look like at that frame.</mark>

---

### The frame number drives everything

`useCurrentFrame()` is a React hook that returns the frame being rendered, starting at 0. The component computes every animated value from it.

```tsx
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";

export const Title: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 30], [0, 1], { extrapolateRight: "clamp" });
  return <AbsoluteFill style={{ opacity }}>Leader and replicas</AbsoluteFill>;
};
```

`interpolate()` maps a range of frames to a range of values: here frames 0 to 30 fade the title from invisible to fully visible, and `clamp` holds it at 1 afterwards.

<mark style="background: #ABF7F7A6;">Because the component depends only on the frame number, Remotion can render any frame directly, which makes every Remotion video a deterministic animation by construction.</mark>

---

### Composition: the component plus video metadata

A **composition** registers a component as a renderable video by adding the facts a video needs and a component does not have.

```tsx
<Composition id="Title" component={Title}
  durationInFrames={150} fps={30} width={1920} height={1080} />
```

The first frame is 0 and the last is `durationInFrames - 1`, so 150 frames at 30 fps is a five-second video.

#### Sequence shifts time

`<Sequence from={60}>` mounts its children at frame 60 and makes `useCurrentFrame()` inside them start from 0 again. Scenes are written as if each began at zero and placed on the timeline from outside.

---

### Rendering and licence

Remotion renders each frame in Chrome Headless Shell and encodes with its bundled FFmpeg, the same mechanism as [[Headless browser capture turns a web animation into MP4 by seeking each frame and piping it to FFmpeg|hand-written headless capture]], already packaged.

<mark style="background: #FF5582A6;">Remotion is free for individuals, non-profits and for-profit companies with up to 3 employees; a larger company needs a paid Company License.</mark>

---

### Read more
- [[A deterministic animation computes every frame as a pure function of time so retiming is a data edit]]
- [[Headless browser capture turns a web animation into MP4 by seeking each frame and piping it to FFmpeg]]
- [[Choose Manim for math, Remotion for text and data, Motion Canvas for explainers and three.js for 3D video]]
- [[AI Video Production MOC]]
- [[React Learning Path - MOC]]

### External Resources
- [Remotion documentation](https://www.remotion.dev/docs/)
- [Remotion: the fundamentals](https://www.remotion.dev/docs/the-fundamentals)
- [Remotion licence (LICENSE.md)](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)
