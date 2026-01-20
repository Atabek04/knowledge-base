# Data Ownership defines responsibility for object lifecycle

## What is Data Ownership?

**Ownership** = Which code is responsible for:
- Managing the object's lifetime
- Protecting it from mutations
- Ensuring thread safety
- Cleaning up resources

Without clear ownership, bugs occur because each side assumes the other is protecting the data.

---

## The Problem: Ambiguous Ownership

```java
public class PaymentProcessor {
    private List<String> logs;

    // Ambiguous: Who owns the logs?
    public void setLogs(List<String> logs) {
        this.logs = logs;
    }

    public void processTransaction(String tx) {
        logs.add(tx);  // Are we allowed to modify?
    }

    public List<String> getLogs() {
        return logs;  // Can caller modify?
    }
}
```

**Caller code (confused):**

```java
List<String> myLogs = new ArrayList<>();
myLogs.add("Initial log");

PaymentProcessor processor = new PaymentProcessor();
processor.setLogs(myLogs);

// Question: Can I modify myLogs now?
// If I do, does processor break?
myLogs.add("External modification");

// Question: Does processor have latest logs or cached copy?
// Is this thread-safe?
processor.processTransaction("BUY 100 STOCKS");

List<String> retrieved = processor.getLogs();
// Question: Can I modify retrieved list? Will it affect processor?
retrieved.clear();
```

**Result:** Unpredictable behavior. Race conditions. Data corruption.

---

## The Solution: Explicit Ownership Rules

**Rule 1: Class owns the data**

The class is responsible for protecting and managing the data.

```java
public class PaymentProcessor {
    private List<String> logs;

    // Caller transfers ownership - we make a copy
    public void setLogs(List<String> logs) {
        this.logs = new ArrayList<>(logs);  // ✅ We own a copy
    }

    public void processTransaction(String tx) {
        logs.add(tx);  // ✅ We safely modify our copy
    }

    // Caller gets a copy - cannot affect our state
    public List<String> getLogs() {
        return new ArrayList<>(logs);  // ✅ Return copy only
    }
}
```

**Caller code (clear expectations):**

```java
List<String> myLogs = new ArrayList<>();
myLogs.add("Initial log");

PaymentProcessor processor = new PaymentProcessor();
processor.setLogs(myLogs);  // ✅ Clear: processor owns a copy

// Safe - processor won't see changes
myLogs.add("External modification");

processor.processTransaction("BUY 100 STOCKS");

List<String> retrieved = processor.getLogs();  // ✅ Clear: I got a copy

// Safe - processor won't see changes
retrieved.clear();
```

---

## Rule 2: Caller owns the data

The caller remains owner. Class just references it (read-only).

```java
public class ReadOnlyProcessor {
    private final List<String> logs;

    // Caller transfers ownership. We store reference (read-only)
    public ReadOnlyProcessor(List<String> logs) {
        this.logs = Collections.unmodifiableList(logs);  // ✅ Caller owns, we read-only
    }

    public int countLogs() {
        return logs.size();  // ✅ Read-only access only
    }

    // Don't expose - caller owns the data
}
```

**Caller code (retains control):**

```java
List<String> myLogs = new ArrayList<>();
myLogs.add("Log 1");

ReadOnlyProcessor processor = new ReadOnlyProcessor(myLogs);

// ✅ Caller modifies, processor sees updates
myLogs.add("Log 2");
System.out.println(processor.countLogs());  // 2

// ✅ Processor cannot modify
// processor.getLogs().add("..."); // Throws UnsupportedOperationException
```

---

## Real-World Example: Payment Service

### Without Clear Ownership (BAD)

```java
public class PaymentService {
    private List<Payment> payments;

    public void loadPayments(List<Payment> payments) {
        this.payments = payments;  // 🔴 Ambiguous
    }

    public void addPayment(Payment p) {
        payments.add(p);
    }
}

// Caller confused
List<Payment> myPayments = database.fetch();
service.loadPayments(myPayments);

// Does modifying myPayments affect service?
// Does service modifying affect myPayments?
// Can another thread access myPayments safely?
```

### With Clear Ownership (GOOD)

```java
public class PaymentService {
    private final List<Payment> payments;

    // ✅ Clear: Service owns a copy
    public PaymentService(List<Payment> payments) {
        this.payments = new ArrayList<>(payments);
    }

    public void addPayment(Payment p) {
        payments.add(p);  // ✅ Safe, we own the data
    }

    // ✅ Clear: Caller gets copy only
    public List<Payment> getPayments() {
        return new ArrayList<>(payments);
    }
}

// Caller knows the contract
List<Payment> myPayments = database.fetch();
PaymentService service = new PaymentService(myPayments);

// ✅ Safe: Service owns a copy. External changes don't affect it.
myPayments.clear();

// ✅ Safe: Retrieved list is a copy. Modifying it won't affect service.
List<Payment> retrieved = service.getPayments();
retrieved.clear();
```

---

## Ownership Decision Tree

```
Does the class need to protect the data?
├─ YES → Class owns (copy on input/output)
└─ NO → Caller owns (reference, mark read-only)

Is the data multi-threaded?
├─ YES → Class owns (synchronization responsibility)
└─ NO → Either works (depends on use case)

Is the data mutable?
├─ YES → Copy at boundaries
└─ NO → Reference is safe
```

---

## Summary

| Aspect | Class Owns | Caller Owns |
|--------|-----------|------------|
| Input | Copy the data | Reference is OK |
| Output | Return copy | Return reference |
| Modification | Class responsibility | Caller responsibility |
| Thread safety | Class handles | Caller handles |
| When to use | Most common | Read-only scenarios |

**Golden rule:** When unclear, choose "Class owns." It's safer and clearer.
