---
difficulty: Hard
status: Not started
topic: [2-D Dynamic Programming]
tags: [dfs, bfs, graph, topological-sort, memoization, array, dynamic-programming, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/longest-increasing-path-in-a-matrix/"
---

### Problem
Given an m x n integer matrix, find the length of the longest strictly increasing path. From any cell you may move up, down, left, or right, but not diagonally and not outside the grid boundary. You must always move to a cell with a strictly greater value.

### Constraints
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- 0 <= matrix[i][j] <= 2^31 - 1

### Examples
```
matrix = [[9,9,4],[6,6,8],[2,1,1]]    →  4     (path: 1→2→6→9)
matrix = [[3,4,5],[3,2,6],[2,2,1]]    →  4     (path: 3→4→5→6)
matrix = [[1]]                         →  1
```

### Next solve approach
1. Brute Force first — DFS from every cell, track visited to avoid revisiting, return max path length
2. Optimized — DFS with memoization (cache[i][j] = longest path from cell (i,j)), no visited set needed since strictly increasing prevents cycles

---

### Java

```java
public class Solution {

    // TODO: implement
    public int longestIncreasingPath(int[][] matrix) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.longestIncreasingPath(new int[][]{{9,9,4},{6,6,8},{2,1,1}})); // expected: 4
        System.out.println(sol.longestIncreasingPath(new int[][]{{3,4,5},{3,2,6},{2,2,1}})); // expected: 4
        System.out.println(sol.longestIncreasingPath(new int[][]{{1}}));                      // expected: 1
    }
}
```

### Python

```python
from typing import List

def longest_increasing_path(matrix: List[List[int]]) -> int:
    # TODO: implement
    pass


print(longest_increasing_path([[9,9,4],[6,6,8],[2,1,1]]))  # expected: 4
print(longest_increasing_path([[3,4,5],[3,2,6],[2,2,1]]))  # expected: 4
print(longest_increasing_path([[1]]))                        # expected: 1
```
