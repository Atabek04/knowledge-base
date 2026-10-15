---
created: 2026-10-07
aliases: [word timestamps, narration sync, audio-first timing, word-level alignment]
tags: [ai-video, speech, code-to-video]
---

In a narrated explainer, a box should light up at the moment the narrator says its name. Timing that by hand means scrubbing the audio and writing down seconds, and every re-recording throws the numbers away.

<mark style="background: #FFF3A3A6;">A word timestamp is the start and end time of one spoken word inside an audio file, produced automatically by a speech model.</mark>

---

### Two ways to get the timestamps

#### From the voice you generated

Text-to-speech services can return timing with the audio. ElevenLabs' convert-with-timestamps endpoint returns, next to the audio, each character's start and end time in seconds.

#### From any recording

Speech-to-text recovers the timing from audio that already exists, including your own voice. [[Whisper transcribes audio using an encoder-decoder Transformer trained end-to-end on 680k hours|Whisper]] does this with one flag:

```python
import whisper
result = whisper.load_model("small").transcribe("narration.wav", word_timestamps=True)
for seg in result["segments"]:
    for w in seg["words"]:
        print(w["word"], w["start"], w["end"])   # " replica" 12.48 12.91
```

---

### Cues keyed to words, not seconds

The animation should not say "highlight the replica at 12.48 s". It should say "highlight the replica when the word *replica* starts", and look the time up.

```json
[
  { "on": "replica",  "do": "highlight", "target": "replicaBox" },
  { "on": "leader",   "do": "pulse",     "target": "leaderBox" }
]
```

<mark style="background: #ABF7F7A6;">Keying cues to words means a re-recorded or re-paced narration re-times every cue automatically, because the lookup simply finds new seconds for the same words.</mark>

---

### Audio first, animation second

<mark style="background: #ADCCFFA6;">Lock the narration before animating, since the voice sets the clock that every visual cue reads from.</mark>

Animating first and recording afterwards forces the narrator to match the pictures, which produces rushed or padded speech.

#### Repeated words

<mark style="background: #FF5582A6;">A word that appears several times in the script matches several timestamps, so a cue must name which occurrence it means or it fires on the first one.</mark>

---

### Read more
- [[Whisper transcribes audio using an encoder-decoder Transformer trained end-to-end on 680k hours]]
- [[A deterministic animation computes every frame as a pure function of time so retiming is a data edit]]
- [[Code-rendered video suits teaching because labels, diagrams and numbers stay exact and editable]]
- [[AI Video Production MOC]]

### External Resources
- [OpenAI Whisper (GitHub)](https://github.com/openai/whisper)
- [ElevenLabs documentation](https://elevenlabs.io/docs)
- [ElevenLabs: text-to-speech with timestamps](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps)
