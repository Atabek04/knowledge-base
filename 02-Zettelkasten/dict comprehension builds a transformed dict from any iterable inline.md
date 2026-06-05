---
created: 2026-06-04
aliases: [dict comprehension, transform dict, map dict values]
tags:
  - python/core
---

Transforming a dict the manual way means an empty dict plus a loop of assignments. A **dict comprehension** does it in one expression — same idea as a [[List comprehension is Python's inline filter-map equivalent to Stream API|list comprehension]], but with <mark style="background: #FFF3A3A6;">a `key: value` pair before the `for` and curly braces around it</mark>.

```python
prices = {"apple": 100, "bread": 40}

# Transform values
{name: p * 2 for name, p in prices.items()}
# {'apple': 200, 'bread': 80}

# Filter entries
{name: p for name, p in prices.items() if p > 50}
# {'apple': 100}

# Invert key ↔ value
{p: name for name, p in prices.items()}
# {100: 'apple', 40: 'bread'}
```

The source is usually [[dict keys values and items return live views not lists|items()]] consumed with [[Python for loop unpacks tuples into multiple loop variables|tuple unpacking]] — but *any* iterable works:

```python
{word: len(word) for word in ["apple", "bee"]}
# {'apple': 5, 'bee': 3}
```

For a Java developer: this is `stream().collect(Collectors.toMap(keyFn, valueFn))` — without the ceremony.

---

### It builds a new dict

A comprehension <mark style="background: #BBFABBA6;">never mutates the source — it returns a fresh dict</mark>, same as `sorted()` vs `list.sort()`. To "modify" a dict functionally, rebind: `prices = {k: v * 2 for k, v in prices.items()}`.

<mark style="background: #FF5582A6;">Duplicate keys silently overwrite</mark> — in the inversion example, two names with the same price keep only the last one.

---

### Read more

- [[List comprehension is Python's inline filter-map equivalent to Stream API]]
- [[dict keys values and items return live views not lists]]
- [[Python for loop unpacks tuples into multiple loop variables]]
- [[Python MOC]]
