---
difficulty: Medium
status: Not started
topic: [Greedy]
tags: [greedy, array, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/jump-game/"
---

### Problem
You start at the first index of an integer array. Each element tells you the maximum number of positions you can jump forward from that index. Return true if you can reach the last index, false otherwise. A zero value traps you if you haven't already jumped past it.

### Constraints
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5

### Examples
```
[2,3,1,1,4]  →  true     (jump 1 to index 1, then 3 to last)
[3,2,1,0,4]  →  false    (always land on index 3 which has jump 0)
```

### Next solve approach
1. Brute Force first — recursively try every jump from each position, memoize reachability
2. Optimized — greedy: track the farthest reachable index; if current index exceeds it, return false

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean canJump(int[] nums) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.canJump(new int[]{2,3,1,1,4})); // expected: true
        System.out.println(sol.canJump(new int[]{3,2,1,0,4})); // expected: false
    }
}
```

### Python

```python
def can_jump(nums: list[int]) -> bool:
    # TODO: implement
    pass


print(can_jump([2,3,1,1,4]))  # expected: True
print(can_jump([3,2,1,0,4]))  # expected: False
```
