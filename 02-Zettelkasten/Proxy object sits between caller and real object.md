### Why Proxy object?

Because we want to add some extra logic to it.
Those logics aren't business logics, instead it's infrastructure code:
- interceptors
- logging
- auth filter
- transactions

You want to add those codes, without polluting your business code.
You don't create those proxy objects, they're created automatically.

---

### How does Proxy work?

- EJB implements an interface
- Container **creates a new class at runtime** that implements the same interface.
- This generated class wraps your object and adds behavior

> When someone calls your bean,
> they're actually calling the **proxy**
> which does extra work
> then delegates to the real bean

---

### Spring also uses Proxy Pattern

```java
@Transactional
@Secured("ROLE_ADMIN")
public void placeOrder(Order order) {
    // your code
}
```

1. at startup, Spring scans you classes
2. Sees `@Transactional` and `@Secured` annotations
3. Creates a <mark style="background: #ABF7F7A6;">proxy</mark> that wraps your bean
4. When injected, other classes **receive the proxy**, not original object
5. Proxy **intercepts** method calls, applies transaction/security logic, then calls original method
