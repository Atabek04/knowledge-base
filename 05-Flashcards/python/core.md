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
<!--ID: 1782128730441-->
END

START
Coding Questions
How does `list.sort()` differ from `sorted()` in what it changes and returns?
Back:
- `list.sort()` — **mutates the list in place**, returns `None`
- `sorted()` — leaves the original alone, returns a new list

So `x = nums.sort()` sets `x` to `None`.
Tags: python sorted
<!--ID: 1782128730443-->
END

START
Coding Questions
What does the `key` argument of `sorted()` do?
Back: A function applied to **every element before comparison** — Python sorts by the returned values but keeps the original elements in the result.

```python
sorted(words, key=len)   # sort by length, keep the words
```
Tags: python sorted key
<!--ID: 1782128730446-->
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
<!--ID: 1782128730448-->
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
<!--ID: 1782128730450-->
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
<!--ID: 1782128730452-->
END

START
Coding Questions
What is the position order of the three parts in a list comprehension?
Back: `[expression for item in iterable if condition]`
- **expression** (map) first
- **for** loop in the middle
- **if** filter last (optional)
Tags: python comprehension
<!--ID: 1782128730454-->
END

START
Coding Questions
What does `for k, v in pairs:` actually do — is the two-variable form special loop syntax?
Back: No — it's ordinary **tuple unpacking** applied once per element.

Each element is a tuple; `k, v = element` runs on every iteration. Same mechanic as `x, y = (1, "a")`.
Tags: python forloop unpacking
<!--ID: 1782128730456-->
END

START
Coding Questions
In a for loop unpacking tuples, what happens when an element has more values than loop variables?
Back: `ValueError: too many values to unpack` — unpacking is **strict** about count.

Relax it with a catch-all: `for first, *rest in rows:`
Tags: python forloop unpacking
<!--ID: 1782128730458-->
END

START
Coding Questions
What does `enumerate(iterable)` yield on each iteration?
Back: An **(index, value) tuple** — `enumerate` pairs each item with its running index, so you never maintain a manual counter.

```python
for i, char in enumerate("abc"):   # 0 a → 1 b → 2 c
```
Tags: python enumerate
<!--ID: 1782128730460-->
END

START
Coding Questions
How do you make `enumerate` count from 1 instead of 0 (e.g. line numbers)?
Back: Pass the `start` argument:

```python
for line_no, line in enumerate(lines, start=1):
```
Tags: python enumerate
<!--ID: 1782128730462-->
END

START
Coding Questions
Does `enumerate` build a list of pairs up front?
Back: No — it returns a **lazy iterator** that computes each `(index, value)` pair on demand, like `range`.

Wrap in `list()` only if you need all pairs at once.
Tags: python enumerate
<!--ID: 1782128730465-->
END

START
Coding Questions
What is `collections.Counter`, and why does `counter[x] += 1` never need a guard?
Back: A **dict subclass purpose-built for counting** — a missing key reads as `0` instead of raising `KeyError`, so incrementing starts from nothing.

```python
counts = Counter("aab")   # Counter({'a': 2, 'b': 1})
counts["z"] += 1          # works, no setup
```
Tags: python counter collections
<!--ID: 1782128730467-->
END

START
Coding Questions
What does `len(counter)` count — total occurrences or something else?
Back: **Distinct keys**, not total occurrences — `Counter("aab")` has `len` 2.

This is exactly what a sliding window checks to know how many distinct characters it holds.
Tags: python counter collections
<!--ID: 1782128730469-->
END

START
Coding Questions
In a Counter, you decrement a key's count to 0. Does `len()` stop counting it?
Back: No — **a zero count does NOT remove the key**; `len()` still includes it.

You must remove it manually:
```python
if window[ch] == 0:
    window.pop(ch)
```
Tags: python counter collections
<!--ID: 1782128730473-->
END

START
Coding Questions
What does `counter.most_common(n)` return?
Back: The top-n **(item, count) tuples**, sorted by count descending.

```python
Counter("aab").most_common(1)   # [('a', 2)]
```
Tags: python counter collections
<!--ID: 1782128730475-->
END

START
Coding Questions
What does `collections.defaultdict` do when you access a missing key?
Back: Calls the **factory** you gave it, **inserts** the result under that key, and returns it — no `KeyError`, no guard code.

```python
groups = defaultdict(list)
groups["a"].append("apple")   # [] created on the fly
```
Tags: python defaultdict collections
<!--ID: 1782128730477-->
END

