---
difficulty: Medium
status: Cheated
topic:
  - Arrays & Hashing
tags:
  - union-find
  - array
  - hash-table
  - neetcode-150
solved: 0
last_solved: 2026-06-05
link: https://leetcode.com/problems/longest-consecutive-sequence/
---

### Problem
Given an unsorted array of integers, find the length of the longest sequence of consecutive integers (e.g. 1, 2, 3, 4). The algorithm must run in O(n) time, ruling out sorting. Duplicates in the input do not extend a sequence.

### Constraints
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

### Examples
```
nums = [100,4,200,1,3,2]      →  4    ([1,2,3,4])
nums = [0,3,7,2,5,8,4,6,0,1]  →  9    ([0..8])
nums = [1,0,1,2]               →  3    ([0,1,2])
```

### Next solve approach
1. Brute Force first — sort the array then scan for the longest run of consecutive values, O(n log n)
2. Optimized — put all numbers in a hash set; for each number that has no left neighbor (n-1 not in set), walk right counting the streak, O(n)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int longestConsecutive(int[] nums) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.longestConsecutive(new int[]{100, 4, 200, 1, 3, 2}));      // expected: 4
        System.out.println(s.longestConsecutive(new int[]{0, 3, 7, 2, 5, 8, 4, 6, 0, 1})); // expected: 9
        System.out.println(s.longestConsecutive(new int[]{1, 0, 1, 2}));                 // expected: 3
    }
}
```

### Python

```python
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    # TODO: implement
    pass


print(longest_consecutive([100, 4, 200, 1, 3, 2]))       # expected: 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # expected: 9
print(longest_consecutive([1, 0, 1, 2]))                   # expected: 3
```
