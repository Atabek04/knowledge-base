---
created: 2026-06-03
aliases: [Comparator, comparing, thenComparing, sort by comparator]
tags:
  - java
  - collections
---

[[Comparable defines a type's natural ordering through compareTo()|Comparable]] bakes one ordering into a class. But you often need to sort the *same* type many different ways — users by name here, by age there, by signup date elsewhere. `Comparator` is how you supply an ordering from the **outside**, without touching the class.

`Comparator<T>` defines <mark style="background: #FFF3A3A6;">`int compare(T a, T b)`</mark> — same sign convention as `compareTo`, but it lives in a separate object you pass in. The name fits: a `Comparator` is a standalone *thing that compares* two others.

### compareTo vs compare

- <mark style="background: #ABF7F7A6;">`Comparable.compareTo(other)`</mark> — one argument; the object compares *itself* to another. One per class, internal.
- <mark style="background: #ABF7F7A6;">`Comparator.compare(a, b)`</mark> — two arguments; an outside judge compares *two* objects. Many per type, external and swappable.

### Building comparators

You rarely write `compare` by hand. The static factory `Comparator.comparing()` builds one from a <mark style="background: #BBFABBA6;">key extractor</mark> — a function that pulls out the field to sort by (the Java cousin of Python's `sorted(key=...)`).

```java
Comparator<Person> byName = Comparator.comparing(Person::getName);
Comparator<Person> byAge  = Comparator.comparingInt(Person::getAge);
```

`comparingInt` / `comparingLong` / `comparingDouble` avoid boxing for primitive keys.

### Chaining and reversing

Comparators compose, which is their real power:

```java
Comparator<Person> order = Comparator
        .comparing(Person::getLastName)
        .thenComparing(Person::getFirstName)   // tie-breaker
        .reversed();                           // flip the whole thing
```

- `thenComparing` — <mark style="background: #BBFABBA6;">breaks ties</mark> using the next key, like a tuple key in Python.
- `reversed` — flips the direction of the comparator built so far.

### Using it

Anything that sorts accepts a `Comparator` as an explicit override of natural ordering:

```java
list.sort(byAge);
people.stream().sorted(byName).toList();
new TreeMap<>(byName);
```

<mark style="background: #FF5582A6;">Watch the scope of `reversed()`:</mark> it reverses *everything* chained before it. To reverse just one key, use `Comparator.comparing(Person::getAge, Comparator.reverseOrder())`.

---

### Read more

- [[Comparable defines a type's natural ordering through compareTo()]]
- [[Stream.sorted() orders a stream by natural ordering or a Comparator]]
- [[Python sorted() key argument maps each element to the value used for comparison]]
- [[Java MOC]]
