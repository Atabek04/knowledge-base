---
difficulty: Medium
status: Not started
topic: [Fast & Slow Pointers, Bit Manipulation]
tags: [fast-slow-pointers, bit-manipulation, grokking-patterns, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/happy-number/"
---

### Problem
A number is "happy" if repeatedly replacing it with the sum of the squares of its digits eventually produces 1. Numbers that are not happy cycle endlessly through other values and never reach 1. Given a positive integer, return true if it is a happy number, false otherwise.

### Constraints
- 1 <= num <= 2^31 - 1
- Input fits in memory

### Examples
```
23  →  true   (2²+3²=13 → 1²+3²=10 → 1²+0²=1)
12  →  false  (cycles: 1²+2²=5 → 25 → 29 → 85 → 89 → loops back to 89)
```

### Next solve approach
1. Brute Force first — use a HashSet to store seen numbers; return true if 1 is hit, false on any repeat
2. Optimized (Fast & Slow Pointers) — treat digit-square sums as a virtual linked list; slow advances one step, fast two; if they meet at 1 it's happy, any other meeting point means a non-1 cycle

---

### Java

```java
public class Solution {

    // TODO: implement
    public static boolean find(int num) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        System.out.println(find(23)); // expected: true
        System.out.println(find(12)); // expected: false
    }
}
```

### Python

```python
def find(num: int) -> bool:
    # TODO: implement
    pass


print(find(23))  # expected: True
print(find(12))  # expected: False
```
