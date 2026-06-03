---
difficulty: Medium
status: Not started
topic: [K-way Merge, Arrays, Heap]
tags: [k-way-merge, array, heap, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given M sorted arrays, find the K-th smallest number across all elements combined. You do not need to fully merge them — just identify which value would appear at position K in the merged sorted sequence.

### Constraints
- 1 <= K <= total number of elements across all lists
- Each list is sorted in ascending order
- All values are integers

### Examples
```
L1=[2,6,8], L2=[3,6,7], L3=[1,3,4], K=5  →  4   (merged: [1,2,3,3,4,6,6,7,8], 5th = 4)
L1=[5,8,9], L2=[1,7],               K=3  →  7   (merged: [1,5,7,8,9], 3rd = 7)
```

### Next solve approach
1. Brute Force first — merge all lists into one array, sort it, return element at index K-1, O(N log N)
2. Optimized (K-way Merge) — push the first element of each list into a min-heap; pop K times, each time pushing the next element from the same list, O(K log M)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int findKthSmallest(List<Integer[]> lists, int k) {
        // TODO
        return -1;
    }

    public static void main(String[] args) {
        Integer[] l1 = new Integer[]{2, 6, 8};
        Integer[] l2 = new Integer[]{3, 6, 7};
        Integer[] l3 = new Integer[]{1, 3, 4};
        List<Integer[]> lists = new ArrayList<>();
        lists.add(l1);
        lists.add(l2);
        lists.add(l3);
        System.out.println(findKthSmallest(lists, 5)); // expected: 4

        Integer[] l4 = new Integer[]{5, 8, 9};
        Integer[] l5 = new Integer[]{1, 7};
        List<Integer[]> lists2 = new ArrayList<>();
        lists2.add(l4);
        lists2.add(l5);
        System.out.println(findKthSmallest(lists2, 3)); // expected: 7
    }
}
```

### Python

```python
def find_kth_smallest(lists: list[list[int]], k: int) -> int:
    # TODO: implement
    pass


print(find_kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5))  # expected: 4
print(find_kth_smallest([[5, 8, 9], [1, 7]], 3))                  # expected: 7
```
