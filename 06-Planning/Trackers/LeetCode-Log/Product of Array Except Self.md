---
difficulty: Medium
status: Cheated
topic:
  - Arrays & Hashing
tags:
  - array
  - prefix-sum
  - neetcode-150
solved: 0
last_solved: 2026-06-04
link: https://leetcode.com/problems/product-of-array-except-self/
---

### Problem
Given an integer array, return a new array where each element at index i equals the product of all elements in the original array except the one at index i. The solution must run in O(n) time and cannot use the division operation. Any prefix or suffix product is guaranteed to fit in a 32-bit integer.

### Constraints
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The answer for each position is guaranteed to fit in a 32-bit integer.

### Examples
```
nums = [1,2,3,4]      →  [24,12,8,6]
nums = [-1,1,0,-3,3]  →  [0,0,9,0,0]
```

### Next solve approach
1. Brute Force first — for each index multiply all other elements in a nested loop, O(n²)
2. Optimized — two passes: left-prefix products then right-suffix products accumulated in place, O(n) time O(1) extra space

---

### Java

```java
public class Solution {

    // TODO: implement
    public int[] productExceptSelf(int[] nums) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(java.util.Arrays.toString(s.productExceptSelf(new int[]{1, 2, 3, 4})));      // expected: [24, 12, 8, 6]
        System.out.println(java.util.Arrays.toString(s.productExceptSelf(new int[]{-1, 1, 0, -3, 3}))); // expected: [0, 0, 9, 0, 0]
    }
}
```

### Python

```python
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    # TODO: implement
    pass


print(product_except_self([1, 2, 3, 4]))       # expected: [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # expected: [0, 0, 9, 0, 0]
```
