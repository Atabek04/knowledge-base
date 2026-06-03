---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [bfs, array, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/walls-and-gates/"
---

### Problem
You are given an m x n grid initialized with -1 (wall/obstacle), 0 (gate), or INF = 2147483647 (empty room). Fill each empty room with the distance to its nearest gate. If a room cannot reach any gate, leave it as INF. Modify the grid in-place; return nothing.

### Constraints
- m == rooms.length
- n == rooms[i].length
- 1 <= m, n <= 250
- rooms[i][j] is -1, 0, or 2^31 - 1

### Examples
```
[[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]  →  [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
[[-1]]  →  [[-1]]
```

### Next solve approach
1. Brute Force first — BFS/DFS from each empty room to find nearest gate; O(m^2 * n^2)
2. Optimized — multi-source BFS: seed all gates simultaneously into a queue, expand outward level by level assigning distances

---

### Java

```java
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

public class Solution {

    // TODO: implement
    public void wallsAndGates(int[][] rooms) {
        // TODO
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int INF = Integer.MAX_VALUE;
        int[][] rooms = {
            {INF, -1, 0, INF},
            {INF, INF, INF, -1},
            {INF, -1, INF, -1},
            {0, -1, INF, INF}
        };
        sol.wallsAndGates(rooms);
        System.out.println(Arrays.deepToString(rooms));
        // expected: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

        int[][] rooms2 = {{-1}};
        sol.wallsAndGates(rooms2);
        System.out.println(Arrays.deepToString(rooms2)); // expected: [[-1]]
    }
}
```

### Python

```python
def walls_and_gates(rooms: list[list[int]]) -> None:
    # TODO: implement
    pass


INF = 2147483647
rooms = [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
walls_and_gates(rooms)
print(rooms)  # expected: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```
