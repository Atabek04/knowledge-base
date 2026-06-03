---
difficulty: Easy
status: Cheated
topic: [Sliding Window, Arrays]
tags: [sliding-window, array, grokking-patterns]
solved: 0
last_solved: 2026-06-01
link: ""
---

### Problem
Given an array of positive integers and a positive integer k, find the maximum sum among all contiguous subarrays of exactly size k. Slide a window of length k across the array and return the highest sum you find.

### Constraints
- 1 <= k <= arr.length
- Array contains positive integers
- Input fits in memory

### Examples
```
[2, 1, 5, 1, 3, 2], k=3  →  9   (subarray [5, 1, 3])
[2, 3, 4, 1, 5],    k=2  →  7   (subarray [3, 4])
```

### Next solve approach
1. Brute Force first — nested loop over every window of size k, O(n*k)
2. Optimized (Sliding Window) — maintain a running sum, subtract the element leaving the window and add the new one, O(n)

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int findMaxSumSubArray(int k, int[] arr) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findMaxSumSubArray(3, new int[]{2, 1, 5, 1, 3, 2})); // expected: 9
        System.out.println(findMaxSumSubArray(2, new int[]{2, 3, 4, 1, 5}));    // expected: 7
    }
}
```

### Python

```python
def find_max_sum_sub_array(k: int, arr: list[int]) -> int:
    # TODO: implement
    pass


print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2]))  # expected: 9
print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5]))      # expected: 7
```
