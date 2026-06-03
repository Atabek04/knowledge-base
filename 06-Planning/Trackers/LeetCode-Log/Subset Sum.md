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
Given a set of positive integers and a target sum S, determine whether any subset of the set adds up to exactly S. Each number can be used at most once. Return true if such a subset exists, false otherwise.

### Constraints
- 1 <= num.length <= 200
- 1 <= num[i] <= 100
- 1 <= S <= 10000

### Examples
```
{1,2,3,7}, S=6   →  true    ({1,2,3} sums to 6)
{1,2,7,1,5}, S=10 →  true   ({1,2,7} sums to 10)
{1,3,4,8}, S=6   →  false   (no subset sums to 6)
```

### Next solve approach
1. Brute Force first — recursively include or exclude each number; check if any branch reaches sum S, O(2^n)
2. Optimized (0/1 Knapsack) — DP boolean table dp[i][s]: can we reach sum s using first i numbers, O(N*S)

---

### Java

```java
public class Solution {

    // TODO: implement
    static boolean canPartition(int[] num, int sum) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        System.out.println(canPartition(new int[]{1, 2, 3, 7}, 6));    // expected: true
        System.out.println(canPartition(new int[]{1, 2, 7, 1, 5}, 10)); // expected: true
        System.out.println(canPartition(new int[]{1, 3, 4, 8}, 6));    // expected: false
    }
}
```

### Python

```python
def can_partition(num: list[int], sum: int) -> bool:
    # TODO: implement
    pass


print(can_partition([1, 2, 3, 7], 6))    # expected: True
print(can_partition([1, 2, 7, 1, 5], 10)) # expected: True
print(can_partition([1, 3, 4, 8], 6))    # expected: False
```
