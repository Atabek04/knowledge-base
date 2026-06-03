---
difficulty: Hard
status: Not started
topic: [Sliding Window, Arrays]
tags: [sliding-window, array, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a binary array (containing only 0s and 1s) and an integer k, you may flip at most k zeros to ones. Find the length of the longest contiguous subarray that consists entirely of 1s after those flips.

### Constraints
- 0 <= k <= arr.length
- Array contains only 0s and 1s
- arr.length >= 1
- Input fits in memory

### Examples
```
[0,1,1,0,0,0,1,1,0,1,1], k=2  →  6   (flip index 5 and 8)
[0,1,0,0,1,1,0,1,1,0,0,1,1],  k=3  →  9   (flip index 6, 9, and 10)
```

### Next solve approach
1. Brute Force first — try every subarray, count zeros, keep maximum length where zeros <= k, O(n²)
2. Optimized (Sliding Window) — track zero count in window; when zeros > k, shrink left until valid again, O(n)

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int findLength(int[] arr, int k) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findLength(new int[]{0,1,1,0,0,0,1,1,0,1,1}, 2));      // expected: 6
        System.out.println(findLength(new int[]{0,1,0,0,1,1,0,1,1,0,0,1,1}, 3));  // expected: 9
    }
}
```

### Python

```python
def find_length(arr: list[int], k: int) -> int:
    # TODO: implement
    pass


print(find_length([0,1,1,0,0,0,1,1,0,1,1], 2))      # expected: 6
print(find_length([0,1,0,0,1,1,0,1,1,0,0,1,1], 3))  # expected: 9
```
