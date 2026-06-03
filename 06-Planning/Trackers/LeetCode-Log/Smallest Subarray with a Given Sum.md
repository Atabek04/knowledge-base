---
difficulty: Easy
status: Solved
tags:
  - grokking-patterns
topic:
  - Sliding Window
  - Arrays
solved: 1
last_solved: 2026-06-02
link: https://leetcode.com/problems/minimum-size-subarray-sum
---

### Problem
Given an array of positive integers and a target sum S, find the length of the smallest contiguous subarray whose sum is greater than or equal to S. If no such subarray exists, return 0.

### Constraints
- 1 <= arr.length
- Array contains positive integers
- S > 0
- Return 0 if no valid subarray exists

### Examples
```
[2, 1, 5, 2, 3, 2], S=7  →  2   (subarray [5, 2])
[2, 1, 5, 2, 8],    S=7  →  1   (subarray [8])
[3, 4, 1, 1, 6],    S=8  →  3   (subarray [3, 4, 1] or [1, 1, 6])
```

### Next solve approach
1. Brute Force first — check every subarray, track minimum length with sum >= S, O(n²)
2. Optimized (Sliding Window) — expand right until sum >= S, then shrink left to find minimum length, O(n)

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int findMinSubArray(int S, int[] arr) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findMinSubArray(7, new int[]{2, 1, 5, 2, 3, 2})); // expected: 2
        System.out.println(findMinSubArray(7, new int[]{2, 1, 5, 2, 8}));    // expected: 1
        System.out.println(findMinSubArray(8, new int[]{3, 4, 1, 1, 6}));    // expected: 3
    }
}
```

### Python

```python
def find_min_sub_array(s: int, arr: list[int]) -> int:
    # TODO: implement
    pass


print(find_min_sub_array(7, [2, 1, 5, 2, 3, 2]))  # expected: 2
print(find_min_sub_array(7, [2, 1, 5, 2, 8]))      # expected: 1
print(find_min_sub_array(8, [3, 4, 1, 1, 6]))      # expected: 3
```
