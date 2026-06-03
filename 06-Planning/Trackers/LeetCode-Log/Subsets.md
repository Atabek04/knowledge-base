---
difficulty: Easy
status: Not started
topic: [Subsets, Arrays, Backtracking]
tags: [subsets, array, backtracking, grokking-patterns, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/subsets/"
---

### Problem
Given a set of distinct integers, return all possible subsets (the power set). Every combination of elements must appear — including the empty set and the full set. The input has no duplicates, so no de-duplication is needed.

### Constraints
- 1 <= nums.length <= 10
- All elements are distinct
- Input fits in memory

### Examples
```
[1, 3]     →  [[], [1], [3], [1,3]]
[1, 5, 3]  →  [[], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]]
```

### Next solve approach
1. Brute Force first — recursive DFS, include or exclude each element
2. Optimized (Subsets/BFS) — start with empty set, for each number add it to every existing subset

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static List<List<Integer>> findSubsets(int[] nums) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        System.out.println(findSubsets(new int[]{1, 3}));    // expected: [[], [1], [3], [1, 3]]
        System.out.println(findSubsets(new int[]{1, 5, 3})); // expected: [[], [1], [5], [3], [1, 5], [1, 3], [5, 3], [1, 5, 3]]
    }
}
```

### Python

```python
def find_subsets(nums: list[int]) -> list[list[int]]:
    # TODO: implement
    pass


print(find_subsets([1, 3]))    # expected: [[], [1], [3], [1, 3]]
print(find_subsets([1, 5, 3])) # expected: [[], [1], [5], [3], [1, 5], [1, 3], [5, 3], [1, 5, 3]]
```
