---
aliases: [Strategy pattern, Strategy]
---

The name says what it does: a **strategy** is *a chosen way to accomplish a task*, and you can switch to a different strategy when the situation changes. This pattern lets a program pick its strategy for a job at runtime, swapping one for another without touching the code that uses it.

### Intent

Give each algorithm its own class behind a shared interface, so the client swaps behavior by switching objects — never by changing its own code.

### Problem

One task can be done several ways, and the right way is only known at runtime — charging a customer by credit card, PayPal, or crypto. Cramming every variation into one method with a growing `if/else` makes that method fragile: adding a new way means editing code that already works, risking the parts that were fine.

### Solution

Pull each algorithm out into its own object that implements a common interface (the **Strategy**). The original class (the **Context**) no longer does the work itself — it holds a strategy and delegates to it. To change behavior, you hand it a different strategy.

### Real-world analogy

To reach the airport you can take a taxi, a bus, or a bike. Each is a *strategy* for the same goal. You pick one based on budget and time — but "get to the airport" stays the same. Swapping taxi for bus doesn't change the trip's purpose, only how it's carried out.

### Structure — the three roles

- <mark style="background: yellow">**Strategy**</mark> — the interface declaring the operation (`execute()` / `processPayment()`). The contract every algorithm obeys.
- <mark style="background: yellow">**Concrete Strategy**</mark> — one implementation per algorithm (credit card, PayPal, crypto).
- <mark style="background: yellow">**Context**</mark> — holds a Strategy and calls it, never knowing which concrete one it is.

### Pseudocode

```
interface Strategy:
    execute(input)

class ConcreteA implements Strategy:
    execute(input): ...one way...

class Context:
    strategy
    run(input):
        strategy.execute(input)   # no if/else here
```

### When to use

- Many related classes differ only in *behavior*.
- You need different *variants* of an algorithm and want to switch at runtime.
- A class has a massive `if/else` (or `switch`) choosing between variants of the same operation.
- You want to isolate algorithm details from the code that uses them.

### Combinations in one strategy are a design mistake

Bundling two responsibilities into one strategy (e.g. `SortAndFilterStrategy`) seems convenient until you need one without the other. Now you have to create `SortOnlyStrategy` and `FilterOnlyStrategy` anyway — and the combined one becomes dead weight.

<mark style="background: pink">**One strategy = one algorithm.**</mark> When behaviors vary independently, give each its own strategy family and let the Context hold both — this is exactly the [[Favor composition over inheritance when behaviors vary independently|composition over inheritance]] principle applied inside the pattern itself.

---

### Pros and cons

**Pros**
- Swap algorithms at runtime.
- Isolates each algorithm's details from its callers.
- Replaces conditionals with polymorphism (<mark style="background: cyan">choice happens once, at the edge</mark>).
- Open/Closed: add a new algorithm without editing existing code.

**Cons**
- More objects/classes for simple cases — if behavior rarely changes, a plain `if/else` is fine.
- Clients must know the strategies exist to choose one.
- <mark style="background: pink">Common mistake:</mark> thinking Strategy *removes* `if/else` everywhere. It only *isolates* the choice to one place; the selection still picks a concrete strategy somewhere.

### Read more
- Implementations:
    - [[Strategy pattern in Kotlin uses a function type instead of an interface]]
    - [[Strategy pattern in Python uses a first-class function as the strategy]]
    - [[Strategy pattern in Java is an interface implemented by interchangeable algorithm classes]]
- Underlying concepts:
    - [[Favor composition over inheritance when behaviors vary independently]]
    - [[First-class functions treat functions as values that can be passed, stored, and returned]]
    - [[Kotlin typealias creates a readable alias for an existing type without creating a new class]]
- [[Design Patterns - MOC]]
