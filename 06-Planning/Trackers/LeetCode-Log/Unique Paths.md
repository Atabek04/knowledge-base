---
difficulty: Medium
status: Not started
topic: [2-D Dynamic Programming]
tags: [math, dynamic-programming, combinatorics, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/unique-paths/"
---

### Problem
A robot starts at the top-left corner of an m x n grid and must reach the bottom-right corner. The robot can only move right or down at each step. Given the grid dimensions m and n, count the total number of unique paths from start to finish. The answer is guaranteed to be at most 2 * 10^9.

### Constraints
- 1 <= m, n <= 100

### Examples
```
m = 3, n = 7  →  28
m = 3, n = 2  →  3     (Right→Down→Down, Down→Down→Right, Down→Right→Down)
```

### Next solve approach
1. Brute Force first — recursively explore all right/down moves, count paths to bottom-right
2. Optimized — 2-D DP table where dp[i][j] = dp[i-1][j] + dp[i][j-1]

---

### Java

```java
public class Solution {

    // TODO: implement
    public int uniquePaths(int m, int n) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.uniquePaths(3, 7)); // expected: 28
        System.out.println(sol.uniquePaths(3, 2)); // expected: 3
    }
}
```

### Python

```python
def unique_paths(m: int, n: int) -> int:
    # TODO: implement
    pass


print(unique_paths(3, 7))  # expected: 28
print(unique_paths(3, 2))  # expected: 3
```
