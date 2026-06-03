---
difficulty: Easy
status: Not started
topic: [Bit Manipulation]
tags: [bit-manipulation, divide-and-conquer, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/number-of-1-bits/"
---

### Problem
Given a positive integer `n`, count how many bits are set to 1 in its binary representation — this count is also called the Hamming weight. For example, 11 in binary is `1011`, which has three set bits. The function must treat the input as an unsigned value.

### Constraints
- 1 <= n <= 2^31 - 1

### Examples
```
n = 11          →  3     (binary 1011 has three 1s)
n = 128         →  1     (binary 10000000 has one 1)
n = 2147483645  →  30
```

### Next solve approach
1. Brute Force first — shift through all 32 bits and count each 1
2. Optimized — use `n &= n - 1` to strip the lowest set bit each iteration (Brian Kernighan)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int hammingWeight(int n) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.hammingWeight(11));          // expected: 3
        System.out.println(sol.hammingWeight(128));         // expected: 1
        System.out.println(sol.hammingWeight(2147483645));  // expected: 30
    }
}
```

### Python

```python
def hammingWeight(n: int) -> int:
    # TODO: implement
    pass


print(hammingWeight(11))          # expected: 3
print(hammingWeight(128))         # expected: 1
print(hammingWeight(2147483645))  # expected: 30
```
