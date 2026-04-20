---
aliases: [Java variable types, instance variable, static field, local variable, parameter]
---

Java has 4 variable types. They differ in who owns them, where they're accessible, and where the JVM stores them.

---

### 1. Instance Variables (Non-static Fields)

- Belong to an **object**, not the class
- Each object has its own copy
- Hold the object's internal state
- <mark style="background: cyan">Stored in the **Heap** — inside the object allocation</mark>

```java
public class Car {
    String color; // instance variable — each Car has its own color
}
```

---

### 2. Static Fields

- Belong to the **class**, not any object
- <mark style="background: yellow">Shared across all instances</mark> — same value for every object
- <mark style="background: cyan">Stored in the **Heap** — inside the Class object (Metaspace holds class metadata, but static field values live on the heap)</mark>

```java
public class Car {
    static int totalCars; // one value shared by all Car objects
}
```

---

### 3. Local Variables

- Declared inside a method
- Only accessible within that method
- Destroyed when the method returns
- <mark style="background: cyan">Stored in the **Stack** — inside the method's stack frame</mark>

```java
public void drive() {
    int speed = 60; // local variable — gone after drive() returns
}
```

---

### 4. Parameters

- Variables passed into a method at call time
- Scoped to the method body, same as local variables
- <mark style="background: cyan">Stored in the **Stack** — part of the same stack frame as local variables</mark>

```java
public void accelerate(int amount) { // amount is a parameter
    speed += amount;
}
```

---

### Memory Summary

| Variable Type    | Belongs To | Scope       | JVM Storage |
| ---------------- | ---------- | ----------- | ----------- |
| Instance field   | Object     | Whole class | Heap        |
| Static field     | Class      | Whole app   | Heap        |
| Local variable   | Method     | Method only | Stack       |
| Parameter        | Method     | Method only | Stack       |

<mark style="background: pink">Local variables and parameters are NOT initialized by default — compiler forces explicit assignment before use.</mark>
Instance and static fields ARE default-initialized (`0`, `null`, `false`).

---

Read more:
- [[Primitive types store actual value, references store only address in memory]]
- [[Variable scope - where var exists and can be accessed]]
- [[JVM has 5 key responsibilities]]
