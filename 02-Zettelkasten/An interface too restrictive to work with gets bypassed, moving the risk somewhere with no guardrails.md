---
aliases: [human error, operator error, restrictive interfaces, workarounds]
created: 2026-09-03
tags: [reliability, operations, architecture, ddia]
---

Humans build the systems and humans operate them, and one study of large internet services found <mark style="background: #FFF3A3A6;">configuration errors by operators were the <b>leading</b> cause of outages — with hardware faults implicated in only 10–25%.</mark>

The obvious response is to design interfaces that make the right thing easy and the wrong thing hard: good abstractions, good APIs, good admin tooling. That's correct, and it comes with a caveat that is easy to skip past.

---

### The caveat

If the interface is too restrictive, people work around it — and the workaround negates the benefit entirely.

<mark style="background: #FF5582A6;">A restriction removes a safe path but not the need. So the work relocates to an unsafe path, and that path has no guardrails at all.</mark>

You end up strictly worse off than with a permissive interface, because the dangerous action is now also **invisible** to you.

#### What this looks like

**Deploy tooling that permits only one pipeline.** At 3am the on-call engineer SSHes to the box and hand-edits the config. Prod now differs from the repo and nothing recorded the change. The audit trail is intact and lying.

**An admin UI that refuses bulk operations** for safety. Ops needs to fix 40,000 rows, so they script it against the database directly — skipping every validation the UI existed to enforce.

**A guard blocking `DELETE` without a `WHERE` clause.** Someone disables it for a legitimate one-off, and it stays disabled, because re-enabling it is a task with no deadline attached.

**A service layer forbidding repository access from controllers.** Under deadline someone adds a `@Query(nativeQuery = true)` that bypasses the entity listeners doing audit logging. The architectural rule held; the audit log quietly stopped being complete.

---

### The design lesson

<mark style="background: #ABF7F7A6;">An interface must make the right thing <b>easy</b>, not merely make the wrong thing <b>hard</b>.</mark> Do only the second and you have relocated risk, not reduced it.

This is why the rest of the human-error toolkit assumes the mistake happens anyway and works on containment: sandbox environments with real data, gradual rollout, fast rollback, and detailed telemetry. It's the same tolerate-don't-prevent stance from [[Preventing a fault beats tolerating it only when no cure exists|the fault discussion]], applied to people.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[A fault is a component deviating from spec while a failure is the system no longer serving users]]
- [[Preventing a fault beats tolerating it only when no cure exists]]
