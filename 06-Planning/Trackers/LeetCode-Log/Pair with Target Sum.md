---
difficulty: Easy
status: Not started
topic: [Two Pointers, Arrays, Binary Search]
tags: [two-pointers, array, binary-search, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a sorted array of numbers and a target sum, find the pair of elements whose sum equals the target. Return their indices. Since the array is sorted, you can use two pointers starting from both ends to converge on the answer without extra space.

### Constraints
- Array is sorted in ascending order
- Exactly one pair is guaranteed to exist
- 1 <= arr.length <= 10^5
- Values fit in int range

### Examples
```
[1, 2, 3, 4, 6], target=6   →  [1, 3]   (2 + 4 = 6)
[2, 5, 9, 11],   target=11  →  [0, 2]   (2 + 9 = 11)
```

### Next solve approach
1. Brute Force first — nested loop checking all pairs, O(n²)
2. Optimized (Two Pointers) — left and right pointers, move inward based on sum vs target, O(n)

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int[] search(int[] arr, int targetSum) {
        // TODO
        return new int[] { -1, -1 };
    }

    public static void main(String[] args) {
        System.out.println(java.util.Arrays.toString(search(new int[]{1, 2, 3, 4, 6}, 6)));   // expected: [1, 3]
        System.out.println(java.util.Arrays.toString(search(new int[]{2, 5, 9, 11}, 11)));    // expected: [0, 2]
    }
}
```

### Python

```python
def search(arr: list[int], target_sum: int) -> list[int]:
    # TODO: implement
    pass


print(search([1, 2, 3, 4, 6], 6))   # expected: [1, 3]
print(search([2, 5, 9, 11], 11))    # expected: [0, 2]
```
