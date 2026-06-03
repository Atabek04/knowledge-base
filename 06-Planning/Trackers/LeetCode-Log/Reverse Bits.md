---
difficulty: Easy
status: Not started
topic: [Bit Manipulation]
tags: [bit-manipulation, divide-and-conquer, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/reverse-bits/"
---

### Problem
Given a 32-bit unsigned integer `n`, reverse the order of its bits and return the result as an integer. For example, the bit at position 0 (LSB) moves to position 31 (MSB), and so on. The input must be treated as an unsigned value even though Java uses signed ints.

### Constraints
- 0 <= n <= 2^31 - 2
- n is even

### Examples
```
n = 43261596   →  964176192    (00000010100101000001111010011100 → 00111001011110000010100101000000)
n = 2147483644 →  1073741822   (01111111111111111111111111111100 → 00111111111111111111111111111110)
```

### Next solve approach
1. Brute Force first — loop 32 times, extract LSB with `n & 1`, shift it to position `31 - i`, OR into result, then unsigned-right-shift n
2. Optimized — same bit-by-bit loop; early exit when n == 0 saves iterations

---

### Java

```java
public class Solution {

    // TODO: implement
    public int reverseBits(int n) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.reverseBits(43261596));   // expected: 964176192
        System.out.println(sol.reverseBits(2147483644)); // expected: 1073741822
    }
}
```

### Python

```python
def reverseBits(n: int) -> int:
    # TODO: implement
    pass


print(reverseBits(43261596))   # expected: 964176192
print(reverseBits(2147483644)) # expected: 1073741822
```
