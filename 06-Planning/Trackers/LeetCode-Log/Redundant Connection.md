---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [dfs, bfs, union-find, graph, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/redundant-connection/"
---

### Problem
A graph of n nodes (labeled 1 to n) started as a tree but had one extra edge added. You are given all n edges; find and return the redundant edge that can be removed to restore the tree. If multiple answers exist, return the one that appears last in the input.

### Constraints
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges
- The given graph is connected

### Examples
```
edges = [[1,2],[1,3],[2,3]]              →  [2,3]
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]  →  [1,4]
```

### Next solve approach
1. Brute Force first — try removing each edge from back to front, check if remaining graph is a valid tree
2. Optimized — Union-Find: process edges in order; the first edge where both endpoints already share a root is the redundant one

---

### Java

```java
public class Solution {

    // TODO: implement
    public int[] findRedundantConnection(int[][] edges) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(java.util.Arrays.toString(
            sol.findRedundantConnection(new int[][]{{1,2},{1,3},{2,3}})
        )); // expected: [2, 3]

        System.out.println(java.util.Arrays.toString(
            sol.findRedundantConnection(new int[][]{{1,2},{2,3},{3,4},{1,4},{1,5}})
        )); // expected: [1, 4]
    }
}
```

### Python

```python
def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    # TODO: implement
    pass


print(find_redundant_connection([[1,2],[1,3],[2,3]]))              # expected: [2, 3]
print(find_redundant_connection([[1,2],[2,3],[3,4],[1,4],[1,5]])) # expected: [1, 4]
```
