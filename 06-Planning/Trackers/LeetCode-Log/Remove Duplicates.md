---
difficulty: Easy
status: Not started
topic: [Two Pointers, Arrays]
tags: [two-pointers, array, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a sorted array, remove all duplicate elements in-place so that each value appears only once. Do not allocate any extra array. Return the length of the deduplicated prefix — the caller will read only that many elements from the front.

### Constraints
- Array is sorted in non-decreasing order
- Modification must be done in-place (O(1) extra space)
- 1 <= arr.length <= 10^5
- Values fit in int range

### Examples
```
[2, 3, 3, 3, 6, 9, 9]  →  4   (unique prefix: [2, 3, 6, 9])
[2, 2, 2, 11]           →  2   (unique prefix: [2, 11])
```

### Next solve approach
1. Brute Force first — use a Set to collect uniques, copy back, O(n) time but O(n) space
2. Optimized (Two Pointers) — slow pointer marks next write position, fast pointer scans ahead, O(n) time O(1) space

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int remove(int[] arr) {
        // TODO
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(remove(new int[]{2, 3, 3, 3, 6, 9, 9}));  // expected: 4
        System.out.println(remove(new int[]{2, 2, 2, 11}));           // expected: 2
    }
}
```

### Python

```python
def remove(arr: list[int]) -> int:
    # TODO: implement
    pass


print(remove([2, 3, 3, 3, 6, 9, 9]))  # expected: 4
print(remove([2, 2, 2, 11]))           # expected: 2
```
