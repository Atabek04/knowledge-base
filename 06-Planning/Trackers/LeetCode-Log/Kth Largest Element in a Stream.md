---
difficulty: Easy
status: Not started
topic: [Heap / Priority Queue]
tags: [tree, design, bst, binary-tree, data-stream, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/kth-largest-element-in-a-stream/"
---

### Problem
Design a class that tracks the kth largest element in a continuously growing stream of scores. It is initialized with k and an initial list of numbers. Each time a new score is added via add(), the method returns the current kth largest value across all scores seen so far.

### Constraints
- 0 <= nums.length <= 10^4
- 1 <= k <= nums.length + 1
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- At most 10^4 calls to add

### Examples
```
KthLargest(3, [4,5,8,2]), then add: 3,5,10,9,4
→  [null, 4, 5, 5, 8, 8]

KthLargest(4, [7,7,7,7,8,3]), then add: 2,10,9,9
→  [null, 7, 7, 7, 8]
```

### Next solve approach
1. Brute Force first — keep a sorted list, insert new value, return element at index size-k
2. Optimized — maintain a min-heap of exactly size k; heap.peek() is always the kth largest

---

### Java

```java
public class Solution {

    static class KthLargest {

        // TODO: implement
        public KthLargest(int k, int[] nums) {
            // TODO
        }

        public int add(int val) {
            // TODO
            return 0;
        }
    }

    public static void main(String[] args) {
        KthLargest kl1 = new KthLargest(3, new int[]{4, 5, 8, 2});
        System.out.println(kl1.add(3));  // expected: 4
        System.out.println(kl1.add(5));  // expected: 5
        System.out.println(kl1.add(10)); // expected: 5
        System.out.println(kl1.add(9));  // expected: 8
        System.out.println(kl1.add(4));  // expected: 8

        KthLargest kl2 = new KthLargest(4, new int[]{7, 7, 7, 7, 8, 3});
        System.out.println(kl2.add(2));  // expected: 7
        System.out.println(kl2.add(10)); // expected: 7
        System.out.println(kl2.add(9));  // expected: 7
        System.out.println(kl2.add(9));  // expected: 8
    }
}
```

### Python

```python
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # TODO: implement
        pass

    def add(self, val: int) -> int:
        # TODO
        pass


kl1 = KthLargest(3, [4, 5, 8, 2])
print(kl1.add(3))   # expected: 4
print(kl1.add(5))   # expected: 5
print(kl1.add(10))  # expected: 5
print(kl1.add(9))   # expected: 8
print(kl1.add(4))   # expected: 8
```
