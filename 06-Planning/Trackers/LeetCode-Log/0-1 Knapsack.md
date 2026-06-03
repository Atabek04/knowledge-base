---
difficulty: Medium
status: Not started
topic: [0/1 Knapsack, Dynamic Programming, Arrays]
tags: [knapsack, dynamic-programming, array, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
You have N items, each with a weight and a profit. Given a knapsack with a maximum weight capacity C, choose a subset of items — each item used at most once — that maximizes total profit without exceeding C. Return the maximum achievable profit.

### Constraints
- 1 <= N <= 1000
- 1 <= capacity <= 1000
- profits.length == weights.length == N
- All profits and weights are positive integers

### Examples
```
profits=[1,6,10,16], weights=[1,2,3,5], capacity=7  →  22   (items B+D: weight 2+5=7, profit 6+16=22)
profits=[1,6,10,16], weights=[1,2,3,5], capacity=6  →  17   (items A+B+C: weight 1+2+3=6, profit 1+6+10=17)
```

### Next solve approach
1. Brute Force first — recursively try including or excluding each item, return max profit of both branches, O(2^n)
2. Optimized (0/1 Knapsack) — bottom-up DP table dp[i][c] = max profit using first i items with capacity c, O(N*C)

---

### Java

```java
public class Solution {

    // TODO: implement
    static int solveKnapsack(int[] profits, int[] weights, int capacity) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        int[] profits = {1, 6, 10, 16};
        int[] weights = {1, 2, 3, 5};
        System.out.println(solveKnapsack(profits, weights, 7)); // expected: 22
        System.out.println(solveKnapsack(profits, weights, 6)); // expected: 17
    }
}
```

### Python

```python
def solve_knapsack(profits: list[int], weights: list[int], capacity: int) -> int:
    # TODO: implement
    pass


profits = [1, 6, 10, 16]
weights = [1, 2, 3, 5]
print(solve_knapsack(profits, weights, 7))  # expected: 22
print(solve_knapsack(profits, weights, 6))  # expected: 17
```
