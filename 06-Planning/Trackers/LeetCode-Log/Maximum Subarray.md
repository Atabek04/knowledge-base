---
difficulty: Medium
status: Not started
topic: [Greedy]
tags: [array, divide-and-conquer, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/maximum-subarray/"
---

### Problem
Given an integer array, find the contiguous subarray that has the largest sum and return that sum. The subarray must contain at least one element. Negative numbers can make extending a subarray harmful, so you must decide when to start fresh.

### Constraints
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

### Examples
```
[-2,1,-3,4,-1,2,1,-5,4]  →  6     ([4,-1,2,1] has sum 6)
[1]                        →  1
[5,4,-1,7,8]               →  23    (entire array)
```

### Next solve approach
1. Brute Force first — try every pair of start/end indices, track max sum O(n²)
2. Optimized — Kadane's algorithm (greedy DP): carry running sum, reset to 0 when it goes negative

---

### Java

```java
public class Solution {

    // TODO: implement
    public int maxSubArray(int[] nums) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxSubArray(new int[]{-2,1,-3,4,-1,2,1,-5,4})); // expected: 6
        System.out.println(sol.maxSubArray(new int[]{1}));                       // expected: 1
        System.out.println(sol.maxSubArray(new int[]{5,4,-1,7,8}));              // expected: 23
    }
}
```

### Python

```python
def max_sub_array(nums: list[int]) -> int:
    # TODO: implement
    pass


print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))  # expected: 6
print(max_sub_array([1]))                        # expected: 1
print(max_sub_array([5,4,-1,7,8]))               # expected: 23
```
