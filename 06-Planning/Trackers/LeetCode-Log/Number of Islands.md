---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [dfs, bfs, union-find, array, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/number-of-islands/"
---

### Problem
Given an m x n grid of '1's (land) and '0's (water), count the number of islands. An island is a group of horizontally or vertically connected land cells, and is completely surrounded by water. You can assume all four edges of the grid are surrounded by water.

### Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'

### Examples
```
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]  →  1
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]  →  3
```

### Next solve approach
1. Brute Force first — iterate every cell; when '1' found, DFS/BFS to sink the island and increment counter
2. Optimized — Union-Find: merge adjacent land cells, count distinct roots

---

### Java

```java
public class Solution {

    // TODO: implement
    public int numIslands(char[][] grid) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        char[][] grid1 = {
            {'1','1','1','1','0'},
            {'1','1','0','1','0'},
            {'1','1','0','0','0'},
            {'0','0','0','0','0'}
        };
        System.out.println(sol.numIslands(grid1)); // expected: 1

        char[][] grid2 = {
            {'1','1','0','0','0'},
            {'1','1','0','0','0'},
            {'0','0','1','0','0'},
            {'0','0','0','1','1'}
        };
        System.out.println(sol.numIslands(grid2)); // expected: 3
    }
}
```

### Python

```python
def num_islands(grid: list[list[str]]) -> int:
    # TODO: implement
    pass


grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(num_islands(grid1))  # expected: 1

grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(num_islands(grid2))  # expected: 3
```
