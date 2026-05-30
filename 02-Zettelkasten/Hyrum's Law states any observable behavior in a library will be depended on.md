---
created: 2026-05-30
aliases: [Hyrum's Law, implicit API contract, observable behavior coupling]
tags:
  - software-design/principles
  - api-design
---

> "With a sufficient number of users of an API, it does not matter what you promise in the contract — all observable behaviors of your system will be depended on by somebody." — Hyrum Wright, Google

### What it means

No matter how carefully you mark something as internal or private, users of your library will find it and depend on it — especially if the library is large or widely used.

- They depend on the *order* of returned results, even if you never guaranteed it
- They depend on *error messages*, even if they're implementation details
- They depend on *timing behavior*, *memory layout*, *side effects*

### Why this undermines the case for private

The argument for `private` is: "this can change without breaking users."

Hyrum's Law says: in practice, it *will* break users, because some of them routed around your access modifiers — through reflection, JNI, or just by copying the logic they observed.

Private buys you *less* protection than you think.

### The implication

API design isn't just about what you document. The real API is everything observable. This is why:
- Changing *anything* in a popular library is dangerous
- Semver alone isn't enough — behavioral compatibility matters as much as signature compatibility

---

Read more:
- [[Private fields are a type-level fix for a module-level problem]]
- [[Getters and setters add boilerplate without real encapsulation]]
- [[Software Engineering Principles - MOC]]