START
Coding Questions
What do you pass to `defaultdict()` — a default value or something else?
Back: A **zero-arg callable** (the factory itself), not a value:
- `defaultdict(int)` → missing key starts at `0`
- `defaultdict(list)` → starts as `[]`
- `defaultdict(lambda: "N/A")` → custom default
Tags: python defaultdict collections
<!--ID: 1782128730480-->
END

START
Coding Questions
Gotcha: what side effect does merely *reading* a missing key from a defaultdict have?
Back: It **inserts the default** — even `if d[key]:` silently grows the dict.

Use `key in d` for pure membership checks.
Tags: python defaultdict collections
<!--ID: 1782128730481-->
END

START
Coding Questions
Counter vs defaultdict(int): how does each handle *reading* a missing key?
Back:
- **Counter** — returns `0` **without inserting** the key
- **defaultdict** — calls the factory **and inserts** the key

Both live in `collections`; for pure counting prefer Counter.
Tags: python counter defaultdict collections
<!--ID: 1782128730483-->
END

START
Coding Questions
`d["z"]` vs `d.get("z")` on a missing key — what does each do?
Back:
- `d["z"]` — raises **KeyError** (loud failure)
- `d.get("z")` — returns **None**
- `d.get("z", 0)` — returns **your default**

(Opposite of Java, where `map.get()` returns null silently.)
Tags: python dict
<!--ID: 1782128730486-->
END

START
Coding Questions
When should you prefer `d[key]` over `d.get(key, default)`?
Back: When the key **must exist** — a missing key is a bug, and the immediate `KeyError` points straight at it.

`get` there hides the bug: you read `None` and crash later with a worse message.
Tags: python dict
<!--ID: 1782128730488-->
END

START
Coding Questions
What does `dict.pop(key)` do that `del d[key]` doesn't?
Back: **Returns the removed value** — pop is read-and-delete in one call.

Both raise `KeyError` on a missing key (unless pop gets a default).
Tags: python dict pop
<!--ID: 1782128730490-->
END

START
Coding Questions
What's the one-liner idiom to "remove a dict key if present, no error if absent"?
Back:
```python
d.pop(key, None)
```
The second argument replaces the `KeyError` with a fallback — no `if key in d:` guard needed.
Tags: python dict pop
<!--ID: 1782128730492-->
END

START
Coding Questions
What type of object do `d.keys()`, `d.values()`, `d.items()` return?
Back: **Live view objects** (`dict_keys`, `dict_values`, `dict_items`) — windows into the dict that **reflect later changes**, not list copies.

```python
view = d.items()
d["c"] = 3
view   # already contains ('c', 3)
```
Tags: python dict views
<!--ID: 1782128730494-->
END

START
Coding Questions
What is each element yielded by `d.items()`, and what's the idiomatic way to consume it?
Back: A **(key, value) tuple** — consumed with tuple unpacking:

```python
for key, value in d.items():
```
(Looping the dict directly gives keys only.)
Tags: python dict views
<!--ID: 1782128730496-->
END

START
Coding Questions
You need to remove entries from a dict while looping over its keys. How do you avoid `RuntimeError: dictionary changed size during iteration`?
Back: Iterate a **snapshot**, not the live view:

```python
for key in list(d.keys()):
    if d[key] == 0:
        d.pop(key)
```
`list()` detaches a real list from the view.
Tags: python dict views
<!--ID: 1782128730498-->
END

START
Coding Questions
What is the single difference between a `list` and a `tuple`?
Back: A tuple is **immutable** — after creation: no item assignment, no append, no removal.

Everything else (indexing, slicing, iteration) works the same.
Tags: python tuple
<!--ID: 1782128730500-->
END

START
Coding Questions
Why can a tuple be a dict key while a list cannot?
Back: Dict keys must be **hashable** — the hash must stay constant.

- tuple: **immutable → hash never changes → hashable**
- list: mutation would change the hash → `TypeError: unhashable type`
Tags: python tuple dict
<!--ID: 1782128730502-->
END

START
Coding Questions
How do you convert a tuple to a list and back?
Back: Each constructor accepts the other:
- `list((1, 2))` → `[1, 2]` — mutable copy
- `tuple([1, 2])` → `(1, 2)` — frozen, hashable
Tags: python tuple
<!--ID: 1782128730505-->
END

