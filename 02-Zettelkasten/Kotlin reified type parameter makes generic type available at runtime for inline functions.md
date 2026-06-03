---
aliases: [reified, reified type parameter, filterIsInstance, inline reified]
created: 2026-05-05
tags: [kotlin, generics, inline, type-system]
---

<mark style="background: yellow">**`reified`** makes a generic type parameter available at runtime. Normally generics are erased — `reified` keeps the type info alive, but only inside `inline` functions.</mark>

### The problem without `reified`

```kotlin
fun <T> filterByType(list: List<*>): List<T> {
    return list.filterIsInstance<T>()  // ❌ compile error — T is erased at runtime
}
```

The JVM doesn't know what `T` is at runtime, so `is T` check is impossible.

---

### With `reified` + `inline`

```kotlin
inline fun <reified T> filterByType(list: List<*>): List<T> {
    return list.filterIsInstance<T>()  // ✓ T is known at runtime
}
```

`inline` copies the function body to every call site at compile time. At each call site, `T` is a concrete type (`String`, `Int`, etc.) — the compiler substitutes it directly. No erasure.

---

### `filterIsInstance<String>()` — stdlib example

```kotlin
public inline fun <reified R> Iterable<*>.filterIsInstance(): List<R> {
    return filterIsInstanceTo(ArrayList<R>())
}
```

- `Iterable<*>` — works on any collection with unknown element type
- `reified R` — `R` is the target type, available at runtime
- Internally does `if (element is R)` — possible only because `reified`

Usage:

```kotlin
(claims["roles"] as? List<*>)
    ?.filterIsInstance<String>()   // keeps only elements that are actually String
```

Safe. No cast exceptions. Elements that aren't `String` are silently dropped.

---

### Why only `inline` can have `reified`

`inline` = compiler copies the function body to the call site. At that point `T` = `String` (or whatever you passed). The compiler writes `is String` directly into the bytecode. Non-inline functions are called as-is — `T` is erased before the call reaches them.

<mark style="background: pink">You can't call `reified` functions via reflection — they don't exist as separate functions in bytecode at runtime.</mark>

---

### Java equivalent

Java has no `reified`. Workaround: pass `Class<T>` explicitly:

```java
public <T> List<T> filterByType(List<?> list, Class<T> type) {
    return list.stream()
        .filter(type::isInstance)
        .map(type::cast)
        .collect(toList());
}
```

Kotlin `reified` eliminates this boilerplate.

---

### Read more

- [[Kotlin star projection List<*> means element type is unknown at compile time]]
- [[Kotlin MOC]]
