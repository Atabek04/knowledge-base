---
aliases: [nested class, inner class]
created: 2026-03-27
tags: [kotlin, oop]
---

### Java's problem

In Java, [[Java inner classes hold a hidden reference to the outer instance by default|inner classes hold a hidden reference to the outer instance by default]]. The compiler secretly adds a `this$0` field pointing to the outer object — which means memory leak risk if you forget to add `static`.

<mark style="background: #FF5582A6;">The dangerous option (holding outer reference) is Java's default. You have to remember `static` every time.</mark>

---

### Kotlin flips the default

Kotlin learned from Java's mistake. Nested classes are **static by default** — no outer reference:

```kotlin
class Report(val id: String) {

    // Nested — no reference to Report (Java's static class)
    class Metadata(val author: String, val version: Int)

    // Inner — holds reference to outer Report (Java's default)
    inner class Page(val number: Int) {
        fun header() = "Report $id — Page $number"  // can access outer id
    }
}
```

```kotlin
// Nested — created independently
val meta = Report.Metadata("Ayub", 1)

// Inner — needs an outer instance
val page = Report("R-001").Page(1)
page.header()  // "Report R-001 — Page 1"
```

---

### Side by side

| | Java | Kotlin |
|---|---|---|
| No outer reference | `static class` | `class` (default) |
| Has outer reference | `class` (default) | `inner class` |

<mark style="background: #FFF3A3A6;">Kotlin makes the safe choice the default. You opt *into* the outer reference with `inner`, not out of it.</mark>

---

### Rule of thumb

Use nested (default) for logical grouping. Use `inner` only when the nested class genuinely needs the outer instance's state. In practice, `inner` is rare.

---

Read more:

- [[Java inner classes hold a hidden reference to the outer instance by default]]
- [[Kotlin primary constructor is declared in the class header with parentheses]]
- [[Kotlin data class auto-generates common methods for data holders]]
- [[Kotlin MOC]]
