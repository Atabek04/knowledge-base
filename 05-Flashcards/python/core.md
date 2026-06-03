TARGET DECK: Tech-KB::Python::Core
Tags: python core
**Related:** [[Python MOC]]

---

START
Coding Questions
In Python, what does `sorted(iterable)` return, and what happens to the original?
Back:
- Returns a **new sorted list**
- The original iterable is **left unchanged**

Works on any iterable (tuple, set, dict keys, generator) and always hands back a `list`.
Tags: python sorted
END

START
Coding Questions
How does `list.sort()` differ from `sorted()` in what it changes and returns?
Back:
- `list.sort()` — **mutates the list in place**, returns `None`
- `sorted()` — leaves the original alone, returns a new list

So `x = nums.sort()` sets `x` to `None`.
Tags: python sorted
END

START
Coding Questions
What does the `key` argument of `sorted()` do?
Back: A function applied to **every element before comparison** — Python sorts by the returned values but keeps the original elements in the result.

```python
sorted(words, key=len)   # sort by length, keep the words
```
Tags: python sorted key
END

START
Coding Questions
Write a `sorted()` call that sorts `(item, count)` pairs by count, highest first.
Back:
```python
sorted(pairs, key=lambda x: x[1], reverse=True)
```
- `key=lambda x: x[1]` → sort by the count
- `reverse=True` → descending
Tags: python sorted key lambda
END

START
Coding Questions
With `sorted()`, how do you sort by two fields at once (e.g. name, then age)?
Back: Return a **tuple** from `key` — Python compares tuples element by element.

```python
sorted(people, key=lambda p: (p[0], p[1]))
```
Mix directions by negating a numeric field: `(p[0], -p[1])`.
Tags: python sorted key tuple
END

START
Coding Questions
A list comprehension is shorthand for what plain construct?
Back: A **`for` loop that builds a list**, rewritten as one expression.

```python
result = [item[0] for item in pairs]
# same as:
result = []
for item in pairs:
    result.append(item[0])
```
Tags: python comprehension
END

START
Coding Questions
What is the position order of the three parts in a list comprehension?
Back: `[expression for item in iterable if condition]`
- **expression** (map) first
- **for** loop in the middle
- **if** filter last (optional)
Tags: python comprehension
END
