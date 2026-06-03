---
difficulty: Medium
status: Not started
topic: [Two Pointers, Arrays, Sliding Window]
tags: [two-pointers, array, sliding-window, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an array of positive numbers and a target, find all contiguous subarrays whose product of elements is strictly less than the target. Return a list of all such subarrays. A single element counts as a subarray.

### Constraints
- All numbers are positive integers
- 1 <= arr.length <= 10^4
- 1 <= target <= 10^6
- Each element >= 1

### Examples
```
[2, 5, 3, 10], target=30  →  [2],[5],[2,5],[3],[5,3],[10]           (6 subarrays)
[8, 2, 6, 5],  target=50  →  [8],[2],[8,2],[6],[2,6],[5],[6,5]      (7 subarrays)
```

### Next solve approach
1. Brute Force first — enumerate all subarrays with two loops, compute product each time, O(n³)
2. Optimized (Two Pointers / Sliding Window) — expand right pointer, shrink left when product >= target, add all subarrays ending at right, O(n²) output due to result size

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static List<List<Integer>> findSubarrays(int[] arr, int target) {
        List<List<Integer>> subarrays = new ArrayList<>();
        // TODO
        return subarrays;
    }

    public static void main(String[] args) {
        System.out.println(findSubarrays(new int[]{2, 5, 3, 10}, 30));  // expected: [[2],[5],[2,5],[3],[5,3],[10]]
        System.out.println(findSubarrays(new int[]{8, 2, 6, 5}, 50));   // expected: [[8],[2],[8,2],[6],[2,6],[5],[6,5]]
    }
}
```

### Python

```python
def find_subarrays(arr: list[int], target: int) -> list[list[int]]:
    # TODO: implement
    pass


print(find_subarrays([2, 5, 3, 10], 30))  # expected: [[2],[5],[2,5],[3],[5,3],[10]]
print(find_subarrays([8, 2, 6, 5], 50))   # expected: [[8],[2],[8,2],[6],[2,6],[5],[6,5]]
```
