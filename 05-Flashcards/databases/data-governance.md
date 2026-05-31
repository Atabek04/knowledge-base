TARGET DECK: Tech-KB::Databases::Data Governance
Tags: data-governance data-modeling system-analysis
**Chapter:** Data Governance
**Related:** [[Databases - MOC]]

---

START
Coding Questions
What is the difference between a data owner and a data steward?
Back:
- **Data Owner** — **accountable** for a data domain: sets rules, approves access, answers for correctness/compliance (senior business role). The owner **decides**.
- **Data Steward** — **responsible** for day-to-day: enforces rules, fixes quality issues, maintains definitions (hands-on role). The steward **does**.
Tags: data-governance roles ownership
END

START
Coding Questions
Why separate the data owner and data steward roles?
Back:
The person with **authority** to set policy (owner) rarely has the **time/proximity** to maintain data daily (steward).

Naming both makes accountability unambiguous: when data is wrong, a named owner answers for it and a named steward fixes it — no diffuse "the system" no one owns.
Tags: data-governance roles
END

START
Coding Questions
What is master data, and why do duplicates/inconsistencies arise across systems?
Back:
**Master data** = core shared entities many systems reference (customers, products, suppliers) — the **nouns** transactions act on.

Each system keeps its own copy → "Acme Corp" vs "ACME Corporation"; an update in one app never reaches the others → the same entity **fragments into conflicting records**.
Tags: data-governance master-data mdm
END

START
Coding Questions
What does Master Data Management (MDM) enforce, and how?
Back:
**One trusted, authoritative record per entity — the "golden record"** — kept aligned across all systems.

How:
- **Match & merge** duplicates
- Define a **system of record** per entity
- **Propagate** changes to all consumers
- Apply ownership/stewardship

It's "one fact, one place" raised from one DB (normalization) to the enterprise.
Tags: data-governance mdm golden-record
END

START
Coding Questions
What are the four core data quality dimensions, with a one-line meaning each?
Back:
- **Completeness** — is required data present? (mandatory fields non-null)
- **Accuracy** — does it match real-world truth? (validated against a source)
- **Consistency** — does it agree with itself across systems? (CRM == billing)
- **Timeliness** — is it current enough for its use? (within a freshness threshold)
Tags: data-governance data-quality
END

START
Coding Questions
Why must a data quality dimension be phrased with a threshold and a metric?
Back:
"Data should be accurate" is a wish; **"≥99% of addresses must validate against the postal service"** is a testable requirement.

A dimension only becomes useful — monitorable by a steward, alertable by a system — once it has a **threshold + measurement**, making "good data" auditable.
Tags: data-governance data-quality requirements
END

START
Coding Questions
What three lifecycle policies does data governance document for each data class?
Back:
- **Retention** — how long active data must be kept (often legally mandated)
- **Archival** — when data moves from hot to cheap cold storage
- **Deletion** — when data must be permanently destroyed

Each specifies a trigger, an action, and an owner (e.g. orders → keep 7 yrs → archive 3 → hard-delete).
Tags: data-governance retention lifecycle
END

START
Coding Questions
Why is keeping data too long a liability, not an asset?
Back:
- Regulations (GDPR, tax, health) mandate **deletion deadlines** and the right to erasure
- Old data is **attack surface** + storage cost with no offsetting value
- Erasure can't be honored if "delete this customer" was never defined across systems

Also: document **soft vs hard delete** per class (audit vs true erasure).
Tags: data-governance retention compliance
END

START
Coding Questions
What is process mining, and what input does it require?
Back:
**Process mining** reconstructs how a process *actually* runs from the **event logs systems already produce**, then compares it to the documented process (Celonis, ProM).

Needs per event: **case ID** (which case), **activity** (what), **timestamp** (when). From many traces it rebuilds the real flow graph.
Tags: data-governance process-mining analytics
END

START
Coding Questions
What does process mining reveal that a documented AS-IS model misses?
Back:
Documentation shows how people *think* work flows; mining shows reality:

- **Deviations** — undocumented shortcuts and rework loops
- **Bottlenecks** — where cases pile up
- **Conformance gaps** — compliance steps skipped

It replaces interviews-and-guessing with **evidence from the log**.
Tags: data-governance process-mining conformance
END
