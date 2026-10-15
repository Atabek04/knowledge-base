---
created: 2026-10-07
aliases: [three.js, threejs, WebGLRenderer]
tags: [ai-video, code-to-video, 3d, javascript]
---

three.js is the most widely used JavaScript library for 3D graphics in the browser. It hides WebGL, the browser's low-level interface to the graphics card, behind objects like meshes, lights and cameras.

<mark style="background: #FFF3A3A6;">A three.js picture is produced by a renderer that draws a scene of objects as seen through a camera, and every image needs all three.</mark>

---

### The three parts

```js
import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, 1920 / 1080, 0.1, 100);
const renderer = new THREE.WebGLRenderer({ antialias: true });

const cube = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshStandardMaterial({ color: 0x4488ff })
);
scene.add(cube, new THREE.DirectionalLight(0xffffff, 2));
camera.position.z = 4;

renderer.render(scene, camera);
```

| Part | Role |
|---|---|
| **Scene** | The container holding every object, light and helper |
| **Camera** | The viewpoint; `PerspectiveCamera` takes field of view, aspect ratio, and near and far clipping distances |
| **Renderer** | Draws the scene from the camera into a canvas using WebGL |

#### Mesh: geometry plus material

A **mesh** combines a geometry (the shape) with a material (how its surface reacts to light). `MeshStandardMaterial` responds to lights; with no light in the scene it renders black.

---

### The render loop

A live three.js page redraws continuously with `renderer.setAnimationLoop(fn)`, which calls `fn` once per screen refresh.

<mark style="background: #ABF7F7A6;">Each call to renderer.render draws one still image of the scene's current state, so motion is nothing more than changing positions between calls.</mark>

That separation is what lets a harness render a three.js scene frame by frame instead of in real time, as described in [[A deterministic animation computes every frame as a pure function of time so retiming is a data edit|deterministic animation]].

#### Capturing the canvas

<mark style="background: #FF5582A6;">A WebGL canvas clears its drawing buffer after each frame by default, so a screenshot taken later can come back blank unless preserveDrawingBuffer is enabled or the capture happens right after render.</mark>

---

### Read more
- [[A deterministic animation computes every frame as a pure function of time so retiming is a data edit]]
- [[Headless browser capture turns a web animation into MP4 by seeking each frame and piping it to FFmpeg]]
- [[Choose Manim for math, Remotion for text and data, Motion Canvas for explainers and three.js for 3D video]]
- [[AI Video Production MOC]]

### External Resources
- [three.js documentation](https://threejs.org/docs/)
- [three.js manual: fundamentals](https://threejs.org/manual/#en/fundamentals)
- [claude-motion-promo-skill: a Claude Code skill rendering three.js scenes to MP4](https://github.com/habibtalib/claude-motion-promo-skill)
