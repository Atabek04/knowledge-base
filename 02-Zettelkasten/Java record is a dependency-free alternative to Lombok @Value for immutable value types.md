---
created: 2026-06-08
tags: [java, records, lombok]
aliases: [record vs @Value, when to use record over @Value]
---

Both `record` and Lombok `@Value` produce immutable value types with generated `equals()`, `hashCode()`, and `toString()`. The difference is where generation happens — the JDK compiler vs an annotation processor — and what each allows beyond the basics.

---

### Side-by-side

| | `record` | Lombok `@Value` |
|---|---|---|
| Java version | 16+ (stable) | Any |
| External dependency | None | Lombok required |
| IDE support | Native | Lombok plugin needed |
| Accessor naming | `name()` | `getName()` |
| Can extend a class | ❌ | ✅ |
| JPA entity | ❌ | ❌ (no default constructor) |
| Jackson deserialization | 2.12+ natively | Any version |

---

### Prefer `record` when

- Java 16+ project
- No Lombok, or actively reducing Lombok usage
- DTO or value object with no need to extend a base class
- Core domain type where zero external dependencies matter

---

### Prefer `@Value` when

<mark style="background: #FFF3A3A6;">Use `@Value` when you need to extend a base class</mark> — records [[Java records can implement interfaces but cannot extend classes or other records|cannot extend any class]]. A common case is a shared `BaseDto` carrying audit fields (`createdAt`, `updatedBy`): `@Value` subclasses it, a record cannot.

Also prefer `@Value` in pre-Java-16 codebases, or when the project requires JavaBeans-convention accessors (`getName()`) for framework compatibility.

---

### Read more

- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Java records are natural DTOs — immutable value carriers with generated equality]]
- [[Java records can implement interfaces but cannot extend classes or other records]]
