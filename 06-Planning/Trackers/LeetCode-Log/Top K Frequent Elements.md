---
difficulty: Medium
status: Cheated
topic:
  - Arrays & Hashing
  - Top K Elements
tags:
  - array
  - hash-table
  - divide-and-conquer
  - bucket-sort
  - counting
  - quickselect
  - sorting
  - heap
  - neetcode-150
  - top-k-elements
  - grokking-patterns
solved: 0
last_solved: 2026-06-03
link: https://leetcode.com/problems/top-k-frequent-elements/
---

### Problem
Given an integer array and an integer k, return the k most frequently occurring elements in any order. The answer is guaranteed to be unique, and k is always valid (between 1 and the number of distinct elements). The follow-up asks for better than O(n log n) time.

### Constraints
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

### Examples
```
nums = [1,1,1,2,2,3], k = 2  →  [1,2]
nums = [1], k = 1             →  [1]
```

### Next solve approach
1. Brute Force first — count frequencies with a map, sort by count descending, take first k, O(n log n)
2. Optimized — bucket sort by frequency (index = count, max index = n), scan buckets from high to low, O(n)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int[] topKFrequent(int[] nums, int k) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(java.util.Arrays.toString(s.topKFrequent(new int[]{1, 1, 1, 2, 2, 3}, 2))); // expected: [1, 2]
        System.out.println(java.util.Arrays.toString(s.topKFrequent(new int[]{1}, 1)));                  // expected: [1]
    }
}
```

### Python

```python
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    # TODO: implement
    pass


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # expected: [1, 2]
print(top_k_frequent([1], 1))                   # expected: [1]
```
