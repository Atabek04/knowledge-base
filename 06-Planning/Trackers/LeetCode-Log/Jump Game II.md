---
difficulty: Medium
status: Not started
topic: [Greedy]
tags: [greedy, array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/jump-game-ii/"
---

### Problem
You start at index 0 of an integer array where each element is the maximum forward jump length from that position. The problem guarantees you can always reach the last index. Return the minimum number of jumps needed to get there.

### Constraints
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1]

### Examples
```
[2,3,1,1,4]  →  2     (index 0 → index 1 → last)
[2,3,0,1,4]  →  2
```

### Next solve approach
1. Brute Force first — BFS level by level from index 0, each level is one jump
2. Optimized — greedy: track current jump boundary; when you reach it, increment jump count and extend boundary to farthest seen so far

---

### Java

```java
public class Solution {

    // TODO: implement
    public int jump(int[] nums) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.jump(new int[]{2,3,1,1,4})); // expected: 2
        System.out.println(sol.jump(new int[]{2,3,0,1,4})); // expected: 2
    }
}
```

### Python

```python
def jump(nums: list[int]) -> int:
    # TODO: implement
    pass


print(jump([2,3,1,1,4]))  # expected: 2
print(jump([2,3,0,1,4]))  # expected: 2
```
