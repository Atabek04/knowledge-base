---
difficulty: Easy
status: Not started
topic: [1-D Dynamic Programming]
tags: [memoization, math, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/climbing-stairs/"
---

### Problem
You are climbing a staircase that has n steps. Each move you can climb either 1 or 2 steps. Count the total number of distinct ways to reach the top. The answer follows a Fibonacci-like pattern: the number of ways to reach step n equals the sum of ways to reach step n-1 and step n-2.

### Constraints
- 1 <= n <= 45

### Examples
```
n = 2  →  2     (1+1 or 2)
n = 3  →  3     (1+1+1, 1+2, or 2+1)
```

### Next solve approach
1. Brute Force first — recursively try climbing 1 or 2 steps from each position (exponential, lots of repeated work)
2. Optimized — bottom-up DP keeping only the last two values (Fibonacci iteration, O(n) time, O(1) space)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int climbStairs(int n) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.climbStairs(2)); // expected: 2
        System.out.println(sol.climbStairs(3)); // expected: 3
    }
}
```

### Python

```python
def climb_stairs(n: int) -> int:
    # TODO: implement
    pass


print(climb_stairs(2))  # expected: 2
print(climb_stairs(3))  # expected: 3
```