START
Coding Questions
Write a dict comprehension that doubles every value of `prices`.
Back:
```python
{name: p * 2 for name, p in prices.items()}
```
`key: value` pair before the `for`, curly braces around it.
Tags: python dict comprehension
<!--ID: 1782128730507-->
END

START
Coding Questions
Does a dict comprehension modify the source dict?
Back: No — it always builds a **new dict** (like `sorted()` vs `list.sort()`).

To "transform in place", rebind: `prices = {k: v*2 for k, v in prices.items()}`
Tags: python dict comprehension
<!--ID: 1782128730509-->
END

START
Coding Questions
In a dict comprehension that inverts `{name: price}` to `{price: name}`, what happens when two names share a price?
Back: **Duplicate keys silently overwrite** — only the *last* one survives. No error, no warning.
Tags: python dict comprehension
<!--ID: 1782128730511-->
END

START
Coding Questions
`list.append(x)` vs `list.insert(i, x)` — what does each cost and why?
Back:
- `append(x)` — adds to the **end**, **O(1)** amortized (spare capacity lives there)
- `insert(i, x)` — places at index `i`, **O(n)**: shifts every element after `i` one slot right
Tags: python list
<!--ID: 1782128730513-->
END

START
Coding Questions
Why is `list.insert(0, x)` inside a loop a performance trap, and what are the fixes?
Back: Each call shifts the **entire list** → O(n) per insert → **O(n²) total**.

Fixes:
- `append` + index from the back
- `append` + one final `.reverse()`
- `collections.deque` — `appendleft` is O(1)
Tags: python list performance
<!--ID: 1782128730515-->
END

START
Coding Questions
In Java and C++, how do you append to a dynamic array without an index (like Python's `append`)?
Back:
- Java: `list.add(42)` — index-free append; `list.add(0, 42)` for insert
- C++: `v.push_back(42)`; `v.insert(v.begin(), 42)` for front

End-insertion is the cheap, index-free default in **every** language — not a Python quirk.
Tags: python list java cpp
<!--ID: 1782128730517-->
END

START
Coding Questions
`list.pop()` vs `list.pop(0)` — what's the cost difference?
Back:
- `pop()` — removes + returns the **last** element, **O(1)**
- `pop(0)` — removes the **first**, **O(n)** — shifts everything left

Same shift problem as `insert(0, x)`.
Tags: python list
<!--ID: 1782128730519-->
END

START
Coding Questions
What do the 1-, 2-, and 3-argument forms of `range()` mean?
Back:
- `range(stop)` — from 0 up to stop
- `range(start, stop)`
- `range(start, stop, step)`

`stop` is **always exclusive** — the sequence ends one step before it.
Tags: python range
<!--ID: 1782128730521-->
END

START
Coding Questions
Write the `range()` call that visits every index of `nums` from last down to 0.
Back:
```python
range(len(nums) - 1, -1, -1)
```
- start = last index
- stop = `-1`, exclusive → 0 included
- step = `-1`, walk backward
Tags: python range
<!--ID: 1782128730523-->
END

START
Coding Questions
What does `range(0, 5, -1)` produce — error or something else?
Back: **Silently empty** — with a negative step, start must be *greater* than stop. No error raised.

(Only `step=0` raises `ValueError`.)
Tags: python range
<!--ID: 1782128730526-->
END

START
Coding Questions
Why does Python make `range`'s stop exclusive instead of inclusive?
Back: So `range(len(nums))` yields **exactly the valid indexes** — length and stop are the same number, no off-by-one adjustment.

Same convention as slicing: `nums[0:3]` is 3 elements.
Tags: python range
<!--ID: 1782128730528-->
END

START
Coding Questions
You're looping a list backward. When do you use `reversed(nums)` and when `range(len(nums)-1, -1, -1)`?
Back:
- **Values only** → `reversed(nums)` — no index math, no off-by-ones
- **Index needed** (write to `arr[i]`, compare `nums[i]` with `nums[i+1]`) → `range` with negative step
Tags: python reversed range
<!--ID: 1782128730530-->
END

START
Coding Questions
Compare the three ways to "reverse" a list: `reversed(nums)`, `nums[::-1]`, `nums.reverse()`.
Back:
- `reversed(nums)` — **lazy iterator**, no copy, original untouched
- `nums[::-1]` — **new reversed list**, full copy
- `nums.reverse()` — reverses **in place**, returns `None`
Tags: python reversed list
<!--ID: 1782128730532-->
END
