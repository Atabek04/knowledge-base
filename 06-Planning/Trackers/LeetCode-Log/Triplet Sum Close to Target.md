---
difficulty: Medium
status: Not started
topic: [Two Pointers, Arrays]
tags: [two-pointers, array, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an unsorted array and a target number, find the triplet whose sum is closest to the target. Return that sum. If two triplets are equally close to the target, return the one with the smaller sum.

### Constraints
- Array is unsorted
- Array has at least 3 elements
- -10^4 <= values <= 10^4
- -10^5 <= target <= 10^5

### Examples
```
[-2, 0, 1, 2],  target=2    →  1   (triplet [-2,1,2], sum=1)
[-3, -1, 1, 2], target=1    →  0   (triplet [-3,1,2], sum=0)
[1, 0, 1, 1],   target=100  →  3   (triplet [1,1,1], sum=3)
```

### Next solve approach
1. Brute Force first — three nested loops, track minimum absolute difference, O(n³)
2. Optimized (Two Pointers) — sort array, fix one element, use two pointers to minimize distance to target, O(n²)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int searchTriplet(int[] arr, int targetSum) {
        // TODO
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(searchTriplet(new int[]{-2, 0, 1, 2}, 2));    // expected: 1
        System.out.println(searchTriplet(new int[]{-3, -1, 1, 2}, 1));   // expected: 0
        System.out.println(searchTriplet(new int[]{1, 0, 1, 1}, 100));   // expected: 3
    }
}
```

### Python

```python
def search_triplet(arr: list[int], target_sum: int) -> int:
    # TODO: implement
    pass


print(search_triplet([-2, 0, 1, 2], 2))    # expected: 1
print(search_triplet([-3, -1, 1, 2], 1))   # expected: 0
print(search_triplet([1, 0, 1, 1], 100))   # expected: 3
```
