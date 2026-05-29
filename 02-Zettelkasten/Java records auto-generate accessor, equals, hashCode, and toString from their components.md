---
created: 2026-05-29
tags: [java, records]
aliases: [record built-in methods, record accessor]
---

A Java record auto-generates boilerplate for every component declared in its header.

Given `record Account(List<String> transactions, String owner) {}`, the compiler generates:

- **Accessor methods** — `transactions()`, `owner()` — one per component
- **`equals()`** — compares all components by value
- **`hashCode()`** — derived from all components
- **`toString()`** — `Account[transactions=[...], owner=...]`
- **Canonical constructor** — takes all components as parameters

No setters are generated. Records are value carriers — mutate by creating a new instance.

---

### Accessors vs Lombok getters

| | Naming | Example |
|---|---|---|
| **Record** | field name, no prefix | `acc.transactions()` |
| **Lombok `@Getter`** | `get` + capitalized field | `acc.getTransactions()` |

Both return the raw reference — neither makes a defensive copy by default.

---

### No setters — by design

Records have no setters. To "update" a record, create a new one:

```java
record Account(String owner, int balance) {}

var acc = new Account("Alice", 100);
var updated = new Account(acc.owner(), acc.balance() + 50); // new instance
```

Java 14+ `with` pattern (via `wither` libraries or manual) can make this cleaner, but the JDK has no built-in `with` yet.

**Manual wither method:**
```java
record Account(String owner, int balance) {
    Account withBalance(int newBalance) {
        return new Account(owner, newBalance);
    }
}

var updated = acc.withBalance(acc.balance() + 50);
```

**Lombok `@With`** (generates wither methods automatically):
```java
@With
record Account(String owner, int balance) {}

var updated = acc.withBalance(acc.balance() + 50); // Lombok-generated
```

---

### Accessor returns reference, not copy

```java
record Account(List<String> transactions) {}

var acc = new Account(new ArrayList<>());
acc.transactions().add("FAKE"); // ✅ — accessor returns the raw reference
```

The field is `private final` — can't reassign it. But the returned reference lets you mutate the list.
Fix: [[Java records are shallowly immutable — final fields prevent reassignment but not mutation of mutable objects]].

---

### Read more

- [[Java records are shallowly immutable — final fields prevent reassignment but not mutation of mutable objects]]
- [[Defensive copying prevents external mutation of internal state]]
