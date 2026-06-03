---
difficulty: Hard
status: Not started
topic: [Sliding Window]
tags: [queue, array, sliding-window, monotonic-queue, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/sliding-window-maximum/"
---

### Problem
You are given an integer array `nums` and a window size `k`. A sliding window of size `k` moves from the leftmost position to the rightmost position one step at a time. For each position of the window, return the maximum value visible inside it. The result array has length `n - k + 1`.

### Constraints
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

### Examples
```
nums = [1,3,-1,-3,5,3,6,7], k = 3  →  [3,3,5,5,6,7]
nums = [1], k = 1                   →  [1]
```

### Next solve approach
1. Brute Force first — iterate every window position and scan all k elements for the max in O(n*k)
2. Optimized — monotonic deque storing indices in decreasing value order; front is always the current window max in O(n)

---

### Java

```java
import java.util.Arrays;

public class Solution {

    // TODO: implement
    public int[] maxSlidingWindow(int[] nums, int k) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(Arrays.toString(sol.maxSlidingWindow(new int[]{1, 3, -1, -3, 5, 3, 6, 7}, 3))); // expected: [3, 3, 5, 5, 6, 7]
        System.out.println(Arrays.toString(sol.maxSlidingWindow(new int[]{1}, 1)));                         // expected: [1]
    }
}
```

### Python

```python
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    # TODO: implement
    pass


print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # expected: [3, 3, 5, 5, 6, 7]
print(max_sliding_window([1], 1))                            # expected: [1]
```
