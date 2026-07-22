---
created: 2025-12-30
tags: [moc]
---

Kotlin language fundamentals covering variables, types, and collections.
Includes core concepts for writing idiomatic Kotlin code with proper type handling and modern language features.

## Basic Types

### Variables & Mutability

- [[Variable declaration in Kotlin is done by var and val|var vs val — mutable vs immutable references]]
- [[val in Kotlin guards only its own level of reference not nested objects|val guards only its own reference level, not nested objects]]
- [[Kotlin tells you to declare variables with initialization|Variables must be initialized before they are read]]
- [[Kotlin is single type system, no wrappers|Single type system, no wrappers]]

### Functions

- [[Kotlin allows top-level functions|Top-level functions need no class]]
- [[Kotlin single-expression functions use equals sign instead of block body|Single-expression functions with =]]
- [[Kotlin default parameters reduce function overloads|Default parameters replace overloads]]
- [[Kotlin named arguments improve call-site readability|Named arguments improve call-site readability]]
- [[Kotlin extension functions add methods to existing types without modifying them|Extension functions add methods via a receiver type]]
- [[First-class functions treat functions as values that can be passed, stored, and returned|First-class functions — pass, store, return]]
- [[Kotlin typealias creates a readable alias for an existing type without creating a new class|typealias — readable name for existing type]]
- [ ] Operator overloading

### String Handling

- [[Use String templates for string concatenation|String templates interpolate variables]]
- [[Kotlin string format specifiers use percent prefix with type flags|Format specifiers: %d, %f, %, ]]

## Classes

- [[Kotlin classes are final by default and Spring needs open classes for CGLIB proxying|Classes final by default; open for CGLIB proxies]]
- [[Kotlin primary constructor is declared in the class header with parentheses|Primary constructor lives in the class header ()]]
- [[Kotlin data class auto-generates common methods for data holders|data class auto-generates equals, toString, copy]]
- [[Kotlin object declaration creates a singleton instance immediately|object declaration = eager singleton]]
- [[Kotlin companion object holds class-level members like Java static|companion object = class-level members (Java static)]]
- [[Kotlin nested classes are static by default unlike Java|Nested classes static by default; inner opts in]]
- [[Kotlin constructor parameters without val or var are not stored as properties|Param without val/var is init-only, not a field]]
- [ ] Value classes (`@JvmInline`) — zero-overhead wrappers
- [ ] Delegation with the `by` keyword

## Enums

- [[Kotlin enums can have methods that enforce business rules|Enums can hold methods that enforce rules]]
- [[Kotlin enums provide entries and valueOf for iteration and string conversion|Enum entries and valueOf()]]

## Sealed Types

- [[Kotlin sealed types restrict subclasses to compile-time known set|Sealed types = fixed compile-time subclass set]]
- [[Kotlin sealed interface is preferred over sealed class|Prefer sealed interface over sealed class]]
- [[Kotlin data object is a singleton with toString for free|data object = singleton with toString]]

## Control Flow

- [[Kotlin for loop iterates over ranges and collections|for loop over ranges (1..5) and collections]]
- [[Kotlin if expression replaces ternary operator|if is an expression, replacing the ternary]]
- [[Kotlin when expression replaces switch with more power and flexibility|when expression replaces switch]]
- [[Kotlin when expression without subject uses boolean conditions|Subjectless when replaces if-else chains]]

## Null Safety

- [[Kotlin nullable types are declared with question mark suffix|Nullable types use the ? suffix]]
- [[Safe call operator avoids null crashes by returning null instead|Safe call ?. returns null instead of crashing]]
- [[Elvis operator provides a default when left side is null|Elvis ?: provides a default for null]]
- [[Kotlin provides multiple strategies for safely extracting and validating nullable values|Strategies to extract and validate nullables]]
- [[Not-null assertion operator bypasses null safety and throws NPE|Not-null assertion !! throws NPE]]

## Scope Functions

- [[Kotlin has five scope functions that differ by object reference and return value|Five scope functions: let, apply, also, run, with]]
- [[Kotlin let executes a block on a non-null object and returns the result|let runs a block and returns its result]]

## Collections

### Overview

- [[Kotlin has 3 main collections for grouping items|Three collections: List, Set, Map]]
- [[Kotlin read-only List type omits mutators so the reference cannot modify the collection|Read-only List omits mutators (List vs MutableList)]]

### Collection Operations

- [[To check that an item is in a list, use in operator|in operator tests membership]]
- [[To obtain map's keys and values use these methods|Map keys and values accessors]]
- [[Kotlin collection transformations chain operations to process data|Transformations: filter, map, flatMap, groupBy]]

## Annotations

- [[Kotlin data class properties need use-site targets for framework annotations|Use-site targets (@field:) for annotations]]
- [[Kotlin custom validation annotations combine annotation class with ConstraintValidator|Custom validation = annotation + ConstraintValidator]]

## Coroutines

- [ ] `suspend` functions — what they compile to
- [ ] `CoroutineScope`, `CoroutineContext`, `Job`
- [ ] Builders — `launch`, `async`, `runBlocking`
- [ ] Dispatchers — `IO`, `Default`, `Main`, `Unconfined`
- [ ] Structured concurrency
- [ ] `Flow` — cold streams, operators, collection
- [ ] `StateFlow` and `SharedFlow`
- [ ] Exception handling in coroutines
- [ ] Coroutines vs virtual threads — when to use each

## Build & DSL

- [ ] Gradle with Kotlin DSL
- [ ] Kotlin DSL construction (type-safe builders)

## Kotlin + Spring

- [ ] Kotlin Spring Boot setup
- [ ] Null-safety and Spring
- [ ] Data classes as DTOs
- [ ] Repository with Kotlin
- [ ] Coroutines with Spring WebFlux
- [ ] Testing with Kotlin

## Kotlin vs Java

- [ ] When to use Kotlin
- [ ] Interoperability with Java
- [ ] Platform types and nullability annotations
- [ ] Kotlin-specific Spring features
- [ ] Migration strategies

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Kotlin in Action** — Manning | 🟡 Important | ⏳ |

## Related MOCs

- [[Java MOC]]
- [[Spring Ecosystem - MOC]]

## Practice

- [[basics]] — variables, functions, strings (17 cards)
- [[classes]] — constructors, data class, object, companion, nested (15 cards)
- [[enums-sealed]] — enum methods, sealed types, data object (12 cards)
- [[null-safety]] — nullable types, safe call, elvis, when expression (17 cards)
- [[collections]] — scope functions, let, collections, transformations (23 cards)

## External Resources

- [Kotlin Official Documentation](https://kotlinlang.org/docs/)
- [Kotlin Collections Overview](https://kotlinlang.org/docs/collections-overview.html)
- [Kotlin Coding Conventions](https://kotlinlang.org/docs/coding-conventions.html)
