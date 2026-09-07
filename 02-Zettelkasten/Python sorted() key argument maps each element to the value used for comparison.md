---
created: 2026-06-03
aliases: [sorted key, key argument, sort by key, key lambda]
tags:
  - python/core
---

By default `sorted()` compares elements directly — fine for numbers and strings, useless the moment your elements are tuples, dicts, or objects. The `key` argument fixes this.

`key` takes a <mark style="background: #FFF3A3A6;">function applied to every element before comparison</mark>. Python calls it once per element, then sorts by the returned values — but the *original* elements are what ends up in the result.

```python
words = ["banana", "kiwi", "apple"]
sorted(words, key=len)        # ['kiwi', 'apple', 'banana']
#                   ^ sort by len(word), but keep the words themselves
```

### Why a lambda

`len` is a named function you can pass by name. When the mapping has no built-in name — "the second element", "the count field" — you write it inline with <mark style="background: #BBFABBA6;">lambda</mark>, an anonymous one-expression function.

```python
pairs = [("a", 3), ("b", 1), ("c", 2)]
sorted(pairs, key=lambda x: x[1])   # [('b', 1), ('c', 2), ('a', 3)]
#                       ^ each tuple x → its count x[1]
```

`lambda x: x[1]` reads as "given an element `x`, the thing to sort by is `x[1]`". Python feeds each tuple in as `x` and sorts by the number it returns.

### Sorting by count, descending

This is the exact move for "top-K by frequency": count items, then sort the `(item, count)` pairs by count, highest first.

```python
sorted(counts.items(), key=lambda x: x[1], reverse=True)
#      ^ dict → (key, value) pairs   ^ sort by value   ^ biggest first
```

<mark style="background: #ABF7F7A6;">`key` and `reverse` combine freely</mark> — `key` picks *what* to compare, `reverse` picks the *direction*.

### Multi-level sort with a tuple key

Return a tuple to sort by several fields at once. Python compares tuples element by element — first field, then ties broken by the second.

```python
people = [("Ann", 30), ("Bob", 25), ("Ann", 25)]
sorted(people, key=lambda p: (p[0], p[1]))
# [('Ann', 25), ('Ann', 30), ('Bob', 25)]
#  sort by name, then by age within the same name
```

To mix directions — name ascending but age descending — negate the numeric field: `key=lambda p: (p[0], -p[1])`.

### Sorting objects

The same idea works for class instances — point `key` at the attribute.

```python
sorted(users, key=lambda u: u.age)
```

<mark style="background: #ADCCFFA6;">For repeated sorts on the same field</mark>, `operator.itemgetter(1)` and `operator.attrgetter("age")` are faster, C-level replacements for these lambdas.

---

### Read more

- [[Python sorted() returns a new sorted list while list.sort() mutates in place]]
- [[Comparator defines interchangeable orderings external to a class]]
- [[Python MOC]]
