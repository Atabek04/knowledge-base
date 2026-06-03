---
difficulty: Hard
status: Not started
topic: [Two Heaps, Heap, Sliding Window]
tags: [two-heaps, heap, sliding-window, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an array of numbers and a window size k, slide a window of size k across the array one step at a time and compute the median of the elements inside the window at each position. Return all window medians as an array. If k is even, the median is the average of the two middle elements.

### Constraints
- 1 <= k <= nums.length
- nums can contain negative numbers
- Input fits in memory

### Examples
```
nums=[1, 2, -1, 3, 5], k=2  →  [1.5, 0.5, 1.0, 4.0]   (windows: [1,2], [2,-1], [-1,3], [3,5])
nums=[1, 2, -1, 3, 5], k=3  →  [1.0, 2.0, 3.0]          (windows: [1,2,-1], [2,-1,3], [-1,3,5])
```

### Next solve approach
1. Brute Force first — sort each window of size k, pick middle, O(n * k log k)
2. Optimized (Two Heaps) — maintain a max-heap (lower half) and min-heap (upper half); slide window by removing outgoing element and adding incoming, rebalance heaps each step

---

### Java

```java
import java.util.*;

class SlidingWindowMedian {

    public double[] findSlidingWindowMedian(int[] nums, int k) {
        double[] result = new double[nums.length - k + 1];
        // TODO: Write your code here
        return result;
    }

    public static void main(String[] args) {
        SlidingWindowMedian slidingWindowMedian = new SlidingWindowMedian();
        double[] result = slidingWindowMedian.findSlidingWindowMedian(new int[]{1, 2, -1, 3, 5}, 2);
        System.out.print("Sliding window medians are: ");
        for (double num : result) System.out.print(num + " "); // expected: 1.5 0.5 1.0 4.0
        System.out.println();

        slidingWindowMedian = new SlidingWindowMedian();
        result = slidingWindowMedian.findSlidingWindowMedian(new int[]{1, 2, -1, 3, 5}, 3);
        System.out.print("Sliding window medians are: ");
        for (double num : result) System.out.print(num + " "); // expected: 1.0 2.0 3.0
    }
}
```

### Python

```python
def find_sliding_window_median(nums: list[int], k: int) -> list[float]:
    # TODO: implement
    pass


result = find_sliding_window_median([1, 2, -1, 3, 5], 2)
print(result)  # expected: [1.5, 0.5, 1.0, 4.0]

result = find_sliding_window_median([1, 2, -1, 3, 5], 3)
print(result)  # expected: [1.0, 2.0, 3.0]
```
