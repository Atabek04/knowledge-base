---
difficulty: Hard
status: Not started
topic: [Miscellaneous, Heap, Binary Search]
tags: [miscellaneous, heap, binary-search, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an unsorted array of numbers, find the Kth smallest number in sorted order. Duplicates count as separate elements — if the same value appears twice, it can occupy two different positions in the sorted ranking. Return the value at position K when the array is sorted ascending.

### Constraints
- 1 <= K <= nums.length
- Array may contain negative numbers and duplicates
- Input fits in memory

### Examples
```
[1, 5, 12, 2, 11, 5], K=3  →  5    (sorted: [1, 2, 5, 5, 11, 12]; 3rd is 5)
[1, 5, 12, 2, 11, 5], K=4  →  5    (sorted: [1, 2, 5, 5, 11, 12]; 4th is 5)
[5, 12, 11, -1, 12],  K=3  →  11   (sorted: [-1, 5, 11, 12, 12]; 3rd is 11)
```

### Next solve approach
1. Brute Force first — sort the array, return element at index K-1, O(n log n)
2. Optimized (Heap) — maintain a max-heap of size K; after processing all elements the root is the Kth smallest, O(n log k)

---

### Java

```java
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
