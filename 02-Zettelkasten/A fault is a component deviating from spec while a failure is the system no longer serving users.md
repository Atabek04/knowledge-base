---
aliases: [fault vs failure, fault, failure, resilience]
created: 2026-09-03
tags: [reliability, architecture, distributed-systems, ddia]
---

"Reliability" means continuing to work correctly even when things go wrong. That's only a usable engineering target once you split *things going wrong* into two words that are constantly used as synonyms and aren't.

---

### The two words

<mark style="background: #FFF3A3A6;">A <b>fault</b> is one component deviating from its spec. A <b>failure</b> is the system as a whole stopping delivery of the service to the user.</mark>

A disk dies. A downstream service starts returning corrupted responses. An operator pastes the wrong config at 3am. Each of those is a fault — bounded, internal, and so far invisible to anyone outside.

The user never experiences a fault. The user only ever experiences a failure.

---

### Why the distinction is the whole design

You cannot drive the probability of a fault to zero. Hardware wears out, kernels have bugs, people are people.

So the engineering target was never "fewer faults." <mark style="background: #ABF7F7A6;">The target is <b>the arrow between the two</b> — fewer faults that propagate into failures.</mark>

Your Postgres primary dying is a fault. Whether it becomes a failure depends entirely on whether a replica is promoted before anyone notices. Same fault, two different outcomes, and everything you build lives in that gap.

Replication, failover, quorums, retries, circuit breakers — every reliability mechanism in the book is a device for interrupting that arrow.

#### "Fault-tolerant" is a slightly misleading label

It implies a system could tolerate *every* kind of fault, which is never true. Tolerate the datacenter being swallowed by a black hole and you'll need hosting in space.

<mark style="background: #FFB8EBA6;">"Is it fault-tolerant?" is unanswerable. "Which faults does it tolerate?" is the real question</mark> — and asking it back is the correct move in an interview.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- What the arrow is made of:
    - [[Redundancy only defeats faults that fail independently so it cannot save you from a shared bug]]
    - [[Deliberately triggering faults is the only way to exercise error-handling code that otherwise never runs]]
    - [[Preventing a fault beats tolerating it only when no cure exists]]
    - [[A cold cache sends every request to the database, causing a thundering herd]]
