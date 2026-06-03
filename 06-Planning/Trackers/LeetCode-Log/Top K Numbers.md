---
difficulty: Easy
status: Not started
topic: [Top K Elements, Arrays, Heap]
tags: [top-k-elements, array, heap, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an unsorted array of integers, return the K largest numbers from it. The result does not need to be sorted — just the top K values. Duplicates count separately, so if multiple copies of a value qualify, include them all.

### Constraints
- 1 <= K <= nums.length
- Array may contain negative numbers and duplicates

### Examples
```
[3, 1, 5, 12, 2, 11], K=3  →  [5, 12, 11]
[5, 12, 11, -1, 12],  K=3  →  [12, 11, 12]
```

### Next solve approach
1. Brute Force first — sort descending, slice first K elements, O(n log n)
2. Optimized (Top K Elements) — maintain a min-heap of size K; push each element and pop the smallest when size exceeds K, O(n log K)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static List<Integer> findKLargestNumbers(int[] nums, int k) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        System.out.println(findKLargestNumbers(new int[]{3, 1, 5, 12, 2, 11}, 3)); // expected: [5, 12, 11]
        System.out.println(findKLargestNumbers(new int[]{5, 12, 11, -1, 12}, 3));  // expected: [12, 11, 12]
    }
}
```

### Python

```python
def find_k_largest_numbers(nums: list[int], k: int) -> list[int]:
    # TODO: implement
    pass


print(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))  # expected: [5, 12, 11]
print(find_k_largest_numbers([5, 12, 11, -1, 12], 3))   # expected: [12, 11, 12]
```
