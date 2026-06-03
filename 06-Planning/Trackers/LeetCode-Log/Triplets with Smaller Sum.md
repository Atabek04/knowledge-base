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
Given an unsorted array and a target value, count how many triplets (using three distinct indices i, j, k) satisfy arr[i] + arr[j] + arr[k] < target. The same three indices in different order do not count as separate triplets.

### Constraints
- Array is unsorted and may contain negative numbers
- Triplets use three distinct indices
- 0 <= arr.length <= 3000
- Values fit in int range

### Examples
```
[-1, 0, 2, 3],    target=3  →  2   (triplets: [-1,0,3], [-1,0,2])
[-1, 4, 2, 1, 3], target=5  →  4   (triplets: [-1,1,4], [-1,1,3], [-1,1,2], [-1,2,3])
```

### Next solve approach
1. Brute Force first — three nested loops counting valid triplets, O(n³)
2. Optimized (Two Pointers) — sort array, fix one element, use two pointers: when sum < target all pairs between left and right are valid, add (right - left) to count, O(n²)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int searchTriplets(int[] arr, int target) {
        int count = -1;
        // TODO
        return count;
    }

    public static void main(String[] args) {
        System.out.println(searchTriplets(new int[]{-1, 0, 2, 3}, 3));       // expected: 2
        System.out.println(searchTriplets(new int[]{-1, 4, 2, 1, 3}, 5));    // expected: 4
    }
}
```

### Python

```python
def search_triplets(arr: list[int], target: int) -> int:
    # TODO: implement
    pass


print(search_triplets([-1, 0, 2, 3], 3))      # expected: 2
print(search_triplets([-1, 4, 2, 1, 3], 5))   # expected: 4
```
