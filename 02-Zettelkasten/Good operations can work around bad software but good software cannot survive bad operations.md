---
aliases: [operability, operations team, runbook, operational model]
created: 2026-09-03
tags: [maintainability, operations, architecture, ddia]
---

**Operability** is the first of the three maintainability principles: make it easy for an operations team to keep the system running smoothly.

The claim that gives it weight is asymmetric, and worth remembering in that shape.

---

### The asymmetry

<mark style="background: #FFF3A3A6;">Good operations can often work around the limitations of bad or incomplete software. Good software cannot run reliably with bad operations.</mark>

Operations is the load-bearing side. Automation helps, but humans still have to build that automation and verify it's working — so "we'll automate it" relocates the human judgment rather than removing it.

A good ops team monitors health and restores service, tracks down causes, keeps platforms patched, watches how systems affect each other, plans capacity ahead of problems, runs deployment and config management, and — the one that's easy to miss — **preserves the organization's knowledge of the system as people come and go.**

---

### What software can do to help

<mark style="background: #ABF7F7A6;">Good operability means making the routine tasks easy, so the ops team's effort goes to high-value work instead.</mark>

The properties that buy this:

- **Visibility** into runtime behaviour and internals, through good monitoring
- **Automation support** and integration with standard tools
- **No dependency on individual machines** — any box can be taken down for maintenance while the system keeps serving
- **An understandable operational model**: *if I do X, Y will happen*
- **Good defaults, with the freedom to override them**
- **Self-healing where appropriate, with manual control still available**
- **Predictable behaviour** — minimizing surprises

That last one is the through-line. <mark style="background: #FFB8EBA6;">Every item on the list is a way of buying predictability</mark>, because an operator's real job at 3am is reasoning about what the system will do next, and a system that surprises them cannot be operated no matter how good its uptime looks on a normal day.

The machine-independence point also connects back to reliability: a system that tolerates losing any node can be patched one node at a time, so [[A fault is a component deviating from spec while a failure is the system no longer serving users|fault tolerance]] buys operability for free.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[The majority of software cost falls in maintenance, so design targets the engineers who arrive later]]
- [[An interface too restrictive to work with gets bypassed, moving the risk somewhere with no guardrails]]
- [[Kubernetes probes let the kubelet check container health the app reports]]
