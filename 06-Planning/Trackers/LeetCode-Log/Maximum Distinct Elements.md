---
difficulty: Medium
status: Not started
topic: [Top K Elements, Arrays, Heap]
tags: [top-k-elements, array, heap, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an array of numbers and an integer K, remove exactly K elements from the array to maximize the count of distinct values remaining. You should preferentially remove duplicates (extra copies of repeated numbers) to make as many numbers distinct as possible.

### Constraints
- 1 <= K <= nums.length
- Array may contain many duplicates
- After removing K elements, count how many distinct values are left

### Examples
```
[7, 3, 5, 8, 5, 3, 3], K=2  →  3   (remove two 3s → [7, 3, 5, 8] or [7, 5, 8, 3]; 3 distinct)
[3, 5, 12, 11, 12],     K=3  →  2   (remove one 12 to make all distinct, then remove 2 more → 2 distinct left)
[1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], K=2  →  3   (remove one 4; 3 distinct remain)
```

### Next solve approach
1. Brute Force first — try all combinations of K removals, count distinct each time, O(n choose K)
2. Optimized (Top K Elements) — count frequencies; use duplicates first to make numbers distinct; if K budget remains, remove full distinct numbers; O(n log n)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int findMaximumDistinctElements(int[] nums, int k) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findMaximumDistinctElements(new int[]{7, 3, 5, 8, 5, 3, 3}, 2));               // expected: 3
        System.out.println(findMaximumDistinctElements(new int[]{3, 5, 12, 11, 12}, 3));                  // expected: 2
        System.out.println(findMaximumDistinctElements(new int[]{1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5}, 2));  // expected: 3
    }
}
```

### Python

```python
def find_maximum_distinct_elements(nums: list[int], k: int) -> int:
    # TODO: implement
    pass


print(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2))               # expected: 3
print(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3))                  # expected: 2
print(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2))  # expected: 3
```
