---
aliases: [Data Retention, Retention and Deletion, Data Lifecycle Policy]
tags: [data-governance, data-modeling, system-analysis, compliance]
created: 2026-05-31
---

### The data lifecycle doesn't end at "store"

Most modeling stops at how data is created and used. Governance insists on documenting how it <mark style="background: yellow">ends</mark> — when it is archived, and when it is destroyed.

Three policies, defined per class of data:

- **Retention** — how long active data must be kept (often legally mandated)
- **Archival** — when data moves from hot, queryable storage to cheap cold storage
- **Deletion** — when data must be permanently destroyed

---

### Why these are rules, not afterthoughts

**Keeping data too long is a liability, not an asset.**

- Regulations (GDPR, tax law, healthcare records) *require* both minimum retention *and* deletion deadlines — "keep invoices 7 years," "erase PII on request."
- Old data is attack surface and storage cost with no offsetting value.
- A user's <mark style="background: #f9a8d4">right to erasure</mark> can't be honored if no one defined what "delete this customer" actually means across systems.

---

### What good documentation specifies

For each data class: the trigger, the action, and the owner.

> *Order records → retain 7 years (tax) → then archive to cold storage 3 years → then hard-delete. Owner: Finance.*

This is the lifecycle gap a [[A CRUD matrix maps entities against operations to expose missing or unowned data lifecycles|CRUD matrix]] exposes when an entity has no **D**: someone has to decide what deletion means and when it happens.

---

### Soft vs hard delete

A subtlety engineers must document: does "delete" mean <mark style="background: #93d4d4">soft delete</mark> (flag a row inactive, keep it) or <mark style="background: #93d4d4">hard delete</mark> (physically remove)?

Compliance often demands true erasure; auditing often demands keeping a trace. The governance policy must say which, per data class.

---

Read more:
- [[A CRUD matrix maps entities against operations to expose missing or unowned data lifecycles]]
- [[A data owner is accountable for a data domain while a data steward maintains its quality]]
- [[Data quality is measured along completeness accuracy consistency and timeliness]]
- [[Databases - MOC]]
