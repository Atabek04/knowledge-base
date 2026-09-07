---
aliases: [systematic fault, software error, latent bug, leap second bug]
created: 2026-09-03
tags: [reliability, architecture, ddia]
---

Hardware faults are random and roughly independent — you can plan against them with a failure rate. Software faults are a different species, and the difference is not that they're more common. It's that there is no rate to plan against.

---

### The shape of the bug

<mark style="background: #FFF3A3A6;">A systematic fault is code making an assumption about its environment that has been true so far.</mark>

The code is deterministic. It has worked perfectly, possibly for years. It will keep working until the one circumstance arrives that invalidates the assumption — and then it fails identically every single time.

The canonical case: the **leap second on June 30, 2012**, which hung applications everywhere at once via a Linux kernel bug. Nobody had that on a risk register, because until that day the assumption "a minute has 60 seconds" had never once been wrong.

---

### Why it can't be anticipated the way hardware can

<mark style="background: #FFB8EBA6;">There is no mean time to failure for a wrong assumption.</mark> You cannot buy a second one, and testing only finds it if your test happens to contain the circumstance you didn't know to think of.

The bug lies dormant, sometimes for years, until an unusual set of circumstances reveals what the software believed about the world.

This is a different property from [[Redundancy only defeats faults that fail independently so it cannot save you from a shared bug|being correlated across nodes]]. Both are true of systematic faults and neither causes the other — dormancy is why you don't see it coming, correlation is why it's expensive when it lands.

---

### What actually helps

No single fix, only accumulation: thinking carefully about the assumptions and interactions in the system, thorough testing, process isolation, letting processes crash and restart, and measuring behaviour in production.

<mark style="background: #ABF7F7A6;">The strongest one: if a system is supposed to guarantee something, have it check itself continuously while running and alert on a discrepancy.</mark> A queue where incoming and outgoing message counts should match can verify that claim about itself, live — turning a silent wrong assumption into a page.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[A fault is a component deviating from spec while a failure is the system no longer serving users]]
- [[Redundancy only defeats faults that fail independently so it cannot save you from a shared bug]]
- [[Deliberately triggering faults is the only way to exercise error-handling code that otherwise never runs]]
