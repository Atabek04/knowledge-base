---
aliases: [redundancy, correlated failure, independent failure, RAID assumption]
created: 2026-09-03
tags: [reliability, architecture, distributed-systems, ddia]
---

The reflex answer to hardware faults is redundancy: disks in a RAID array, dual power supplies in the chassis, batteries and diesel generators behind the rack. Duplicate the component, keep the machine alive while the dead part is swapped.

It works, and it hides an assumption that is easy to carry into places where it is false.

---

### The assumption

<mark style="background: #FFF3A3A6;">Every redundancy technique assumes failures are <b>independent</b> — that one disk dying tells you nothing about whether the next one will.</mark>

For hardware that's broadly true. Correlations exist — a hot rack cooks several disks at once — but they're weak, which is why a 10,000-disk cluster loses roughly one disk a day rather than all of them on Tuesday.

Two mirrored disks only give you safety because the odds of both dying at once are the product of two small numbers.

---

### Where it collapses

<mark style="background: #FF5582A6;">Systematic software faults are perfectly correlated, so redundancy buys nothing against them.</mark>

Every node runs the same JAR, carrying the same wrong assumption. The trigger doesn't hit one node — it hits all of them within the same second. Three replicas of your service crash on the identical bad input, and the failover machinery has nowhere healthy to fail over to.

This is why software faults cause many more system failures than uncorrelated hardware faults do, despite being rarer.

The uncomfortable version: **you deliberately built the correlation.** Running identical code everywhere is the point of a deployment pipeline. It is also the thing that guarantees a bug arrives everywhere simultaneously.

Practical consequence — [[A systematic software fault is a dormant wrong assumption about the environment|the class of bug that does this]] is exactly the class your staging environment shares with production.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[A fault is a component deviating from spec while a failure is the system no longer serving users]]
- [[A systematic software fault is a dormant wrong assumption about the environment]]
- [[Eventual consistency lets replicas accept writes during a partition and converge afterward]]
