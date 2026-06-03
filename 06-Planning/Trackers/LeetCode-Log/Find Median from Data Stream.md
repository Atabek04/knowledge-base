---
difficulty: Hard
status: Not started
topic: [Heap / Priority Queue]
tags: [design, two-pointers, data-stream, sorting, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/find-median-from-data-stream/"
---

### Problem
Design a data structure that supports adding integers from a stream and querying the median at any point. The median is the middle value in a sorted list; for even-length lists it is the average of the two middle values. Both operations must be efficient as the stream grows.

### Constraints
- -10^5 <= num <= 10^5
- At least one element is added before findMedian is called
- At most 5 * 10^4 calls to addNum and findMedian

### Examples
```
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[], [1], [2], [], [3], []]
→  [null, null, null, 1.5, null, 2.0]
```

### Next solve approach
1. Brute Force first — keep a sorted list, insert in O(n), return middle element
2. Optimized — two heaps: max-heap for lower half, min-heap for upper half; balance sizes after each insert

---

### Java

```java
public class Solution {

    static class MedianFinder {

        // TODO: implement
        public MedianFinder() {
            // TODO
        }

        public void addNum(int num) {
            // TODO
        }

        public double findMedian() {
            // TODO
            return 0;
        }
    }

    public static void main(String[] args) {
        MedianFinder mf = new MedianFinder();
        mf.addNum(1);                                        // arr = [1]
        mf.addNum(2);                                        // arr = [1, 2]
        System.out.println(mf.findMedian());                 // expected: 1.5
        mf.addNum(3);                                        // arr = [1, 2, 3]
        System.out.println(mf.findMedian());                 // expected: 2.0
    }
}
```

### Python

```python
class MedianFinder:
    def __init__(self):
        # TODO: implement
        pass

    def add_num(self, num: int) -> None:
        # TODO
        pass

    def find_median(self) -> float:
        # TODO
        pass


mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
print(mf.find_median())  # expected: 1.5
mf.add_num(3)
print(mf.find_median())  # expected: 2.0
```
