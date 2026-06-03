---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [dfs, bfs, union-find, graph, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/"
---

### Problem
Given n nodes (labeled 0 to n-1) and a list of undirected edges, return the number of connected components in the graph. Isolated nodes with no edges each count as their own component.

### Constraints
- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges

### Examples
```
n = 5, edges = [[0,1],[1,2],[3,4]]          →  2
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]    →  1
```

### Next solve approach
1. Brute Force first — build adjacency list, DFS/BFS from each unvisited node to explore its component and count starts
2. Optimized — Union-Find: union each edge; count distinct roots at the end (start with n components, decrement each successful union)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int countComponents(int n, int[][] edges) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.countComponents(5, new int[][]{{0,1},{1,2},{3,4}}));       // expected: 2
        System.out.println(sol.countComponents(5, new int[][]{{0,1},{1,2},{2,3},{3,4}})); // expected: 1
    }
}
```

### Python

```python
def count_components(n: int, edges: list[list[int]]) -> int:
    # TODO: implement
    pass


print(count_components(5, [[0,1],[1,2],[3,4]]))       # expected: 2
print(count_components(5, [[0,1],[1,2],[2,3],[3,4]])) # expected: 1
```
