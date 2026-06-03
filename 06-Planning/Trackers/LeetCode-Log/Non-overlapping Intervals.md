---
difficulty: Medium
status: Not started
topic: [Intervals]
tags: [greedy, array, dynamic-programming, sorting, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/non-overlapping-intervals/"
---

### Problem
Given a list of intervals, return the minimum number of intervals to remove so that the remaining intervals have no overlaps. Two intervals that only touch at a single point (e.g. [1,2] and [2,3]) are considered non-overlapping and do not need to be separated.

### Constraints
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= start_i < end_i <= 5 * 10^4

### Examples
```
[[1,2],[2,3],[3,4],[1,3]]  →  1     ([1,3] removed, rest are non-overlapping)
[[1,2],[1,2],[1,2]]        →  2     (two duplicates removed)
[[1,2],[2,3]]              →  0     (already non-overlapping)
```

### Next solve approach
1. Brute Force first — try all subsets of removed intervals, check remaining for overlaps
2. Optimized — greedy: sort by end time, keep intervals with earliest end, count skipped overlaps

---

### Java

```java
public class Solution {

    // TODO: implement
    public int eraseOverlapIntervals(int[][] intervals) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] intervals1 = {{1, 2}, {2, 3}, {3, 4}, {1, 3}};
        System.out.println(sol.eraseOverlapIntervals(intervals1)); // expected: 1

        int[][] intervals2 = {{1, 2}, {1, 2}, {1, 2}};
        System.out.println(sol.eraseOverlapIntervals(intervals2)); // expected: 2

        int[][] intervals3 = {{1, 2}, {2, 3}};
        System.out.println(sol.eraseOverlapIntervals(intervals3)); // expected: 0
    }
}
```

### Python

```python
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    # TODO: implement
    pass


print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # expected: 1
print(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]))           # expected: 2
print(erase_overlap_intervals([[1, 2], [2, 3]]))                   # expected: 0
```
