---
difficulty: Medium
status: Not started
topic: [Binary Search]
tags: [array, binary-search, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/search-in-rotated-sorted-array/"
---

### Problem
A sorted array of distinct integers may have been rotated at some unknown pivot point. Given this possibly-rotated array and a target integer, return the index of the target if it exists, or -1 otherwise. The algorithm must run in O(log n) time.

### Constraints
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is an ascending array that is possibly rotated
- -10^4 <= target <= 10^4

### Examples
```
nums = [4,5,6,7,0,1,2], target = 0  →  4
nums = [4,5,6,7,0,1,2], target = 3  →  -1
nums = [1], target = 0               →  -1
```

### Next solve approach
1. Brute Force first — linear scan to find target and return its index
2. Optimized — binary search: determine which half is sorted, then check if target falls within that sorted half

---

### Java

```java
public class Solution {

    // TODO: implement
    public int search(int[] nums, int target) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.search(new int[]{4, 5, 6, 7, 0, 1, 2}, 0));  // expected: 4
        System.out.println(sol.search(new int[]{4, 5, 6, 7, 0, 1, 2}, 3));  // expected: -1
        System.out.println(sol.search(new int[]{1}, 0));                      // expected: -1
    }
}
```

### Python

```python
def search(nums: list[int], target: int) -> int:
    # TODO: implement
    pass


print(search([4, 5, 6, 7, 0, 1, 2], 0))  # expected: 4
print(search([4, 5, 6, 7, 0, 1, 2], 3))  # expected: -1
print(search([1], 0))                      # expected: -1
```
