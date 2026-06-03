---
difficulty: Easy
status: Not started
topic: [Subsets, Arrays, Backtracking]
tags: [subsets, array, backtracking, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a list of integers that may contain duplicates, return all distinct subsets. Unlike the basic subsets problem, duplicate numbers can produce identical subsets, so the solution must avoid generating them more than once.

### Constraints
- 1 <= nums.length <= 10
- Elements may repeat
- Input fits in memory

### Examples
```
[1, 3, 3]     →  [[], [1], [3], [1,3], [3,3], [1,3,3]]
[1, 5, 3, 3]  →  [[], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]]
```

### Next solve approach
1. Brute Force first — generate all subsets, store in a set to remove duplicates
2. Optimized (Subsets) — sort first, then for duplicate numbers only extend the subsets added in the previous round

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
        System.out.println(findSubsets(new int[]{1, 3, 3}));    // expected: [[], [1], [3], [1,3], [3,3], [1,3,3]]
        System.out.println(findSubsets(new int[]{1, 5, 3, 3})); // expected: [[], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]]
    }
}
```

### Python

```python
def find_subsets(nums: list[int]) -> list[list[int]]:
    # TODO: implement
    pass


print(find_subsets([1, 3, 3]))    # expected: [[], [1], [3], [1,3], [3,3], [1,3,3]]
print(find_subsets([1, 5, 3, 3])) # expected: [[], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]]
```
