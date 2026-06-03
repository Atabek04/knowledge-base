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
Given an array of n integers where each value is unique and falls in the range 1 to n, sort the array in-place in O(n) time with O(1) extra space. Each number i belongs at index i-1, so we can iterate and swap each element directly into its correct position.

### Constraints
- Array length n >= 1
- Each element is a unique integer in range [1, n]
- Must sort in-place, O(n) time, O(1) space

### Examples
```
[3, 1, 5, 4, 2]     →  [1, 2, 3, 4, 5]
[2, 6, 4, 3, 1, 5]  →  [1, 2, 3, 4, 5, 6]
[1, 5, 6, 4, 3, 2]  →  [1, 2, 3, 4, 5, 6]
```

### Next solve approach
1. Brute Force first — comparison-based sort, O(n log n)
2. Optimized (Cyclic Sort) — for each index i, swap nums[i] to its correct slot (nums[i]-1) until every element is in place

---

### Java

```java
public class Solution {

    // TODO: implement
    public static void sort(int[] nums) {
        // TODO
    }

    public static void main(String[] args) {
        int[] a = {3, 1, 5, 4, 2};
        sort(a);
        System.out.println(java.util.Arrays.toString(a)); // expected: [1, 2, 3, 4, 5]

        int[] b = {2, 6, 4, 3, 1, 5};
        sort(b);
        System.out.println(java.util.Arrays.toString(b)); // expected: [1, 2, 3, 4, 5, 6]

        int[] c = {1, 5, 6, 4, 3, 2};
        sort(c);
        System.out.println(java.util.Arrays.toString(c)); // expected: [1, 2, 3, 4, 5, 6]
    }
}
```

### Python

```python
def sort(nums: list[int]) -> None:
    # TODO: implement
    pass


a = [3, 1, 5, 4, 2]
sort(a)
print(a)  # expected: [1, 2, 3, 4, 5]

b = [2, 6, 4, 3, 1, 5]
sort(b)
print(b)  # expected: [1, 2, 3, 4, 5, 6]

c = [1, 5, 6, 4, 3, 2]
sort(c)
print(c)  # expected: [1, 2, 3, 4, 5, 6]
```
