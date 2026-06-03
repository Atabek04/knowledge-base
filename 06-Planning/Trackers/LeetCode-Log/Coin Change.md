---
difficulty: Medium
status: Not started
topic: [1-D Dynamic Programming]
tags: [bfs, array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/coin-change/"
---

### Problem
You have coins of various denominations and an unlimited supply of each. Given a target amount, find the minimum number of coins needed to make exactly that amount. If no combination of coins can reach the target, return -1.

### Constraints
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

### Examples
```
coins = [1,2,5], amount = 11  →  3     (5+5+1)
coins = [2], amount = 3       →  -1    (impossible)
coins = [1], amount = 0       →  0     (no coins needed)
```

### Next solve approach
1. Brute Force first — recursively try every coin at each step, return min depth that reaches amount
2. Optimized — bottom-up DP array of size amount+1, fill each position with min coins needed (complete knapsack pattern)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int coinChange(int[] coins, int amount) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.coinChange(new int[]{1, 2, 5}, 11)); // expected: 3
        System.out.println(sol.coinChange(new int[]{2}, 3));        // expected: -1
        System.out.println(sol.coinChange(new int[]{1}, 0));        // expected: 0
    }
}
```

### Python

```python
from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    # TODO: implement
    pass


print(coin_change([1, 2, 5], 11)) # expected: 3
print(coin_change([2], 3))        # expected: -1
print(coin_change([1], 0))        # expected: 0
```
