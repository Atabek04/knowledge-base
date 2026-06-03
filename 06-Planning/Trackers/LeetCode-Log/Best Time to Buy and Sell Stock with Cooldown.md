---
difficulty: Medium
status: Not started
topic: [2-D Dynamic Programming]
tags: [array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/"
---

### Problem
You are given an array of stock prices where prices[i] is the price on day i. You may buy and sell as many times as you like, but after selling you must wait one cooldown day before buying again. You cannot hold more than one share at a time. Return the maximum profit achievable.

### Constraints
- 1 <= prices.length <= 5000
- 0 <= prices[i] <= 1000

### Examples
```
prices = [1,2,3,0,2]  →  3     (buy→sell→cooldown→buy→sell)
prices = [1]           →  0
```

### Next solve approach
1. Brute Force first — recursively try all buy/sell/cooldown decisions at each day
2. Optimized — DP with two states per day: holding stock and not holding, tracking cooldown via i-2 transition

---

### Java

```java
public class Solution {

    // TODO: implement
    public int maxProfit(int[] prices) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxProfit(new int[]{1, 2, 3, 0, 2})); // expected: 3
        System.out.println(sol.maxProfit(new int[]{1}));              // expected: 0
    }
}
```

### Python

```python
from typing import List

def max_profit(prices: List[int]) -> int:
    # TODO: implement
    pass


print(max_profit([1, 2, 3, 0, 2]))  # expected: 3
print(max_profit([1]))               # expected: 0
```
