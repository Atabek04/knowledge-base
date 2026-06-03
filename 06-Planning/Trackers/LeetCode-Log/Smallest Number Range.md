---
difficulty: Hard
status: Not started
topic: [K-way Merge, Arrays, Heap]
tags: [k-way-merge, array, heap, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given M sorted arrays, find the smallest range [lo, hi] such that the range contains at least one number from each array. "Smallest" means the shortest span (hi - lo); when two ranges have equal length, prefer the one with the smaller lo.

### Constraints
- 1 <= M <= number of lists
- Each list is sorted in ascending order and non-empty
- Values are integers

### Examples
```
L1=[1,5,8], L2=[4,12], L3=[7,8,10]  →  [4,7]    (covers 5 from L1, 4 from L2, 7 from L3)
L1=[1,9],   L2=[4,12], L3=[7,10,16] →  [9,12]   (covers 9 from L1, 12 from L2, 10 from L3)
```

### Next solve approach
1. Brute Force first — try all combinations of one element per list, compute range for each, track minimum, O(N^M)
2. Optimized (K-way Merge) — use a min-heap with one entry per list; track the current global max; range = [heap-min, current-max]; advance the list that contributed the min to shrink the window greedily, O(N log M)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int[] findSmallestRange(List<Integer[]> lists) {
        // TODO
        return new int[]{-1, -1};
    }

    public static void main(String[] args) {
        Integer[] l1 = new Integer[]{1, 5, 8};
        Integer[] l2 = new Integer[]{4, 12};
        Integer[] l3 = new Integer[]{7, 8, 10};
        List<Integer[]> lists = new ArrayList<>();
        lists.add(l1);
        lists.add(l2);
        lists.add(l3);
        System.out.println(Arrays.toString(findSmallestRange(lists))); // expected: [4, 7]

        Integer[] l4 = new Integer[]{1, 9};
        Integer[] l5 = new Integer[]{4, 12};
        Integer[] l6 = new Integer[]{7, 10, 16};
        List<Integer[]> lists2 = new ArrayList<>();
        lists2.add(l4);
        lists2.add(l5);
        lists2.add(l6);
        System.out.println(Arrays.toString(findSmallestRange(lists2))); // expected: [9, 12]
    }
}
```

### Python

```python
def find_smallest_range(lists: list[list[int]]) -> list[int]:
    # TODO: implement
    pass


print(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]]))   # expected: [4, 7]
print(find_smallest_range([[1, 9], [4, 12], [7, 10, 16]]))      # expected: [9, 12]
```
