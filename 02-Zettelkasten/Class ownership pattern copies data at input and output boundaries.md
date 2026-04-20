---
aliases: [class ownership, defensive copy]
---

In the <mark style="background: yellow">class ownership pattern</mark>, the class takes full control of the data by copying it on the way in and on the way out.

This means external code can't accidentally mutate the class's internal state.

---

### Implementation

```java
public class PaymentProcessor {
    private List<String> logs;

    // Copy on input — we own the data
    public void setLogs(List<String> logs) {
        this.logs = new ArrayList<>(logs);
    }

    public void processTransaction(String tx) {
        logs.add(tx); // safe — we own this list
    }

    // Copy on output — caller cannot affect our state
    public List<String> getLogs() {
        return new ArrayList<>(logs);
    }
}
```

Caller modifying their original list after `setLogs()` has no effect.
Caller modifying the returned list has no effect either.

---

### When to Use

- Class needs to modify the data internally
- Data is accessed across threads
- You want strong encapsulation

<mark style="background: pink">Default choice when ownership is unclear</mark> — copying is safer than sharing.

---

Read more:
- [[Data ownership defines which code is responsible for an object's lifecycle]]
- [[Caller ownership pattern stores a read-only reference to external data]]
- [[Defensive copying prevents external mutation of internal state]]
