---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [dfs, bfs, union-find, array, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/max-area-of-island/"
---

### Problem
Given an m x n binary grid where 1 represents land and 0 represents water, an island is a group of 1s connected 4-directionally. The area of an island is the count of land cells it contains. Return the maximum area among all islands, or 0 if there are none.

### Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1

### Examples
```
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]  →  6
grid = [[0,0,0,0,0,0,0,0]]  →  0
```

### Next solve approach
1. Brute Force first — for each unvisited land cell, DFS to count the connected island's area and track the max
2. Optimized — same DFS but mark cells as visited in-place (set to 0) to avoid a separate visited array

---

### Java

```java
public class Solution {

    // TODO: implement
    public int maxAreaOfIsland(int[][] grid) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] grid1 = {
            {0,0,1,0,0,0,0,1,0,0,0,0,0},
            {0,0,0,0,0,0,0,1,1,1,0,0,0},
            {0,1,1,0,1,0,0,0,0,0,0,0,0},
            {0,1,0,0,1,1,0,0,1,0,1,0,0},
            {0,1,0,0,1,1,0,0,1,1,1,0,0},
            {0,0,0,0,0,0,0,0,0,0,1,0,0},
            {0,0,0,0,0,0,0,1,1,1,0,0,0},
            {0,0,0,0,0,0,0,1,1,0,0,0,0}
        };
        System.out.println(sol.maxAreaOfIsland(grid1)); // expected: 6

        System.out.println(sol.maxAreaOfIsland(new int[][]{{0,0,0,0,0,0,0,0}})); // expected: 0
    }
}
```

### Python

```python
def max_area_of_island(grid: list[list[int]]) -> int:
    # TODO: implement
    pass


grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(max_area_of_island(grid1))                    # expected: 6
print(max_area_of_island([[0,0,0,0,0,0,0,0]]))      # expected: 0
```
