---
aliases: [Process Mining, Celonis]
tags: [data-governance, system-analysis, process, analytics]
created: 2026-05-31
---

### What it is

**Process mining** reconstructs how a process *actually* runs by analyzing the <mark style="background: yellow">event logs that systems already produce</mark> — then compares that discovered reality against the documented "should-be" process.

Tools: Celonis, ProM, Apromore.

---

### The input: event logs

Any workflow that touches IT systems leaves a trail: timestamps of when an order was placed, approved, shipped, invoiced.

Process mining needs three things per event:
- a **case ID** (which order?),
- an **activity** (what happened?),
- a **timestamp** (when?).

From thousands of such traces it rebuilds the real flow graph — including the paths nobody documented.

---

### Why it matters

Documented processes ([[AS-IS process modeling with BPMN reveals current workflow bottlenecks|AS-IS BPMN models]]) describe how people *think* work flows. Reality differs.

Process mining surfaces:
- **Deviations** — the undocumented shortcuts and rework loops people actually use
- **Bottlenecks** — where cases pile up and wait
- **Conformance gaps** — steps skipped that compliance requires

<mark style="background: #f9a8d4">It replaces interviews-and-guessing with evidence</mark>: the log is what happened, not what someone remembers happening.

---

### Where it fits in governance

It's the audit counterpart to documentation: a [[A data dictionary is the authoritative catalog defining every data element and its rules|data dictionary]] defines what data *should* mean, and process mining checks whether the *process* over that data actually conformed.

For an analyst, it turns the AS-IS model from an opinion into a measured fact before any TO-BE redesign.

---

Read more:
- [[AS-IS process modeling with BPMN reveals current workflow bottlenecks]]
- [[Data governance documents the retention archival and deletion rules for each class of data]]
- [[Databases - MOC]]
