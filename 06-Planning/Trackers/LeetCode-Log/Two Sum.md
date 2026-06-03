---
difficulty: Easy
status: Not started
topic: [Arrays & Hashing]
tags: [array, hash-table, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/two-sum/"
---

### Problem
Given an array of integers and a target value, find the two numbers that add up to the target and return their indices. Each input has exactly one valid answer, and you cannot use the same element twice. The answer indices can be returned in any order.

### Constraints
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

### Examples
```
nums = [2,7,11,15], target = 9  →  [0,1]     (nums[0] + nums[1] == 9)
nums = [3,2,4], target = 6      →  [1,2]
nums = [3,3], target = 6        →  [0,1]
```

### Next solve approach
1. Brute Force first — nested loops checking every pair, O(n²)
2. Optimized — hash map storing each value→index, look up complement in O(1) per element

---

### Java

```java
public class Solution {

    // TODO: implement
    public int[] twoSum(int[] nums, int target) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(java.util.Arrays.toString(s.twoSum(new int[]{2, 7, 11, 15}, 9)));  // expected: [0, 1]
        System.out.println(java.util.Arrays.toString(s.twoSum(new int[]{3, 2, 4}, 6)));       // expected: [1, 2]
        System.out.println(java.util.Arrays.toString(s.twoSum(new int[]{3, 3}, 6)));           // expected: [0, 1]
    }
}
```

### Python

```python
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    # TODO: implement
    pass


print(two_sum([2, 7, 11, 15], 9))  # expected: [0, 1]
print(two_sum([3, 2, 4], 6))       # expected: [1, 2]
print(two_sum([3, 3], 6))           # expected: [0, 1]
```
