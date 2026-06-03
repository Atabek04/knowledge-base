---
difficulty: Hard
status: Not started
topic: [Binary Search]
tags: [array, binary-search, divide-and-conquer, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/median-of-two-sorted-arrays/"
---

### Problem
Given two sorted arrays nums1 and nums2 of sizes m and n respectively, return the median of the two arrays combined. If the combined length is even, the median is the average of the two middle elements. The overall runtime must be O(log(m+n)).

### Constraints
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

### Examples
```
nums1 = [1,3], nums2 = [2]      →  2.00000    (merged = [1,2,3], median = 2)
nums1 = [1,2], nums2 = [3,4]    →  2.50000    (merged = [1,2,3,4], median = (2+3)/2)
```

### Next solve approach
1. Brute Force first — merge both arrays, sort, pick middle element(s)
2. Optimized — divide and conquer / binary search for the k-th smallest element across both arrays without merging

---

### Java

```java
public class Solution {

    // TODO: implement
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.findMedianSortedArrays(new int[]{1, 3}, new int[]{2}));       // expected: 2.00000
        System.out.println(sol.findMedianSortedArrays(new int[]{1, 2}, new int[]{3, 4}));    // expected: 2.50000
    }
}
```

### Python

```python
def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    # TODO: implement
    pass


print(find_median_sorted_arrays([1, 3], [2]))     # expected: 2.0
print(find_median_sorted_arrays([1, 2], [3, 4]))  # expected: 2.5
```
