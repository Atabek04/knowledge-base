---
difficulty: Medium
status: Not started
topic: [Bitwise XOR, Bit Manipulation]
tags: [bitwise-xor, bit-manipulation, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a non-negative integer N, flip every bit in its binary representation (change each 0 to 1 and each 1 to 0) and return the resulting value as a base-10 integer. For example, 8 in binary is `1000`; flipping all bits gives `0111`, which is 7.

### Constraints
- N >= 0
- N fits in a standard 32-bit integer
- Complement is taken over the significant bits only (no infinite leading zeros)

### Examples
```
8   →  7   (1000 → 0111)
10  →  5   (1010 → 0101)
```

### Next solve approach
1. Brute Force first — convert N to binary string, flip each character, parse back to int
2. Optimized (Bitwise XOR) — build an all-ones mask of the same bit-length as N, then XOR N with the mask

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int bitwiseComplement(int n) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(bitwiseComplement(8));  // expected: 7
        System.out.println(bitwiseComplement(10)); // expected: 5
    }
}
```

### Python

```python
def bitwise_complement(n: int) -> int:
    # TODO: implement
    pass


print(bitwise_complement(8))   # expected: 7
print(bitwise_complement(10))  # expected: 5
```
