---
difficulty: Medium
status: Not started
topic: [Advanced Graphs]
tags: [union-find, graph, array, minimum-spanning-tree, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/min-cost-to-connect-all-points/"
---

### Problem
You are given a set of points on a 2D plane. The cost of connecting any two points is the Manhattan distance between them: |x1 - x2| + |y1 - y2|. Return the minimum total cost to connect all points such that there is exactly one simple path between any two points (i.e., build a minimum spanning tree).

### Constraints
- 1 <= points.length <= 1000
- -10^6 <= xi, yi <= 10^6
- All pairs (xi, yi) are distinct

### Examples
```
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]  →  20
points = [[3,12],[-2,5],[-4,1]]            →  18
```

### Next solve approach
1. Brute Force first — generate all edges with their Manhattan distances, sort them, try connecting greedily
2. Optimized — Prim's algorithm with a dist array (or Kruskal's with Union-Find) to build the MST in O(n^2) or O(n^2 log n)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public int minCostConnectPoints(int[][] points) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.minCostConnectPoints(new int[][]{{0,0},{2,2},{3,10},{5,2},{7,0}})); // expected: 20
        System.out.println(sol.minCostConnectPoints(new int[][]{{3,12},{-2,5},{-4,1}}));           // expected: 18
    }
}
```

### Python

```python
from typing import List

def min_cost_connect_points(points: List[List[int]]) -> int:
    # TODO: implement
    pass


print(min_cost_connect_points([[0,0],[2,2],[3,10],[5,2],[7,0]]))  # expected: 20
print(min_cost_connect_points([[3,12],[-2,5],[-4,1]]))            # expected: 18
```
