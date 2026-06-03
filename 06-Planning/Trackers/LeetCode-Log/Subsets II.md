---
difficulty: Medium
status: Not started
topic: [Backtracking]
tags: [bit-manipulation, array, backtracking, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/subsets-ii/"
---

### Problem
Given an integer array that may contain duplicate values, return all possible subsets (the power set) without any duplicate subsets in the result. The order of the output does not matter.

### Constraints
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

### Examples
```
nums = [1,2,2]  →  [[],[1],[1,2],[1,2,2],[2],[2,2]]
nums = [0]      →  [[],[0]]
```

### Next solve approach
1. Brute Force first — generate all 2^n subsets and deduplicate using a set
2. Optimized — sort array then backtracking DFS, skip duplicate elements at the same recursion level

---

### Java

```java
public class Solution {

    // TODO: implement
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.subsetsWithDup(new int[]{1, 2, 2})); // expected: [[],[1],[1,2],[1,2,2],[2],[2,2]]
        System.out.println(sol.subsetsWithDup(new int[]{0}));       // expected: [[],[0]]
    }
}
```

### Python

```python
def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    # TODO: implement
    pass


print(subsets_with_dup([1, 2, 2]))  # expected: [[], [1], [1,2], [1,2,2], [2], [2,2]]
print(subsets_with_dup([0]))        # expected: [[], [0]]
```
