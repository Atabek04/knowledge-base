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

### String Handling

- [[Use String templates for string concatenation]] — variable interpolation in strings
- [[Kotlin string format specifiers use percent prefix with type flags]] — `%d` for integers, `%f` for doubles, `%,` for thousands

## Classes

- [[Kotlin primary constructor is declared in the class header with parentheses]] — why `()` not `{}`
- [[Kotlin data class auto-generates common methods for data holders]] — equals, toString, copy for free
- [[Kotlin object declaration creates a singleton instance immediately]] — one instance, no constructor, replaces Java singleton pattern
- [[Kotlin companion object holds class-level members like Java static]] — factory methods, constants, no `static` keyword
- [[Kotlin nested classes are static by default unlike Java]] — `inner` opts into outer reference, safe default

## Enums

- [[Kotlin enums can have methods that enforce business rules]] — transition logic inside the enum itself
- [[Kotlin enums provide entries and valueOf for iteration and string conversion]] — `entries`, `valueOf()`

## Sealed Types

- [[Kotlin sealed types restrict subclasses to compile-time known set]] — when enums aren't enough, each variant carries different data
- [[Kotlin sealed interface is preferred over sealed class]] — prefer interface unless you need shared state
- [[Kotlin data object is a singleton with toString for free]] — for variants with no data

## Control Flow

- [[Kotlin when expression replaces switch with more power and flexibility]] — pattern matching, ranges, type checks, and more

## Null Safety

- [[Kotlin nullable types are declared with question mark suffix]] — `Type?` allows null, plain `Type` does not
- [[Safe call operator avoids null crashes by returning null instead]] — `?.` returns null instead of crashing
- [[Elvis operator provides a default when left side is null]] — `?:` fallback when value is null
- [[Kotlin provides multiple strategies for safely extracting and validating nullable values]] — `?.`, `?:`, `?.let`, `requireNotNull()`, `require()`

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

## Related MOCs

- [[Java MOC]] — Java primitives and wrapper types for comparison

## Practice

(Flashcards to be added)

## External Resources

- [Kotlin Official Documentation](https://kotlinlang.org/docs/)
- [Kotlin Collections Overview](https://kotlinlang.org/docs/collections-overview.html)
- [Kotlin Coding Conventions](https://kotlinlang.org/docs/coding-conventions.html)
