---
difficulty: Easy
status: Not started
topic: [Math & Geometry]
tags: [array, math, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/plus-one/"
---

### Problem
You are given a large non-negative integer stored as an array of its individual digits in most-significant to least-significant order, with no leading zeros. Add one to this number and return the updated digit array. The main edge case is a carry that propagates all the way through, for example [9,9,9] becomes [1,0,0,0].

### Constraints
- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's

### Examples
```
[1,2,3]  →  [1,2,4]     (123 + 1 = 124)
[4,3,2,1]  →  [4,3,2,2]  (4321 + 1 = 4322)
[9]  →  [1,0]            (9 + 1 = 10)
```

### Next solve approach
1. Brute Force first — traverse from the last digit, increment and handle carry, prepend 1 if overflow
2. Optimized — same single-pass approach is already optimal at O(n)

---

### Java

```java
import java.util.Arrays;

public class Solution {

    // TODO: implement
    public int[] plusOne(int[] digits) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(Arrays.toString(sol.plusOne(new int[]{1,2,3})));   // expected: [1, 2, 4]
        System.out.println(Arrays.toString(sol.plusOne(new int[]{4,3,2,1}))); // expected: [4, 3, 2, 2]
        System.out.println(Arrays.toString(sol.plusOne(new int[]{9})));       // expected: [1, 0]
    }
}
```

### Python

```python
def plus_one(digits: list[int]) -> list[int]:
    # TODO: implement
    pass


print(plus_one([1, 2, 3]))    # expected: [1, 2, 4]
print(plus_one([4, 3, 2, 1])) # expected: [4, 3, 2, 2]
print(plus_one([9]))           # expected: [1, 0]
```
