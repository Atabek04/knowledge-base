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
Given a set of positive integers, determine whether it can be split into two non-empty subsets such that both subsets have equal sums. Return true if such a partition exists, false otherwise.

### Constraints
- 1 <= num.length <= 200
- 1 <= num[i] <= 100
- Total sum of the array fits in a 32-bit integer

### Examples
```
{1,2,3,4}    →  true    ({1,4} and {2,3} both sum to 5)
{1,1,3,4,7}  →  true    ({1,3,4} and {1,7} both sum to 8)
{2,3,4,6}    →  false   (no equal-sum partition exists)
```

### Next solve approach
1. Brute Force first — recursively try every subset; check if any has sum == totalSum/2, O(2^n)
2. Optimized (0/1 Knapsack) — DP on target = totalSum/2; if totalSum is odd return false immediately, O(N*S)

---

### Java

```java
public class Solution {

    // TODO: implement
    static boolean canPartition(int[] num) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        System.out.println(canPartition(new int[]{1, 2, 3, 4}));    // expected: true
        System.out.println(canPartition(new int[]{1, 1, 3, 4, 7})); // expected: true
        System.out.println(canPartition(new int[]{2, 3, 4, 6}));    // expected: false
    }
}
```

### Python

```python
def can_partition(num: list[int]) -> bool:
    # TODO: implement
    pass


print(can_partition([1, 2, 3, 4]))    # expected: True
print(can_partition([1, 1, 3, 4, 7])) # expected: True
print(can_partition([2, 3, 4, 6]))    # expected: False
```
