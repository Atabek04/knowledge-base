---
difficulty: Hard
status: Not started
topic: [Two Pointers]
tags: [stack, array, two-pointers, dynamic-programming, monotonic-stack, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/trapping-rain-water/"
---

### Problem
Given n non-negative integers representing an elevation map where each bar has a width of 1, compute how much rainwater can be trapped between the bars after it rains. Water at any position is bounded above by the minimum of the tallest bar to its left and the tallest bar to its right, minus the bar's own height.

### Constraints
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

### Examples
```
[0,1,0,2,1,0,1,3,2,1,2,1]  →  6
[4,2,0,3,2,5]               →  9
```

### Next solve approach
1. Brute Force first — for each position scan left and right to find the max bar on each side, compute trapped water per cell (O(n^2)).
2. Optimized — precompute prefix max from the left and suffix max from the right in two passes, then sum min(left[i], right[i]) - height[i] for each index (O(n) time, O(n) space); alternatively use two pointers for O(1) space.

---

### Java

```java
public class Solution {

    // TODO: implement
    public int trap(int[] height) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.trap(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1})); // expected: 6
        System.out.println(sol.trap(new int[]{4, 2, 0, 3, 2, 5}));                    // expected: 9
    }
}
```

### Python

```python
from typing import List


def trap(height: List[int]) -> int:
    # TODO: implement
    pass


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # expected: 6
print(trap([4, 2, 0, 3, 2, 5]))                      # expected: 9
```
