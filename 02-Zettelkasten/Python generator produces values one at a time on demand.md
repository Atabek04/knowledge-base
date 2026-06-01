---
created: 2026-06-01
aliases: [generator, python generator]
tags:
  - python/core
---

A **generator** is named after what it does: it *generates* values — one at a time, on demand, instead of producing all of them upfront.

---

### The problem: RAM explosion

```python
def count_up_list(n):
    result = []
    for i in range(n):
        result.append(i)
    return result  # all n integers sitting in RAM at once

for num in count_up_list(1_000_000_000):
    print(num)
```

Python allocates ~36 GB RAM before printing a single number.

**Why so much?** 

- Because every Python value is a [[Python has no primitives because every value is a heap-allocated object|heap object]] 
	- `42` isn't 4 bytes like in Java, it's ~28 bytes on the heap.
- A list stores 8-byte pointers to those objects
	- 1B pointers (8 GB) + 1B integer objects (~28 GB) = ~36 GB, all created upfront.

You only use one number at a time — the other 999,999,999 [[A list holds all values in RAM even when you only process one at a time|sit idle]].

---

### The fix: generate on demand

```python
def count_up_gen(n):
    for i in range(n):
        yield i

for num in count_up_gen(1_000_000_000):
    print(num)
```

Calling `count_up_gen(n)` runs **no code** — it immediately returns a **generator object**.
The function body is frozen, waiting.

Memory used: constant, regardless of how many values.

---

### How the generator object works

The `for` loop drives it by calling `next()` on each iteration:

```python
gen = count_up_gen(3)

next(gen)   # runs until first yield → returns 0, freezes
next(gen)   # resumes → returns 1, freezes
next(gen)   # resumes → returns 2, freezes
next(gen)   # nothing left → raises StopIteration → loop stops
```

Each yielded value is just an `int`. The generator object is the wrapper that makes repeated extraction possible.

The object stores only two things: local variables + current position (which `yield` it's paused at). No list, no pre-allocated memory.

It also implements the [[Python for loop works with any iterable not just lists|iterator protocol]]:

```python
gen.__next__()   # same as next(gen)
gen.__iter__()   # returns itself — so it works in for loops directly
gen.close()      # force-stop the generator
```

---

### Why RAM releases immediately

CPython uses [[CPython manages memory through reference counting with immediate deallocation|reference counting]] — each object is freed the moment nothing points to it.

With a list, all 1B objects stay alive (list holds a reference to each). Nothing freed until the list is deleted.

With a generator, after each `print(num)`, `num` rebinds to the next value → old integer's refcount drops to 0 → freed immediately. Only one object alive at a time.

---

### When NOT to use a generator

Generators trade flexibility for memory. Use a list when you need:

| Need | List | Generator |
|------|------|-----------|
| Random access `nums[500]` | ✓ | ✗ forward-only |
| `len(nums)` | ✓ | ✗ unknown until exhausted |
| Iterate **twice** | ✓ | ✗ exhausted after first pass |
| Sort / reverse | ✓ | ✗ needs all values first |

<mark style="background: #FFF3A3A6;">**Rule:** generator when reading once, top to bottom, on large data. List when you need flexibility or data is small.</mark>

---

### What "yielding" means

> **Yielding**
> - General English: *to yield* = to produce or hand something over ("the field yields crops")
> - Programming: a function *yields* one value to its caller, then **pauses** — frozen in place until the next value is requested
> - SSE: each `yield` hands one chunk to the HTTP layer → that chunk is immediately flushed to the client
>
> **Flushing** (in the networking context)
> - General English: *to flush* = push something out completely ("flush the pipe")
> - Networking: empty the output buffer and transmit now — don't wait for more data to accumulate
> - SSE: after each `yield`, the server flushes → chunk travels to the client immediately
>
> **The cycle:** yield one chunk → flush to client → pause → resume → yield next → flush → …

---

### Read more

- [[A generator object is a suspended stack frame that resumes at yield]]
- [[A list holds all values in RAM even when you only process one at a time]]
- [[Python range computes values on demand without storing them]]
- [[yield in Python is one keyword with three different jobs]]
- [[Python for loop works with any iterable not just lists]]
- [[Python has no primitives because every value is a heap-allocated object]]
- [[CPython manages memory through reference counting with immediate deallocation]]
- [[SSE keeps HTTP response body open to push text chunks continuously|yielding chunks in SSE]]
- [[Python MOC]]
