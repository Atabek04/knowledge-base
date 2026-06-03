---
difficulty: Hard
status: Not started
topic: [Stack]
tags: [stack, array, monotonic-stack, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/largest-rectangle-in-histogram/"
---

### Problem
Given an array of bar heights in a histogram where every bar has width 1, find the area of the largest rectangle that can be formed. The rectangle must be contained within consecutive bars and cannot exceed the height of any bar it spans.

### Constraints
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4

### Examples
```
[2,1,5,6,2,3]  →  10    (bars at indices 2-3, height 5, width 2)
[2,4]          →  4     (single bar of height 4)
```

### Next solve approach
1. Brute Force first — for every pair of indices compute the minimum height and multiply by width, O(n^2)
2. Optimized — monotonic stack to find, for each bar, the nearest shorter bar on both sides; area = height * (right - left - 1)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int largestRectangleArea(int[] heights) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.largestRectangleArea(new int[]{2, 1, 5, 6, 2, 3}));
        // expected: 10

        System.out.println(sol.largestRectangleArea(new int[]{2, 4}));
        // expected: 4
    }
}
```

### Python

```python
from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    # TODO: implement
    pass


print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # expected: 10
print(largest_rectangle_area([2, 4]))               # expected: 4
```
