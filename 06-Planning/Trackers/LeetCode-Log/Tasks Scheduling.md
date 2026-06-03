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
You have N tasks labeled 0 to N-1, and a list of prerequisite pairs where each pair [A, B] means task A must be completed before task B. Determine whether it is possible to schedule all tasks — i.e., whether the dependency graph is free of cycles.

### Constraints
- 1 <= tasks <= 1000
- prerequisites is a list of directed pairs; may be empty
- If a cycle exists among prerequisites, scheduling is impossible

### Examples
```
tasks=3, [[0,1],[1,2]]                           →  true    (order: [0, 1, 2])
tasks=3, [[0,1],[1,2],[2,0]]                     →  false   (cyclic dependency)
tasks=6, [[2,5],[0,5],[0,4],[1,4],[3,2],[1,3]]   →  true    (order: [0,1,4,3,2,5])
```

### Next solve approach
1. Brute Force first — DFS with visited/recursion-stack coloring to detect cycles
2. Optimized (Topological Sort / Kahn's BFS) — count in-degrees; if processed node count equals tasks → no cycle → true

---

### Java

```java
import java.util.*;

class TaskScheduling {

    // TODO: implement
    public static boolean isSchedulingPossible(int tasks, int[][] prerequisites) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        System.out.println("Tasks execution possible: " +
            TaskScheduling.isSchedulingPossible(3, new int[][] {
                new int[] { 0, 1 }, new int[] { 1, 2 }
            })); // expected: true

        System.out.println("Tasks execution possible: " +
            TaskScheduling.isSchedulingPossible(3, new int[][] {
                new int[] { 0, 1 }, new int[] { 1, 2 }, new int[] { 2, 0 }
            })); // expected: false

        System.out.println("Tasks execution possible: " +
            TaskScheduling.isSchedulingPossible(6, new int[][] {
                new int[] { 2, 5 }, new int[] { 0, 5 },
                new int[] { 0, 4 }, new int[] { 1, 4 },
                new int[] { 3, 2 }, new int[] { 1, 3 }
            })); // expected: true
    }
}
```

### Python

```python
def is_scheduling_possible(tasks: int, prerequisites: list[list[int]]) -> bool:
    # TODO: implement
    pass


print(is_scheduling_possible(3, [[0,1],[1,2]]))                           # expected: True
print(is_scheduling_possible(3, [[0,1],[1,2],[2,0]]))                     # expected: False
print(is_scheduling_possible(6, [[2,5],[0,5],[0,4],[1,4],[3,2],[1,3]]))  # expected: True
```
