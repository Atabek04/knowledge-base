TARGET DECK: Tech-KB::Java::Streams
Tags: java streams
**Related:** [[Java MOC]]

---

START
Coding Questions
What does the `Comparable` interface define, and through which method?
Back: A type's **natural ordering** — its one built-in way to sort — through `int compareTo(T other)`.

A `Comparable` object can compare *itself* to another of its kind.
Tags: java comparable
<!--ID: 1782128730005-->
END

START
Coding Questions
What does the sign of `compareTo`'s return value mean?
Back:
- **negative** → `this` comes **before** `other`
- **zero** → equal in ordering
- **positive** → `this` comes **after** `other`

Only the sign matters.
Tags: java comparable
<!--ID: 1782128730008-->
END

START
Coding Questions
Why use `Integer.compare(a, b)` instead of `a - b` in `compareTo`?
Back: Subtraction **overflows** for large or negative ints, giving the wrong sign. `Integer.compare()` is overflow-safe.
Tags: java comparable gotcha
<!--ID: 1782128730014-->
END

START
Coding Questions
What problem does `Comparator` solve that `Comparable` cannot?
Back: It supplies an ordering from the **outside**, so the same type can be sorted **many different ways** — without touching the class.

`Comparable` allows only one natural ordering (one `compareTo`).
Tags: java comparator
<!--ID: 1782128730016-->
END

START
Coding Questions
How do `Comparable.compareTo` and `Comparator.compare` differ in arguments and location?
Back:
- `compareTo(other)` — **one** arg; object compares itself; **internal**, one per class
- `compare(a, b)` — **two** args; outside judge compares two objects; **external**, many per type
Tags: java comparator comparable
<!--ID: 1782128730019-->
END

START
Coding Questions
How do you build a `Comparator` that sorts people by name, breaking ties by age?
Back:
```java
Comparator.comparing(Person::getName)
          .thenComparing(Person::getAge);
```
- `comparing` — key extractor for the main field
- `thenComparing` — tie-breaker
Tags: java comparator
<!--ID: 1782128730021-->
END

START
Coding Questions
What does `Comparator.reversed()` reverse, and what's the gotcha?
Back: It reverses **everything chained before it**, not just the last key.

To reverse one key only:
```java
Comparator.comparing(Person::getAge, Comparator.reverseOrder())
```
Tags: java comparator gotcha
<!--ID: 1782128730024-->
END

START
Coding Questions
What are the two forms of `Stream.sorted()`?
Back:
- `sorted()` — natural ordering; elements **must** implement `Comparable` or you get `ClassCastException`
- `sorted(Comparator)` — any custom ordering
Tags: java streams sorted
<!--ID: 1782128730027-->
END

START
Coding Questions
A `Map` can't be sorted directly. How do you sort one by value (descending) in a stream?
Back: Stream the `entrySet()`, sort with a `Map.Entry` comparator:
```java
counts.entrySet().stream()
      .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
```
`comparingByKey()` sorts by key instead.
Tags: java streams map
<!--ID: 1782128730029-->
END

START
Coding Questions
After sorting map entries in a stream, how do you collect them so the order is kept?
Back: Collect into a **`LinkedHashMap`** (preserves insertion order). A `HashMap` throws the order away.

```java
.collect(Collectors.toMap(k, v, (a, b) -> a, LinkedHashMap::new))
```
Tags: java streams map gotcha
<!--ID: 1782128730032-->
END

START
Coding Questions
Why filter before `sorted()` in a stream pipeline?
Back: `sorted()` is a **stateful, blocking** step — it buffers the whole stream at `O(n log n)`. Filtering first means sorting fewer elements.
Tags: java streams sorted performance
<!--ID: 1782128730034-->
END
