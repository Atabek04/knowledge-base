---
difficulty: Medium
status: Not started
topic: [Math & Geometry]
tags: [array, math, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/rotate-image/"
---

### Problem
Given an n x n 2D matrix representing an image, rotate it 90 degrees clockwise in-place. You cannot allocate a new 2D matrix for the rotation. The trick is a two-step operation: first flip the matrix upside down (reverse rows), then transpose it along the main diagonal (swap matrix[i][j] with matrix[j][i]).

### Constraints
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

### Examples
```
[[1,2,3],[4,5,6],[7,8,9]]  →  [[7,4,1],[8,5,2],[9,6,3]]
[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]  →  [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

### Next solve approach
1. Brute Force first — copy to a new matrix placing each element at its rotated position
2. Optimized — flip vertically then transpose in-place (O(n^2) time, O(1) space)

---

### Java

```java
public class Solution {

    // TODO: implement
    public void rotate(int[][] matrix) {
        // TODO
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] matrix1 = {{1,2,3},{4,5,6},{7,8,9}};
        sol.rotate(matrix1);
        // expected: [[7,4,1],[8,5,2],[9,6,3]]

        int[][] matrix2 = {{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}};
        sol.rotate(matrix2);
        // expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    }
}
```

### Python

```python
def rotate(matrix: list[list[int]]) -> None:
    # TODO: implement
    pass


matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix1)
print(matrix1)  # expected: [[7,4,1],[8,5,2],[9,6,3]]

matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix2)
print(matrix2)  # expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```
