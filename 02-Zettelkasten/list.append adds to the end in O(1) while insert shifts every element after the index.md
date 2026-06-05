---
created: 2026-06-04
aliases: [list append, list insert, append vs insert]
tags:
  - python/core
---

A Python list grows two ways: `append(x)` puts the element <mark style="background: #FFF3A3A6;">at the end — no index needed</mark>, `insert(i, x)` places it at position `i` and <mark style="background: #FFF3A3A6;">shifts everything after it one slot right</mark>.

```python
nums = [1, 2, 3]
nums.append(4)      # [1, 2, 3, 4]      — end, O(1) amortized
nums.insert(0, 0)   # [0, 1, 2, 3, 4]   — front, O(n): all 4 elements shifted
```

Appending without an index is not a Python quirk — every language's dynamic array works this way:

```java
list.add(42);        // Java — append to end
list.add(0, 42);     // Java — insert at index
```
```cpp
v.push_back(42);            // C++ — append to end
v.insert(v.begin(), 42);    // C++ — insert at front
```

The end is where a dynamic array has spare capacity, so end-insertion is the cheap default everywhere.

---

### The insert(0) trap

`insert(0, x)` inside a loop is <mark style="background: #FF5582A6;">O(n) per call → O(n²) total</mark> — each insert re-shifts the entire list. Classic case: building a list right-to-left.

```python
# O(n²) — every insert shifts everything
for i in range(len(nums) - 2, -1, -1):
    right.insert(0, right[0] * nums[i + 1])

# O(n) — append, then index from the back instead
# or append and reverse once at the end
```

Fixes: `append` + index arithmetic from the back, `append` + one final `.reverse()`, or `collections.deque` whose `appendleft` is O(1).

---

### Other mutators worth knowing

- `nums.pop()` — remove + return **last** element, O(1); `pop(0)` is O(n), same shift problem
- `nums.extend(other)` — append all elements of another iterable (`+=` does the same)
- `nums.remove(x)` — delete first occurrence *by value*, O(n)

---

### Read more

- [[Python sorted() returns a new sorted list while list.sort() mutates in place]]
- [[A list holds all values in RAM even when you only process one at a time]]
- [[Python MOC]]
