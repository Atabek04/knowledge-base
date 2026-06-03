---
difficulty: Medium
status: Not started
topic: [1-D Dynamic Programming]
tags: [array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/partition-equal-subset-sum/"
---

### Problem
Given an integer array, determine whether it can be split into two subsets that have equal sums. If the total sum is odd, it is immediately impossible. Otherwise the problem reduces to a 0/1 knapsack: can any subset of numbers sum to exactly half the total? Return true if yes, false otherwise.

### Constraints
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

### Examples
```
nums = [1,5,11,5]  →  true    ([1,5,5] and [11])
nums = [1,2,3,5]   →  false   (no valid partition exists)
```

### Next solve approach
1. Brute Force first — recursively try including or excluding each element, check if any subset reaches sum/2
2. Optimized — 1-D boolean DP array of size sum/2+1; for each number iterate backwards and set dp[j] |= dp[j-num] (0/1 knapsack)

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean canPartition(int[] nums) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.canPartition(new int[]{1, 5, 11, 5})); // expected: true
        System.out.println(sol.canPartition(new int[]{1, 2, 3, 5}));  // expected: false
    }
}
```

### Python

```python
from typing import List

def can_partition(nums: List[int]) -> bool:
    # TODO: implement
    pass


print(can_partition([1, 5, 11, 5])) # expected: True
print(can_partition([1, 2, 3, 5]))  # expected: False
```
