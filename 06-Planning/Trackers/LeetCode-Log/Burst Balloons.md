---
difficulty: Hard
status: Not started
topic: [2-D Dynamic Programming]
tags: [array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/burst-balloons/"
---

### Problem
You have n balloons, each labeled with a number. When you burst balloon i, you earn nums[i-1] * nums[i] * nums[i+1] coins; balloons out of bounds are treated as 1. Burst all balloons in the order that maximizes your total coins.

### Constraints
- n == nums.length
- 1 <= n <= 300
- 0 <= nums[i] <= 100

### Examples
```
nums = [3,1,5,8]  →  167     (3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167)
nums = [1,5]      →  10
```

### Next solve approach
1. Brute Force first — try every permutation of burst order, keep track of maximum coins
2. Optimized — interval DP: think of k as the LAST balloon burst in range (i,j); dp[i][j] = max coins for open interval (i,j)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int maxCoins(int[] nums) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxCoins(new int[]{3, 1, 5, 8})); // expected: 167
        System.out.println(sol.maxCoins(new int[]{1, 5}));        // expected: 10
    }
}
```

### Python

```python
from typing import List

def max_coins(nums: List[int]) -> int:
    # TODO: implement
    pass


print(max_coins([3, 1, 5, 8]))  # expected: 167
print(max_coins([1, 5]))         # expected: 10
```
