---
difficulty: Medium
status: Not started
topic: [Greedy]
tags: [greedy, array, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/merge-triplets-to-form-target-triplet/"
---

### Problem
You have a list of triplets and a target triplet [x, y, z]. The only allowed operation is to pick two triplets and replace one of them with the element-wise maximum of both. You can repeat this any number of times. Return true if you can make the target triplet appear in the list, false otherwise.

### Constraints
- 1 <= triplets.length <= 10^5
- triplets[i].length == target.length == 3
- 1 <= ai, bi, ci, x, y, z <= 1000

### Examples
```
triplets=[[2,5,3],[1,8,4],[1,7,5]], target=[2,7,5]  →  true
triplets=[[3,4,5],[4,5,6]],         target=[3,2,5]  →  false    (no 2 exists in any triplet)
triplets=[[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target=[5,5,5]  →  true
```

### Next solve approach
1. Brute Force first — try merging all valid triplets whose values don't exceed target on any dimension
2. Optimized — greedy: skip triplets that exceed any target dimension; take element-wise max of the rest; check if result equals target

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.mergeTriplets(
            new int[][]{{2,5,3},{1,8,4},{1,7,5}}, new int[]{2,7,5})); // expected: true
        System.out.println(sol.mergeTriplets(
            new int[][]{{3,4,5},{4,5,6}}, new int[]{3,2,5}));          // expected: false
        System.out.println(sol.mergeTriplets(
            new int[][]{{2,5,3},{2,3,4},{1,2,5},{5,2,3}}, new int[]{5,5,5})); // expected: true
    }
}
```

### Python

```python
def merge_triplets(triplets: list[list[int]], target: list[int]) -> bool:
    # TODO: implement
    pass


print(merge_triplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))          # expected: True
print(merge_triplets([[3,4,5],[4,5,6]], [3,2,5]))                   # expected: False
print(merge_triplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]))   # expected: True
```
