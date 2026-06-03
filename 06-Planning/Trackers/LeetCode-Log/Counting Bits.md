---
difficulty: Easy
status: Not started
topic: [Bit Manipulation]
tags: [bit-manipulation, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/counting-bits/"
---

### Problem
Given an integer `n`, return an array of length `n + 1` where each index `i` holds the count of 1-bits in the binary representation of `i`. The straightforward approach runs in O(n log n) by counting bits per number, but an O(n) DP solution exists using the relationship between a number and the number with its lowest set bit cleared.

### Constraints
- 0 <= n <= 10^5

### Examples
```
n = 2  →  [0,1,1]      (0→0, 1→1, 2→10)
n = 5  →  [0,1,1,2,1,2]
```

### Next solve approach
1. Brute Force first — for each i from 0 to n, count its set bits with Integer.bitCount
2. Optimized — DP: `ans[i] = ans[i & (i - 1)] + 1` (strip lowest set bit and add 1)

---

### Java

```java
class Solution {

    // TODO: implement
    public int[] countBits(int n) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(java.util.Arrays.toString(sol.countBits(2))); // expected: [0, 1, 1]
        System.out.println(java.util.Arrays.toString(sol.countBits(5))); // expected: [0, 1, 1, 2, 1, 2]
    }
}
```

### Python

```python
from typing import List

def countBits(n: int) -> List[int]:
    # TODO: implement
    pass


print(countBits(2))  # expected: [0, 1, 1]
print(countBits(5))  # expected: [0, 1, 1, 2, 1, 2]
```
