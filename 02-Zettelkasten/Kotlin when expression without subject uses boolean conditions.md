---
aliases: [when without subject, subjectless when, when boolean conditions]
---

`when` can be used without a subject — each branch is a boolean expression.

```kotlin
val trafficAction = when {
    trafficLightState == "Green" -> "Go"
    trafficLightState == "Yellow" -> "Slow down"
    trafficLightState == "Red" -> "Stop"
    else -> "Malfunction"
}
```

Conditions are evaluated top to bottom — first match wins.

This replaces `if-else` chains when branches involve different variables or complex expressions that don't share a common subject.

---

### Read more
- [[Kotlin when expression replaces switch with more power and flexibility]]
- [[Kotlin if expression replaces ternary operator]]
- [[Kotlin MOC]]
