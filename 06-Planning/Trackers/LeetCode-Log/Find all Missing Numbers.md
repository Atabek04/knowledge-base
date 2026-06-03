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
Given an unsorted array of n numbers where each value is in the range 1 to n, some numbers appear more than once while others are absent. Find and return all missing numbers. Duplicates consume index slots that should belong to the missing values.

### Constraints
- Array length n >= 1
- Each element is in range [1, n]
- Duplicates are allowed; multiple numbers may be missing

### Examples
```
[2, 3, 1, 8, 2, 3, 5, 1]  →  [4, 6, 7]   (duplicates push out 4, 6, and 7)
[2, 4, 1, 2]               →  [3]
[2, 3, 2, 1]               →  [4]
```

### Next solve approach
1. Brute Force first — use a frequency array of size n+1, collect indices with count 0, O(n) time but O(n) space
2. Optimized (Cyclic Sort) — place each number at index nums[i]-1 (skip if already correct), then collect all indices where nums[i] != i+1

---

### Java

```java
import java.util.ArrayList;
import java.util.List;

public class Solution {

    // TODO: implement
    public static List<Integer> findNumbers(int[] nums) {
        List<Integer> missingNumbers = new ArrayList<>();
        // TODO
        return missingNumbers;
    }

    public static void main(String[] args) {
        System.out.println(findNumbers(new int[]{2, 3, 1, 8, 2, 3, 5, 1})); // expected: [4, 6, 7]
        System.out.println(findNumbers(new int[]{2, 4, 1, 2}));              // expected: [3]
        System.out.println(findNumbers(new int[]{2, 3, 2, 1}));              // expected: [4]
    }
}
```

### Python

```python
def find_numbers(nums: list[int]) -> list[int]:
    # TODO: implement
    pass


print(find_numbers([2, 3, 1, 8, 2, 3, 5, 1]))  # expected: [4, 6, 7]
print(find_numbers([2, 4, 1, 2]))               # expected: [3]
print(find_numbers([2, 3, 2, 1]))               # expected: [4]
```
