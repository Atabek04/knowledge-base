---
aliases: [format specifiers, string format]
created: 2026-03-27
tags: [kotlin, strings]
---

### `%,d` breakdown

| Symbol | Meaning |
|---|---|
| `%` | Start of format specifier |
| `,` | Flag: add thousands separator |
| `d` | Type: integer (`Int`, `Long`) |

```kotlin
"%d".format(1234)     // 1234
"%,d".format(1234)    // 1,234
```

<mark style="background: #FF5582A6;">`%d` is for integers only — NOT doubles.</mark>

---

### For doubles use `%f`

```kotlin
"%f".format(3.14)       // 3.140000
"%.2f".format(3.14)     // 3.14
"%,.2f".format(1234.5)  // 1,234.50
```

| Specifier | Meaning |
|---|---|
| `%f` | Floating point, default 6 decimals |
| `%.2f` | Floating point, 2 decimal places |
| `%,.2f` | Thousands separator + 2 decimals |

---

Read more:

- [[Use String templates for string concatenation]]
- [[Kotlin MOC]]
