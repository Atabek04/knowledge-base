---
difficulty: Medium
status: Not started
topic: [Bit Manipulation]
tags: [math, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/reverse-integer/"
---

### Problem
Given a signed 32-bit integer `x`, reverse its digits and return the result. If the reversed value falls outside the signed 32-bit range [-2^31, 2^31 - 1], return 0 instead. You cannot use 64-bit integers, so overflow must be detected before it happens by checking intermediate values against `Integer.MIN_VALUE / 10` and `Integer.MAX_VALUE / 10`.

### Constraints
- -2^31 <= x <= 2^31 - 1

### Examples
```
x = 123   →  321
x = -123  →  -321
x = 120   →  21    (leading zero dropped)
```

### Next solve approach
1. Brute Force first — convert to string, reverse, parse back — but must handle overflow separately
2. Optimized — peel digits with `x % 10` one at a time, guard overflow before multiplying ans by 10

---

### Java

```java
class Solution {

    // TODO: implement
    public int reverse(int x) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.reverse(123));   // expected: 321
        System.out.println(sol.reverse(-123));  // expected: -321
        System.out.println(sol.reverse(120));   // expected: 21
    }
}
```

### Python

```python
def reverse(x: int) -> int:
    # TODO: implement
    pass


print(reverse(123))   # expected: 321
print(reverse(-123))  # expected: -321
print(reverse(120))   # expected: 21
```
