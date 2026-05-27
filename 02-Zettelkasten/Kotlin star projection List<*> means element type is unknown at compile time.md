---
aliases: [star projection, List star, generics star, wildcard kotlin]
created: 2026-05-05
tags: [kotlin, generics, type-system, java]
---

<mark style="background: yellow">**`List<*>`** is Kotlin's star projection — "I know it's a `List`, but I make no claim about what the elements are." Java equivalent: `List<?>`.</mark>

### Why it exists — type erasure

Generics exist only at compile time. At runtime, the JVM erases them:

```kotlin
listOf("a", "b")  // compiled to → List (raw, no type info at runtime)
listOf(1, 2, 3)   // compiled to → List (same raw type)
```

This means:

```kotlin
something is List<String>   // ❌ compile warning: "unchecked cast" — JVM can't verify element type
something is List<*>        // ✓ JVM can check "is it a List?" — element type not claimed
```

---

### `List<*>` vs `List<String>`

```kotlin
val raw: Any = listOf("a", "b", "c")

raw as? List<String>  // ⚠ unchecked cast — compiles with warning, might silently lie
raw as? List<*>       // ✓ safe — JVM verifies "is List", you handle elements separately
```

After getting `List<*>`, use `filterIsInstance<String>()` to safely extract typed elements:

```kotlin
(claims["roles"] as? List<*>)
    ?.filterIsInstance<String>()   // → List<String>, no cast exception possible
```

---

### Java equivalent

| Kotlin | Java |
|---|---|
| `List<*>` | `List<?>` |
| `Map<String, *>` | `Map<String, ?>` |
| `Class<*>` | `Class<?>` |

In Java, `?` is called a **wildcard**. In Kotlin, `*` is called **star projection**. Same concept, different syntax.

---

### Checked vs unchecked cast

**Checked cast** — JVM can verify the type at runtime:

```kotlin
something as String      // JVM checks: is it String? ClassCastException if not
something as? List<*>    // JVM checks: is it List? null if not
```

**Unchecked cast** — JVM can only partially verify:

```kotlin
something as List<String>  // JVM checks "is List?" ✓, but skips element type check
                           // You might get a ClassCastException later when reading an element
```

<mark style="background: pink">Unchecked casts compile with a warning. They're not blocked — the compiler trusts you. The crash appears later, at the use site, not at the cast.</mark>

---

### Read more

- [[Kotlin reified type parameter makes generic type available at runtime for inline functions]]
- [[Kotlin safe cast as? returns null instead of throwing ClassCastException]]
- [[Kotlin - MOC]]
