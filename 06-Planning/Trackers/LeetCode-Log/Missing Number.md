---
difficulty: Easy
status: Not started
topic: [Bit Manipulation]
tags: [bit-manipulation, array, hash-table, math, binary-search, sorting, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/missing-number/"
---

### Problem
You are given an array of `n` distinct integers drawn from the range `[0, n]`. Exactly one number in that range is absent. Find and return the missing number. The array has no duplicates and contains all values except one.

### Constraints
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All numbers in nums are unique

### Examples
```
nums = [3,0,1]         →  2
nums = [0,1]           →  2
nums = [9,6,4,2,3,5,7,0,1]  →  8
```

### Next solve approach
1. Brute Force first — compute expected sum n*(n+1)/2, subtract actual sum
2. Optimized — XOR all indices 0..n with all elements; duplicates cancel, leaving the missing number

---

### Java

```java
class Solution {

    // TODO: implement
    public int missingNumber(int[] nums) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.missingNumber(new int[]{3, 0, 1}));                  // expected: 2
        System.out.println(sol.missingNumber(new int[]{0, 1}));                     // expected: 2
        System.out.println(sol.missingNumber(new int[]{9, 6, 4, 2, 3, 5, 7, 0, 1})); // expected: 8
    }
}
```

### Python

```python
from typing import List

def missingNumber(nums: List[int]) -> int:
    # TODO: implement
    pass


print(missingNumber([3, 0, 1]))                  # expected: 2
print(missingNumber([0, 1]))                     # expected: 2
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])) # expected: 8
```
