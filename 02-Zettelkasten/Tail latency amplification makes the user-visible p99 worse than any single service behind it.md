---
aliases: [tail latency amplification, fan-out latency, slowest call dominates]
created: 2026-09-03
tags: [performance, latency, microservices, architecture, ddia]
---

This is the idea from Ch1 that most directly changes architecture decisions, and it is the one people get wrong when drawing service diagrams.

---

### The mechanism

A single end-user request usually requires several backend calls. Even when you issue them **in parallel**, the request cannot finish until the slowest one returns.

<mark style="background: #FFF3A3A6;">One slow call makes the entire end-user request slow. Parallelism does not help, because you are waiting on a maximum, not a sum.</mark>

Now add probability. Each backend has some chance of landing in its own tail. The more backends a request touches, the higher the chance that **at least one** of them does — so a larger proportion of end-user requests end up slow than any individual service's p99 would suggest.

<mark style="background: #FF5582A6;">Every service you add to a request path pushes the user-visible p99 the wrong way, even when no individual service got any slower.</mark>

---

### What it means for design

It's a direct argument against gratuitous service decomposition. The microservice split that looks free on an architecture diagram is not free on the latency histogram, and the cost compounds with each hop.

<mark style="background: #ABF7F7A6;">Useful interview move: when someone proposes splitting a service, ask how many backend calls one user request will make afterwards.</mark> That number is the multiplier on their tail.

It also reframes what a service-level p99 means. Your service reporting a healthy p99 says nothing about the experience of a user whose request touched six services — [[Response time is a distribution so percentiles describe it and the mean does not|the median describes one request, and users make many]].

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[Response time is a distribution so percentiles describe it and the mean does not]]
- [[Tail latency is a business metric because the slowest requests belong to your heaviest users]]
- [[Queueing delay is invisible to server-side metrics and to closed-loop load generators]]
