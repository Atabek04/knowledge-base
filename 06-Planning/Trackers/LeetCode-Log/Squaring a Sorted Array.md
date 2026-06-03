---
difficulty: Easy
status: Not started
topic: [Two Pointers, Arrays]
tags: [two-pointers, array, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a sorted array that may contain negative numbers, return a new array of the squares of each element, also in sorted order. The tricky part is that squaring negatives can produce large values that interleave with squares of small positives.

### Constraints
- Input array is sorted in non-decreasing order
- Array may contain negative numbers
- 1 <= arr.length <= 10^5
- Output must be sorted in non-decreasing order

### Examples
```
[-2, -1, 0, 2, 3]   →  [0, 1, 4, 4, 9]
[-3, -1, 0, 1, 2]   →  [0, 1, 1, 4, 9]
```

### Next solve approach
1. Brute Force first — square all elements, then sort the result, O(n log n)
2. Optimized (Two Pointers) — left and right pointers compare absolute values, fill result from the end, O(n)

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int[] makeSquares(int[] arr) {
        int[] squares = new int[arr.length];
        // TODO
        return squares;
    }

    public static void main(String[] args) {
        System.out.println(java.util.Arrays.toString(makeSquares(new int[]{-2, -1, 0, 2, 3})));  // expected: [0, 1, 4, 4, 9]
        System.out.println(java.util.Arrays.toString(makeSquares(new int[]{-3, -1, 0, 1, 2})));  // expected: [0, 1, 1, 4, 9]
    }
}
```

### Python

```python
def make_squares(arr: list[int]) -> list[int]:
    # TODO: implement
    pass


print(make_squares([-2, -1, 0, 2, 3]))  # expected: [0, 1, 4, 4, 9]
print(make_squares([-3, -1, 0, 1, 2]))  # expected: [0, 1, 1, 4, 9]
```
