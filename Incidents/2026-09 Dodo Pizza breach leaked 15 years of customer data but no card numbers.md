---
created: 2026-10-03
tags: [incident, security]
aliases: [Dodo Pizza breach, DataSuckers breach]
severity: high
status: public report, attack vector undisclosed
---

> Dodo Pizza lost its customer database to an extortion group. Every field it stored leaked; card numbers did not, because it never stored them.

### Symptom

On 27 and 28 September 2026 the DataSuckers group announced on Telegram that it was downloading the customer base of a fast-food delivery service, then named Dodo Pizza. The company confirmed that names, delivery addresses, emails, phones, birth dates and order contents of part of its customers may have been accessed. The attackers claim 68 million records and 15 years of orders; no independent confirmation yet.

### Root cause

The entry point is undisclosed. The blast radius is known: the customer database held contact data plus the full order history since launch, with no visible retention cutoff, so the leak reached back 15 years. Payments went through a processor, so no card numbers existed to steal. Response: attacker access blocked, all user sessions revoked, regulator notified.

### Where to look next time

- What would leak if this database were copied tonight? List the fields and the oldest row.
- Which data classes have no retention period and no owner? Those grow forever.
- Old exports outside the main database (shared folders, mailboxes) are in scope too.

### Lessons

- [[A breach can only leak data the system still stores, so deleting data is a security control]]

### Read more
- [[Debugging & Troubleshooting - MOC]]
- Source: [Хакер, 29 Sep 2026](https://xakep.ru/2026/09/29/datasuckers-dodo/)
