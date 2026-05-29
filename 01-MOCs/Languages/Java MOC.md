---
created: 2026-01-12
tags: [moc, java]
---

Master Java fundamentals before frameworks. This MOC tracks atomic notes (already written) and topics still pending notes.

## Progress

- [ ] Java fundamentals review
- [ ] OOP deep dive + SOLID
- [ ] Generics, Collections internals
- [ ] Streams, Lambdas, Optional
- [ ] Java 17+ features
- [ ] Java 21+ features

---

## Part 1 — JVM & Compilation

### Notes

- [[Differences between JDK, JRE, JVM]]
- [[Write Once, Run Anywhere principle works because of JVM]]
- [[JVM has 5 key responsibilities]]
- [[JVM interpreter executes bytecode by mapping instructions to pre-compiled C functions]]
- [[Java bytecode isn't Machine code]]

### Topics pending notes

- [ ] JVM memory areas (stack, heap, metaspace, method area)
- [ ] Class loading process (loading, linking, initialization)
- [ ] Just-In-Time (JIT) compilation
- [ ] Garbage collection algorithms

---

## Part 2 — Variables & Types

### Notes

- [[Java has 4 types of variables each with distinct scope and memory location]] — instance, static, local, parameter + JVM storage
- [[Primitive types store actual value, references store only address in memory]]
- [[Java has dual type system because JVM optimizes primitives for performance]] — primitives vs wrappers and autoboxing
- [[Casting converts between types in an inheritance hierarchy]] — upcasting, downcasting, and instanceof
- [[Java objects always live on heap; reference location depends on declaration site]] — stack vs heap for references vs objects
- [[Object variable types start with capital letter, whereas primitives with small letter]]
- [[Variable scope - where var exists and can be accessed]]

### Topics pending notes

- [ ] Strings and String Pool
- [ ] StringBuilder vs StringBuffer
- [ ] Arrays and memory layout
- [ ] Wrapper classes and caching (Integer cache -128 to 127)
- [ ] `var` keyword (local variable type inference, Java 10+)

---

## Part 3 — Classes & OOP

### Notes

- [[Java inner classes hold a hidden reference to the outer instance by default]] — hidden `this$0`, memory leak risk, `static` fix

### Topics pending notes

- [ ] Encapsulation, Inheritance, Polymorphism
- [ ] Abstract classes vs Interfaces
- [ ] Composition over inheritance
- [ ] `final`, `static`, `abstract` keywords
- [ ] Nested vs inner vs anonymous vs local classes
- [ ] SOLID principles
  - [ ] Single Responsibility
  - [ ] Open/Closed
  - [ ] Liskov Substitution
  - [ ] Interface Segregation
  - [ ] Dependency Inversion

---

## Part 4 — Data Ownership

### Notes

- [[Data ownership defines which code is responsible for an object's lifecycle]]
- [[Class ownership pattern copies data at input and output boundaries]] — defensive copy, class takes full control
- [[Defensive copying prevents external mutation of internal state]] — copy on input and output, `List.copyOf()` vs `new ArrayList<>()`
- [[Caller ownership pattern stores a read-only reference to external data]] — no copy, class reads only

---

## Part 5 — Generics

### Topics pending notes

- [ ] Type parameters and bounds
- [ ] Wildcards (`?`, `extends`, `super`)
- [ ] Type erasure
- [ ] Generic methods
- [ ] PECS (Producer Extends, Consumer Super)

---

## Part 6 — Collections Framework

### Topics pending notes

- [ ] List implementations (ArrayList, LinkedList)
- [ ] Set implementations (HashSet, TreeSet, LinkedHashSet)
- [ ] Map implementations (HashMap, TreeMap, LinkedHashMap)
- [ ] Queue and Deque
- [ ] Collections internals (hashing, red-black trees)
- [ ] Choosing the right collection
- [ ] Iterator vs ListIterator, fail-fast vs fail-safe

---

## Part 7 — Exception Handling

### Topics pending notes

- [ ] Checked vs unchecked exceptions
- [ ] try-with-resources
- [ ] Multi-catch
- [ ] Custom exception design
- [ ] Best practices (don't swallow, log with cause, fail fast)

---

## Part 8 — Streams & Functional

### Topics pending notes

- [ ] Lambda expressions
- [ ] Functional interfaces (Function, Predicate, Consumer, Supplier)
- [ ] Method references
- [ ] Stream API (intermediate vs terminal operations)
- [ ] Optional (proper usage, anti-patterns)
- [ ] Collectors
- [ ] Parallel streams — when worth it, when not

---

## Part 9 — Language Features by Version

### Notes

- [[From Java 10 you can use Type Inference]]

### Notes

- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Java records are shallowly immutable — final fields prevent reassignment but not mutation of mutable objects]]

### Topics pending notes — Java 17+
- [ ] Sealed classes
- [ ] Pattern matching for `instanceof`
- [ ] Text blocks
- [ ] Switch expressions

### Topics pending notes — Java 21+

- [ ] Virtual Threads (Project Loom)
- [ ] Pattern matching for `switch`
- [ ] Record patterns
- [ ] Sequenced Collections
- [ ] String templates (preview)

---

## Part 10 — Runtime Optimizations

### Notes

- [[Method inlining - replacing method call with method's actual code]]
- [[Eliminate dead code that never executes]]

### Topics pending notes

- [ ] Escape analysis & stack allocation
- [ ] Loop unrolling
- [ ] JIT tiered compilation (C1, C2)

---

## Part 11 — Tooling

### Notes

- [[javap disassembles compiled class files into readable bytecode]]

### Topics pending notes

- [ ] `jar` — packaging class files
- [ ] `jdeps` — dependency analysis
- [ ] `jstack`, `jmap`, `jstat` — runtime diagnostics
- [ ] `jshell` — REPL

---

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Effective Java** — Joshua Bloch | Critical | ⏳ |
| **Modern Java in Action** — Manning | Important | ⏳ |
| **The Well-Grounded Java Developer** | Nice to have | ⏳ |
| **100 Java Mistakes and How to Avoid Them** | Nice to have | ⏳ |

---

## Project Tasks

**E-Commerce Stage 1:** Product catalog CRUD

- [ ] Create Product entity with JPA
- [ ] Implement ProductRepository
- [ ] Create ProductService with business logic
- [ ] Build REST controller
- [ ] Use records for DTOs
- [ ] Apply streams for data transformation

---

## Related MOCs

- [[Java Concurrency - MOC]]
- [[Kotlin - MOC]]
- [[Spring Ecosystem - MOC]]
- [[Design Patterns - MOC]]
- [[Senior Java-Kotlin Developer Roadmap]]
