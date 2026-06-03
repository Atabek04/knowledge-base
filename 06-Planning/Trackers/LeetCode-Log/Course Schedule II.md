---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [dfs, bfs, graph, topological-sort, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/course-schedule-ii/"
---

### Problem
There are numCourses courses labeled 0 to numCourses - 1 with prerequisite pairs where [a, b] means b must come before a. Return any valid ordering of all courses to finish them all, or an empty array if a cycle makes it impossible.

### Constraints
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- All pairs [ai, bi] are distinct

### Examples
```
numCourses = 2, prerequisites = [[1,0]]                      →  [0,1]
numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]    →  [0,2,1,3]   (or [0,1,2,3])
numCourses = 1, prerequisites = []                           →  [0]
```

### Next solve approach
1. Brute Force first — DFS with cycle detection; collect nodes in post-order (reversed topological sort)
2. Optimized — Kahn's BFS: track in-degrees, process zero-in-degree nodes into result list, return empty if count < numCourses

---

### Java

```java
public class Solution {

    // TODO: implement
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(java.util.Arrays.toString(
            sol.findOrder(2, new int[][]{{1,0}})
        )); // expected: [0, 1]

        System.out.println(java.util.Arrays.toString(
            sol.findOrder(4, new int[][]{{1,0},{2,0},{3,1},{3,2}})
        )); // expected: [0, 1, 2, 3] or [0, 2, 1, 3]

        System.out.println(java.util.Arrays.toString(
            sol.findOrder(1, new int[][]{})
        )); // expected: [0]
    }
}
```

### Python

```python
def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    # TODO: implement
    pass


print(find_order(2, [[1,0]]))                       # expected: [0, 1]
print(find_order(4, [[1,0],[2,0],[3,1],[3,2]]))     # expected: [0, 1, 2, 3] or similar
print(find_order(1, []))                            # expected: [0]
```
