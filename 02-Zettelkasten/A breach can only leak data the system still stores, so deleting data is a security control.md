---
aliases: [Data minimization, Store less leak less, Retention as security control]
tags: [security, data-governance, privacy]
created: 2026-10-03
---

Security spending usually goes to keeping attackers out. A second lever costs nothing and works even after the attacker is in: shrink what there is to take.

---

### Why storing less limits a breach

<mark style="background: #ABF7F7A6;">A breach copies what the compromised system holds at that moment, so its worst case is bounded by the data kept, not by how well the system is defended.</mark>

The cleanest example is card numbers.
A shop that hands payments to a processor and keeps only a token cannot leak card numbers, because none exist on its servers.
Card data is safe there by absence, not by encryption.

The same arithmetic applies to everything else: fifteen years of order history leaks as fifteen years; a policy that kept two years would have leaked two.

#### Data minimization

<mark style="background: #FFF3A3A6;">Data minimization means collecting only the fields a purpose needs and keeping them only as long as that purpose lasts.</mark>
It has two halves: do not collect (the card token case), and do not keep (the retention case).

---

### Why forgotten data accumulates

<mark style="background: #FF5582A6;">Deleting data needs someone's sign-off, while keeping it needs nothing, so without an assigned retention period every copy lives forever by default.</mark>

The usual residue: a CRM export made for one mailing and left in a shared folder, scans of ex-employees' passports, mailboxes never cleaned since the company started.
None of it serves a current purpose, and all of it is in scope for the next breach.

<mark style="background: #ADCCFFA6;">Give every class of personal data a retention period and an owner at the moment it is first stored.</mark>
That turns deletion from a decision someone must take into a default someone must override; the policy itself is what [[Data governance documents the retention archival and deletion rules for each class of data|data governance]] writes down.

---

### Read more
- [[Data governance documents the retention archival and deletion rules for each class of data]]
- [[A CRUD matrix maps entities against operations to expose missing or unowned data lifecycles]]
- [[2026-09 Dodo Pizza breach leaked 15 years of customer data but no card numbers]]
- [[Databases - MOC]]
