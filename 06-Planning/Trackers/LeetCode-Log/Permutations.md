---
difficulty: Medium
status: Not started
topic: [Subsets, Arrays, Backtracking]
tags: [subsets, array, backtracking, grokking-patterns, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/permutations/"
---

### Problem
Given a set of distinct numbers, return all possible orderings (permutations) of those elements. Every element must appear exactly once in each permutation. A set of n distinct elements produces n! total permutations.

### Constraints
- 1 <= nums.length <= 6
- All elements are distinct
- Input fits in memory

### Examples
```
[1, 3, 5]  →  [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
```

### Next solve approach
1. Brute Force first — recursive backtracking, swap each element into the current position
2. Optimized (Subsets/BFS) — iteratively insert each new number into every position of every existing permutation

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static List<List<Integer>> findPermutations(int[] nums) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        System.out.println(findPermutations(new int[]{1, 3, 5}));
        // expected: [[1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]]
    }
}
```

### Python

```python
def find_permutations(nums: list[int]) -> list[list[int]]:
    # TODO: implement
    pass


print(find_permutations([1, 3, 5]))
# expected: [[1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]]
```
