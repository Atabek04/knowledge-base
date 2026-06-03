---
difficulty: Medium
status: Not started
topic: [Merge Intervals, Arrays]
tags: [merge-intervals, array, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an array of appointment intervals, determine whether a single person can attend every appointment without any conflict. Two appointments conflict when they overlap — i.e. one starts before the other has ended. Return true only if all appointments are mutually non-overlapping.

### Constraints
- 1 <= intervals.length <= 10^4
- intervals[i].start < intervals[i].end
- Values fit in int range

### Examples
```
[[1,4],[2,5],[7,9]]   →  false   ([1,4] and [2,5] overlap)
[[6,7],[2,4],[8,12]]  →  true    (no overlaps after sorting)
[[4,5],[2,3],[3,6]]   →  false   ([4,5] and [3,6] overlap)
```

### Next solve approach
1. Brute Force first — compare every pair of appointments for overlap O(n²)
2. Optimized (Merge Intervals) — sort by start time, then check each adjacent pair: if next.start < current.end there is a conflict O(n log n)

---

### Java

```java
import java.util.*;

class Interval {
    int start;
    int end;
    public Interval(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

public class Solution {

    // TODO: implement
    public static boolean canAttendAllAppointments(Interval[] intervals) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        System.out.println(canAttendAllAppointments(new Interval[]{
            new Interval(1, 4), new Interval(2, 5), new Interval(7, 9)
        })); // expected: false

        System.out.println(canAttendAllAppointments(new Interval[]{
            new Interval(6, 7), new Interval(2, 4), new Interval(8, 12)
        })); // expected: true

        System.out.println(canAttendAllAppointments(new Interval[]{
            new Interval(4, 5), new Interval(2, 3), new Interval(3, 6)
        })); // expected: false
    }
}
```

### Python

```python
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def can_attend_all_appointments(intervals: list[Interval]) -> bool:
    # TODO: implement
    pass


print(can_attend_all_appointments([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))   # expected: False
print(can_attend_all_appointments([Interval(6, 7), Interval(2, 4), Interval(8, 12)]))  # expected: True
print(can_attend_all_appointments([Interval(4, 5), Interval(2, 3), Interval(3, 6)]))   # expected: False
```
