---
difficulty: Medium
status: Not started
topic: [Math & Geometry]
tags: [array, matrix, simulation, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/spiral-matrix/"
---

### Problem
Given an m x n matrix, return all of its elements collected in spiral order: start at the top-left, move right along the top row, then down the right column, then left along the bottom row, then up the left column, and keep spiraling inward until every element is visited. The result is a flat list of all m*n elements.

### Constraints
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

### Examples
```
[[1,2,3],[4,5,6],[7,8,9]]  →  [1,2,3,6,9,8,7,4,5]
[[1,2,3,4],[5,6,7,8],[9,10,11,12]]  →  [1,2,3,4,8,12,11,10,9,5,6,7]
```

### Next solve approach
1. Brute Force first — track four boundaries (top, bottom, left, right) and shrink them after each pass
2. Optimized — direction array simulation with a visited boolean grid, rotate direction on boundary/visited hit

---

### Java

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {

    // TODO: implement
    public List<Integer> spiralOrder(int[][] matrix) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] matrix1 = {{1,2,3},{4,5,6},{7,8,9}};
        System.out.println(sol.spiralOrder(matrix1));
        // expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]

        int[][] matrix2 = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};
        System.out.println(sol.spiralOrder(matrix2));
        // expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    }
}
```

### Python

```python
def spiral_order(matrix: list[list[int]]) -> list[int]:
    # TODO: implement
    pass


print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))          # expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
```
