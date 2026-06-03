---
aliases: [Strategy in Java, Java Strategy pattern]
---

This is the idiomatic Java implementation of the [[The Strategy pattern makes algorithms interchangeable by hiding each behind a common interface|Strategy pattern]]. Java has no [[First-class functions treat functions as values that can be passed, stored, and returned|first-class functions]], so the natural expression is an **interface plus one class per algorithm**.

### The Strategy interface

```java
interface PaymentStrategy {
    void processPayment(Order order);
}
```

### Concrete Strategies

```java
class CreditCardPayment implements PaymentStrategy {
    public void processPayment(Order order) { /* charge card */ }
}

class PayPalPayment implements PaymentStrategy {
    public void processPayment(Order order) { /* redirect to PayPal */ }
}
```

### The Context

```java
@RequiredArgsConstructor
class CheckoutService {
    private final PaymentStrategy strategy;       // injected via constructor

    void checkout(Order order) {
        strategy.processPayment(order);           // no if/else
    }
}
```

### Selecting the strategy (the one allowed lookup)

The customer's choice arrives as data (a `String` or enum). A factory maps it to the right object — <mark style="background: cyan">the single place the `if/else` is allowed to live</mark>:

```java
class PaymentStrategyFactory {
    PaymentStrategy resolve(String type) {
        return switch (type) {
            case "card"   -> new CreditCardPayment();
            case "paypal" -> new PayPalPayment();
            default       -> throw new IllegalArgumentException(type);
        };
    }
}
```

The factory and strategy resolution live in the **service layer** — choosing an algorithm is business logic, not HTTP wiring.

```java
// Controller — thin: parse HTTP, delegate, return
@RestController
@RequestMapping("/orders")
@RequiredArgsConstructor
class OrderController {
    private final OrderService orderService;

    @PostMapping("/{id}/checkout")
    void checkout(@PathVariable Long id, @RequestParam String paymentType) {
        orderService.checkout(id, paymentType);
    }
}
```

```java
// Service — owns the strategy decision
@Service
@RequiredArgsConstructor
class OrderService {
    private final PaymentStrategyFactory factory;

    void checkout(Long orderId, String paymentType) {
        Order order = // ... load order
        PaymentStrategy strategy = factory.resolve(paymentType); // "paypal" → PayPalPayment
        new CheckoutService(strategy).checkout(order);
    }
}
```

`CheckoutService` never knows which strategy it received — it just calls `processPayment()`.

### The Spring idiom

Spring can dissolve even that switch. `@Autowired Map<String, PaymentStrategy>` is filled automatically by Spring — keys are **bean names**, values are all beans implementing `PaymentStrategy`.

#### Bean naming is explicit — default names won't match

By default Spring derives the bean name from the class name with a lowercased first letter: `CreditCardPayment` → `"creditCardPayment"`. That will never match `"card"` from a request param.

<mark style="background: pink">You must name each bean explicitly to match the key your caller will look up:</mark>

```java
@Component("card")
class CreditCardPayment implements PaymentStrategy {
    public void processPayment(Order order) { /* charge card */ }
}

@Component("paypal")
class PayPalPayment implements PaymentStrategy {
    public void processPayment(Order order) { /* redirect to PayPal */ }
}
```

#### The factory

```java
@Service
@RequiredArgsConstructor
class PaymentStrategyFactory {
    private final Map<String, PaymentStrategy> strategies;   // Spring fills this — key = @Component name

    PaymentStrategy resolve(String type) {
        PaymentStrategy strategy = strategies.get(type);     // "paypal" → PayPalPayment bean
        if (strategy == null) throw new IllegalArgumentException("Unknown payment type: " + type);
        return strategy;
    }
}
```

<mark style="background: green">Add a new payment type: write a new `@Component("crypto")` class — factory and Context stay untouched.</mark>

<mark style="background: pink">Note:</mark> in Kotlin or Python the same pattern often needs no interface at all — a plain function type or first-class function is enough. The interface-per-algorithm shape here is a Java trait, not the pattern itself.

### Interface, not abstract class

Java developers often reach for an abstract class here — it feels natural when you expect strategies to share some logic. <mark style="background: pink">That shared base becomes hidden coupling.</mark> A change in the abstract class propagates silently to every concrete strategy, even ones that didn't need the change.

An interface carries only the contract. Each concrete strategy is fully independent — it can extend whatever it likes and owns only its own state. This is the correct shape.

**Use an abstract class only when** two or more concrete strategies share genuine, non-trivial implementation that cannot be extracted to a utility — and even then, treat it as a last resort.

### Read more
- [[The Strategy pattern makes algorithms interchangeable by hiding each behind a common interface]]
- [[First-class functions treat functions as values that can be passed, stored, and returned]]
- [[Design Patterns - MOC]]
