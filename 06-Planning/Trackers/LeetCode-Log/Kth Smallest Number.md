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
Given an unsorted array of numbers, find the Kth smallest element in sorted order. The Kth smallest is not the Kth distinct value — duplicates count as separate positions in the ordering.

### Constraints
- 1 <= K <= nums.length
- Array may contain duplicates and negative numbers

### Examples
```
[1, 5, 12, 2, 11, 5], K=3  →  5    (sorted: [1,2,5,5,11,12]; 3rd is 5)
[1, 5, 12, 2, 11, 5], K=4  →  5    (4th is also 5)
[5, 12, 11, -1, 12],  K=3  →  11   (sorted: [-1,5,11,12,12]; 3rd is 11)
```

### Next solve approach
1. Brute Force first — sort array, return element at index K-1, O(n log n)
2. Optimized (Top K Elements) — maintain a max-heap of size K; any element smaller than heap top replaces it; root is the Kth smallest, O(n log K)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int findKthSmallestNumber(int[] nums, int k) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findKthSmallestNumber(new int[]{1, 5, 12, 2, 11, 5}, 3)); // expected: 5
        System.out.println(findKthSmallestNumber(new int[]{1, 5, 12, 2, 11, 5}, 4)); // expected: 5
        System.out.println(findKthSmallestNumber(new int[]{5, 12, 11, -1, 12}, 3));  // expected: 11
    }
}
```

### Python

```python
def find_kth_smallest_number(nums: list[int], k: int) -> int:
    # TODO: implement
    pass


print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3))  # expected: 5
print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4))  # expected: 5
print(find_kth_smallest_number([5, 12, 11, -1, 12], 3))   # expected: 11
```
