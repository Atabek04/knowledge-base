---
created: 2026-05-30
aliases: [private keyword wrong abstraction, encapsulation level mismatch, module vs type encapsulation]
tags:
  - software-design/principles
  - language-design
---

> The real goal of encapsulation is preventing users from coupling to implementation details. That's a *module boundary* problem. The `private` keyword solves it at the *type* level — the wrong level of abstraction.

### The mismatch

A module (a library, a package, a compiled unit) is the natural boundary between "your code" and "user code."

`private` operates at the class level — it restricts field access within a single file or compilation unit, not across the module boundary.

This means:
- Code *inside* your library can freely access private fields of other classes
- The module still exposes more than it should to internal components
- Users outside the module can sometimes route around `private` (reflection, JNI, Unsafe)

### What would actually work

True module-level encapsulation:
- **C opaque pointers** — hide the struct definition from the header entirely
- **Go unexported identifiers** — lowercase = package-private, enforced at the package boundary
- **Java modules (JPMS)** — `module-info.java` controls what packages are exported
- **Zig** — no `private` at all; separation is achieved through what you expose in the public interface file

### The Zig / Odin argument

Andrew Kelly (Zig) and the Odin community argue: getters/setters and `private` are anti-patterns because they solve the wrong problem at the wrong level. Better to design module APIs deliberately and trust your users.

The backlash against this stance is largely habitual — developers internalized `private` as a virtue without examining what it actually protects.

---

Read more:
- [[Getters and setters add boilerplate without real encapsulation]]
- [[Hyrum's Law states any observable behavior in a library will be depended on]]
- [[C achieves data hiding by omitting struct definitions from headers]]
- [[Private keyword in C++ created header dependencies and long compile times]]
- [[Software Engineering Principles - MOC]]
