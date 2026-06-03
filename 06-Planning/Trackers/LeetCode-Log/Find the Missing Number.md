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
Given an array of n distinct integers drawn from the range 0 to n, find the single number that is missing. The array holds n elements but the full range has n+1 values, so exactly one is absent.

### Constraints
- Array length n >= 1
- All elements are distinct
- Elements are taken from the range [0, n]

### Examples
```
[4, 0, 3, 1]              →  2
[8, 3, 5, 2, 4, 6, 0, 1]  →  7
```

### Next solve approach
1. Brute Force first — sort the array then scan for the gap, O(n log n)
2. Optimized (Cyclic Sort) — place each number at index nums[i] (skip n since there is no slot for it), then return the first index where nums[i] != i; if all match, the missing number is n

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int findMissingNumber(int[] nums) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findMissingNumber(new int[]{4, 0, 3, 1}));              // expected: 2
        System.out.println(findMissingNumber(new int[]{8, 3, 5, 2, 4, 6, 0, 1})); // expected: 7
    }
}
```

### Python

```python
def find_missing_number(nums: list[int]) -> int:
    # TODO: implement
    pass


print(find_missing_number([4, 0, 3, 1]))               # expected: 2
print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))  # expected: 7
```
