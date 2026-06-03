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
You have N tasks labeled 0 to N-1 with prerequisite pairs [A, B] meaning A must finish before B. Find and return one valid ordering in which all tasks can be executed. If a cyclic dependency makes scheduling impossible, return an empty list.

### Constraints
- 1 <= tasks <= 1000
- Prerequisites form a directed graph; may contain cycles
- Return empty list [] if no valid ordering exists

### Examples
```
tasks=3, [[0,1],[1,2]]                           →  [0, 1, 2]
tasks=3, [[0,1],[1,2],[2,0]]                     →  []              (cycle → impossible)
tasks=6, [[2,5],[0,5],[0,4],[1,4],[3,2],[1,3]]   →  [0, 1, 4, 3, 2, 5]
```

### Next solve approach
1. Brute Force first — DFS post-order on each unvisited node, detect cycle via recursion stack, reverse output
2. Optimized (Topological Sort / Kahn's BFS) — in-degree map + queue; if output size < tasks, cycle detected → return []

---

### Java

```java
import java.util.*;

class TaskSchedulingOrder {

    // TODO: implement
    public static List<Integer> findOrder(int tasks, int[][] prerequisites) {
        List<Integer> sortedOrder = new ArrayList<>();
        // TODO
        return sortedOrder;
    }

    public static void main(String[] args) {
        System.out.println(TaskSchedulingOrder.findOrder(3, new int[][] {
            new int[] { 0, 1 }, new int[] { 1, 2 }
        })); // expected: [0, 1, 2]

        System.out.println(TaskSchedulingOrder.findOrder(3, new int[][] {
            new int[] { 0, 1 }, new int[] { 1, 2 }, new int[] { 2, 0 }
        })); // expected: []

        System.out.println(TaskSchedulingOrder.findOrder(6, new int[][] {
            new int[] { 2, 5 }, new int[] { 0, 5 },
            new int[] { 0, 4 }, new int[] { 1, 4 },
            new int[] { 3, 2 }, new int[] { 1, 3 }
        })); // expected: [0, 1, 4, 3, 2, 5]
    }
}
```

### Python

```python
def find_order(tasks: int, prerequisites: list[list[int]]) -> list[int]:
    # TODO: implement
    pass


print(find_order(3, [[0,1],[1,2]]))                           # expected: [0, 1, 2]
print(find_order(3, [[0,1],[1,2],[2,0]]))                     # expected: []
print(find_order(6, [[2,5],[0,5],[0,4],[1,4],[3,2],[1,3]]))  # expected: [0, 1, 4, 3, 2, 5]
```
