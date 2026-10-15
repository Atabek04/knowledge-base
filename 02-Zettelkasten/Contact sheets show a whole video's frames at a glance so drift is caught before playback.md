---
created: 2026-10-07
aliases: [contact sheet, frame grid, thumbnail sheet]
tags: [ai-video, review, ffmpeg]
---

Watching a three-minute video to check it takes three minutes per round, and the eye misses a label that overlaps for half a second. Reviewing many rounds that way is slow and unreliable.

<mark style="background: #FFF3A3A6;">A contact sheet is a single image that tiles frames sampled at regular intervals across a video, so its whole length can be inspected at once.</mark>

The name comes from photography: a roll of film was pressed in direct *contact* with photo paper to print every shot at negative size on one *sheet*.

---

### Making one with FFmpeg

```bash
ffmpeg -i out.mp4 -vf "fps=1,scale=320:-1,tile=8x5" -frames:v 1 sheet.png
```

- `fps=1` keeps one frame per second.
- `scale=320:-1` shrinks each frame to 320 pixels wide.
- `tile=8x5` arranges 40 of them in a grid.

---

### What a sheet catches

<mark style="background: #ABF7F7A6;">Laid side by side, frames reveal drift that playback hides: a character whose hair changes colour, a label that slides off its arrow, a scene that stays frozen too long.</mark>

It also makes feedback precise, since each tile corresponds to a known second, which feeds directly into [[Frame-anchored review notes turn vague video feedback into precise fix requests for an AI agent|frame-anchored review notes]].

For a coding agent, a sheet is the cheapest way to "see" its own render: one image instead of thousands of frames.

---

### What a sheet misses

<mark style="background: #FF5582A6;">A contact sheet samples, so a glitch that lasts less than the sampling interval falls between two tiles and never appears.</mark>

FFmpeg's `blackdetect` and `freezedetect` filters scan every frame for blank or frozen stretches and cover that gap. A final full-speed watch is still required before publishing.

---

### Read more
- [[Frame-anchored review notes turn vague video feedback into precise fix requests for an AI agent]]
- [[Headless browser capture turns a web animation into MP4 by seeking each frame and piping it to FFmpeg]]
- [[Character reference sheets keep an AI character consistent across separately generated shots]]
- [[AI Video Production MOC]]

### External Resources
- [FFmpeg filters: tile](https://ffmpeg.org/ffmpeg-filters.html#tile-1)
- [FFmpeg documentation](https://ffmpeg.org/documentation.html)
