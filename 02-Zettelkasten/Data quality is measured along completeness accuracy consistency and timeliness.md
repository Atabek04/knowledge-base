---
aliases: [Data Quality, Data Quality Dimensions]
tags: [data-governance, data-modeling, system-analysis, quality]
created: 2026-05-31
---

### Why dimensions?

"Good data" is too vague to act on. **Data quality** is broken into named **dimensions**, each of which can be turned into a <mark style="background: yellow">verifiable, measurable requirement</mark>.

The four core ones:

---

### The four dimensions

**Completeness** — is required data present?
*Rule:* every customer record must have a non-null email.
*Metric:* % of records with all mandatory fields populated.

**Accuracy** — does the data match the real-world truth?
*Rule:* a shipping address must be a real, deliverable address.
*Metric:* % of records validated against an authoritative source.

**Consistency** — does the data agree with itself across places?
*Rule:* a customer's status must be identical in CRM and billing.
*Metric:* % of cross-system values that match.

**Timeliness** — is the data current enough for its use?
*Rule:* inventory counts must be no more than 5 minutes stale.
*Metric:* data age vs the freshness threshold.

---

### Why phrase them as requirements

<mark style="background: #93d4d4">A quality dimension only becomes useful when it has a threshold and a measurement.</mark>

"Data should be accurate" is a wish. "≥ 99% of addresses must validate against the postal service" is a testable requirement a [[A data owner is accountable for a data domain while a data steward maintains its quality|steward]] can monitor and a system can alert on.

This is the same move as turning a vague NFR into a measurable one — quality dimensions make "good data" auditable.

---

### Beyond the core four

Other dimensions appear (uniqueness, validity, integrity), but completeness, accuracy, consistency, and timeliness are the canonical set to reason from.

---

Read more:
- [[A data owner is accountable for a data domain while a data steward maintains its quality]]
- [[A data dictionary is the authoritative catalog defining every data element and its rules]]
- [[Master data management enforces one trusted record for entities shared across systems]]
- [[Databases - MOC]]
