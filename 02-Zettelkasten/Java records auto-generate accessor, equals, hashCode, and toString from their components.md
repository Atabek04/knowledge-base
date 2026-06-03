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

#### Wither methods — cleaner updates

The manual `new Account(...)` call gets verbose with many components. The **wither** pattern wraps it: a `withX()` method returns a fresh copy with one field changed. The JDK has no built-in `with` yet (Java 14+ only via libraries or manual code).

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

### Compact constructor — validate and normalize components

The compiler already generates a canonical constructor that copies every component into its field. The **compact constructor** lets you hook into that step to validate or normalize the incoming values — without rewriting the whole assignment.

```java
record Account(List<String> transactions) {
    Account {
        if (transactions == null) throw new IllegalArgumentException("null");
        transactions = List.copyOf(transactions); // normalize before assignment
    }
}
```

#### No parameter list — `Account { }` not `Account(...) { }`

<mark style="background: #FFF3A3A6;">The `()` is omitted on purpose.</mark> The record header `(List<String> transactions)` already declares the parameters, so the compact form receives them **implicitly** — you never redeclare them.

#### No explicit field assignment

You also never write `this.transactions = transactions`. At the **end** of the block the compiler auto-assigns each (possibly reassigned) parameter to its matching field. Your job is only to check or transform the parameter — reassigning `transactions` inside the block changes what eventually lands in the field.

This is the natural place to drop in a [[Defensive copying prevents external mutation of internal state|defensive copy]], the fix for the leak shown below.

---

### Accessor returns reference, not copy

```java
record Account(List<String> transactions) {}

var acc = new Account(new ArrayList<>());
acc.transactions().add("FAKE"); // ✅ — accessor returns the raw reference
```

The field is `private final` — can't reassign it. But the returned reference lets you mutate the list.
Fix: [[Java records are shallowly immutable — final fields prevent reassignment but not mutation of mutable objects|wrap the list in a defensive copy]].

The leak exists because `java.util.List` declares `add()`, so the accessor's return type still carries mutators. Kotlin avoids it at the type level — its [[Kotlin read-only List type omits mutators so the reference cannot modify the collection|read-only `List` has no `add()`]], so the same mutation fails to compile.

---

### Read more

- [[Java records are shallowly immutable — final fields prevent reassignment but not mutation of mutable objects]]
- [[Defensive copying prevents external mutation of internal state]]
- [[Kotlin read-only List type omits mutators so the reference cannot modify the collection]]
