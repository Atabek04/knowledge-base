---
aliases: [caller ownership, read-only reference]
---

In the <mark style="background: yellow">caller ownership pattern</mark>, the caller retains ownership of the data. The class only holds a read-only reference — it never copies or modifies.

---

### Implementation

```java
public class ReadOnlyProcessor {
    private final List<String> logs;

    // Store reference, but wrap as unmodifiable
    public ReadOnlyProcessor(List<String> logs) {
        this.logs = Collections.unmodifiableList(logs);
    }

    public int countLogs() {
        return logs.size(); // read-only access only
    }
}
```

The caller can still modify their list — the class sees those changes.

```java
List<String> myLogs = new ArrayList<>();
myLogs.add("Log 1");

ReadOnlyProcessor processor = new ReadOnlyProcessor(myLogs);

myLogs.add("Log 2");
System.out.println(processor.countLogs()); // 2 — sees the update
```

<mark style="background: pink">`Collections.unmodifiableList()` prevents the class from mutating the list, but does NOT prevent the caller from mutating it through their original reference.</mark>

---

### When to Use

- Class only needs to read, never modify
- Data is immutable or effectively immutable
- Copying would be expensive and unnecessary

---

Read more:
- [[Data ownership defines which code is responsible for an object's lifecycle]]
- [[Class ownership pattern copies data at input and output boundaries]]
