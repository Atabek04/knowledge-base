---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [dfs, bfs, graph, topological-sort, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/course-schedule/"
---

### Problem
There are numCourses courses labeled 0 to numCourses - 1. You are given a list of prerequisite pairs where [a, b] means you must take course b before course a. Return true if it is possible to finish all courses, and false if the prerequisites form a cycle that makes completion impossible.

### Constraints
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All pairs prerequisites[i] are unique

### Examples
```
numCourses = 2, prerequisites = [[1,0]]          →  true    (take 0 then 1)
numCourses = 2, prerequisites = [[1,0],[0,1]]    →  false   (cycle: 0 requires 1, 1 requires 0)
```

### Next solve approach
1. Brute Force first — DFS with a visited/in-cycle state array to detect cycles in the dependency graph
2. Optimized — Kahn's algorithm (BFS topological sort): track in-degrees, process zero-in-degree nodes, check if all nodes were processed

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.canFinish(2, new int[][]{{1,0}}));          // expected: true
        System.out.println(sol.canFinish(2, new int[][]{{1,0},{0,1}}));    // expected: false
    }
}
```

### Python

```python
def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    # TODO: implement
    pass


print(can_finish(2, [[1,0]]))         # expected: True
print(can_finish(2, [[1,0],[0,1]]))   # expected: False
```
