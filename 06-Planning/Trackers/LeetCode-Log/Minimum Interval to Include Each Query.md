---
difficulty: Hard
status: Not started
topic: [Intervals]
tags: [array, binary-search, sorting, sweep-line, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/minimum-interval-to-include-each-query/"
---

### Problem
You are given a list of intervals and a list of query points. For each query, find the size (right - left + 1) of the smallest interval that contains the query point. If no interval covers the query point, return -1 for that query. Return answers in the same order as the original queries.

### Constraints
- 1 <= intervals.length <= 10^5
- 1 <= queries.length <= 10^5
- intervals[i].length == 2
- 1 <= left_i <= right_i <= 10^7
- 1 <= queries[j] <= 10^7

### Examples
```
intervals=[[1,4],[2,4],[3,6],[4,4]], queries=[2,3,4,5]  →  [3,3,1,4]
intervals=[[2,3],[2,5],[1,8],[20,25]], queries=[2,19,5,22]  →  [2,-1,4,6]
```

### Next solve approach
1. Brute Force first — for each query, scan all intervals to find the smallest one containing it, O(n*m)
2. Optimized — sort intervals by left endpoint and queries by value; sweep with a min-heap keyed on interval size, evicting intervals whose right endpoint is past the current query

---

### Java

```java
public class Solution {

    // TODO: implement
    public int[] minInterval(int[][] intervals, int[] queries) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] intervals1 = {{1, 4}, {2, 4}, {3, 6}, {4, 4}};
        int[] queries1 = {2, 3, 4, 5};
        System.out.println(java.util.Arrays.toString(sol.minInterval(intervals1, queries1))); // expected: [3, 3, 1, 4]

        int[][] intervals2 = {{2, 3}, {2, 5}, {1, 8}, {20, 25}};
        int[] queries2 = {2, 19, 5, 22};
        System.out.println(java.util.Arrays.toString(sol.minInterval(intervals2, queries2))); // expected: [2, -1, 4, 6]
    }
}
```

### Python

```python
def min_interval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    # TODO: implement
    pass


print(min_interval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]))     # expected: [3, 3, 1, 4]
print(min_interval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22])) # expected: [2, -1, 4, 6]
```
