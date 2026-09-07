---
aliases: [abstraction, good abstraction, facade, reuse]
created: 2026-09-03
tags: [maintainability, architecture, software-engineering, ddia]
---

Once you accept that [[Simplicity means removing accidental complexity, not removing functionality|accidental complexity]] is the target, the question is what removes it. The answer is abstraction — with a caveat that gets skipped in most retellings.

---

### What a good abstraction buys

<mark style="background: #FFF3A3A6;">A good abstraction hides a great deal of implementation detail behind a clean, simple-to-understand façade — and can be reused across a wide range of different applications.</mark>

The reuse is worth more than the saved typing. <mark style="background: #ADCCFFA6;">Quality improvements inside the abstracted component benefit every application using it</mark>, so effort spent there compounds instead of being spent once.

Two examples that make the scale of the hiding obvious:

**High-level programming languages** abstract machine code, CPU registers, and syscalls. You are still using machine code — you're just not thinking about it.

**SQL** abstracts on-disk and in-memory data structures, concurrent requests from other clients, and inconsistencies after crashes. Three genuinely hard problems, behind a declarative sentence.

---

### The caveat

<mark style="background: #FFB8EBA6;">Finding good abstractions is very hard.</mark>

Kleppmann is explicit that in distributed systems specifically, there are many good *algorithms* but it is much less clear how to package them into abstractions that keep system complexity manageable.

That's an honest admission rather than a hedge, and it sets up much of the book: consensus, transactions, and replication all have solid algorithms and contested interfaces.

It also implies the failure mode. <mark style="background: #FF5582A6;">A bad abstraction is worse than none</mark> — it adds a layer to learn without removing the layer beneath, so you now reason about both. A leaky abstraction still charges the full price of the thing it hides.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[Simplicity means removing accidental complexity, not removing functionality]]
- [[Evolvability is agility at the data system level and it rides on simplicity]]
- [[A document database stores self-describing records queried by their nested content]]
