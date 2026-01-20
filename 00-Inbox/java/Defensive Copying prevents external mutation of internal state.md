
## The Problem

When you assign a reference directly, both internal and external code point to the **same object**. 
External code can mutate your state at any time.

### Example: Banking System

```java
public class Account {
    private final List<String> transactions;

    public Account(List<String> transactions) {
        this.transactions = transactions;  
        // ❌ DANGER: sharing reference
    }

    public List<String> getTransactions() {
        return transactions;  
        // ❌ DANGER: exposing mutable list
    }
}
```

**Caller can destroy internal state:**

```java
List<String> myTransactions = new ArrayList<>();
myTransactions.add("Deposit: $100");
myTransactions.add("Withdrawal: $50");

Account account = new Account(myTransactions);

// Attacker modifies original list
myTransactions.add("FRAUD: $10000 transferred");
myTransactions.add("Hacked by: evil.com");

// Account's internal state is now corrupted!
System.out.println(account.getTransactions());
// Output: [Deposit: $100, Withdrawal: $50, FRAUD: $10000 transferred, Hacked by: evil.com]
```

**From getter side:**

```java
Account account = new Account(someTransactions);
List<String> stolen = account.getTransactions();

// Attacker can modify through the returned reference
stolen.clear();  // All transactions gone!
stolen.add("Balance reset to $1,000,000");
```

---

## The Solution: Defensive Copying

Make a **new copy** of the data. Internal and external objects are separate.

### Correct Implementation

```java
public class Account {
    private final List<String> transactions;

    public Account(List<String> transactions) {
        this.transactions = List.copyOf(transactions);  
        // ✅ Defensive copy
    }

    public List<String> getTransactions() {
        return List.copyOf(transactions);  
        // ✅ Return unmodifiable copy
    }
}
```

Or pre-Java 10:

```java
public Account(List<String> transactions) {
    this.transactions = new ArrayList<>(transactions);  
    // ✅ New list
}

public List<String> getTransactions() {
    return Collections.unmodifiableList(
		    new ArrayList<>(transactions)
		);
}
```

**Now external mutations are harmless:**

```java
List<String> myTransactions = new ArrayList<>();
myTransactions.add("Deposit: $100");

Account account = new Account(myTransactions);

// Try to corrupt
myTransactions.add("FRAUD");

// Account's state is unchanged! ✅
System.out.println(account.getTransactions());  // [Deposit: $100]
```

---

## Why This Matters

At **Stripe** or any fintech company:
- Money is involved
- One mutation = production bug
- One bug = lost customer trust or regulatory violations

Defensive copying is not optional—it's a **safety requirement** at API boundaries.

---

## When to Copy

| Situation | Action |
|-----------|--------|
| Mutable object in constructor | Copy on input |
| Returning mutable object | Copy on output |
| Storing external objects | Copy immediately |
| Internal-only data | No copy needed |

---

## Performance Note

Copying has overhead. But:
- Correctness > Performance (always)
- In real systems, transaction lists are small
- Security cost is negligible vs. attack cost

Use `List.copyOf()` (modern, immutable) unless performance profiling shows bottleneck.
