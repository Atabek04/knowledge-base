---
aliases: [as keyword, type cast, unsafe cast, safe cast, as?]
created: 2026-05-05
tags: [kotlin, type-system, null-safety]
---

<mark style="background: yellow">**`as`** is Kotlin's explicit type cast. It tells the compiler: "I know this `Any` is actually a `String` — treat it as one."</mark>

You need it when a value's static type is too broad (`Any`, `Any?`, `Object`) but you know the runtime type. The compiler can't figure it out alone.

---

### Two forms

```kotlin
val claims = principal as Claims        // unsafe cast — ClassCastException if wrong
val name   = principal as? String       // safe cast   — returns null if wrong
```

<mark style="background: cyan">`as?` is almost always safer. Use `as` only when you're certain of the type and a crash is the right failure mode.</mark>

---

### Why you can't skip it

```kotlin
val claims = authentication.principal   // type: Any?
claims["iin"]                           // ❌ compile error — Any? has no [] operator
(claims as Claims)["iin"]              // ✓ Claims implements Map<String, Any>
```

Spring Security types `principal` as `Any?` — it doesn't know what your filter stored there. `as` bridges the gap between what the compiler sees and what you know at runtime.

---

### vs smart cast

Kotlin auto-casts after an `is` check — no `as` needed:

```kotlin
if (principal is Claims) {
    principal["iin"]   // ✓ smart cast — compiler already knows the type here
}
```

Smart cast works when the compiler can guarantee the value doesn't change between the check and the use. For local `val`s this is usually fine. For `var`s or properties from other threads — not safe, so `as` is required.

---

### Not an alias

`as` in type casts is unrelated to `as` in imports:

```kotlin
import java.util.Date as JDate   // ← import alias, rename only
val d = something as JDate       // ← type cast, runtime check
```

Same keyword, different purpose depending on context.

---

### Read more

- [[Kotlin is single type system, no wrappers]]
- [[Spring HandlerMethodArgumentResolver injects custom objects into controller parameters by type]]
- [[01-MOCs/Frameworks/Spring Ecosystem - MOC]]
