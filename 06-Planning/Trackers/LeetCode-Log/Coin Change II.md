---
difficulty: Medium
status: Not started
topic: [2-D Dynamic Programming]
tags: [array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/coin-change-ii/"
---

### Problem
Given an array of coin denominations and a target amount, count the number of distinct combinations that sum to that amount. You may use each coin denomination an unlimited number of times. If no combination reaches the target, return 0. The answer is guaranteed to fit in a 32-bit signed integer.

### Constraints
- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- All coin values are unique
- 0 <= amount <= 5000

### Examples
```
amount = 5,  coins = [1,2,5]  →  4     (5; 2+2+1; 2+1+1+1; 1+1+1+1+1)
amount = 3,  coins = [2]      →  0     (can't make 3 with only 2s)
amount = 10, coins = [10]     →  1
```

### Next solve approach
1. Brute Force first — recursively try each coin at every position, count combinations that hit the target
2. Optimized — complete knapsack 2-D DP: dp[i][j] = dp[i-1][j] + dp[i][j-coin]

---

### Java

```java
public class Solution {

    // TODO: implement
    public int change(int amount, int[] coins) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.change(5, new int[]{1, 2, 5}));  // expected: 4
        System.out.println(sol.change(3, new int[]{2}));         // expected: 0
        System.out.println(sol.change(10, new int[]{10}));       // expected: 1
    }
}
```

### Python

```python
from typing import List

def change(amount: int, coins: List[int]) -> int:
    # TODO: implement
    pass


print(change(5, [1, 2, 5]))  # expected: 4
print(change(3, [2]))         # expected: 0
print(change(10, [10]))       # expected: 1
```
