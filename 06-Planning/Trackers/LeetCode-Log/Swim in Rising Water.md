---
difficulty: Hard
status: Not started
topic: [Advanced Graphs]
tags: [dfs, bfs, union-find, array, binary-search, matrix, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/swim-in-rising-water/"
---

### Problem
You are given an n x n grid where each cell holds a unique elevation value. As time t increases, every cell with elevation <= t becomes passable. You start at (0, 0) and want to reach (n-1, n-1) by moving 4-directionally between cells. Return the minimum time t at which a continuous path exists from the top-left to the bottom-right corner.

### Constraints
- n == grid.length
- n == grid[i].length
- 1 <= n <= 50
- 0 <= grid[i][j] < n^2
- Each value grid[i][j] is unique

### Examples
```
grid = [[0,2],[1,3]]                                              →  3   (need t=3 for all cells to be passable)
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]  →  16
```

### Next solve approach
1. Brute Force first — binary search on t, and for each t do BFS/DFS to check if (0,0) reaches (n-1,n-1)
2. Optimized — Union-Find: iterate heights 0..n^2-1, merge each cell with passable neighbors, stop when 0 and n^2-1 are connected

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public int swimInWater(int[][] grid) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.swimInWater(new int[][]{{0,2},{1,3}})); // expected: 3
        System.out.println(sol.swimInWater(new int[][]{
            {0,1,2,3,4},
            {24,23,22,21,5},
            {12,13,14,15,16},
            {11,17,18,19,20},
            {10,9,8,7,6}
        })); // expected: 16
    }
}
```

### Python

```python
from typing import List

def swim_in_water(grid: List[List[int]]) -> int:
    # TODO: implement
    pass


print(swim_in_water([[0,2],[1,3]]))  # expected: 3
print(swim_in_water([
    [0,1,2,3,4],
    [24,23,22,21,5],
    [12,13,14,15,16],
    [11,17,18,19,20],
    [10,9,8,7,6]
]))  # expected: 16
```
