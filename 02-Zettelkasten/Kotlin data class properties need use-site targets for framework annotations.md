---
aliases: [use-site target, use-site targets, field target]
created: 2026-03-30
tags: [kotlin, spring, validation]
---

### One line, three JVM elements

In Java, a constructor parameter, a field, and a getter are three separate things you write yourself:

```java
public class GenerateReportRequest {
    // 1. field — stores the value
    private final String reportName;

    // 2. constructor parameter — receives the value
    public GenerateReportRequest(String reportName) {
        this.reportName = reportName;
    }

    // 3. getter — exposes the value
    public String getReportName() {
        return reportName;
    }
}
```

In Kotlin, `val reportName: String` in the constructor generates **all three at once** — the parameter, the backing field, and the getter. One line of Kotlin, three JVM elements.

This matters because when you annotate that property, the compiler must choose **which** element gets the annotation. You control this with **use-site targets**:

| Target | Where the annotation goes |
|---|---|
| `@param:` | Constructor parameter **(default)** |
| `@field:` | Backing field |
| `@get:` | Getter method |
| `@set:` | Setter method |
| `@property:` | Kotlin property (not visible to Java) |

---

### Why parameter is the default

Kotlin's primary constructor is the "source" declaration — the field and getter are *derived* from it. So the compiler targets the most direct element: the parameter.

This is also the practical choice. Frameworks like Jackson deserialize JSON by **calling the constructor**, so they need annotations on the **parameter**:

```kotlin
data class User(
    @JsonProperty("user_name")  // needs @param: — Jackson calls the constructor
    val name: String,
)
```

If Kotlin defaulted to `@field:`, Jackson wouldn't see this during deserialization — because it reads constructor parameters, not fields.

---

### The problem with field-based frameworks

But not every framework reads constructor parameters. Jakarta Validation inspects **fields** (or getters). So `@NotBlank` with the default `@param:` target does nothing — validation silently passes on invalid input:

```kotlin
data class GenerateReportRequest(
    @NotBlank val reportName: String,  // annotation goes to constructor PARAMETER — validation skipped
)
```

| Framework | Reads from | Needs target |
|---|---|---|
| Jackson | Constructor parameter | `@param:` (default) |
| Jakarta Validation | Field or getter | `@field:` |
| JPA | Field | `@field:` |

---

### The fix — explicit use-site target

The `@field:` prefix tells the Kotlin compiler to place the annotation on the **backing field**, where Jakarta Validation looks:

```kotlin
data class GenerateReportRequest(
    @field:NotBlank(message = "reportName is required")
    val reportName: String,
)
```

Without `@field:`, the annotation targets the parameter and validation is skipped entirely. <mark style="background: #FF5582A6">This is the single most common Kotlin + Spring gotcha.</mark>

---

### Compiler flag alternative

The flag `-Xannotation-default-target=param-property` changes the default target so `@NotBlank` without `@field:` may work. But being explicit with `@field:` is safer and more readable — makes intent clear regardless of compiler settings.

---

Read more:

- [[Kotlin primary constructor is declared in the class header with parentheses]]
- [[Kotlin data class auto-generates common methods for data holders]]
- [[Kotlin MOC]]
