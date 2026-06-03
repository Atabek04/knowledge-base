---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [dfs, bfs, array, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/pacific-atlantic-water-flow/"
---

### Problem
An island borders both the Pacific Ocean (top and left edges) and the Atlantic Ocean (bottom and right edges). Rain water can flow from a cell to a neighbor if the neighbor's height is less than or equal to the current cell's height. Return all cells from which water can flow to both oceans.

### Constraints
- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5

### Examples
```
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]  →  [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
heights = [[1]]                                                              →  [[0,0]]
```

### Next solve approach
1. Brute Force first — for each cell, run DFS/BFS forward to check if it can reach both oceans; O(m^2 * n^2)
2. Optimized — reverse BFS from each ocean's border cells inward (water flows uphill in reverse); take intersection of the two reachable sets

---

### Java

```java
import java.util.ArrayList;
import java.util.List;

public class Solution {

    // TODO: implement
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] heights1 = {
            {1,2,2,3,5},
            {3,2,3,4,4},
            {2,4,5,3,1},
            {6,7,1,4,5},
            {5,1,1,2,4}
        };
        System.out.println(sol.pacificAtlantic(heights1)); // expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

        System.out.println(sol.pacificAtlantic(new int[][]{{1}})); // expected: [[0,0]]
    }
}
```

### Python

```python
def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    # TODO: implement
    pass


heights1 = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacific_atlantic(heights1))  # expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(pacific_atlantic([[1]]))     # expected: [[0,0]]
```
