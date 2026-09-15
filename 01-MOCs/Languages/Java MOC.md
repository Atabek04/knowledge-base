---
created: 2026-01-12
tags: [moc, java]
---

## JVM & Compilation

- [[Differences between JDK, JRE, JVM|JDK vs JRE vs JVM — what each layer adds]]
- [[Write Once, Run Anywhere principle works because of JVM|Write Once, Run Anywhere via the JVM]]
- [[JVM has 5 key responsibilities|The JVM's 5 core responsibilities]]
- [[JVM interpreter executes bytecode by mapping instructions to pre-compiled C functions|Interpreter maps bytecode to C functions]]
- [[Java bytecode is not machine code — it targets the JVM instruction set, not a physical CPU|Bytecode is not machine code — targets JVM, not the CPU]]
- [ ] JVM memory areas (stack, heap, metaspace, method area)
- [ ] Class loading process (loading, linking, initialization)
- [ ] Just-In-Time (JIT) compilation
- [ ] Garbage collection algorithms

---

## Variables & Types

- [[Java has 4 types of variables each with distinct scope and memory location|Four variable types: scope & storage]]
- [[Primitive types store actual value, references store only address in memory|Primitives hold value, references hold address]]
- [[Java has dual type system because JVM optimizes primitives for performance|Dual type system: primitives vs wrappers]]
- [[Casting converts between types in an inheritance hierarchy|Casting in an inheritance hierarchy]]
- [[Java objects always live on heap; reference location depends on declaration site|Objects on heap, references stack-or-heap]]
- [[Object variable types start with capital letter, whereas primitives with small letter|Capital = object type, lowercase = primitive]]
- [[Variable scope - where var exists and can be accessed|Variable scope]]
- [[From Java 10 you can use Type Inference|var — local type inference, eliminates redundant type declarations]]
- [[A parameter is the variable in the method signature; an argument is the value passed at the call site|Parameter vs argument — slot in signature vs value at call site]]
- [ ] Strings and String Pool
- [ ] StringBuilder vs StringBuffer
- [ ] Arrays and memory layout
- [ ] Wrapper classes and caching (Integer cache -128 to 127)
- [ ] Text blocks — multiline string literals
- [ ] Switch expressions — value-producing switch
- [ ] String templates (preview)

---

## Classes & OOP

- [[Java inner classes hold a hidden reference to the outer instance by default|Inner classes hold a hidden outer reference]]
- [[Object's default equals and hashCode are identity-based|Default equals & hashCode are identity-based]]
- [[The equals contract requires reflexive, symmetric, transitive, and consistent|The equals() contract: 5 clauses]]
- [[Equal objects must return equal hash codes|hashCode contract: equal objects, equal hashes]]
- [ ] Encapsulation, Inheritance, Polymorphism
- [[Java interfaces define a contract with no state, while abstract classes can hold state and partial implementation|Abstract classes vs Interfaces — contract-only vs shared state + partial implementation]]
- [[Java interface default methods carry a body so existing implementers don't break when the interface gains a new method|Interface default methods — add a method without breaking existing implementers]]
- [[Java interface static methods belong to the interface's own namespace, not to any implementing class|Interface static methods — belong to the interface, not to implementers]]
- [ ] Composition over inheritance
- [ ] `final`, `static`, `abstract` keywords
- [ ] Nested vs inner vs anonymous vs local classes
- [ ] Sealed classes — restrict which classes can extend a type
- [[Java instanceof pattern matching binds the checked type to a variable, eliminating the cast|instanceof pattern matching — binds the type check and cast into one]]
- [ ] Pattern matching for `switch`

### SOLID Principles

- [ ] Single Responsibility
- [ ] Open/Closed
- [ ] Liskov Substitution
- [ ] Interface Segregation
- [ ] Dependency Inversion

---

## Records

- [[Java records auto-generate accessor, equals, hashCode, and toString from their components|Records auto-generate accessors, equals, hashCode, toString]]
- [[Java records are shallowly immutable — final fields prevent reassignment but not mutation of mutable objects|Records are shallowly immutable]]
- [[Java records auto-generate accessor, equals, hashCode, and toString from their components#Compact constructor — validate and normalize components|Compact constructor — validates and normalizes components before field assignment]]
- [[Java records support convenience constructors by delegating to the canonical constructor|Convenience constructors — must delegate to canonical via this()]]
- [[Java records can implement interfaces but cannot extend classes or other records|Records implement interfaces but cannot extend classes]]
- [[Java records are natural DTOs — immutable value carriers with generated equality|Records as DTOs — value equality and immutability built-in]]
- [[Java record is a dependency-free alternative to Lombok @Value for immutable value types|record vs @Value — record needs no dependency, @Value allows class extension]]
- [[Java record patterns destructure record components directly inside pattern matching|Record patterns — destructure components directly in instanceof and switch]]

---

## Data Ownership

- [[Data ownership defines which code is responsible for an object's lifecycle|Data ownership = responsibility for lifecycle]]
- [[Class ownership pattern copies data at input and output boundaries|Class ownership: copy at boundaries]]
- [[Defensive copying prevents external mutation of internal state|Defensive copying blocks external mutation]]
- [[Caller ownership pattern stores a read-only reference to external data|Caller ownership: read-only reference]]

---

## Generics

- [ ] Type parameters and bounds
- [ ] Wildcards (`?`, `extends`, `super`)
- [ ] Type erasure
- [ ] Generic methods
- [ ] PECS (Producer Extends, Consumer Super)

---

## Collections Framework

- [[Java List is an interface and its mutability depends on the implementation, not the type|List is an interface; mutability is the impl's job]]
- [ ] List implementations (ArrayList, LinkedList)
- [ ] Set implementations (HashSet, TreeSet, LinkedHashSet)
- [ ] Map implementations (HashMap, TreeMap, LinkedHashMap)
- [ ] Queue and Deque
- [ ] Collections internals (hashing, red-black trees)
- [ ] Choosing the right collection
- [ ] Iterator vs ListIterator, fail-fast vs fail-safe
- [ ] Sequenced Collections — ordered access to first/last elements

---

## Exception Handling

- [ ] Checked vs unchecked exceptions
- [ ] try-with-resources
- [ ] Multi-catch
- [ ] Custom exception design
- [ ] Best practices (don't swallow, log with cause, fail fast)

---

## Streams & Functional

- [[Comparable defines a type's natural ordering through compareTo()|Comparable: natural ordering via compareTo()]]
- [[Comparator defines interchangeable orderings external to a class|Comparator: external, swappable orderings]]
- [[Stream.sorted() orders a stream by natural ordering or a Comparator|Stream.sorted() orders by Comparable or Comparator]]
- [[A Java lambda is an anonymous object implementing a functional interface's single abstract method, not a value of a function type|Lambda — an anonymous object implementing one functional interface method]]
- [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit|Functional interface — exactly one abstract method; default/static don't count]]
- [[A Java lambda closure captures references to variables from its enclosing scope, which must be final or effectively final|Closure — captures enclosing-scope variables, which must be final or effectively final]]
- [ ] Method references
- [ ] Stream API (intermediate vs terminal operations)
- [ ] Optional (proper usage, anti-patterns)
- [ ] Collectors
- [ ] Parallel streams — when worth it, when not

---

## Concurrency

### Prerequisites

- [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit|Functional interface — exactly one abstract method; default/static don't count]]
- [[A Java lambda is an anonymous object implementing a functional interface's single abstract method, not a value of a function type|Lambda — an anonymous object implementing one functional interface method]]
- [[A Java lambda closure captures references to variables from its enclosing scope, which must be final or effectively final|Closure — captures enclosing-scope variables, which must be final or effectively final]]
- [[Each Java thread has its own call stack, so a local variable is never directly visible to another thread|Per-thread stacks — why a local variable is invisible across threads]]

### Threading Basics

<!-- Teaching Progress: Executor & ThreadPoolTaskExecutor track — landed Thread/Runnable + start() vs run(). Next: why raw threads don't scale → Executor. -->

- [[Thread.start() launches a new OS thread asynchronously, while calling run() directly executes synchronously on the caller's thread|Thread + Runnable — start() spins up a new thread, run() just blocks like any method]]
- [ ] Callable — a Runnable that returns a value and can throw
- [ ] Thread lifecycle and states
- [ ] Thread priorities
- [ ] Daemon vs user threads
- [ ] Thread.sleep(), join(), yield()
- [ ] Thread interruption

### Synchronization

- [ ] Race conditions
- [ ] synchronized keyword (methods, blocks)
- [ ] Intrinsic locks and monitors
- [ ] wait(), notify(), notifyAll()
- [ ] Deadlock, livelock, starvation
- [ ] volatile keyword

### java.util.concurrent

- [ ] Executor framework
- [ ] ExecutorService, ThreadPoolExecutor
- [ ] ScheduledExecutorService
- [ ] Future and Callable
- [ ] ForkJoinPool

### Locks & Conditions

- [ ] ReentrantLock
- [ ] ReadWriteLock
- [ ] StampedLock
- [ ] Condition objects
- [ ] Lock fairness

### Concurrent Collections

- [ ] ConcurrentHashMap
- [ ] CopyOnWriteArrayList
- [ ] BlockingQueue implementations
- [ ] ConcurrentLinkedQueue
- [ ] ConcurrentSkipListMap

### Synchronizers

- [ ] CountDownLatch
- [ ] CyclicBarrier
- [ ] Semaphore
- [ ] Phaser
- [ ] Exchanger

### CompletableFuture

- [ ] Creating CompletableFutures
- [ ] Chaining (thenApply, thenCompose, thenCombine)
- [ ] Exception handling (exceptionally, handle)
- [ ] Combining futures (allOf, anyOf)
- [ ] Async execution

### Atomic Classes

- [ ] AtomicInteger, AtomicLong, AtomicBoolean
- [ ] AtomicReference
- [ ] Compare-and-swap (CAS)
- [ ] LongAdder, LongAccumulator

### Thread Safety Patterns

- [[Each Java thread has its own call stack, so a local variable is never directly visible to another thread|Per-thread stacks — why a local variable is invisible across threads]]
- [[A plain shared variable's write is not guaranteed to be visible to another thread without synchronization|Visibility — a write isn't guaranteed visible to another thread without synchronization]]
- [[Java ThreadLocal stores per-thread values to isolate state in concurrent environments|ThreadLocal: per-thread isolated state]]
- [ ] Immutability
- [ ] Thread confinement
- [ ] Safe publication
- [ ] Happens-before relationship

### Virtual Threads

- [ ] Virtual vs platform threads
- [ ] Creating virtual threads
- [ ] Structured concurrency
- [ ] When to use virtual threads
- [ ] Migration from thread pools

---

## Runtime Optimizations

- [[Method inlining - replacing method call with method's actual code|Method inlining]]
- [[Eliminate dead code that never executes|Dead code elimination]]
- [ ] Escape analysis & stack allocation
- [ ] Loop unrolling
- [ ] JIT tiered compilation (C1, C2)

---

## Tooling

- [[javap disassembles compiled class files into readable bytecode|javap disassembles class files to bytecode]]
- [ ] `jar` — packaging class files
- [ ] `jdeps` — dependency analysis
- [ ] `jstack`, `jmap`, `jstat` — runtime diagnostics
- [ ] `jshell` — REPL

---

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Effective Java** — Joshua Bloch | Critical | ⏳ |
| **Java Concurrency in Practice** — Brian Goetz | Critical | ⏳ |
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

**E-Commerce:** Apply concurrency patterns

- [ ] Implement async product search
- [ ] Use CompletableFuture for parallel API calls
- [ ] Implement rate limiting with Semaphore
- [ ] Use virtual threads for high-throughput endpoints

---

## Related MOCs

- [[Kotlin MOC]]
- [[Spring Ecosystem - MOC]]
- [[Design Patterns - MOC]]
- [[Testing - MOC]]
- Java and Kotlin roadmap: Ribaat vault, `06-Planning/Topics/Java-Kotlin-Roadmap.md`
