---
difficulty: Easy
status: Not started
topic: [Top K Elements, Arrays, Heap]
tags: [top-k-elements, array, heap, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an array of 2D points and an integer K, return the K points closest to the origin (0, 0) using Euclidean distance. The result does not need to be in any particular order.

### Constraints
- 1 <= K <= points.length
- Distance comparison can use squared distance (avoids sqrt)
- Coordinates can be negative

### Examples
```
[[1,2],[1,3]], K=1         →  [[1,2]]       (sqrt(5) < sqrt(10))
[[1,3],[3,4],[2,-1]], K=2  →  [[1,3],[2,-1]]
```

### Next solve approach
1. Brute Force first — compute all distances, sort, take first K, O(n log n)
2. Optimized (Top K Elements) — max-heap of size K on squared distance; replace when a closer point is found, O(n log K)

---

### Java

```java
import java.util.*;

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int distFromOrigin() {
        // ignoring sqrt
        return (x * x) + (y * y);
    }
}

public class Solution {

    // TODO: implement
    public static List<Point> findClosestPoints(Point[] points, int k) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Point[] points1 = new Point[]{new Point(1, 2), new Point(1, 3)};
        List<Point> result1 = findClosestPoints(points1, 1);
        for (Point p : result1) System.out.print("[" + p.x + ", " + p.y + "] ");
        System.out.println(); // expected: [1, 2]

        Point[] points2 = new Point[]{new Point(1, 3), new Point(3, 4), new Point(2, -1)};
        List<Point> result2 = findClosestPoints(points2, 2);
        for (Point p : result2) System.out.print("[" + p.x + ", " + p.y + "] ");
        System.out.println(); // expected: [1, 3] [2, -1]
    }
}
```

### Python

```python
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_from_origin(self) -> int:
        return self.x * self.x + self.y * self.y


def find_closest_points(points: list[Point], k: int) -> list[Point]:
    # TODO: implement
    pass


result1 = find_closest_points([Point(1, 2), Point(1, 3)], 1)
print([[p.x, p.y] for p in result1])  # expected: [[1, 2]]

result2 = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
print([[p.x, p.y] for p in result2])  # expected: [[1, 3], [2, -1]]
```
