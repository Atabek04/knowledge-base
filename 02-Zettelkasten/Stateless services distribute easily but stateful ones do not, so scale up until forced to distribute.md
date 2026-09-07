---
aliases: [scaling up, scaling out, vertical scaling, horizontal scaling, shared-nothing, elastic scaling]
created: 2026-09-03
tags: [scalability, architecture, system-design, ddia]
---

The usual framing is a dichotomy: **scaling up** (vertical — a more powerful machine) versus **scaling out** (horizontal — distributing load across several smaller machines, also called a **shared-nothing** architecture).

Treating it as a binary choice misses where the actual difficulty sits.

---

### The asymmetry that decides it

<mark style="background: #FFF3A3A6;">Distributing <b>stateless</b> services across machines is fairly straightforward. Taking a <b>stateful</b> data system from one node to a distributed setup introduces a great deal of additional complexity.</mark>

That asymmetry is why the two halves of your architecture get scaled differently, and why "just add more instances" works for your Spring app and not for the database behind it.

Hence the common wisdom: <mark style="background: #ABF7F7A6;">keep the database on a single node — scale it <b>up</b> — until cost or high-availability requirements force you to distribute it.</mark>

Kleppmann flags that this wisdom may shift as distributed tooling improves, and distributed data systems could become the default even where volume doesn't demand it. Worth holding as a trend rather than a rule.

---

### It is not actually a dichotomy

A system that runs on a single machine is simpler, but high-end machines get very expensive, so intensive workloads often can't avoid scaling out.

In practice good architectures are a pragmatic mixture. <mark style="background: #ADCCFFA6;">Several fairly powerful machines can be simpler <b>and</b> cheaper than a large number of small virtual machines</mark> — the cost curve and the complexity curve don't point the same way, and the optimum is usually neither extreme.

#### Elastic vs manual scaling

**Elastic** systems add resources automatically on detecting load; **manually scaled** systems have a human decide.

Elastic is useful when load is genuinely unpredictable. But <mark style="background: #FFB8EBA6;">manually scaled systems are simpler and produce fewer operational surprises</mark> — and automation that reacts to load has its own failure modes, including [[Auto-scaling is reactive so it always trails a sudden traffic spike|always trailing the spike it is reacting to]].

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[There is no generic scalable architecture because scaling is built around which operations are common]]
- [[Scalability is not a property of a system but a question about a specific direction of growth]]
- [[Auto-scaling is reactive so it always trails a sudden traffic spike]]
- [[A newly launched instance needs warm-up before it can serve traffic]]
