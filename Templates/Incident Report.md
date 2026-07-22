---
created:
tags: [incident]
aliases:
severity:
status: resolved
---

> One-line summary of what broke and when.

---

### Symptom

What was observed — the error, the alert, the user-visible behavior. Quote exact messages.

### Impact

Who and what was affected, for how long. Scope it: one user, one service, all traffic?

### Timeline

- `HH:MM` — first signal
- `HH:MM` — investigation started
- `HH:MM` — root cause found
- `HH:MM` — resolved

### Investigation

The actual thought path — hypotheses formed, what you checked, the dead ends. This is the most valuable section: future-you needs the *reasoning*, not just the answer.

### Root cause

The real *why*, not the surface why. Run [[The Five Whys traces a symptom to its root cause by asking why repeatedly|the Five Whys]] until you reach something systemic.

### Fix

What actually resolved it — the change, the command, the rollback.

### Prevention

The guardrail so this class of bug can't return — a test, an alert, a checklist item, a config default.

---

### Lessons

Reusable takeaways. Promote each one into an atomic note and link it here, so the incident feeds the permanent knowledge base.

### Read more
- [[Debugging & Troubleshooting - MOC]]
