---
difficulty: Medium
status: Not started
topic: [2-D Dynamic Programming]
tags: [array, dynamic-programming, backtracking, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/target-sum/"
---

### Problem
Given an integer array nums and a target integer, assign a '+' or '-' sign to each element and evaluate the resulting expression. Return the number of distinct sign assignments that produce a sum equal to target.

### Constraints
- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums[i]) <= 1000
- -1000 <= target <= 1000

### Examples
```
nums = [1,1,1,1,1], target = 3  →  5     (five ways to place one minus)
nums = [1],         target = 1  →  1
```

### Next solve approach
1. Brute Force first — backtrack assigning + or - to each number, count expressions that equal target
2. Optimized — reduce to 0/1 knapsack: find count of subsets summing to (sum - target) / 2

---

### Java

```java
public class Solution {

    // TODO: implement
    public int findTargetSumWays(int[] nums, int target) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.findTargetSumWays(new int[]{1, 1, 1, 1, 1}, 3)); // expected: 5
        System.out.println(sol.findTargetSumWays(new int[]{1}, 1));              // expected: 1
    }
}
```

### Python

```python
from typing import List

def find_target_sum_ways(nums: List[int], target: int) -> int:
    # TODO: implement
    pass


print(find_target_sum_ways([1, 1, 1, 1, 1], 3))  # expected: 5
print(find_target_sum_ways([1], 1))               # expected: 1
```
