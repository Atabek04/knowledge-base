---
difficulty: Medium
status: Not started
topic: [Greedy]
tags: [greedy, array, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/gas-station/"
---

### Problem
There are n gas stations arranged in a circle. Station i provides gas[i] fuel, and traveling from station i to the next costs cost[i] fuel. Your tank starts empty and is unlimited. Find the index of the starting station from which you can complete the full circular route, or return -1 if it's impossible. The answer is guaranteed to be unique if it exists.

### Constraints
- n == gas.length == cost.length
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4
- The input is generated such that the answer is unique

### Examples
```
gas=[1,2,3,4,5], cost=[3,4,5,1,2]  →  3
gas=[2,3,4],     cost=[3,4,3]       →  -1
```

### Next solve approach
1. Brute Force first — try starting at each station and simulate the full loop O(n²)
2. Optimized — greedy: if total gas < total cost return -1; otherwise scan and reset candidate start whenever running tank goes negative

---

### Java

```java
public class Solution {

    // TODO: implement
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.canCompleteCircuit(
            new int[]{1,2,3,4,5}, new int[]{3,4,5,1,2})); // expected: 3
        System.out.println(sol.canCompleteCircuit(
            new int[]{2,3,4}, new int[]{3,4,3}));           // expected: -1
    }
}
```

### Python

```python
def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    # TODO: implement
    pass


print(can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]))  # expected: 3
print(can_complete_circuit([2,3,4], [3,4,3]))           # expected: -1
```
