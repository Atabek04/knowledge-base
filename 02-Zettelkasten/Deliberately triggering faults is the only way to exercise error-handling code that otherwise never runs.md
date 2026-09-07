---
aliases: [chaos engineering, Chaos Monkey, fault injection]
created: 2026-09-03
tags: [reliability, testing, architecture, ddia]
---

Everything else about reliability is an argument for reducing faults. This one runs the other way: in a fault-tolerant system it makes sense to **raise** the rate of faults on purpose, by randomly killing processes without warning.

Netflix's **Chaos Monkey** is the well-known instance.

---

### Why increasing faults increases reliability

<mark style="background: #FFF3A3A6;">Many critical bugs are not in the happy path — they're in the error-handling code. And error-handling code is the least-executed code in the system.</mark>

A `catch` block nobody has ever entered is not tested recovery logic. It is a guess with syntax highlighting. The failover you've never triggered is a hypothesis.

So the fault-tolerance machinery has the same problem as any rarely-run code: it rots silently, and you find out it was broken at precisely the moment you needed it.

<mark style="background: #ABF7F7A6;">Injecting faults continuously keeps that machinery exercised, so you learn it works <b>before</b> the fault arrives on its own schedule.</mark>

---

### The reframe

Normal testing asks *does the feature work.* Fault injection asks *does the recovery work* — and the second question is the one your on-call rotation actually depends on.

It also converts an unknown into a scheduled cost. A replica failing at 2pm on a Tuesday while you watch is enormously cheaper than the same fault at 3am during a traffic peak.

Detection is the first link in that chain, which is why [[Kubernetes probes let the kubelet check container health the app reports|health probes]] belong in the same conversation — an undetected fault is guaranteed to become a failure.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[A fault is a component deviating from spec while a failure is the system no longer serving users]]
- [[A systematic software fault is a dormant wrong assumption about the environment]]
- [[Kubernetes probes let the kubelet check container health the app reports]]
