---
aliases: [Jev, System One model, TypeSafe Jev]
created: 2026-09-20
---

Jev is the first model from TypeSafe AI, a San Francisco lab that left stealth on 15 September 2026. It is an AI model but not an LLM, and the difference is in what comes out of it.

An LLM composes an answer one token at a time, so any string is a possible output, including a wrong or malformed one. <mark style="background: #FFF3A3A6;">A System One model takes program state plus a schema of allowed answers, and returns one of those answers with a calibrated probability, in a single parallel pass.</mark> The name borrows Kahneman's fast, non-deliberative "System 1": a snap judgement, not a reasoning chain.

Because every valid output is enumerated in the schema before the call, <mark style="background: #ABF7F7A6;">the model cannot hallucinate or return a type error; it can only be miscalibrated, and calibration is what its training optimises.</mark> Jev is trained with RLCD (reinforcement learning for calibrated decisions), which scores probabilities against real outcomes rather than human preference.

---

### The three question primitives

A request is `state` (any text or JSON) plus one or more typed `questions`. Only three shapes exist:

- **Choice**: one option from a set of up to 255
- **Score**: a position on an ordered scale of 2 to 10 levels
- **Noul**: a yes/no returned as a probability from 0 to 1

```python
client.system_one(
    state={"ticket": {...}},
    questions={
        "department": Choice(instructions="Which team?",
                             criteria={"billing": "...", "technical": "..."}),
        "urgency": Noul(instructions="Conveys urgency?"),
    },
)
```

Access is a hosted API only (`POST https://api.typesafe.ai/v1/systemone`, SDKs `typesafe-sdk` for Python and `@typesafe-ai/sdk` for Node, also through Vercel AI Gateway). There is no self-hosted option at launch.

---

### Cost and latency

Input is $0.042 per million tokens and output is free, since no tokens are generated. A typical call costs about $0.0004 and returns in 70 to 500 ms, which TypeSafe quotes as 40 to 200x faster and 40 to 400x cheaper than a frontier LLM.

---

### When to reach for it, and when not

<mark style="background: #ADCCFFA6;">If the set of acceptable answers can be written down before the call, use a System One model; if the answer has to be composed, use an LLM.</mark>

Fits: routing, classification, moderation, scoring, gating, picking the next step in an agent loop. High-volume, repeated decisions over a shared state.

Does not fit: writing, summarising, code generation, chat, extraction into a structure you do not know in advance, anything that needs a reasoning chain. <mark style="background: #FF5582A6;">"Never hallucinates" only means the output is always a schema member; it says nothing about whether that member was the right one.</mark>

---

### Read more

- [[AI Engineering MOC]]
- [[Autoregressive token prediction generates responses in a single forward pass without deliberation]]
- [[Chain-of-thought prompting uses model output as a working memory scratchpad]]
- Official: [typesafe.ai](https://typesafe.ai/), [launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
