---
difficulty: Hard
status: Not started
topic: [Backtracking]
tags: [array, backtracking, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/n-queens/"
---

### Problem
Place n queens on an n x n chessboard such that no two queens threaten each other — no two queens share the same row, column, or diagonal. Return all distinct board configurations that satisfy this condition. Each board is represented as a list of strings where 'Q' marks a queen and '.' marks an empty cell.

### Constraints
- 1 <= n <= 9

### Examples
```
n = 4  →  [[".Q..","...Q","Q...","..Q."],[\"..Q.\",\"Q...\",\"...Q\",\".Q..\"]]     (2 solutions)
n = 1  →  [["Q"]]
```

### Next solve approach
1. Brute Force first — try all permutations of queen placements and validate each board
2. Optimized — row-by-row backtracking DFS, tracking occupied columns and both diagonals with boolean arrays to prune invalid placements instantly

---

### Java

```java
public class Solution {

    // TODO: implement
    public List<List<String>> solveNQueens(int n) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solveNQueens(4)); // expected: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        System.out.println(sol.solveNQueens(1)); // expected: [["Q"]]
    }
}
```

### Python

```python
def solve_n_queens(n: int) -> list[list[str]]:
    # TODO: implement
    pass


print(solve_n_queens(4))  # expected: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(solve_n_queens(1))  # expected: [["Q"]]
```
