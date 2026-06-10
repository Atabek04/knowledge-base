---
difficulty: Easy
status: Solved
topic:
  - Arrays & Hashing
tags:
  - array
  - hash-table
  - sorting
  - neetcode-150
solved: 1
last_solved: 2026-06-08
link: https://leetcode.com/problems/contains-duplicate/
---

### Problem
Given an integer array, return true if any value appears at least twice, and false if every element is distinct. The simplest check is whether the number of unique values is smaller than the total length of the array.

### Constraints
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

### Examples
```
nums = [1,2,3,1]          →  true    (1 appears at indices 0 and 3)
nums = [1,2,3,4]          →  false   (all distinct)
nums = [1,1,1,3,3,4,3,2,4,2]  →  true
```

### Next solve approach
1. Brute Force first — sort and check adjacent elements for equality, O(n log n)
2. Optimized — hash set insertion; if add returns false the element was already seen, O(n)

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean containsDuplicate(int[] nums) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.containsDuplicate(new int[]{1, 2, 3, 1}));              // expected: true
        System.out.println(s.containsDuplicate(new int[]{1, 2, 3, 4}));              // expected: false
        System.out.println(s.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2})); // expected: true
    }
}
```

### Python

```python
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    # TODO: implement
    pass


print(contains_duplicate([1, 2, 3, 1]))                    # expected: True
print(contains_duplicate([1, 2, 3, 4]))                    # expected: False
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # expected: True
```
