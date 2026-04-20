---
aliases: [extension function, extension functions]
created: 2026-03-30
tags: [kotlin, functions]
---

### The problem in Java

Adding behavior to a type you don't own means writing a utility class with static methods:

```java
public class StringUtils {
    public static ReportType toReportType(String value) {
        return ReportType.valueOf(value.uppercase());
    }
}

ReportType type = StringUtils.toReportType("overdue_report");
```

The operation is about the `String`, but it's just a passive argument. You end up with bloated `*Utils` classes.

---

### Extension functions

Kotlin lets you add functions directly to existing types — without inheriting or modifying the original class:

```kotlin
fun String.toReportType(): ReportType =
    ReportType.valueOf(this.uppercase())

val type = "overdue_report".toReportType()
```

`String.` before the function name is the **receiver type**. Inside the body, `this` refers to the instance you called it on.

Under the hood it compiles to a static method with the receiver as the first parameter — exactly like a Java util. But the call site reads like a method on the type.

---

### Key rules

- <mark style="background: #FF5582A6">Can only access **public** members of the receiver</mark> — no private field access, encapsulation stays intact
- <mark style="background: #FF5582A6">Resolved **statically**</mark> — the compile-time type determines which extension is called, no polymorphism
- Keep visibility tight — `private` or `internal` when the extension is only relevant in one file/module
- You can also write **extension properties**: `val String.initials: String get() = ...`

---

### When to use

- **Converting between types**: `entity.toDomain()`, `"value".toReportType()`
- **Domain-specific operations** on standard types: `LocalDateTime.toDisplayFormat()`
- **Replacing `*Utils`** static methods with discoverable, readable calls

### When NOT to use

- Don't hide complex logic behind an extension — if it's 20 lines, it's probably a service method
- Don't use them as a replacement for proper class design

---

Read more:

- [[Kotlin allows top-level functions]]
- [[Kotlin single-expression functions use equals sign instead of block body]]
- [[Kotlin MOC]]
