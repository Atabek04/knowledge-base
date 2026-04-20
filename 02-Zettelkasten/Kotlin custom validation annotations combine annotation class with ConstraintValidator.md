---
aliases: [custom validation annotation, custom annotation, ConstraintValidator]
created: 2026-03-30
tags: [kotlin, spring, validation]
---

### When built-in annotations aren't enough

`@NotBlank`, `@Size`, `@Min` validate single fields. But some rules span **multiple fields** — "from-date must be before to-date" can't be expressed with a single-field annotation.

Custom validation annotations let you encode **business rules** that Jakarta Validation enforces automatically.

---

### Three parts to a custom validation

#### 1. The annotation — declares the contract

```kotlin
@Target(AnnotationTarget.CLASS)
@Retention(AnnotationRetention.RUNTIME)
@Constraint(validatedBy = [DateRangeValidator::class])
annotation class ValidDateRange(
    val message: String = "Invalid date range: 'from' must not be after 'to' and range must not exceed 365 days",
    val groups: Array<KClass<*>> = [],
    val payload: Array<KClass<out Payload>> = [],
)
```

- `@Target(CLASS)` — this annotation goes on a class, not a field (because it validates **two fields together**)
- `@Constraint(validatedBy = ...)` — links the annotation to its validator logic
- `message`, `groups`, `payload` — <mark style="background: #FF5582A6">required by Jakarta spec</mark>, every custom constraint must declare all three

#### 2. The validator — implements the logic

```kotlin
class DateRangeValidator : ConstraintValidator<ValidDateRange, ReportFilters.DateRange> {

    override fun isValid(value: ReportFilters.DateRange?, context: ConstraintValidatorContext): Boolean {
        if (value == null) return true

        val fromNotAfterTo = !value.from.isAfter(value.to)
        val withinMaxRange = ChronoUnit.DAYS.between(value.from, value.to) <= MAX_RANGE_DAYS

        return fromNotAfterTo && withinMaxRange
    }

    companion object {
        private const val MAX_RANGE_DAYS = 365L
    }
}
```

- Implements `ConstraintValidator<AnnotationType, ValidatedType>`
- `isValid` returns `true` if valid, `false` triggers the error message
- <mark style="background: #ABF7F7A6">Null check returns `true`</mark> — let `@NotNull` handle nullability separately, keep concerns separated

#### 3. Applying the annotation

```kotlin
data class ReportFilters(
    @field:Valid
    val dateRange: DateRange,
) {
    @ValidDateRange
    data class DateRange(
        val from: LocalDate,
        val to: LocalDate,
    )
}
```

- `@ValidDateRange` on `DateRange` — targets the class itself (`@Target(CLASS)`), so no `@field:` needed
- `@field:Valid` on the parent field — tells Jakarta to **cascade** validation into the nested object
- Without `@field:Valid`, Jakarta won't descend into `dateRange` and the custom annotation never fires

---

### Why `@field:Valid` matters for nested objects

Jakarta Validation only validates the top-level object by default. To validate nested objects, the parent field must be marked with `@Valid`. In Kotlin, that means `@field:Valid` — because the [[Kotlin data class properties need use-site targets for framework annotations|default target is parameter]], not field.

---

Read more:

- [[Kotlin data class properties need use-site targets for framework annotations]]
- [[Kotlin data class auto-generates common methods for data holders]]
- [[Kotlin MOC]]
