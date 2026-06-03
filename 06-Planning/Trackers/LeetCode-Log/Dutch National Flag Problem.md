---
difficulty: Medium
status: Not started
topic: [Two Pointers, Arrays]
tags: [two-pointers, array, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an array containing only 0s, 1s, and 2s, sort it in-place so all 0s come first, then all 1s, then all 2s. You cannot count the values and overwrite — treat them as opaque objects and sort by swapping only.

### Constraints
- Array contains only the values 0, 1, and 2
- Must sort in-place with O(1) extra space
- Cannot use counting sort (values must be treated as objects)
- 1 <= arr.length <= 3 * 10^4

### Examples
```
[1, 0, 2, 1, 0]       →  [0, 0, 1, 1, 2]
[2, 2, 0, 1, 2, 0]    →  [0, 0, 1, 2, 2, 2]
```

### Next solve approach
1. Brute Force first — use standard sort (Arrays.sort), O(n log n), violates spirit of the problem
2. Optimized (Two Pointers — Dutch National Flag) — three pointers: low, mid, high; single pass partitioning 0s to front and 2s to back, O(n)

---

### Java

```java
import java.util.Arrays;

public class Solution {

    // TODO: implement
    public static void sort(int[] arr) {
        // TODO
    }

    public static void main(String[] args) {
        int[] a1 = {1, 0, 2, 1, 0};
        sort(a1);
        System.out.println(Arrays.toString(a1));  // expected: [0, 0, 1, 1, 2]

        int[] a2 = {2, 2, 0, 1, 2, 0};
        sort(a2);
        System.out.println(Arrays.toString(a2));  // expected: [0, 0, 1, 2, 2, 2]
    }
}
```

### Python

```python
def sort(arr: list[int]) -> None:
    # TODO: implement
    pass


a1 = [1, 0, 2, 1, 0]
sort(a1)
print(a1)  # expected: [0, 0, 1, 1, 2]

a2 = [2, 2, 0, 1, 2, 0]
sort(a2)
print(a2)  # expected: [0, 0, 1, 2, 2, 2]
```
