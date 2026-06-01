TARGET DECK: Tech-KB::Java::Data Ownership
Tags: java ownership encapsulation
**Chapter:** Data Ownership
**Related:** [[Java MOC]]

---

START
Coding Questions
What is data ownership in Java?
Back: **Data ownership** — defines which code is responsible for managing an object's lifetime.

The owner is responsible for:
- Protecting the object from unwanted mutations
- Ensuring thread safety
- Cleaning up resources when done

Without clear ownership, each side assumes the other is protecting the data → race conditions, corruption.
Tags: java ownership
<!--ID: 1780311507682-->
END

START
Coding Questions
What are the two strategies for assigning data ownership?
Back:
- **Class owns** — class copies data at input and output; takes full responsibility for the data
- **Caller owns** — caller retains control; class holds a read-only reference, never copies or modifies

Choosing explicitly eliminates ambiguity at every call site.
Tags: java ownership
<!--ID: 1780311507702-->
END

START
Coding Questions
What does the class ownership pattern do at input and output boundaries?
Back: **Copies data in both directions:**
- Constructor/setter: `this.data = new ArrayList<>(input)` — own a separate copy
- Getter: `return new ArrayList<>(data)` — caller gets a copy, can't affect internal state

External mutations to the original list have no effect on the class.
Tags: java ownership encapsulation
<!--ID: 1780311507723-->
END

START
Coding Questions
When should you choose class ownership over caller ownership?
Back: Choose **class ownership** (defensive copy) when:
- Class needs to modify the data internally
- Data is accessed across threads
- You want strong encapsulation

Default choice when ownership is unclear — copying is safer than sharing.
Tags: java ownership
<!--ID: 1780311507744-->
END

START
Coding Questions
What does the caller ownership pattern look like in code?
Back: Store a **read-only reference** — class never copies or modifies:

```java
public class ReadOnlyProcessor {
    private final List<String> logs;

    public ReadOnlyProcessor(List<String> logs) {
        this.logs = Collections.unmodifiableList(logs);
    }
}
```

Caller can still modify their original list — the class sees those changes.
Tags: java ownership
<!--ID: 1780311507764-->
END

START
Coding Questions
What is defensive copying?
Back: **Defensive copying** — making a new copy of mutable data at boundaries so internal and external code point to separate objects.

Copy on input (constructor/setter) and copy on output (getter) so neither side can corrupt the other's state.
Tags: java ownership defensive-copy
<!--ID: 1780311507785-->
END

START
Coding Questions
What is the difference between `List.copyOf()` and `Collections.unmodifiableList(new ArrayList<>())`?
Back:
- **`List.copyOf(input)`** — creates a new **immutable** copy; changes to original don't affect it
- **`Collections.unmodifiableList(list)`** — wraps the **same list** as read-only; changes to original ARE still visible through the wrapper

Use `List.copyOf()` for defensive copies (Java 10+). Use `Collections.unmodifiableList()` for caller-owns pattern.
Tags: java ownership defensive-copy
<!--ID: 1780311507806-->
END

START
Coding Questions
Who is "the caller" in the context of Java encapsulation vulnerabilities?
Back: **Any code** that calls your method — your own code, a teammate, a library, or an attacker.

The vulnerability exists without hacking tools. Anyone holding a leaked reference can mutate your private field:

```java
List<String> leaked = acc.getTransactions(); // points to private field
leaked.clear();        // wipes all internal transactions
leaked.add("FAKE TX"); // injects data
```

No setter called. No reflection. The class never knows its state changed.
Tags: java ownership defensive-copy security
<!--ID: 1780311507826-->
END

START
Coding Questions
What are CWE-374 and CWE-375 in Java?
Back:
- **CWE-374** — passing a mutable object to an untrusted method (input boundary leak)
- **CWE-375** — returning a mutable object to an untrusted caller (output boundary leak)

High-risk targets: transaction logs, audit trails, access control lists — any security-sensitive collection.
Tags: java ownership security cwe
<!--ID: 1780311507847-->
END

START
Coding Questions
What does `Collections.unmodifiableList()` prevent — and what does it NOT prevent?
Back:
- **Prevents:** the class from modifying the list through the wrapped reference
- **Does NOT prevent:** the caller from modifying the list through their original reference — those changes ARE visible through the wrapper

```java
List<String> myList = new ArrayList<>();
var wrapped = Collections.unmodifiableList(myList);
myList.add("x"); // wrapped now shows "x" — NOT blocked
wrapped.add("y"); // throws UnsupportedOperationException — blocked
```
Tags: java ownership
<!--ID: 1780311507867-->
END
