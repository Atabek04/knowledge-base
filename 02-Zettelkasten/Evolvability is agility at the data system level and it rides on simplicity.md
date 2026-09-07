---
aliases: [evolvability, extensibility, modifiability, plasticity, agility]
created: 2026-09-03
tags: [maintainability, architecture, software-engineering, ddia]
---

**Evolvability** is the third maintainability principle: make it easy to change the system for use cases nobody anticipated. Also called extensibility, modifiability, or plasticity.

It exists as a separate word for a specific reason, and the reason is a scale distinction.

---

### Why not just call it "agile"

Requirements are never static. You learn new facts, unanticipated use cases appear, business priorities move, users request features, platforms get replaced, regulations change, and growth itself forces architectural change.

Agile working patterns are the organizational answer to that, and the Agile community produced real technical tools for it — **TDD** and **refactoring**.

<mark style="background: #FFF3A3A6;">But those techniques are discussed at a small, local scale: a few source files inside one application. <b>Evolvability</b> is the same idea raised to the level of a data system</mark> — several applications or services with different characteristics.

The worked question Kleppmann poses: how would you *refactor* Twitter's home-timeline architecture from [[Fan-out on write trades expensive writes for cheap reads and fan-out on read does the reverse|fan-out on read to fan-out on write]]? Nothing in the TDD toolkit answers that, and it is unmistakably a refactor.

---

### It is not an independent property

<mark style="background: #ABF7F7A6;">Evolvability is closely linked to simplicity and to the quality of your abstractions — simple, easy-to-understand systems are usually easier to modify than complex ones.</mark>

Which means you don't get to pursue it directly. There is no evolvability feature to add. You buy it by [[Simplicity means removing accidental complexity, not removing functionality|removing accidental complexity]] and by [[Abstraction is the main tool against accidental complexity but good abstractions are hard to find|finding abstractions with clean seams]], and evolvability is the thing you find you have afterwards.

<mark style="background: #FFB8EBA6;">That's also why "we'll make it flexible for the future" so often produces the opposite</mark> — speculative extension points are added complexity, and complexity is precisely what makes a system hard to change.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[The majority of software cost falls in maintenance, so design targets the engineers who arrive later]]
- [[Simplicity means removing accidental complexity, not removing functionality]]
- [[Abstraction is the main tool against accidental complexity but good abstractions are hard to find]]
- [[Fan-out on write trades expensive writes for cheap reads and fan-out on read does the reverse]]
