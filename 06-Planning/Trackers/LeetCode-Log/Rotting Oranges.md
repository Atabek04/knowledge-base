---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [bfs, array, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/rotting-oranges/"
---

### Problem
You have an m x n grid where each cell is 0 (empty), 1 (fresh orange), or 2 (rotten orange). Every minute, each rotten orange spreads rot to its 4-directionally adjacent fresh neighbors simultaneously. Return the minimum number of minutes until no fresh oranges remain, or -1 if it is impossible.

### Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2

### Examples
```
[[2,1,1],[1,1,0],[0,1,1]]  →  4
[[2,1,1],[0,1,1],[1,0,1]]  →  -1     (bottom-left orange isolated)
[[0,2]]                    →  0      (no fresh oranges to begin with)
```

### Next solve approach
1. Brute Force first — simulate minute by minute, scanning full grid each round to find newly rotten oranges
2. Optimized — multi-source BFS: seed all initially rotten oranges into a queue, BFS level by level counting minutes; check remaining fresh count at the end

---

### Java

```java
import java.util.ArrayDeque;
import java.util.Deque;

public class Solution {

    // TODO: implement
    public int orangesRotting(int[][] grid) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.orangesRotting(new int[][]{{2,1,1},{1,1,0},{0,1,1}})); // expected: 4
        System.out.println(sol.orangesRotting(new int[][]{{2,1,1},{0,1,1},{1,0,1}})); // expected: -1
        System.out.println(sol.orangesRotting(new int[][]{{0,2}}));                   // expected: 0
    }
}
```

### Python

```python
def oranges_rotting(grid: list[list[int]]) -> int:
    # TODO: implement
    pass


print(oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]))  # expected: 4
print(oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]))  # expected: -1
print(oranges_rotting([[0,2]]))                    # expected: 0
```
