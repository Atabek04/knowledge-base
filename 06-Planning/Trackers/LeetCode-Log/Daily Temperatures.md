---
difficulty: Medium
status: Not started
topic: [Stack]
tags: [stack, array, monotonic-stack, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/daily-temperatures/"
---

### Problem
Given an array of daily temperatures, return an array where each element represents how many days you must wait after that day to see a strictly warmer temperature. If no warmer day exists in the future, that position should hold 0.

### Constraints
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

### Examples
```
[73,74,75,71,69,72,76,73]  →  [1,1,4,2,1,1,0,0]
[30,40,50,60]              →  [1,1,1,0]
[30,60,90]                 →  [1,1,0]
```

### Next solve approach
1. Brute Force first — for each day scan forward until a warmer day is found, O(n^2)
2. Optimized — monotonic stack storing indices; pop when a warmer day is found and record the gap

---

### Java

```java
public class Solution {

    // TODO: implement
    public int[] dailyTemperatures(int[] temperatures) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] r1 = sol.dailyTemperatures(new int[]{73, 74, 75, 71, 69, 72, 76, 73});
        System.out.println(java.util.Arrays.toString(r1)); // expected: [1, 1, 4, 2, 1, 1, 0, 0]

        int[] r2 = sol.dailyTemperatures(new int[]{30, 40, 50, 60});
        System.out.println(java.util.Arrays.toString(r2)); // expected: [1, 1, 1, 0]

        int[] r3 = sol.dailyTemperatures(new int[]{30, 60, 90});
        System.out.println(java.util.Arrays.toString(r3)); // expected: [1, 1, 0]
    }
}
```

### Python

```python
from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    # TODO: implement
    pass


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # expected: [1, 1, 4, 2, 1, 1, 0, 0]
print(daily_temperatures([30, 40, 50, 60]))                   # expected: [1, 1, 1, 0]
print(daily_temperatures([30, 60, 90]))                       # expected: [1, 1, 0]
```
