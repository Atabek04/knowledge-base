---
difficulty: Medium
status: Not started
topic: [Backtracking]
tags: [array, backtracking, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/combination-sum/"
---

### Problem
Given an array of distinct integers and a target value, find every unique combination of numbers from the array that adds up to the target. The same number can be picked any number of times. Two combinations are considered different only if the frequency of at least one number differs between them.

### Constraints
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct
- 1 <= target <= 40

### Examples
```
candidates = [2,3,6,7], target = 7  →  [[2,2,3],[7]]     (2 can be reused)
candidates = [2,3,5], target = 8    →  [[2,2,2,2],[2,3,3],[3,5]]
candidates = [2], target = 1        →  []
```

### Next solve approach
1. Brute Force first — generate all combinations with repetition and filter by sum
2. Optimized — sort + backtracking DFS, prune branches where remaining sum < current candidate

---

### Java

```java
public class Solution {

    // TODO: implement
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.combinationSum(new int[]{2, 3, 6, 7}, 7)); // expected: [[2,2,3],[7]]
        System.out.println(sol.combinationSum(new int[]{2, 3, 5}, 8));    // expected: [[2,2,2,2],[2,3,3],[3,5]]
        System.out.println(sol.combinationSum(new int[]{2}, 1));           // expected: []
    }
}
```

### Python

```python
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    # TODO: implement
    pass


print(combination_sum([2, 3, 6, 7], 7))  # expected: [[2,2,3],[7]]
print(combination_sum([2, 3, 5], 8))     # expected: [[2,2,2,2],[2,3,3],[3,5]]
print(combination_sum([2], 1))           # expected: []
```
