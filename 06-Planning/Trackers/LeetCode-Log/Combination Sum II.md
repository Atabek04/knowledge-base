---
difficulty: Medium
status: Not started
topic: [Backtracking]
tags: [array, backtracking, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/combination-sum-ii/"
---

### Problem
Given a list of candidate numbers (which may contain duplicates) and a target, find all unique combinations that sum to the target. Each candidate number may only be used once per combination, and the solution set must not contain duplicate combinations.

### Constraints
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

### Examples
```
candidates = [10,1,2,7,6,1,5], target = 8  →  [[1,1,6],[1,2,5],[1,7],[2,6]]
candidates = [2,5,2,1,2], target = 5       →  [[1,2,2],[5]]
```

### Next solve approach
1. Brute Force first — generate all subsets using each element once, filter by sum, deduplicate
2. Optimized — sort + backtracking DFS, skip duplicate candidates at the same level to avoid duplicate results

---

### Java

```java
public class Solution {

    // TODO: implement
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.combinationSum2(new int[]{10, 1, 2, 7, 6, 1, 5}, 8)); // expected: [[1,1,6],[1,2,5],[1,7],[2,6]]
        System.out.println(sol.combinationSum2(new int[]{2, 5, 2, 1, 2}, 5));         // expected: [[1,2,2],[5]]
    }
}
```

### Python

```python
def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    # TODO: implement
    pass


print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))  # expected: [[1,1,6],[1,2,5],[1,7],[2,6]]
print(combination_sum2([2, 5, 2, 1, 2], 5))          # expected: [[1,2,2],[5]]
```
