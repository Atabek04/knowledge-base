---
difficulty: Medium
status: Not started
topic: [Top K Elements, Arrays, Heap]
tags: [top-k-elements, array, heap, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an array of numbers and two indices K1 and K2, find the sum of all elements that fall strictly between the K1th smallest and K2th smallest values in the array. The K1th and K2th elements themselves are not included in the sum.

### Constraints
- 1 <= K1 < K2 <= nums.length
- Array is unsorted; values may be positive or negative
- "Between" means strictly between the two boundary values

### Examples
```
[1, 3, 12, 5, 15, 11], K1=3, K2=6  →  23   (3rd smallest=5, 6th=15; sum of 11+12=23)
[3, 5, 8, 7],           K1=1, K2=4  →  12   (1st smallest=3, 4th=8; sum of 5+7=12)
```

### Next solve approach
1. Brute Force first — sort array, sum elements at indices K1 to K2-2, O(n log n)
2. Optimized (Top K Elements) — use a max-heap of size K2; find the K1th and K2th smallest, then sum everything strictly between them, O(n log K2)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int findSumOfElements(int[] nums, int k1, int k2) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findSumOfElements(new int[]{1, 3, 12, 5, 15, 11}, 3, 6)); // expected: 23
        System.out.println(findSumOfElements(new int[]{3, 5, 8, 7}, 1, 4));           // expected: 12
    }
}
```

### Python

```python
def find_sum_of_elements(nums: list[int], k1: int, k2: int) -> int:
    # TODO: implement
    pass


print(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6))  # expected: 23
print(find_sum_of_elements([3, 5, 8, 7], 1, 4))            # expected: 12
```
