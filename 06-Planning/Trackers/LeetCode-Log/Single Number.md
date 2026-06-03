---
difficulty: Easy
status: Not started
topic: [Bitwise XOR, Arrays, Bit Manipulation]
tags: [bitwise-xor, array, bit-manipulation, grokking-patterns, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/single-number/"
---

### Problem
Given a non-empty array of integers where every element appears exactly twice except for one, find and return that unique number. You cannot use extra memory to count occurrences — the trick is to cancel out pairs.

### Constraints
- Array is non-empty
- All numbers appear exactly twice except exactly one
- Array can contain any integers (positive or negative)

### Examples
```
[1, 4, 2, 1, 3, 2, 3]  →  4   (4 appears once; all others appear twice)
[7, 9, 7]              →  9   (9 appears once)
```

### Next solve approach
1. Brute Force first — use a HashMap to count frequency, return the key with count == 1
2. Optimized (Bitwise XOR) — XOR all elements; duplicate pairs cancel out (a ^ a = 0), leaving the single number

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int findSingleNumber(int[] arr) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findSingleNumber(new int[]{1, 4, 2, 1, 3, 2, 3})); // expected: 4
        System.out.println(findSingleNumber(new int[]{7, 9, 7}));             // expected: 9
    }
}
```

### Python

```python
def find_single_number(arr: list[int]) -> int:
    # TODO: implement
    pass


print(find_single_number([1, 4, 2, 1, 3, 2, 3]))  # expected: 4
print(find_single_number([7, 9, 7]))               # expected: 9
```
