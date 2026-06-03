---
difficulty: Medium
status: Not started
topic: [Two Pointers]
tags: [array, two-pointers, binary-search, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"
---

### Problem
You are given a 1-indexed integer array `numbers` that is already sorted in non-decreasing order. Find two numbers that add up to a given `target` and return their 1-based indices as `[index1, index2]`. There is exactly one solution and you may not use the same element twice. Your solution must use only constant extra space.

### Constraints
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- Exactly one solution exists.

### Examples
```
numbers = [2,7,11,15], target = 9   →  [1,2]     (2 + 7 = 9)
numbers = [2,3,4],     target = 6   →  [1,3]     (2 + 4 = 6)
numbers = [-1,0],      target = -1  →  [1,2]     (-1 + 0 = -1)
```

### Next solve approach
1. Brute Force first — two nested loops over every pair, return indices when sum matches (O(n^2), O(1) space).
2. Optimized — two pointers at opposite ends; if the sum is too small move the left pointer right, if too large move the right pointer left; guaranteed to find the answer in O(n).

---

### Java

```java
public class Solution {

    // TODO: implement
    public int[] twoSum(int[] numbers, int target) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] r1 = sol.twoSum(new int[]{2, 7, 11, 15}, 9);
        System.out.println(r1[0] + ", " + r1[1]); // expected: 1, 2

        int[] r2 = sol.twoSum(new int[]{2, 3, 4}, 6);
        System.out.println(r2[0] + ", " + r2[1]); // expected: 1, 3

        int[] r3 = sol.twoSum(new int[]{-1, 0}, -1);
        System.out.println(r3[0] + ", " + r3[1]); // expected: 1, 2
    }
}
```

### Python

```python
from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    # TODO: implement
    pass


print(two_sum([2, 7, 11, 15], 9))   # expected: [1, 2]
print(two_sum([2, 3, 4], 6))        # expected: [1, 3]
print(two_sum([-1, 0], -1))         # expected: [1, 2]
```
