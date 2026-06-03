---
difficulty: Medium
status: Not started
topic: [Binary Search]
tags: [array, binary-search, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/"
---

### Problem
A sorted array of unique integers has been rotated between 1 and n times, shifting elements from the front to the back. Given this rotated array, find and return the minimum element. The algorithm must run in O(log n) time.

### Constraints
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All integers in nums are unique
- nums is sorted and rotated between 1 and n times

### Examples
```
nums = [3,4,5,1,2]      →  1    (original [1,2,3,4,5] rotated 3 times)
nums = [4,5,6,7,0,1,2]  →  0    (original [0,1,2,4,5,6,7] rotated 4 times)
nums = [11,13,15,17]    →  11   (rotated 4 times, back to original order)
```

### Next solve approach
1. Brute Force first — scan all elements and track the minimum
2. Optimized — binary search comparing mid to last element; if nums[mid] > nums[n-1], minimum is in right half

---

### Java

```java
public class Solution {

    // TODO: implement
    public int findMin(int[] nums) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.findMin(new int[]{3, 4, 5, 1, 2}));         // expected: 1
        System.out.println(sol.findMin(new int[]{4, 5, 6, 7, 0, 1, 2}));   // expected: 0
        System.out.println(sol.findMin(new int[]{11, 13, 15, 17}));         // expected: 11
    }
}
```

### Python

```python
def find_min(nums: list[int]) -> int:
    # TODO: implement
    pass


print(find_min([3, 4, 5, 1, 2]))        # expected: 1
print(find_min([4, 5, 6, 7, 0, 1, 2]))  # expected: 0
print(find_min([11, 13, 15, 17]))        # expected: 11
```
