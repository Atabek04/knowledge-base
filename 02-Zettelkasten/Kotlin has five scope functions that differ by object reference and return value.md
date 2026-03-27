---
aliases: [scope functions, let apply also run with]
created: 2026-03-27
tags: [kotlin, scope-functions]
---

### All 5 do the same thing

Execute a block of code on an object. They differ in **how you reference the object** and **what they return**:

| Function | Object ref | Returns | Use for |
|---|---|---|---|
| `let` | `it` | lambda result | null checks, transformations |
| `apply` | `this` | the object | object configuration |
| `also` | `it` | the object | side effects (logging) |
| `run` | `this` | lambda result | scoped computation |
| `with(obj)` | `this` | lambda result | multiple ops on same object |

---

### `let` — transform or null-check

```kotlin
val length = name?.let { it.trim().length }
```

---

### `apply` — configure an object you're building

```kotlin
val server = Server().apply {
    port = 8080
    host = "localhost"
}
// returns the Server itself — configured and ready
```

---

### `also` — do something on the side, keep the original flowing

```kotlin
val result = service.generate(request)
    .also { log.info("Generated report: {}", it.id) }
// returns result unchanged — the log is a side effect
```

---

### `run` — scoped computation where you need `this`

```kotlin
val summary = reportJob.run { "$reportType — $reportName ($status)" }
// accesses reportJob's properties directly via `this`
```

---

### `with(obj)` — same as `run`, but object is argument

```kotlin
val summary = with(reportJob) { "$reportType — $reportName" }
// only difference from run: with(obj) vs obj.run
```

---

### The rule that matters

<mark style="background: #FF5582A6;">Don't nest scope functions.</mark>

```kotlin
// ❌ Unreadable
foo.let { it.bar.also { ... }.let { ... } }

// ✅ One level deep, max
```

---

Read more:

- [[Kotlin let executes a block on a non-null object and returns the result]]
- [[Kotlin MOC]]
