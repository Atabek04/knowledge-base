---
difficulty: Medium
status: Not started
topic: [Two Pointers]
tags: [greedy, array, two-pointers, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/container-with-most-water/"
---

### Problem
You are given an integer array `height` of length n, where each element represents the height of a vertical line at position i. Pairs of lines form a container with the x-axis; the water a container holds equals the shorter line's height multiplied by the distance between the two lines. Find the pair of lines that together can hold the most water and return that maximum amount. You cannot tilt the container.

### Constraints
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

### Examples
```
[1,8,6,2,5,4,8,3,7]  →  49    (lines at index 1 and 8: min(8,7) * 7 = 49)
[1,1]                 →  1
```

### Next solve approach
1. Brute Force first — check every pair of lines with two nested loops and track the maximum area (O(n^2)).
2. Optimized — two pointers starting at both ends; always move the pointer pointing at the shorter line inward, since that is the only way to possibly increase the area (O(n)).

---

### Java

```java
public class Solution {

    // TODO: implement
    public int maxArea(int[] height) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7})); // expected: 49
        System.out.println(sol.maxArea(new int[]{1, 1}));                       // expected: 1
    }
}
```

### Python

```python
from typing import List


def max_area(height: List[int]) -> int:
    # TODO: implement
    pass


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # expected: 49
print(max_area([1, 1]))                        # expected: 1
```
