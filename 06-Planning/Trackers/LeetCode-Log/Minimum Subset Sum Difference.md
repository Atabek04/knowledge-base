---
difficulty: Hard
status: Not started
topic: [0/1 Knapsack, Dynamic Programming, Arrays]
tags: [knapsack, dynamic-programming, array, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a set of positive integers, split it into two subsets such that the absolute difference between their sums is minimized. Return the minimum possible difference. Every number must go into one of the two subsets.

### Constraints
- 1 <= num.length <= 200
- 1 <= num[i] <= 100
- Total sum fits in a 32-bit integer

### Examples
```
{1,2,3,9}    →  3    ({1,2,3}=6 vs {9}=9, diff=3)
{1,2,7,1,5}  →  0    ({1,2,5}=8 vs {7,1}=8, diff=0)
{1,3,100,4}  →  92   ({1,3,4}=8 vs {100}=100, diff=92)
```

### Next solve approach
1. Brute Force first — try adding each element to either subset S1 or S2 recursively, return min |S1-S2| at the end, O(2^n)
2. Optimized (0/1 Knapsack) — reduce to Subset Sum: find the largest reachable sum <= totalSum/2 using DP, answer is totalSum - 2*that, O(N*S)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int canPartition(int[] num) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.canPartition(new int[]{1, 2, 3, 9}));    // expected: 3
        System.out.println(sol.canPartition(new int[]{1, 2, 7, 1, 5})); // expected: 0
        System.out.println(sol.canPartition(new int[]{1, 3, 100, 4}));  // expected: 92
    }
}
```

### Python

```python
def can_partition(num: list[int]) -> int:
    # TODO: implement
    pass


print(can_partition([1, 2, 3, 9]))    # expected: 3
print(can_partition([1, 2, 7, 1, 5])) # expected: 0
print(can_partition([1, 3, 100, 4]))  # expected: 92
```
