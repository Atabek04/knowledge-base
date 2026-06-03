---
difficulty: Medium
status: Not started
topic: [Math & Geometry]
tags: [array, hash-table, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/set-matrix-zeroes/"
---

### Problem
Given an m x n integer matrix, find every cell that contains 0 and set its entire row and column to 0. The modification must be done in-place on the original matrix. The key challenge is not to zero out new cells based on zeros you just wrote — you must record which rows and columns were originally zero before modifying anything.

### Constraints
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

### Examples
```
[[1,1,1],[1,0,1],[1,1,1]]  →  [[1,0,1],[0,0,0],[1,0,1]]
[[0,1,2,0],[3,4,5,2],[1,3,1,5]]  →  [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

### Next solve approach
1. Brute Force first — scan once to collect zero positions into a set, then zero out their rows and columns
2. Optimized — use the first row and first column as marker arrays to achieve O(1) extra space

---

### Java

```java
public class Solution {

    // TODO: implement
    public void setZeroes(int[][] matrix) {
        // TODO
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] matrix1 = {{1,1,1},{1,0,1},{1,1,1}};
        sol.setZeroes(matrix1);
        // expected: [[1,0,1],[0,0,0],[1,0,1]]

        int[][] matrix2 = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
        sol.setZeroes(matrix2);
        // expected: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    }
}
```

### Python

```python
def set_zeroes(matrix: list[list[int]]) -> None:
    # TODO: implement
    pass


matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
set_zeroes(matrix1)
print(matrix1)  # expected: [[1,0,1],[0,0,0],[1,0,1]]

matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_zeroes(matrix2)
print(matrix2)  # expected: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```
