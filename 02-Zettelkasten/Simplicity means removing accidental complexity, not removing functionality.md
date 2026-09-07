---
aliases: [simplicity, accidental complexity, essential complexity, big ball of mud]
created: 2026-09-03
tags: [maintainability, architecture, software-engineering, ddia]
---

**Simplicity** is the second maintainability principle: make it easy for a new engineer to understand the system. Note it is *not* simplicity of the user interface — this is about the people maintaining it.

The usual objection is that a simpler system must do less. The distinction that dissolves that objection is the useful part of this idea.

---

### Accidental vs inherent

<mark style="background: #FFF3A3A6;">Complexity is <b>accidental</b> if it is not inherent in the problem the software solves — as seen by the users — but arises only from the implementation.</mark> (Moseley and Marks.)

So making a system simpler does not necessarily mean reducing its functionality. It means deleting the complexity that the problem never asked for.

The test is the phrase *as seen by the users*. If a user would recognize the difficulty as part of their problem, it's inherent and you must carry it. If the difficulty exists only because of how you built it, it's accidental and it's yours to remove.

**The name is the mnemonic:** *accidental* complexity got there by accident of implementation. Nobody chose it.

---

### How it shows up and what it costs

A project mired in complexity is a **big ball of mud**. The symptoms are recognizable: explosion of the state space, tight coupling of modules, tangled dependencies, inconsistent naming and terminology, hacks aimed at performance problems, special-casing to work around issues elsewhere.

The cost is not only that everything takes longer. <mark style="background: #FF5582A6;">In complex software there is a greater risk of <b>introducing bugs</b> when making a change</mark> — when a system is hard to reason about, hidden assumptions, unintended consequences, and unexpected interactions get overlooked.

So complexity compounds: it slows down the work *and* raises the defect rate of the work, and the defects generate more work.

The main tool against it is [[Abstraction is the main tool against accidental complexity but good abstractions are hard to find|abstraction]].

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[The majority of software cost falls in maintenance, so design targets the engineers who arrive later]]
- [[Abstraction is the main tool against accidental complexity but good abstractions are hard to find]]
- [[Evolvability is agility at the data system level and it rides on simplicity]]
