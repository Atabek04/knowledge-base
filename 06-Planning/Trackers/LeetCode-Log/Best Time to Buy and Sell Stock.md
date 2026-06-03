---
difficulty: Easy
status: Not started
topic: [Sliding Window]
tags: [array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
---

### Problem
You are given an array `prices` where `prices[i]` is the stock price on day `i`. You may buy on one day and sell on a strictly later day. Return the maximum profit achievable from a single buy-sell transaction. If no profit is possible, return 0.

### Constraints
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

### Examples
```
prices = [7,1,5,3,6,4]  →  5     (buy at 1, sell at 6)
prices = [7,6,4,3,1]    →  0     (prices only drop, no profit possible)
```

### Next solve approach
1. Brute Force first — try every buy/sell pair in O(n²) and track the max difference
2. Optimized — single pass tracking the running minimum price seen so far (greedy)

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
        System.out.println(sol.maxProfit(new int[]{7, 1, 5, 3, 6, 4})); // expected: 5
        System.out.println(sol.maxProfit(new int[]{7, 6, 4, 3, 1}));    // expected: 0
    }
}
```

### Python

```python
def max_profit(prices: list[int]) -> int:
    # TODO: implement
    pass


print(max_profit([7, 1, 5, 3, 6, 4]))  # expected: 5
print(max_profit([7, 6, 4, 3, 1]))      # expected: 0
```
