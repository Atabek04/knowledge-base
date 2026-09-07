---
aliases: [prevention vs tolerance, prevention over cure]
created: 2026-09-03
tags: [reliability, security, architecture, ddia]
---

The default stance in reliable systems is to **tolerate** faults rather than prevent them — you assume the fault happens and build the machinery that keeps it from becoming a failure. That preference is not universal, and the exception has a precise shape.

---

### The test

<mark style="background: #FFF3A3A6;">Tolerate the faults that can be cured. Prevent the ones that can't.</mark>

A crashed process can be restarted. A dead disk can be rebuilt from a replica. A bad deploy can be rolled back. All of these have a cure, so spending your effort on recovery beats spending it on making them impossible — which you couldn't do anyway.

Security is the standing counterexample. <mark style="background: #FF5582A6;">If an attacker has compromised the system and read sensitive data, that event cannot be undone.</mark> There is no rollback for exfiltration. Detection tells you it happened; it does not put the data back.

So for that class, the entire budget goes to prevention, because the recovery side of the ledger is empty.

---

### Why this is worth holding as a rule

It gives you a question to ask about any new failure mode instead of arguing preference: **what does recovery look like here?**

If you can describe the recovery, build it and stop trying to make the fault impossible. If you cannot describe any recovery, you have found something that must not be allowed to happen at all — and that changes the design, not just the runbook.

Data deletion and irreversible financial actions sit on the same side of the line as security leaks, for the same reason.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[A fault is a component deviating from spec while a failure is the system no longer serving users]]
- [[An interface too restrictive to work with gets bypassed, moving the risk somewhere with no guardrails]]
