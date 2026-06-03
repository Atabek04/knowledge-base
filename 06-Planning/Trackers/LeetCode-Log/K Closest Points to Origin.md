---
difficulty: Medium
status: Not started
topic: [Heap / Priority Queue]
tags: [geometry, array, math, divide-and-conquer, quickselect, sorting, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/k-closest-points-to-origin/"
---

### Problem
Given a list of 2D points and an integer k, return the k points that are closest to the origin (0, 0). Distance is measured using standard Euclidean distance. The answer may be returned in any order and is guaranteed to be unique.

### Constraints
- 1 <= k <= points.length <= 10^4
- -10^4 <= xi, yi <= 10^4

### Examples
```
points = [[1,3],[-2,2]], k = 1  →  [[-2,2]]     (sqrt(8) < sqrt(10))
points = [[3,3],[5,-1],[-2,4]], k = 2  →  [[3,3],[-2,4]]
```

### Next solve approach
1. Brute Force first — compute all distances, sort, return first k points
2. Optimized — max-heap of size k keyed on squared distance; avoids full sort in O(n log k)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int[][] kClosest(int[][] points, int k) {
        // TODO
        return new int[0][];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] r1 = sol.kClosest(new int[][]{{1, 3}, {-2, 2}}, 1);
        System.out.println(java.util.Arrays.deepToString(r1)); // expected: [[-2, 2]]

        int[][] r2 = sol.kClosest(new int[][]{{3, 3}, {5, -1}, {-2, 4}}, 2);
        System.out.println(java.util.Arrays.deepToString(r2)); // expected: [[3,3],[-2,4]] (any order)
    }
}
```

### Python

```python
from typing import List

def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    # TODO: implement
    pass


print(k_closest([[1, 3], [-2, 2]], 1))             # expected: [[-2, 2]]
print(k_closest([[3, 3], [5, -1], [-2, 4]], 2))    # expected: [[3,3],[-2,4]] (any order)
```
