---
difficulty: Medium
status: Not started
topic: [Advanced Graphs]
tags: [dfs, bfs, graph, shortest-path, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/network-delay-time/"
---

### Problem
You have a directed weighted graph of n nodes (labeled 1 to n), and a list of edges where each edge gives a source, destination, and travel time. A signal is sent from node k, and it propagates along the directed edges. Return the minimum time it takes for every node to receive the signal. If some node is unreachable from k, return -1.

### Constraints
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All pairs (ui, vi) are unique (no duplicate edges)

### Examples
```
times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2  →  2
times = [[1,2,1]], n = 2, k = 1                   →  1
times = [[1,2,1]], n = 2, k = 2                   →  -1   (node 1 unreachable from k=2)
```

### Next solve approach
1. Brute Force first — BFS/DFS from k, tracking shortest distances naively with repeated relaxation
2. Optimized — Dijkstra with a min-heap (priority queue) to always expand the closest unvisited node

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public int networkDelayTime(int[][] times, int n, int k) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.networkDelayTime(new int[][]{{2,1,1},{2,3,1},{3,4,1}}, 4, 2)); // expected: 2
        System.out.println(sol.networkDelayTime(new int[][]{{1,2,1}}, 2, 1));                 // expected: 1
        System.out.println(sol.networkDelayTime(new int[][]{{1,2,1}}, 2, 2));                 // expected: -1
    }
}
```

### Python

```python
from typing import List

def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    # TODO: implement
    pass


print(network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # expected: 2
print(network_delay_time([[1,2,1]], 2, 1))                   # expected: 1
print(network_delay_time([[1,2,1]], 2, 2))                   # expected: -1
```
