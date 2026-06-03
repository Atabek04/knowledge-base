---
difficulty: Easy
status: Not started
topic: [Binary Search]
tags: [array, binary-search, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/binary-search/"
---

### Problem
Given a sorted array of integers and a target value, return the index of the target if it exists in the array, or -1 if it does not. All values in the array are unique and the array is sorted in ascending order. The solution must run in O(log n) time.

### Constraints
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All integers in nums are unique
- nums is sorted in ascending order

### Examples
```
nums = [-1,0,3,5,9,12], target = 9  →  4     (9 is at index 4)
nums = [-1,0,3,5,9,12], target = 2  →  -1    (2 not in array)
```

### Next solve approach
1. Brute Force first — linear scan, return index where nums[i] == target
2. Optimized — binary search with two pointers l/r, halve the search space each step

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
        System.out.println(sol.search(new int[]{-1, 0, 3, 5, 9, 12}, 9));  // expected: 4
        System.out.println(sol.search(new int[]{-1, 0, 3, 5, 9, 12}, 2));  // expected: -1
    }
}
```

### Python

```python
def search(nums: list[int], target: int) -> int:
    # TODO: implement
    pass


print(search([-1, 0, 3, 5, 9, 12], 9))   # expected: 4
print(search([-1, 0, 3, 5, 9, 12], 2))   # expected: -1
```
