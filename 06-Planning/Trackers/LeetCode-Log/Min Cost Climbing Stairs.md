---
difficulty: Easy
status: Not started
topic: [1-D Dynamic Programming]
tags: [array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/min-cost-climbing-stairs/"
---

### Problem
You are given an array where cost[i] is the fee to step onto stair i. After paying the cost you can climb one or two steps. You can start from index 0 or index 1. Find the minimum total cost to reach the floor above the last stair (i.e., past the end of the array).

### Constraints
- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999

### Examples
```
cost = [10,15,20]                       →  15    (start at index 1, pay 15, jump 2 steps)
cost = [1,100,1,1,1,100,1,1,100,1]     →  6
```

### Next solve approach
1. Brute Force first — recursive DFS from index 0 and index 1, try both one-step and two-step at each position
2. Optimized — DP where dp[i] = min cost to reach step i; dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]); answer is dp[n]

---

### Java

```java
public class Solution {

    // TODO: implement
    public int minCostClimbingStairs(int[] cost) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minCostClimbingStairs(new int[]{10, 15, 20}));                           // expected: 15
        System.out.println(sol.minCostClimbingStairs(new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1})); // expected: 6
    }
}
```

### Python

```python
from typing import List

def min_cost_climbing_stairs(cost: List[int]) -> int:
    # TODO: implement
    pass


print(min_cost_climbing_stairs([10, 15, 20]))                          # expected: 15
print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])) # expected: 6
```
