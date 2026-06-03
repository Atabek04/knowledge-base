---
difficulty: Medium
status: Not started
topic: [Binary Search]
tags: [array, binary-search, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/search-a-2d-matrix/"
---

### Problem
Given an m x n integer matrix where each row is sorted in non-decreasing order and the first integer of each row is greater than the last integer of the previous row, determine whether a target value exists in the matrix. The solution must run in O(log(m * n)) time.

### Constraints
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4

### Examples
```
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3   →  true
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13  →  false
```

### Next solve approach
1. Brute Force first — scan every cell row by row and compare to target
2. Optimized — treat the matrix as a flattened 1D sorted array and binary search; map mid index via row = mid/n, col = mid%n

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean searchMatrix(int[][] matrix, int target) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] m1 = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
        System.out.println(sol.searchMatrix(m1, 3));   // expected: true
        System.out.println(sol.searchMatrix(m1, 13));  // expected: false
    }
}
```

### Python

```python
def search_matrix(matrix: list[list[int]], target: int) -> bool:
    # TODO: implement
    pass


m1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(search_matrix(m1, 3))   # expected: True
print(search_matrix(m1, 13))  # expected: False
```
