---
created: 2026-06-24
tags: [debugging/method, root-cause]
aliases: [Five Whys, 5 Whys, root cause analysis]
---

A fix that addresses the *symptom* leaves the real fault alive to strike again — you restart the crashed service, but it crashes again tomorrow because you never found *why* it ran out of memory. The Five Whys is a questioning technique that drills past the symptom to the underlying cause you can actually eliminate.

It was developed by <mark style="background: #FFF3A3A6;">Sakichi Toyoda at Toyota</mark> and became a core tool of the Toyota Production System and Kaizen (continuous improvement). The idea: <mark style="background: #FFF3A3A6;">ask "why?" about the symptom, then "why?" about that answer, and keep going until you reach something systemic you can fix.</mark>

---

### How it works

Each answer becomes the subject of the next "why," peeling away one layer of symptom per question:

```
The site went down.
  └ Why? The service was OOM-killed.
      └ Why? A query loaded the entire table into memory.
          └ Why? The endpoint had no pagination.
              └ Why? No review caught the unbounded query.
                  └ Why? The review checklist has no perf item.   ← root cause
```

Fixing the OOM (more memory) treats the symptom. Fixing the **checklist** stops the whole *class* of bug. <mark style="background: #BBFABBA6;">That gap between the first answer and the last is exactly what the technique exists to expose.</mark>

---

#### "Five" is a guide, not a rule

Stop when you hit something you can fix at a systemic level — that might be three whys or seven. The count matters less than reaching a cause that is <mark style="background: #ADCCFFA6;">a process or design flaw, not just the immediate technical glitch.</mark>

---

### Limitation: one linear path

The Five Whys follows a single chain, so it can miss a problem with <mark style="background: #FF5582A6;">multiple independent causes</mark>, and a careless analyst can steer the chain toward a predetermined conclusion. Pair it with [[Differential debugging asks what changed since the system last worked|differential debugging]] to first pin down *what changed*, then use the Five Whys to ask *why that change was allowed to break things*.

---

### Read more
- [[Differential debugging asks what changed since the system last worked]]
- [[Debug by the scientific method observe hypothesize test repeat]]
- [[Debugging & Troubleshooting - MOC]]

### Sources
- [Five whys — Wikipedia](https://en.wikipedia.org/wiki/Five_whys)
- [The power of 5 Whys: analysis and defense — Atlassian](https://www.atlassian.com/incident-management/postmortem/5-whys)
- [Sakichi Toyoda and the Five Whys — Jeff McNeill](https://jeffmcneill.com/sakichi-toyoda-and-the-five-whys-root-cause-analysis/)
