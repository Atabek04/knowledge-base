---
aliases: [not-null assertion, double bang, "!!", non-null assertion]
---

The `!!` operator asserts that a value is not null and bypasses Kotlin's null safety system.

```kotlin
val length = name!!.length  // throws NullPointerException if name is null
```

If the value is `null` at runtime, it throws `NullPointerException` — the same crash Kotlin's null system is designed to prevent.

Use only when you are **absolutely certain** the value cannot be null at that point, typically when an external API returns a nullable type but guarantees non-null in context.

Prefer `?.`, `?:`, or `requireNotNull()` in almost all cases.

---

### Read more
- [[Safe call operator avoids null crashes by returning null instead]]
- [[Kotlin provides multiple strategies for safely extracting and validating nullable values]]
- [[Kotlin MOC]]
