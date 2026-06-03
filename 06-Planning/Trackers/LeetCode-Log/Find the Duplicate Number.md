---
difficulty: Easy
status: Not started
topic: [Cyclic Sort, Arrays]
tags: [cyclic-sort, array, grokking-patterns, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/find-the-duplicate-number/"
---

### Problem
Given an array of n+1 integers where every value is in the range 1 to n, there is exactly one duplicate number but it may appear more than twice. Find that duplicate without using any extra space. You are allowed to modify the input array.

### Constraints
- Array length is n+1, values in range [1, n]
- Exactly one duplicate exists, but may repeat multiple times
- No extra space allowed; in-place modification is permitted

### Examples
```
[1, 4, 4, 3, 2]     →  4
[2, 1, 3, 3, 5, 4]  →  3
[2, 4, 1, 4, 4]     →  4
```

### Next solve approach
1. Brute Force first — sort then check adjacent elements, O(n log n)
2. Optimized (Cyclic Sort) — try placing each number at index nums[i]-1; when a number cannot be placed because the correct index already holds the same value, that number is the duplicate

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int findNumber(int[] nums) {
        // TODO
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(findNumber(new int[]{1, 4, 4, 3, 2}));    // expected: 4
        System.out.println(findNumber(new int[]{2, 1, 3, 3, 5, 4})); // expected: 3
        System.out.println(findNumber(new int[]{2, 4, 1, 4, 4}));    // expected: 4
    }
}
```

### Python

```python
def find_number(nums: list[int]) -> int:
    # TODO: implement
    pass


print(find_number([1, 4, 4, 3, 2]))     # expected: 4
print(find_number([2, 1, 3, 3, 5, 4]))  # expected: 3
print(find_number([2, 4, 1, 4, 4]))     # expected: 4
```
