## Java Basics

### JVM & Compilation Fundamentals

- [[Differences between JDK, JRE, JVM]]
- [[Write Once, Run Anywhere principle works because of JVM]]
- [[JVM has 5 key responsibilities]]
- [[JVM interpreter executes bytecode by mapping instructions to pre-compiled C functions]]

### Variables & Types

- [[Java has 4 types of variables each with distinct scope and memory location]] — instance, static, local, parameter + JVM storage
- [[Primitive types store actual value, references store only address in memory]]
- [[Java has dual type system because JVM optimizes primitives for performance]] — primitives vs wrappers and autoboxing
- [[Casting converts between types in an inheritance hierarchy]] — upcasting, downcasting, and instanceof
- [[Object variable types start with capital letter, whereas primitives with small letter]]
- [[Variable scope - where var exists and can be accessed]]

### Classes

- [[Java inner classes hold a hidden reference to the outer instance by default]] — hidden `this$0`, memory leak risk, `static` fix

### Data Ownership

- [[Data ownership defines which code is responsible for an object's lifecycle]]
- [[Class ownership pattern copies data at input and output boundaries]] — defensive copy, class takes full control
- [[Defensive copying prevents external mutation of internal state]] — copy on input and output, `List.copyOf()` vs `new ArrayList<>()`
- [[Caller ownership pattern stores a read-only reference to external data]] — no copy, class reads only

### Language Features

- [[From Java 10 you can use Type Inference]]

### Runtime Optimizations

- [[Method inlining - replacing method call with method's actual code]]
- [[Eliminate dead code that never executes]]
