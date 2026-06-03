---
created: 2026-05-29
tags: [java, records, immutability]
aliases: [java records immutability, shallow immutability]
---

A Java record makes all its fields `private final` automatically — you cannot reassign them.

This is called **shallow immutability**: the references are frozen, but the objects they point to may still be mutable.

---

### final means: can't reassign. Not: can't mutate.

```java
final List<String> list = new ArrayList<>();
list = new ArrayList<>();  // ❌ compile error — reassignment blocked
list.add("x");             // ✅ fine — mutating the object, not the reference
```

`final` locks the pointer, not the data behind it.

---

### The problem with records + mutable fields

```java
record Account(List<String> transactions) {}

var acc = new Account(new ArrayList<>());
acc.transactions().add("FAKE"); // ✅ compiles — internal list mutated
```

The record looks immutable from the outside, but a caller can corrupt its state. Same vulnerability as [[Defensive copying prevents external mutation of internal state]].

---

### Fix: compact constructor + List.copyOf()

```java
record Account(List<String> transactions) {
    Account {
        transactions = List.copyOf(transactions); // defensive copy + unmodifiable
    }
}
```

`Account { }` is the record's [[Java records auto-generate accessor, equals, hashCode, and toString from their components#Compact constructor — validate and normalize components|compact constructor]] — it normalizes each component before the field is assigned. Here it swaps the incoming list for an [[Java List is an interface and its mutability depends on the implementation, not the type|unmodifiable copy whose `add()` throws]], so a later mutation through the accessor blows up:

```java
acc.transactions().add("FAKE"); // 💥 UnsupportedOperationException
```

The field now holds that unmodifiable copy — the corruption from the previous section is shut down.

---

### Summary

| | Prevents reassignment | Prevents mutation of contents |
|---|---|---|
| `final` field | ✅ | ❌ |
| Record (default) | ✅ | ❌ for mutable fields |
| Record + `List.copyOf()` | ✅ | ✅ |

Records are not a substitute for defensive copying — they only automate `final`.

---

### Read more

- [[Defensive copying prevents external mutation of internal state]]
- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Java List is an interface and its mutability depends on the implementation, not the type]]
- [[Java objects always live on heap; reference location depends on declaration site]]
- [[Primitive types store actual value, references store only address in memory]]
