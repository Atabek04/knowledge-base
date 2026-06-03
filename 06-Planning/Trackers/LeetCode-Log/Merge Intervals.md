---
difficulty: Medium
status: Not started
topic: [Merge Intervals, Arrays]
tags: [merge-intervals, array, grokking-patterns, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/merge-intervals/"
---

### Problem
Given a list of intervals, merge all overlapping intervals and return a new list where every remaining interval is mutually exclusive. Two intervals overlap when the second one starts before the first one ends. The result should cover the same total range but with no redundant overlap.

### Constraints
- 1 <= intervals.length <= 10^4
- intervals[i].start <= intervals[i].end
- Values fit in int range

### Examples
```
[[1,4],[2,5],[7,9]]  →  [[1,5],[7,9]]   ([1,4] and [2,5] overlap → merged to [1,5])
[[6,7],[2,4],[5,9]]  →  [[2,4],[5,9]]   ([6,7] and [5,9] overlap → merged to [5,9])
[[1,4],[2,6],[3,5]]  →  [[1,6]]         (all three overlap → one merged interval)
```

### Next solve approach
1. Brute Force first — compare every pair O(n²), merge on overlap, repeat until no merges happen
2. Optimized (Merge Intervals) — sort by start time, walk linearly and extend current interval's end whenever next.start <= current.end

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
    public static List<Interval> merge(List<Interval> intervals) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        List<Interval> input = new ArrayList<>();
        input.add(new Interval(1, 4));
        input.add(new Interval(2, 5));
        input.add(new Interval(7, 9));
        System.out.println(merge(input)); // expected: [[1,5],[7,9]]

        input = new ArrayList<>();
        input.add(new Interval(6, 7));
        input.add(new Interval(2, 4));
        input.add(new Interval(5, 9));
        System.out.println(merge(input)); // expected: [[2,4],[5,9]]

        input = new ArrayList<>();
        input.add(new Interval(1, 4));
        input.add(new Interval(2, 6));
        input.add(new Interval(3, 5));
        System.out.println(merge(input)); // expected: [[1,6]]
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


def merge(intervals: list[Interval]) -> list[Interval]:
    # TODO: implement
    pass


print(merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]))  # expected: [[1,5],[7,9]]
print(merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]))  # expected: [[2,4],[5,9]]
print(merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]))  # expected: [[1,6]]
```
