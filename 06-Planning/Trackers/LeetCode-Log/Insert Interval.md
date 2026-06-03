---
difficulty: Medium
status: Not started
topic: [Merge Intervals, Arrays]
tags: [merge-intervals, array, grokking-patterns, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/insert-interval/"
---

### Problem
Given a sorted list of non-overlapping intervals and a new interval to insert, place the new interval in the correct position and merge any intervals that now overlap with it. The final list must again be sorted and fully non-overlapping.

### Constraints
- 0 <= intervals.length <= 10^4
- intervals is sorted by start time and non-overlapping before insertion
- newInterval.start <= newInterval.end
- Values fit in int range

### Examples
```
intervals=[[1,3],[5,7],[8,12]], newInterval=[4,6]   →  [[1,3],[4,7],[8,12]]   ([4,6] overlaps [5,7] → [4,7])
intervals=[[1,3],[5,7],[8,12]], newInterval=[4,10]  →  [[1,3],[4,12]]         ([4,10] overlaps [5,7] and [8,12] → [4,12])
intervals=[[2,3],[5,7]],        newInterval=[1,4]   →  [[1,4],[5,7]]          ([1,4] overlaps [2,3] → [1,4])
```

### Next solve approach
1. Brute Force first — insert new interval, then re-run the full merge-intervals scan O(n log n)
2. Optimized (Merge Intervals) — skip intervals ending before new one, merge overlapping ones greedily, then append the rest in one pass O(n)

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
    public static List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        List<Interval> input = new ArrayList<>();
        input.add(new Interval(1, 3));
        input.add(new Interval(5, 7));
        input.add(new Interval(8, 12));
        System.out.println(insert(input, new Interval(4, 6))); // expected: [[1,3],[4,7],[8,12]]

        input = new ArrayList<>();
        input.add(new Interval(1, 3));
        input.add(new Interval(5, 7));
        input.add(new Interval(8, 12));
        System.out.println(insert(input, new Interval(4, 10))); // expected: [[1,3],[4,12]]

        input = new ArrayList<>();
        input.add(new Interval(2, 3));
        input.add(new Interval(5, 7));
        System.out.println(insert(input, new Interval(1, 4))); // expected: [[1,4],[5,7]]
    }
}
```

### Python

```python
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start},{self.end}]"


def insert(intervals: list[Interval], new_interval: Interval) -> list[Interval]:
    # TODO: implement
    pass


print(insert([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 6)))   # expected: [[1,3],[4,7],[8,12]]
print(insert([Interval(1, 3), Interval(5, 7), Interval(8, 12)], Interval(4, 10)))  # expected: [[1,3],[4,12]]
print(insert([Interval(2, 3), Interval(5, 7)], Interval(1, 4)))                    # expected: [[1,4],[5,7]]
```
