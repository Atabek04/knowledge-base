---
aliases: [defensive copy, defensive copying]
---

<mark style="background: yellow">Defensive copying</mark> = making a new copy of mutable data at boundaries so internal and external code point to separate objects.

Without it, both sides share the same reference — external code can corrupt internal state at any time.

---

### The Problem

```java
public class Account {
    private final List<String> transactions;

    public Account(List<String> transactions) {
        this.transactions = transactions; // ❌ shared reference
    }

    public List<String> getTransactions() {
        return transactions; // ❌ exposes mutable internal list
    }
}
```

Caller can mutate `transactions` after passing it in, or clear it after getting it back.

---

### The Fix: Copy on Input and Output

```java
public class Account {
    private final List<String> transactions;

    public Account(List<String> transactions) {
        this.transactions = List.copyOf(transactions); // ✅ copy on input
    }

    public List<String> getTransactions() {
        return List.copyOf(transactions); // ✅ copy on output
    }
}
```

Pre-Java 10 alternative:

```java
this.transactions = new ArrayList<>(transactions);

public List<String> getTransactions() {
    return Collections.unmodifiableList(new ArrayList<>(transactions));
}
```

---

### When to Copy

| Situation | Action |
|-----------|--------|
| Mutable object in constructor | Copy on input |
| Returning mutable object | Copy on output |
| Storing external objects | Copy immediately |
| Internal-only data | No copy needed |

---

### Performance

Copying has overhead, but correctness beats performance — especially at security boundaries.

<mark style="background: pink">Prefer `List.copyOf()` (modern, returns unmodifiable copy) over `new ArrayList<>()` unless you need a mutable internal list.</mark>

---

Read more:
- [[Class ownership pattern copies data at input and output boundaries]]
- [[Data ownership defines which code is responsible for an object's lifecycle]]
