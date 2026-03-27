## Java Basics

### JVM & Compilation Fundamentals

- [[Differences between JDK, JRE, JVM]]
- [[Write Once, Run Anywhere principle works because of JVM]]
- [[JVM has 5 key responsibilities]]
- [[Java bytecode isn't Machine code]]

### Variables & Types

- [[Primitive types store actual value, references store only address in memory]]
- [[Java has dual type system because JVM optimizes primitives for performance]] — primitives vs wrappers and autoboxing
- [[Casting converts between types in an inheritance hierarchy]] — upcasting, downcasting, and instanceof
- [[Object variable types start with capital letter, whereas primitives with small letter]]
- [[Variable scope - where var exists and can be accessed]]

### Classes

- [[Java inner classes hold a hidden reference to the outer instance by default]] — hidden `this$0`, memory leak risk, `static` fix

### Language Features

- [[From Java 10 you can use Type Inference]]

### Runtime Optimizations

- [[Method inlining - replacing method call with method's actual code]]
- [[Eliminate dead code that never executes]]
