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
Given two lists of disjoint intervals each sorted by start time, find all intervals that appear in both lists simultaneously — i.e. their intersection. An intersection exists wherever a segment from the first list and a segment from the second list overlap; the result is the overlapping sub-range.

### Constraints
- 0 <= arr1.length, arr2.length <= 1000
- Each list is sorted by start time and internally non-overlapping
- Values fit in int range

### Examples
```
arr1=[[1,3],[5,6],[7,9]], arr2=[[2,3],[5,7]]  →  [[2,3],[5,6],[7,7]]
arr1=[[1,3],[5,7],[9,12]], arr2=[[5,10]]       →  [[5,7],[9,10]]
```

### Next solve approach
1. Brute Force first — check every pair from arr1 × arr2 for overlap, collect intersections O(n*m)
2. Optimized (Merge Intervals) — two-pointer approach advancing whichever interval ends first, compute intersection per step O(n+m)

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
    public static Interval[] merge(Interval[] arr1, Interval[] arr2) {
        // TODO
        return new Interval[0];
    }

    public static void main(String[] args) {
        Interval[] input1 = new Interval[]{
            new Interval(1, 3), new Interval(5, 6), new Interval(7, 9)
        };
        Interval[] input2 = new Interval[]{
            new Interval(2, 3), new Interval(5, 7)
        };
        System.out.println(Arrays.toString(merge(input1, input2))); // expected: [[2,3],[5,6],[7,7]]

        input1 = new Interval[]{
            new Interval(1, 3), new Interval(5, 7), new Interval(9, 12)
        };
        input2 = new Interval[]{new Interval(5, 10)};
        System.out.println(Arrays.toString(merge(input1, input2))); // expected: [[5,7],[9,10]]
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


def merge(arr1: list[Interval], arr2: list[Interval]) -> list[Interval]:
    # TODO: implement
    pass


print(merge(
    [Interval(1, 3), Interval(5, 6), Interval(7, 9)],
    [Interval(2, 3), Interval(5, 7)]
))  # expected: [[2,3],[5,6],[7,7]]

print(merge(
    [Interval(1, 3), Interval(5, 7), Interval(9, 12)],
    [Interval(5, 10)]
))  # expected: [[5,7],[9,10]]
```
