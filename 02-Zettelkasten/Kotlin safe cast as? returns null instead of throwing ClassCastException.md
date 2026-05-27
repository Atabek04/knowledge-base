---
aliases: [as?, safe cast, nullable cast, kotlin safe cast]
created: 2026-05-05
tags: [kotlin, type-system, null-safety]
---

<mark style="background: yellow">**`as?`** is the safe cast operator. If the value isn't the expected type at runtime, it returns `null` instead of throwing `ClassCastException`.</mark>

### Comparison

```kotlin
val x: Any = "hello"

x as Int        // ❌ ClassCastException at runtime — crashes
x as? Int       // ✓ returns null — safe
x as? String    // ✓ returns "hello" — type matches
```

---

### Why use it over `as`

`as` is appropriate when a wrong type is a programming error that *should* crash. `as?` is appropriate when the type is uncertain and `null` is a valid "not this type" signal.

In `UserContextResolver`:

```kotlin
claims["iin"] as? String
```

`claims["iin"]` returns `Any?` (JWT claim value is `Object`). The claim might be absent, might be a wrong type. `as?` returns `null` in both cases — then `requireValidClaim` converts that `null` into a clean `ReportException` with a useful message.

<mark style="background: cyan">This is the Kotlin pattern: unsafe external data → safe cast to nullable → handle null explicitly. Avoids uncontrolled crashes from raw `as`.</mark>

---

### Also null-safe

`as?` handles `null` input:

```kotlin
val n: String? = null
n as? String    // → null (not a crash)
```

A `null` value can never match any non-null type — `as?` returns `null` consistently.

---

### Java equivalent

Java has no safe cast operator. You guard manually:

```java
Object x = claims.get("iin");
String iin = (x instanceof String) ? (String) x : null;
// or in Java 16+:
String iin = x instanceof String s ? s : null;   // pattern matching
```

Kotlin's `as?` compiles to the same `instanceof` + cast pattern.

---

### Read more

- [[Kotlin as keyword performs explicit type cast at runtime]]
- [[Kotlin - MOC]]
