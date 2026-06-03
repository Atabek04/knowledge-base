---
difficulty: Easy
status: Not started
topic: [Intervals]
tags: [array, sorting, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/meeting-rooms/"
---

### Problem
Given a list of meeting time intervals, determine whether a single person can attend all of them without any conflicts. A person cannot be in two places at once, so any pair of overlapping meetings makes it impossible.

### Constraints
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i < end_i <= 10^6

### Examples
```
[[0,30],[5,10],[15,20]]  →  false     ([0,30] overlaps with [5,10])
[[7,10],[2,4]]           →  true      (no overlap after sorting)
```

### Next solve approach
1. Brute Force first — compare every pair of meetings for overlap, O(n²)
2. Optimized — sort by start time, then check if each meeting starts before the previous ends

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean canAttendMeetings(int[][] intervals) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] intervals1 = {{0, 30}, {5, 10}, {15, 20}};
        System.out.println(sol.canAttendMeetings(intervals1)); // expected: false

        int[][] intervals2 = {{7, 10}, {2, 4}};
        System.out.println(sol.canAttendMeetings(intervals2)); // expected: true
    }
}
```

### Python

```python
def can_attend_meetings(intervals: list[list[int]]) -> bool:
    # TODO: implement
    pass


print(can_attend_meetings([[0, 30], [5, 10], [15, 20]]))  # expected: False
print(can_attend_meetings([[7, 10], [2, 4]]))              # expected: True
```
