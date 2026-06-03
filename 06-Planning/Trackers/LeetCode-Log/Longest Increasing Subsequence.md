---
difficulty: Medium
status: Not started
topic: [1-D Dynamic Programming]
tags: [array, binary-search, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/longest-increasing-subsequence/"
---

### Problem
Given an integer array, find the length of the longest strictly increasing subsequence. A subsequence does not need to be contiguous — you can skip elements — but the chosen elements must be in strictly ascending order relative to the original array.

### Constraints
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

### Examples
```
nums = [10,9,2,5,3,7,101,18]  →  4     ([2,3,7,101])
nums = [0,1,0,3,2,3]          →  4
nums = [7,7,7,7,7,7,7]        →  1     (no strictly increasing pair)
```

### Next solve approach
1. Brute Force first — for each element, recursively find the longest subsequence starting there (exponential)
2. Optimized — DP where dp[i] = LIS ending at index i, O(n^2); or patience sort with binary search for O(n log n)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int lengthOfLIS(int[] nums) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.lengthOfLIS(new int[]{10, 9, 2, 5, 3, 7, 101, 18})); // expected: 4
        System.out.println(sol.lengthOfLIS(new int[]{0, 1, 0, 3, 2, 3}));           // expected: 4
        System.out.println(sol.lengthOfLIS(new int[]{7, 7, 7, 7, 7, 7, 7}));        // expected: 1
    }
}
```

### Python

```python
from typing import List

def length_of_lis(nums: List[int]) -> int:
    # TODO: implement
    pass


print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18])) # expected: 4
print(length_of_lis([0, 1, 0, 3, 2, 3]))            # expected: 4
print(length_of_lis([7, 7, 7, 7, 7, 7, 7]))         # expected: 1
```
