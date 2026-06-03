---
difficulty: Medium
status: Not started
topic: [1-D Dynamic Programming]
tags: [array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/house-robber-ii/"
---

### Problem
Same as House Robber but the houses are arranged in a circle, meaning the first and last houses are adjacent. You cannot rob two adjacent houses. Return the maximum money you can steal without triggering the alarm. The key insight is that the first and last house cannot both be robbed, so you solve two separate linear House Robber problems: one excluding the last house and one excluding the first house, then take the max.

### Constraints
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

### Examples
```
nums = [2,3,2]    →  3     (can't rob both ends; rob house 1: value 3)
nums = [1,2,3,1]  →  4     (rob house 0 and house 2: 1+3)
nums = [1,2,3]    →  3
```

### Next solve approach
1. Brute Force first — try all non-adjacent subsets with the circular constraint enforced
2. Optimized — run linear House Robber twice: on nums[0..n-2] and nums[1..n-1], return the max of both results

---

### Java

```java
public class Solution {

    // TODO: implement
    public int rob(int[] nums) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.rob(new int[]{2, 3, 2}));    // expected: 3
        System.out.println(sol.rob(new int[]{1, 2, 3, 1})); // expected: 4
        System.out.println(sol.rob(new int[]{1, 2, 3}));    // expected: 3
    }
}
```

### Python

```python
from typing import List

def rob(nums: List[int]) -> int:
    # TODO: implement
    pass


print(rob([2, 3, 2]))    # expected: 3
print(rob([1, 2, 3, 1])) # expected: 4
print(rob([1, 2, 3]))    # expected: 3
```
