---
aliases: [data ownership, ownership]
---

<mark style="background: yellow">Data ownership</mark> = which code is responsible for managing an object's lifetime.

The owner is responsible for:
- Protecting the object from unwanted mutations
- Ensuring thread safety
- Cleaning up resources when done

---

### Why It Matters

Without clear ownership, each side assumes the other is protecting the data.

Result: race conditions, data corruption, unpredictable behavior.

---

### Two Ownership Strategies

There are two explicit strategies for assigning ownership:

- <mark style="background: cyan">**Class owns**</mark> — the class copies data at boundaries, takes full responsibility
- <mark style="background: cyan">**Caller owns**</mark> — the caller retains control, class only reads via reference

Choosing explicitly eliminates ambiguity at every call site.

---

Read more:
- [[Class ownership pattern copies data at input and output boundaries]]
- [[Caller ownership pattern stores a read-only reference to external data]]
