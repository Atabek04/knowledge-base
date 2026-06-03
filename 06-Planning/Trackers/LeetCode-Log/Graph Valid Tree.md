---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [dfs, bfs, union-find, graph, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/graph-valid-tree/"
---

### Problem
Given n nodes labeled 0 to n-1 and a list of undirected edges, determine whether these edges form a valid tree. A valid tree must be connected and contain no cycles, which means it must have exactly n-1 edges and all nodes reachable from any single node.

### Constraints
- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no self-loops or repeated edges

### Examples
```
n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]          →  true
n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]    →  false   (cycle between 1-2-3)
```

### Next solve approach
1. Brute Force first — build adjacency list, DFS from node 0, check for cycles and that all n nodes are visited
2. Optimized — Union-Find: first check edge count == n-1; then for each edge if both nodes share a root it's a cycle, otherwise union them

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean validTree(int n, int[][] edges) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.validTree(5, new int[][]{{0,1},{0,2},{0,3},{1,4}}));       // expected: true
        System.out.println(sol.validTree(5, new int[][]{{0,1},{1,2},{2,3},{1,3},{1,4}})); // expected: false
    }
}
```

### Python

```python
def valid_tree(n: int, edges: list[list[int]]) -> bool:
    # TODO: implement
    pass


print(valid_tree(5, [[0,1],[0,2],[0,3],[1,4]]))       # expected: True
print(valid_tree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])) # expected: False
```
