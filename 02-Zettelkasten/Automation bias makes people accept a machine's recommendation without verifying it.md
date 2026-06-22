---
aliases: [automation bias, automation complacency, commission and omission errors]
---

Long before LLMs, human-factors research found a reliable failure mode: once a machine offers a recommendation, people tend to take it as correct and stop checking. This is **automation bias**, and it is the cognitive root of why an AI coding tool's confident-but-wrong output gets approved.

The name is the mechanism: a *bias* toward trusting the *automation* over your own verification.

---

### The definition

Skitka, Mosier and Burdick (1999) defined automation bias as <mark style="background: yellow">the tendency to use automation as a heuristic replacement for vigilant information seeking and processing</mark>.

Put plainly: the machine's answer becomes a shortcut that *replaces* the work of checking, rather than one input *into* it.

The driver is <mark style="background: cyan;">least cognitive effort</mark> — accepting the system's output is cheaper than independently cross-checking it, so under load people default to acceptance.

---

### Two ways it fails

The canonical taxonomy (Mosier & Skitka, aviation cockpit studies) splits the error into two directions:

- <mark style="background: pink;">**Commission error**</mark> — you *follow* a wrong automated directive, in spite of contra-indications you could have seen.
- <mark style="background: pink;">**Omission error**</mark> — you *miss* a problem because the automation didn't flag it, so you never looked.

Accepting AI code that is subtly wrong is a textbook commission error.

---

### The evidence is not soft

This is measured, not anecdotal. In Lyell et al. (2017), 120 medical students prescribing on a simulated system made **~57% more commission errors** when the decision-support tool gave wrong advice — false guidance flipped correct clinicians to incorrect actions at rates above 50%.

#### Verification complexity is the amplifier

Lyell & Coiera (2017) found automation bias is <mark style="background: yellow;">strongest when the task is hard to verify</mark> — high cognitive demand, opaque output, time pressure.

This is the bridge to AI coding: LLM output is fluent, plausible, and expensive to verify, which maximizes exactly the condition that makes the bias worst.

---

### What pushes back on it

The mitigations from the literature are structural, not motivational:

- <mark style="background: green;">**Accountability**</mark> — operators who internalize that *they* are answerable double-check the machine and commit fewer errors (Mosier & Skitka).
- <mark style="background: green;">**First-read before the suggestion**</mark> — forming your own judgment *before* seeing the automation's answer (used in radiology training) preserves the ability to disagree with it.

---

### Read more
- [[You cannot review what you cannot understand so AI oversight collapses into rubber-stamping]]
- [[AI-generated code is harder to review because it looks clean even when the logic is wrong]]
- [[Over-relying on AI coding tools without reading output erodes genuine programming confidence]]
- [[Agentic Engineering MOC]]

### External Resources
- [Skitka, Mosier & Burdick (1999) — Does automation bias decision-making?](https://doi.org/10.1006/ijhc.1999.0252)
- [Lyell & Coiera (2017), JAMIA — Automation bias and verification complexity: a systematic review](https://academic.oup.com/jamia/article/24/2/423/2631492)
