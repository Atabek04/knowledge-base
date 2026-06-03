---
created: 2026-06-03
aliases: [Stream.sorted, sort a stream, sort map by value, sort list stream]
tags:
  - java
  - streams
---

`Stream.sorted()` is the Stream API's sort step — the Java equivalent of Python's `sorted()`. It is an <mark style="background: #FFF3A3A6;">intermediate operation</mark>: it returns a new sorted stream and never mutates the source collection, just like `sorted()` leaves its input untouched.

It comes in two forms.

### Natural ordering — sorted()

With no argument, it sorts by the element's [[Comparable defines a type's natural ordering through compareTo()|natural ordering]]. The elements **must** implement `Comparable`, or you get a `ClassCastException` at runtime.

```java
List<Integer> sorted = nums.stream()
        .sorted()           // ascending, uses Integer.compareTo
        .toList();
```

### Custom ordering — sorted(Comparator)

Pass a [[Comparator defines interchangeable orderings external to a class|Comparator]] to sort any way you like — this is the everyday form.

```java
people.stream()
      .sorted(Comparator.comparingInt(Person::getAge).reversed())  // oldest first
      .toList();
```

### Sorting a List of objects

`List.sort(comparator)` sorts in place; the stream form gives you a sorted *copy* you can keep transforming in the pipeline.

```java
// in place — mutates the list
people.sort(Comparator.comparing(Person::getName));

// in a pipeline — original untouched
List<String> names = people.stream()
        .sorted(Comparator.comparing(Person::getName))
        .map(Person::getName)
        .toList();
```

### Sorting a Map

A `Map` has no order to sort directly — you <mark style="background: #BBFABBA6;">stream its `entrySet()`</mark>, sort the entries, then collect. `Map.Entry` provides ready-made comparators:

```java
// top entries by value, descending — the "top-K by frequency" move
counts.entrySet().stream()
      .sorted(Map.Entry.<String, Integer>comparingByValue(Comparator.reverseOrder()))
      .limit(k)
      .map(Map.Entry::getKey)
      .toList();
```

- `Map.Entry.comparingByValue()` — sort by the value.
- `Map.Entry.comparingByKey()` — sort by the key.

<mark style="background: #FF5582A6;">A plain `HashMap` cannot stay sorted.</mark> To *keep* the order after sorting, collect into a `LinkedHashMap` (insertion order preserved) — collecting into a `HashMap` throws the order away again.

```java
Map<String, Integer> ordered = counts.entrySet().stream()
        .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
        .collect(Collectors.toMap(
                Map.Entry::getKey, Map.Entry::getValue,
                (a, b) -> a, LinkedHashMap::new));   
                // merge fn + ordered map
```

### Cost

<mark style="background: #ABF7F7A6;">`sorted()` is a stateful, blocking step</mark> — it must buffer the entire stream before emitting anything, at `O(n log n)`. Filter before you sort so you sort fewer elements.

---

### Read more

- [[Comparator defines interchangeable orderings external to a class]]
- [[Comparable defines a type's natural ordering through compareTo()]]
- [[Python sorted() returns a new sorted list while list.sort() mutates in place]]
- [[List comprehension is Python's inline filter-map equivalent to Stream API]]
- [[Java MOC]]
