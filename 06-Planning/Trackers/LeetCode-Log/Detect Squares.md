---
difficulty: Medium
status: Not started
topic: [Math & Geometry]
tags: [design, array, hash-table, counting, data-stream, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/detect-squares/"
---

### Problem
Design a data structure that ingests a stream of 2D points (duplicates allowed) and can efficiently answer queries: given a query point, how many ways can you pick three points from the stored set such that the four points form an axis-aligned square with positive area? Each call to add increments the count for that coordinate, and each call to count iterates over distinct x-values to find matching diagonal corners.

### Constraints
- point.length == 2
- 0 <= x, y <= 1000
- At most 3000 calls in total will be made to add and count

### Examples
```
DetectSquares ds = new DetectSquares()
ds.add([3,10]); ds.add([11,2]); ds.add([3,2])
ds.count([11,10])  →  1
ds.count([14,8])   →  0
ds.add([11,2])
ds.count([11,10])  →  2
```

### Next solve approach
1. Brute Force first — for each query enumerate all point triples and check if they form a square with the query point
2. Optimized — hash map cnt[x][y] → count; for each query fix the diagonal x-coordinate and multiply counts of the four corners

---

### Java

```java
import java.util.HashMap;
import java.util.Map;

public class Solution {

    static class DetectSquares {
        private Map<Integer, Map<Integer, Integer>> cnt = new HashMap<>();

        public DetectSquares() {
            // TODO
        }

        public void add(int[] point) {
            // TODO
        }

        public int count(int[] point) {
            // TODO
            return 0;
        }
    }

    public static void main(String[] args) {
        DetectSquares ds = new DetectSquares();
        ds.add(new int[]{3, 10});   // expected: null
        ds.add(new int[]{11, 2});   // expected: null
        ds.add(new int[]{3, 2});    // expected: null
        System.out.println(ds.count(new int[]{11, 10})); // expected: 1
        System.out.println(ds.count(new int[]{14, 8}));  // expected: 0
        ds.add(new int[]{11, 2});   // expected: null
        System.out.println(ds.count(new int[]{11, 10})); // expected: 2
    }
}
```

### Python

```python
class DetectSquares:
    def __init__(self):
        # TODO: implement
        pass

    def add(self, point: list[int]) -> None:
        # TODO
        pass

    def count(self, point: list[int]) -> int:
        # TODO
        pass


ds = DetectSquares()
ds.add([3, 10])
ds.add([11, 2])
ds.add([3, 2])
print(ds.count([11, 10]))  # expected: 1
print(ds.count([14, 8]))   # expected: 0
ds.add([11, 2])
print(ds.count([11, 10]))  # expected: 2
```
