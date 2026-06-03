---
difficulty: Medium
status: Not started
topic: [Two Heaps, Heap, Design]
tags: [two-heaps, heap, design, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Design a class that can continuously accept integers one at a time and report the median of all numbers seen so far at any point. If the total count of numbers is even, the median is the average of the two middle values. If odd, the median is the exact middle value.

### Constraints
- Numbers can be any integer (positive, negative, or zero)
- findMedian() is always called after at least one insertNum()
- Input fits in memory

### Examples
```
insertNum(3), insertNum(1), findMedian()  →  2.0   (middle of [1, 3])
insertNum(5), findMedian()               →  3.0   (middle of [1, 3, 5])
insertNum(4), findMedian()               →  3.5   (average of 3 and 4 from [1, 3, 4, 5])
```

### Next solve approach
1. Brute Force first — keep a sorted list, return middle element(s), O(n log n) per insert
2. Optimized (Two Heaps) — max-heap for lower half, min-heap for upper half; balance after each insert to keep sizes equal or off by one

---

### Java

```java
import java.util.*;

class MedianOfAStream {

    public void insertNum(int num) {
        // TODO: Write your code here
    }

    public double findMedian() {
        // TODO: Write your code here
        return -1;
    }

    public static void main(String[] args) {
        MedianOfAStream medianOfAStream = new MedianOfAStream();
        medianOfAStream.insertNum(3);
        medianOfAStream.insertNum(1);
        System.out.println("The median is: " + medianOfAStream.findMedian()); // expected: 2.0
        medianOfAStream.insertNum(5);
        System.out.println("The median is: " + medianOfAStream.findMedian()); // expected: 3.0
        medianOfAStream.insertNum(4);
        System.out.println("The median is: " + medianOfAStream.findMedian()); // expected: 3.5
    }
}
```

### Python

```python
class MedianOfAStream:
    def insert_num(self, num: int) -> None:
        # TODO: implement
        pass

    def find_median(self) -> float:
        # TODO: implement
        pass


stream = MedianOfAStream()
stream.insert_num(3)
stream.insert_num(1)
print(stream.find_median())  # expected: 2.0
stream.insert_num(5)
print(stream.find_median())  # expected: 3.0
stream.insert_num(4)
print(stream.find_median())  # expected: 3.5
```
