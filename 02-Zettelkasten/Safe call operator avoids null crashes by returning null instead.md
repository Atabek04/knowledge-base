---
aliases: [safe call]
created: 2026-03-26
tags: [kotlin, null-safety]
---

### The problem

When a variable is nullable (`Type?`), Kotlin won't let you call methods on it directly — it might be `null`.

```kotlin
val name: String? = null
println(name.length)  // ❌ Compile error — name could be null
```

---

### Safe call `?.` — "if not null, call it; if null, return null"

```kotlin
val name: String? = null
println(name?.length)  // prints: null (no crash)

val name2: String? = "Ayub"
println(name2?.length)  // prints: 4
```

<mark style="background: #FF5582A6;">`?.` is not "replace with null then call `.length`"</mark> — it's a short-circuit: if `name` is null, **stop immediately and return `null`**. `.length` never gets called.

```kotlin
// name?.length is equivalent to:
if (name != null) name.length else null
```

---

### Chaining safe calls

Works through multiple nullable levels — if any link is null, the whole chain returns `null`:

```kotlin
val city = user?.address?.city  // null if user OR address OR city is null
```

Compare with Java's manual null checking:

```java
String city = null;
if (user != null && user.getAddress() != null) {
    city = user.getAddress().getCity();
}
```

Kotlin does the same in one expression.

---

Read more:

- [[Elvis operator provides a default when left side is null]]
- [[Kotlin tells you to declare variables with initialization]]
- [[Kotlin MOC]]
