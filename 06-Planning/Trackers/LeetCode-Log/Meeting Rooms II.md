---
difficulty: Medium
status: Not started
topic: [Intervals]
tags: [greedy, array, two-pointers, prefix-sum, sorting, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/meeting-rooms-ii/"
---

### Problem
Given a list of meeting time intervals, find the minimum number of conference rooms needed to hold all meetings simultaneously. Two meetings that overlap in time require separate rooms. The answer is the peak number of concurrent meetings at any point in time.

### Constraints
- 1 <= intervals.length <= 10^4
- 0 <= start_i < end_i <= 10^6

### Examples
```
[[0,30],[5,10],[15,20]]  →  2     (meetings at [0,30] and [5,10] overlap)
[[7,10],[2,4]]           →  1     (no overlap)
```

### Next solve approach
1. Brute Force first — check every pair of meetings for overlaps, track max simultaneous
2. Optimized — difference array (or min-heap): increment at start, decrement at end, find prefix sum peak

---

### Java

```java
public class Solution {

    // TODO: implement
    public int minMeetingRooms(int[][] intervals) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] intervals1 = {{0, 30}, {5, 10}, {15, 20}};
        System.out.println(sol.minMeetingRooms(intervals1)); // expected: 2

        int[][] intervals2 = {{7, 10}, {2, 4}};
        System.out.println(sol.minMeetingRooms(intervals2)); // expected: 1
    }
}
```

### Python

```python
def min_meeting_rooms(intervals: list[list[int]]) -> int:
    # TODO: implement
    pass


print(min_meeting_rooms([[0, 30], [5, 10], [15, 20]]))  # expected: 2
print(min_meeting_rooms([[7, 10], [2, 4]]))              # expected: 1
```
