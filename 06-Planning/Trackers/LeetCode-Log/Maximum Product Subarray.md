---
difficulty: Medium
status: Not started
topic: [1-D Dynamic Programming]
tags: [array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/maximum-product-subarray/"
---

### Problem
Given an integer array, find the contiguous subarray that produces the largest product and return that product. The array may contain negative numbers and zeros, which makes this trickier than maximum sum — a large negative number can become the largest positive after multiplication with another negative.

### Constraints
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any subarray fits in a 32-bit integer

### Examples
```
nums = [2,3,-2,4]   →  6     ([2,3])
nums = [-2,0,-1]    →  0     ([-2,-1] is not contiguous)
```

### Next solve approach
1. Brute Force first — compute the product of every subarray with nested loops, track the maximum
2. Optimized — DP tracking both the current max and min product ending at each index (a negative min can flip to a large max when multiplied by a negative number)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int maxProduct(int[] nums) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxProduct(new int[]{2, 3, -2, 4})); // expected: 6
        System.out.println(sol.maxProduct(new int[]{-2, 0, -1}));   // expected: 0
    }
}
```

### Python

```python
from typing import List

def max_product(nums: List[int]) -> int:
    # TODO: implement
    pass


print(max_product([2, 3, -2, 4])) # expected: 6
print(max_product([-2, 0, -1]))   # expected: 0
```
