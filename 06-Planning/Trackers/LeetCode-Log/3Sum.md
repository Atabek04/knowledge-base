---
difficulty: Medium
status: Not started
topic: [Two Pointers]
tags: [array, two-pointers, sorting, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/3sum/"
---

### Problem
Given an integer array `nums`, find all unique triplets of distinct indices i, j, k such that `nums[i] + nums[j] + nums[k] == 0`. The result must not contain duplicate triplets. The order of triplets and values within each triplet does not matter.

### Constraints
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

### Examples
```
[-1,0,1,2,-1,-4]  →  [[-1,-1,2],[-1,0,1]]
[0,1,1]           →  []
[0,0,0]           →  [[0,0,0]]
```

### Next solve approach
1. Brute Force first — three nested loops checking every combination, deduplicate with a set (O(n^3)).
2. Optimized — sort the array, fix one element with a loop, then use two pointers on the remainder to find pairs summing to the negation of the fixed element; skip duplicates at each level (O(n^2)).

---

### Java

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

    // TODO: implement
    public List<List<Integer>> threeSum(int[] nums) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.threeSum(new int[]{-1, 0, 1, 2, -1, -4})); // expected: [[-1,-1,2],[-1,0,1]]
        System.out.println(sol.threeSum(new int[]{0, 1, 1}));             // expected: []
        System.out.println(sol.threeSum(new int[]{0, 0, 0}));             // expected: [[0,0,0]]
    }
}
```

### Python

```python
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    # TODO: implement
    pass


print(three_sum([-1, 0, 1, 2, -1, -4]))  # expected: [[-1, -1, 2], [-1, 0, 1]]
print(three_sum([0, 1, 1]))              # expected: []
print(three_sum([0, 0, 0]))             # expected: [[0, 0, 0]]
```
