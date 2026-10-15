---
created: 2026-10-07
tags: [moc]
---

Making animated and educational video with AI: either a coding agent writes a program that draws every frame, or a generative model synthesizes the pixels directly.

Different from [[Instructional Video Design MOC]], which covers what makes a video teach. This MOC covers how the video itself gets produced.

## Two Ways AI Makes Video

- [[Code-rendered video has an AI write a program that draws every frame instead of generating pixels|Code-rendered video: the AI writes code that draws frames]]
- [[Generative video models synthesize pixels from a prompt so on-screen text and diagrams come out unreliable|Generative video: sampled pixels, unreliable text]]
- [[Code-rendered video suits teaching because labels, diagrams and numbers stay exact and editable|Teaching favours code: labels stay exact and editable]]

## The Code-Rendered Pipeline

- [[A deterministic animation computes every frame as a pure function of time so retiming is a data edit|Deterministic animation: each frame a pure function of time]]
- [[Headless browser capture turns a web animation into MP4 by seeking each frame and piping it to FFmpeg|Headless capture: seek, screenshot, pipe to FFmpeg]]
- [[Word timestamps from speech-to-text let animation cues sync to narration|Word timestamps: key visual cues to spoken words]]
    - [[Whisper transcribes audio using an encoder-decoder Transformer trained end-to-end on 680k hours|Whisper: end-to-end Transformer speech-to-text]]
- [[Contact sheets show a whole video's frames at a glance so drift is caught before playback|Contact sheets: the whole video in one image]]

## Code-to-Video Frameworks

- [[Remotion builds video as React components driven by the current frame number|Remotion: React components driven by the frame number]]
- [[Manim animates mathematical objects in Python with exact programmatic placement|Manim: Python math animation with exact placement]]
- [[Motion Canvas sequences explainer animations as TypeScript generator functions|Motion Canvas: generators as the animation timeline]]
- [[three.js renders 3D scenes in the browser from a scene, a camera and a WebGL renderer|three.js: scene, camera and renderer make a 3D frame]]
- [[Choose Manim for math, Remotion for text and data, Motion Canvas for explainers and three.js for 3D video|Framework choice follows the dominant visual]]

## Generative Video

- [[Character reference sheets keep an AI character consistent across separately generated shots|Reference sheets: stop characters drifting between shots]]
- [[Image-to-video anchors each generated shot to an approved still frame|Image-to-video: approve the still, generate only motion]]
- [[Wan 2.2 runs open-weight video generation locally by trading GPU memory for render time|Wan 2.2: local generation trades memory for time]]

## Direction and Review

- [[Story-first direction separates memorable AI video from generic one-shot output|Story first: the human supplies the point of view]]
- [[Frame-anchored review notes turn vague video feedback into precise fix requests for an AI agent|Frame-anchored review: precise fixes for the agent]]
- [[You cannot review what you cannot understand so AI oversight collapses into rubber-stamping|Rubber-stamping: review without evaluation protects nothing]]

## Sound and Learning Constraints

- [[Background music in instructional video occupies the phonological loop and measurably reduces verbal learning|Background music under narration harms learning]]
- [[Mayer's Multimedia Learning Principles reduce cognitive load through twelve evidence-based design rules|Mayer's 12 multimedia principles]]

## Related MOCs

- [[Instructional Video Design MOC]]
- [[AI Engineering MOC]]
- [[Agentic Engineering MOC]]

## External Resources

**Script and voice**
- [ElevenLabs documentation](https://elevenlabs.io/docs)
- [ElevenLabs: text-to-speech with timestamps](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps)
- [OpenAI Whisper (GitHub)](https://github.com/openai/whisper)

**Code-rendered visuals**
- [Remotion documentation](https://www.remotion.dev/docs/)
- [Manim Community documentation](https://docs.manim.community/en/stable/)
- [Motion Canvas documentation](https://motioncanvas.io/docs/)
- [three.js documentation](https://threejs.org/docs/)
- [Puppeteer documentation](https://pptr.dev/)
- [Playwright documentation](https://playwright.dev/)

**Generative video**
- [Google Veo](https://deepmind.google/models/veo/)
- [Kling AI](https://klingai.com)
- [Runway](https://runway.com)
- [Runway API documentation](https://docs.dev.runwayml.com)
- [Wan 2.2 (GitHub)](https://github.com/Wan-Video/Wan2.2)
- [ComfyUI documentation](https://docs.comfy.org)

**Music**
- [Suno](https://suno.com)

**Assembly**
- [FFmpeg documentation](https://ffmpeg.org/documentation.html)

**Agent skills**
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills)
- [opus-js-animations: directs and renders films in JavaScript](https://github.com/klsoen/opus-js-animations)
- [code-animations: Canvas 2D videos rendered headless to MP4](https://github.com/beriki770-ship-it/code-animations)
- [claude-motion-promo-skill: three.js promo videos with a synced soundtrack](https://github.com/habibtalib/claude-motion-promo-skill)
- [Claude Code Video Toolkit: Remotion, Manim and FFmpeg](https://github.com/wilwaldon/Claude-Code-Video-Toolkit)

**Worked example**
- [LGTM (YouTube): Suno song, Claude-written three.js animation](https://youtu.be/3TNpOD6bov8)
