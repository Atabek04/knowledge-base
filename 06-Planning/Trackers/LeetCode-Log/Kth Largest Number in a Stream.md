---
difficulty: Medium
status: Not started
topic: [Top K Elements, Heap]
tags: [top-k-elements, heap, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Design a class that tracks a stream of numbers and can efficiently report the Kth largest number at any point. The constructor receives an initial array of numbers and K. The `add` method inserts a new number into the stream and immediately returns the current Kth largest.

### Constraints
- K >= 1 and at least K numbers will be present before any add call
- Numbers can be any integer (positive or negative)
- Each add call must return the Kth largest after inserting the new number

### Examples
```
Initial: [3, 1, 5, 12, 2, 11], K=4
add(6)   →  5    (sorted desc: [12,11,6,5,3,2,1]; 4th is 5)
add(13)  →  6    (sorted desc: [13,12,11,6,5,3,2,1]; 4th is 6)
add(4)   →  6    (4th is still 6)
```

### Next solve approach
1. Brute Force first — keep a sorted list, insert in order, read index K-1 from end, O(n) per add
2. Optimized (Top K Elements) — maintain a min-heap of size K; the root is always the Kth largest; add inserts and pops excess, O(log K) per add

---

### Java

```java
import java.util.*;

public class Solution {

    static class KthLargestNumberInStream {

        // TODO: implement
        public KthLargestNumberInStream(int[] nums, int k) {
            // TODO
        }

        public int add(int num) {
            // TODO
            return 0;
        }
    }

    public static void main(String[] args) {
        int[] input = new int[]{3, 1, 5, 12, 2, 11};
        KthLargestNumberInStream kthLargest = new KthLargestNumberInStream(input, 4);
        System.out.println(kthLargest.add(6));  // expected: 5
        System.out.println(kthLargest.add(13)); // expected: 6
        System.out.println(kthLargest.add(4));  // expected: 6
    }
}
```

### Python

```python
class KthLargestNumberInStream:
    def __init__(self, nums: list[int], k: int):
        # TODO: implement
        pass

    def add(self, num: int) -> int:
        # TODO: implement
        pass


stream = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
print(stream.add(6))   # expected: 5
print(stream.add(13))  # expected: 6
print(stream.add(4))   # expected: 6
```
