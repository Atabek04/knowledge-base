---
difficulty: Easy
status: Not started
topic: [Cyclic Sort, Arrays]
tags: [cyclic-sort, array, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an unsorted array of n integers where each value is in the range 1 to n, some numbers appear twice while others appear once. Find all duplicated numbers without using any extra space and return them in any order.

### Constraints
- Array length n >= 1
- Values are in range [1, n]
- Each number appears at most twice
- No extra space allowed

### Examples
```
[3, 4, 4, 5, 5]        →  [4, 5]
[5, 4, 7, 2, 3, 5, 3]  →  [3, 5]
```

### Next solve approach
1. Brute Force first — use a hash set to track seen numbers, collect on second visit, O(n) time but O(n) space
2. Optimized (Cyclic Sort) — place each number at index nums[i]-1; after the sort pass, any index where nums[i] != i+1 means that number appeared twice (it displaced the rightful occupant)

---

### Java

```java
import java.util.ArrayList;
import java.util.List;

public class Solution {

    // TODO: implement
    public static List<Integer> findNumbers(int[] nums) {
        List<Integer> duplicateNumbers = new ArrayList<>();
        // TODO
        return duplicateNumbers;
    }

    public static void main(String[] args) {
        System.out.println(findNumbers(new int[]{3, 4, 4, 5, 5}));       // expected: [4, 5]
        System.out.println(findNumbers(new int[]{5, 4, 7, 2, 3, 5, 3})); // expected: [3, 5]
    }
}
```

### Python

```python
def find_numbers(nums: list[int]) -> list[int]:
    # TODO: implement
    pass


print(find_numbers([3, 4, 4, 5, 5]))        # expected: [4, 5]
print(find_numbers([5, 4, 7, 2, 3, 5, 3]))  # expected: [3, 5]
```
