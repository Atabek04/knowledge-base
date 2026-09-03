---
aliases: [interface static method, static method in interface]
created: 2026-08-19
tags: [java, oop]
---

An interface `static` method is a utility method that lives on the interface type itself — it's never inherited by implementers and can't be called through an implementing instance.

<mark style="background: #FFF3A3A6;"><b>You call it directly on the interface name, like `InterfaceName.method()` — never `implementer.method()`.</b></mark> It exists purely to give an interface a home for helper logic that's related to it but doesn't depend on any particular implementation's state.

```java
interface Comparator<T> {
    int compare(T a, T b);                     // abstract — the one SAM method

    static <T extends Comparable<T>> Comparator<T> naturalOrder() {
        return Comparable::compareTo;           // static factory — belongs to Comparator itself
    }
}

Comparator<String> cmp = Comparator.naturalOrder();  // called on the interface, not an instance
```

Because a `static` method has a body and isn't inherited by implementers, it doesn't count toward the [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit|SAM rule]] either — `Comparator` can carry many static helpers like `naturalOrder()` and still be a functional interface, since only `compare()` is abstract.

### Read more

- [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit]]
- [[Java interfaces define a contract with no state, while abstract classes can hold state and partial implementation]]
- [[Java MOC]]
