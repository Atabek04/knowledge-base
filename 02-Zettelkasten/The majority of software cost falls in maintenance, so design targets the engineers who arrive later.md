---
aliases: [maintainability, cost of software, legacy systems, maintenance cost]
created: 2026-09-03
tags: [maintainability, architecture, software-engineering, ddia]
---

Reliability and scalability are about the system's behaviour. Maintainability is about the people who will work on it — and it earns its place next to them because of where the money actually goes.

---

### The economic claim

<mark style="background: #FFF3A3A6;">The majority of the cost of software is not its initial development but its ongoing maintenance</mark> — fixing bugs, keeping it operational, investigating failures, adapting it to new platforms, modifying it for new use cases, repaying technical debt, adding features.

Which means the code is written once and paid for continuously. Optimizing the writing at the expense of the reading is optimizing the small number.

The awkward part is that many engineers dislike exactly this work. Legacy maintenance means fixing other people's mistakes, on outdated platforms, in systems forced to do things they were never meant for — and every legacy system is unpleasant in its own particular way, which is why there's no general advice for dealing with one.

---

### The reframe

You cannot make maintenance pleasant retroactively. <mark style="background: #ABF7F7A6;">The only available move is to design so that you don't create legacy software in the first place</mark> — treating the future maintainer, who may be you in eighteen months, as the actual user of the design.

Kleppmann names three design principles for this, and the rest of the book keeps returning to them:

- **Operability** — [[Good operations can work around bad software but good software cannot survive bad operations|make it easy to keep the system running]]
- **Simplicity** — [[Simplicity means removing accidental complexity, not removing functionality|make it easy for a new engineer to understand]]
- **Evolvability** — [[Evolvability is agility at the data system level and it rides on simplicity|make it easy to change for use cases nobody anticipated]]

<mark style="background: #FFB8EBA6;">None of the three has an easy solution</mark>, the same as reliability and scalability. They are lenses you hold while designing, not features you add.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- The three principles:
    - [[Good operations can work around bad software but good software cannot survive bad operations]]
    - [[Simplicity means removing accidental complexity, not removing functionality]]
    - [[Evolvability is agility at the data system level and it rides on simplicity]]
