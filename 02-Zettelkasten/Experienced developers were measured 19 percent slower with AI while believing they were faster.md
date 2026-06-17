---
aliases: [METR slowdown study, AI productivity perception gap, felt-speed illusion]
---

Developers overwhelmingly *feel* faster with AI. A randomized controlled trial found that feeling can be exactly backwards — and that you cannot trust your own sense of your speed.

---

### The study

METR (July 2025) ran an RCT with 16 experienced open-source developers on 246 real issues, in repositories they had maintained for years (averaging 22k+ stars, 1M+ lines).

With AI tools allowed, they took <mark style="background: pink">19% longer</mark> to complete issues — not faster, slower.

---

### The perception gap

The striking part is the gap between reality and belief:

- Beforehand they predicted AI would speed them up <mark style="background: yellow">24%</mark>.
- Afterward — *having just lived the slowdown* — they still believed AI had sped them up <mark style="background: yellow">20%</mark>.

That is a ~40-point gap between measured and felt productivity. <mark style="background: cyan;">The felt-speed of AI is not evidence of actual speed.</mark>

---

### Why slower, here

The friction was specific to this setting — experts on mature code they know deeply:

- AI lacks the <mark style="background: green">tacit codebase knowledge</mark> the expert already holds.
- High review standards: 56% of accepted suggestions still needed major cleanup; most devs read every line.
- Prompting and evaluating output cost more than just writing the code.
- Million-line repos overflow the context window.

---

### What it does and doesn't prove

<mark style="background: pink">This is a worst-case setting, not a verdict on all AI coding.</mark> METR explicitly warns against generalizing — the slowdown may not hold for greenfield work, less-expert developers, or newer models.

The durable lesson is narrower and survives the caveats: your *perception* of AI's speedup is unreliable, so measure instead of trusting the feeling.

---

### Read more
- [[AI-assisted learners score about two letter grades lower with debugging the most degraded skill]]
- [[Heavy AI use correlates with weaker critical thinking but the causal arrow may run both ways]]
- [[Doing reps with AI builds intuition for its real limits and capabilities]]
- [[Agentic Engineering MOC]]

### External Resources
- [METR — Measuring the impact of early-2025 AI on experienced open-source developer productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
