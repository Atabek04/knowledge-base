---
difficulty: Medium
status: Not started
topic: [1-D Dynamic Programming]
tags: [array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/house-robber/"
---

### Problem
You are a robber planning to steal from houses along a street. Each house holds some amount of money, but adjacent houses share a security alarm — robbing two neighboring houses on the same night triggers it. Given an array of house values, find the maximum money you can steal without triggering the alarm.

### Constraints
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

### Examples
```
nums = [1,2,3,1]    →  4     (rob house 0 and house 2: 1+3)
nums = [2,7,9,3,1]  →  12    (rob house 0, 2, 4: 2+9+1)
```

### Next solve approach
1. Brute Force first — try all subsets of non-adjacent houses and take the max sum
2. Optimized — DP with two variables tracking the best result including and excluding the current house (O(n) time, O(1) space)

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
        System.out.println(sol.rob(new int[]{1, 2, 3, 1}));    // expected: 4
        System.out.println(sol.rob(new int[]{2, 7, 9, 3, 1})); // expected: 12
    }
}
```

### Python

```python
from typing import List

def rob(nums: List[int]) -> int:
    # TODO: implement
    pass


print(rob([1, 2, 3, 1]))    # expected: 4
print(rob([2, 7, 9, 3, 1])) # expected: 12
```
