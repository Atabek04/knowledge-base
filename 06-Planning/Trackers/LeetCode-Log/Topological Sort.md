---
difficulty: Medium
status: Not started
topic: [Topological Sort, Graphs]
tags: [topological-sort, graph, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a directed acyclic graph (DAG) with a given number of vertices and a list of directed edges, produce a linear ordering of all vertices such that for every edge (U → V), vertex U appears before vertex V in the result. Multiple valid orderings may exist — return any one of them.

### Constraints
- 1 <= vertices <= 1000
- Edges are directed and the graph is acyclic (DAG)
- Input fits in memory

### Examples
```
4 vertices, [[3,2],[3,0],[2,0],[2,1]]                             →  [3, 2, 0, 1]        (one valid order; [3,2,1,0] also valid)
5 vertices, [[4,2],[4,3],[2,0],[2,1],[3,1]]                       →  [4, 2, 3, 0, 1]     (one of several valid orders)
7 vertices, [[6,4],[6,2],[5,3],[5,4],[3,0],[3,1],[3,2],[4,1]]     →  [5, 6, 3, 4, 0, 1, 2]
```

### Next solve approach
1. Brute Force first — DFS post-order on all unvisited nodes, reverse the result
2. Optimized (Topological Sort / Kahn's BFS) — track in-degrees, enqueue zero-in-degree nodes, process level by level

---

### Java

```java
import java.util.*;

class TopologicalSort {

    // TODO: implement
    public static List<Integer> sort(int vertices, int[][] edges) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        System.out.println(TopologicalSort.sort(4, new int[][] {
            new int[] { 3, 2 }, new int[] { 3, 0 },
            new int[] { 2, 0 }, new int[] { 2, 1 }
        })); // expected: [3, 2, 0, 1] or [3, 2, 1, 0]

        System.out.println(TopologicalSort.sort(5, new int[][] {
            new int[] { 4, 2 }, new int[] { 4, 3 },
            new int[] { 2, 0 }, new int[] { 2, 1 },
            new int[] { 3, 1 }
        })); // expected: [4, 2, 3, 0, 1] (one valid order)

        System.out.println(TopologicalSort.sort(7, new int[][] {
            new int[] { 6, 4 }, new int[] { 6, 2 },
            new int[] { 5, 3 }, new int[] { 5, 4 },
            new int[] { 3, 0 }, new int[] { 3, 1 },
            new int[] { 3, 2 }, new int[] { 4, 1 }
        })); // expected: [5, 6, 3, 4, 0, 1, 2] (one valid order)
    }
}
```

### Python

```python
def sort(vertices: int, edges: list[list[int]]) -> list[int]:
    # TODO: implement
    pass


print(sort(4, [[3,2],[3,0],[2,0],[2,1]]))                                    # expected: [3, 2, 0, 1] or [3, 2, 1, 0]
print(sort(5, [[4,2],[4,3],[2,0],[2,1],[3,1]]))                              # expected: [4, 2, 3, 0, 1] (one valid order)
print(sort(7, [[6,4],[6,2],[5,3],[5,4],[3,0],[3,1],[3,2],[4,1]]))            # expected: [5, 6, 3, 4, 0, 1, 2]
```
