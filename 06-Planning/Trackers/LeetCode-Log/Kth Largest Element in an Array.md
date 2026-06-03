---
difficulty: Medium
status: Not started
topic: [Heap / Priority Queue]
tags: [array, divide-and-conquer, quickselect, sorting, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/kth-largest-element-in-an-array/"
---

### Problem
Given an integer array and an integer k, find the kth largest element in the array. This is the kth largest in sorted order, not the kth distinct value. The challenge asks whether you can solve it without fully sorting the array.

### Constraints
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

### Examples
```
nums = [3,2,1,5,6,4], k = 2  →  5
nums = [3,2,3,1,2,4,5,5,6], k = 4  →  4
```

### Next solve approach
1. Brute Force first — sort descending, return element at index k-1
2. Optimized — maintain a min-heap of size k; heap top is the answer in O(n log k)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int findKthLargest(int[] nums, int k) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.findKthLargest(new int[]{3, 2, 1, 5, 6, 4}, 2)); // expected: 5
        System.out.println(sol.findKthLargest(new int[]{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4)); // expected: 4
    }
}
```

### Python

```python
from typing import List

def find_kth_largest(nums: List[int], k: int) -> int:
    # TODO: implement
    pass


print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))          # expected: 5
print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)) # expected: 4
```
