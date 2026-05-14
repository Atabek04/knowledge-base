---
created: 2025-12-30
tags: [moc]
---

Kotlin language fundamentals covering variables, types, and collections.
Includes core concepts for writing idiomatic Kotlin code with proper type handling and modern language features.

## Basic Types

### Variables & Mutability

- [[Variable declaration in Kotlin is done by var and val]] — mutable vs immutable references
- [[val in Kotlin guards only its own level of reference not nested objects]] — val on fields, composition, and cascading immutability
- [[Kotlin tells you to declare variables with initialization]] — variable initialization requirements
- [[Kotlin is single type system, no wrappers]] — unified type handling compared to Java

### Functions

- [[Kotlin allows top-level functions]] — functions outside classes at file level
- [[Kotlin single-expression functions use equals sign instead of block body]] — drop `{}` and `return` for one-liners
- [[Kotlin default parameters reduce function overloads]] — `prefix: String = "Info"` eliminates overloads
- [[Kotlin named arguments improve call-site readability]] — pass by name, swap order, skip optional params
- [[Kotlin extension functions add methods to existing types without modifying them]] — receiver type, replaces `*Utils` classes

### String Handling

- [[Use String templates for string concatenation]] — variable interpolation in strings
- [[Kotlin string format specifiers use percent prefix with type flags]] — `%d` for integers, `%f` for doubles, `%,` for thousands

## Classes

- [[Kotlin classes are final by default and Spring needs open classes for CGLIB proxying]] — `open` keyword, allopen plugin, CGLIB subclass proxying
- [[Kotlin primary constructor is declared in the class header with parentheses]] — why `()` not `{}`
- [[Kotlin data class auto-generates common methods for data holders]] — equals, toString, copy for free
- [[Kotlin object declaration creates a singleton instance immediately]] — one instance, no constructor, replaces Java singleton pattern
- [[Kotlin companion object holds class-level members like Java static]] — factory methods, constants, no `static` keyword
- [[Kotlin nested classes are static by default unlike Java]] — `inner` opts into outer reference, safe default
- [[Kotlin constructor parameters without val or var are not stored as properties]] — plain param → init-only, not a field

## Enums

- [[Kotlin enums can have methods that enforce business rules]] — transition logic inside the enum itself
- [[Kotlin enums provide entries and valueOf for iteration and string conversion]] — `entries`, `valueOf()`

## Sealed Types

- [[Kotlin sealed types restrict subclasses to compile-time known set]] — when enums aren't enough, each variant carries different data
- [[Kotlin sealed interface is preferred over sealed class]] — prefer interface unless you need shared state
- [[Kotlin data object is a singleton with toString for free]] — for variants with no data

## Control Flow

- [[Kotlin for loop iterates over ranges and collections]] — `1..5` range syntax, list iteration
- [[Kotlin if expression replaces ternary operator]] — `if (a > b) a else b` as expression, no `? :` in Kotlin
- [[Kotlin when expression replaces switch with more power and flexibility]] — pattern matching, ranges, type checks, and more
- [[Kotlin when expression without subject uses boolean conditions]] — `when {}` replaces `if-else` chains

## Null Safety

- [[Kotlin nullable types are declared with question mark suffix]] — `Type?` allows null, plain `Type` does not
- [[Safe call operator avoids null crashes by returning null instead]] — `?.` returns null instead of crashing
- [[Elvis operator provides a default when left side is null]] — `?:` fallback when value is null
- [[Kotlin provides multiple strategies for safely extracting and validating nullable values]] — `?.`, `?:`, `?.let`, `requireNotNull()`, `require()`
- [[Not-null assertion operator bypasses null safety and throws NPE]] — `!!` forces non-null, throws NPE if null, use sparingly

## Scope Functions

- [[Kotlin has five scope functions that differ by object reference and return value]] — let, apply, also, run, with overview
- [[Kotlin let executes a block on a non-null object and returns the result]] — `?.let`, scoping, chaining

## Collections

### Overview

- [[Kotlin has 3 main collections for grouping items]] — Lists, Sets, and Maps fundamentals

### Collection Operations

- [[To check that an item is in a list, use in operator]] — membership testing for collections
- [[To obtain map's keys and values use these methods]] — accessing Map properties
- [[Kotlin collection transformations chain operations to process data]] — filter, map, flatMap, groupBy, associate, and more

## Annotations

- [[Kotlin data class properties need use-site targets for framework annotations]] — `@field:` for Jakarta Validation, default targets parameter
- [[Kotlin custom validation annotations combine annotation class with ConstraintValidator]] — annotation + validator + `@field:Valid` for nested objects

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
- [ ] Kotlin-specific Spring features
- [ ] Migration strategies

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Kotlin in Action** — Manning | 🟡 Important | ⏳ |

## Related MOCs

- [[Java MOC]] — Java primitives and wrapper types for comparison
- [[Java Core - MOC]]
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
