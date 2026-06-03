---
created: 2026-06-03
aliases: [Comparable, compareTo, natural ordering]
tags:
  - java
  - collections
---

When you call `Collections.sort(list)` or `stream.sorted()` with no arguments, Java needs to know how two elements compare. That answer lives inside the element's own class, defined by the `Comparable` interface.

`Comparable<T>` has a single method, <mark style="background: #FFF3A3A6;">`int compareTo(T other)`</mark>, which a class implements to declare its <mark style="background: #FFF3A3A6;">natural ordering</mark> — the one obvious, built-in way instances of that type should sort.

The name is the hook: a `Comparable` object can *compare itself to* another of its kind.

### The contract

`compareTo` returns an `int` whose **sign** is all that matters:

- <mark style="background: #BBFABBA6;">negative</mark> → `this` comes **before** `other`
- <mark style="background: #BBFABBA6;">zero</mark> → they are equal in ordering
- <mark style="background: #BBFABBA6;">positive</mark> → `this` comes **after** `other`

```java
class Person implements Comparable<Person> {
    String name;
    int age;

    @Override
    public int compareTo(Person other) {
        return Integer.compare(this.age, other.age);  // natural order = by age
    }
}
```

<mark style="background: #FF5582A6;">Never subtract</mark> (`this.age - other.age`) — it overflows for large or negative ints. Use `Integer.compare()`, `Long.compare()`, etc.

### Why it works automatically

Many standard types already implement `Comparable`: `Integer`, `String` (lexicographic), `LocalDate` (chronological). That is why `sorted()` and `TreeSet` work on them with zero configuration — the ordering ships with the type.

### One ordering only

A class has exactly <mark style="background: #ABF7F7A6;">one natural ordering</mark>, because it can implement `compareTo` once. The moment you need *another* way to sort — by name instead of age, descending instead of ascending — `Comparable` can't help. That is the job of [[Comparator defines interchangeable orderings external to a class|Comparator]].

---

### Read more

- [[Comparator defines interchangeable orderings external to a class]]
- [[Stream.sorted() orders a stream by natural ordering or a Comparator]]
- [[Java MOC]]
