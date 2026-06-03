---
difficulty: Medium
status: Not started
topic: [Bit Manipulation]
tags: [bit-manipulation, math, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/sum-of-two-integers/"
---

### Problem
Add two integers `a` and `b` without using the `+` or `-` operators. The trick is to simulate binary addition: XOR gives the sum bits without carries, and AND shifted left gives the carry bits. Repeat until there is no carry remaining.

### Constraints
- -1000 <= a, b <= 1000

### Examples
```
a = 1, b = 2  →  3
a = 2, b = 3  →  5
```

### Next solve approach
1. Brute Force first — not applicable; the constraint forbids + and -
2. Optimized — recursive/iterative bit trick: `getSum(a ^ b, (a & b) << 1)` until b == 0

---

### Java

```java
class Solution {

    // TODO: implement
    public int getSum(int a, int b) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.getSum(1, 2)); // expected: 3
        System.out.println(sol.getSum(2, 3)); // expected: 5
    }
}
```

### Python

```python
def getSum(a: int, b: int) -> int:
    # TODO: implement
    pass


print(getSum(1, 2))  # expected: 3
print(getSum(2, 3))  # expected: 5
```
