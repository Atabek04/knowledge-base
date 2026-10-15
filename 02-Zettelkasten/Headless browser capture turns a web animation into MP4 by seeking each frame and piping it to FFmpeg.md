---
created: 2026-10-07
aliases: [headless capture, frame capture, headless rendering, image2pipe]
tags: [ai-video, code-to-video, ffmpeg]
---

A web animation lives in a browser tab, and a video platform wants an MP4 file. Screen recording the tab is fragile: a slow machine drops frames and the recording inherits every stutter.

<mark style="background: #FFF3A3A6;">Headless browser capture renders an animation into video by loading it in a browser with no window, setting the time for each frame, taking a screenshot, and streaming the screenshots into FFmpeg.</mark>

---

### The two tools in the pipeline

#### Headless browser

**Headless** means the browser runs without its "head", the visible window. Chrome or Chromium is driven from code through Puppeteer or Playwright, which can load a page, run JavaScript in it, and screenshot it.

#### FFmpeg

**FFmpeg** is the command-line tool that encodes a stream of images and an audio file into a compressed video. Its name comes from MPEG, the family of video standards it was built to handle.

---

### The capture loop

The harness asks the page for each frame by time, never by waiting.

```js
for (let i = 0; i < fps * duration; i++) {
  await page.evaluate(t => window.__anim.seek(t), i / fps);
  const png = await page.screenshot();
  ffmpeg.stdin.write(png);           // FFmpeg reads the images from its standard input
}
```

```bash
ffmpeg -f image2pipe -framerate 30 -i - -i narration.wav \
       -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest out.mp4
```

<mark style="background: #ABF7F7A6;">Because time is set by the loop and not by the clock, a frame that takes two seconds to capture still lands at exactly 1/30 of a second in the output.</mark>

This only works for animations written as [[A deterministic animation computes every frame as a pure function of time so retiming is a data edit|a pure function of time]]; an animation that accumulates state between ticks cannot be seeked.

#### Pixel format

<mark style="background: #FF5582A6;">Without -pix_fmt yuv420p, FFmpeg can keep the screenshots' full colour format, which many phones, browsers and editors refuse to play.</mark>

---

### The same idea inside frameworks

Remotion uses this mechanism internally: it installs Chrome Headless Shell, renders each frame of a React composition, and encodes with a bundled FFmpeg. Its `concurrency` option opens several browser tabs to capture frame ranges in parallel.

Writing the loop by hand gives full control; a framework gives the same loop already tested.

---

### Read more
- [[A deterministic animation computes every frame as a pure function of time so retiming is a data edit]]
- [[Remotion builds video as React components driven by the current frame number]]
- [[three.js renders 3D scenes in the browser from a scene, a camera and a WebGL renderer]]
- [[Contact sheets show a whole video's frames at a glance so drift is caught before playback]]
- [[AI Video Production MOC]]

### External Resources
- [FFmpeg documentation](https://ffmpeg.org/documentation.html)
- [Puppeteer documentation](https://pptr.dev/)
- [Playwright documentation](https://playwright.dev/)
- [Remotion: Chrome Headless Shell](https://www.remotion.dev/docs/miscellaneous/chrome-headless-shell)
