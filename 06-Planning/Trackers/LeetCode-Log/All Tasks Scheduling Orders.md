---
difficulty: Hard
status: Not started
topic: [Topological Sort, Graphs, Backtracking]
tags: [topological-sort, graph, backtracking, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
You have N tasks labeled 0 to N-1 with prerequisite pairs [A, B] meaning A must finish before B. Print every possible valid task ordering that satisfies all prerequisites. If a cycle exists, print nothing.

### Constraints
- 1 <= tasks <= 10 (combinatorial explosion makes large inputs impractical)
- All prerequisite pairs are directed; graph may or may not be a DAG
- All valid permutations satisfying prerequisites must be printed

### Examples
```
tasks=3, [[0,1],[1,2]]                           →  [0, 1, 2]                         (only one valid order)
tasks=4, [[3,2],[3,0],[2,0],[2,1]]               →  [3,2,0,1]  [3,2,1,0]              (two valid orders)
tasks=6, [[2,5],[0,5],[0,4],[1,4],[3,2],[1,3]]   →  [0,1,4,3,2,5] ... 13 total orders
```

### Next solve approach
1. Brute Force first — generate all permutations, filter those satisfying all prerequisites
2. Optimized (Topological Sort + Backtracking) — maintain in-degree map; at each step try all zero-in-degree nodes, recurse, then undo (backtrack)

---

### Java

```java
import java.util.*;

class AllTaskSchedulingOrders {

    // TODO: implement
    public static void printOrders(int tasks, int[][] prerequisites) {
        // TODO
    }

    public static void main(String[] args) {
        AllTaskSchedulingOrders.printOrders(3, new int[][] {
            new int[] { 0, 1 }, new int[] { 1, 2 }
        }); // expected: [0, 1, 2]
        System.out.println();

        AllTaskSchedulingOrders.printOrders(4, new int[][] {
            new int[] { 3, 2 }, new int[] { 3, 0 },
            new int[] { 2, 0 }, new int[] { 2, 1 }
        }); // expected: [3, 2, 0, 1]  [3, 2, 1, 0]
        System.out.println();

        AllTaskSchedulingOrders.printOrders(6, new int[][] {
            new int[] { 2, 5 }, new int[] { 0, 5 },
            new int[] { 0, 4 }, new int[] { 1, 4 },
            new int[] { 3, 2 }, new int[] { 1, 3 }
        }); // expected: 13 valid orderings e.g. [0, 1, 4, 3, 2, 5]
        System.out.println();
    }
}
```

### Python

```python
def print_orders(tasks: int, prerequisites: list[list[int]]) -> None:
    # TODO: implement
    pass


print_orders(3, [[0,1],[1,2]])
# expected: [0, 1, 2]
print()

print_orders(4, [[3,2],[3,0],[2,0],[2,1]])
# expected: [3, 2, 0, 1]  [3, 2, 1, 0]
print()

print_orders(6, [[2,5],[0,5],[0,4],[1,4],[3,2],[1,3]])
# expected: 13 valid orderings e.g. [0, 1, 4, 3, 2, 5]
print()
```
