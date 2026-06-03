---
difficulty: Medium
status: Not started
topic: [Graphs]
tags: [dfs, bfs, union-find, array, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/surrounded-regions/"
---

### Problem
Given an m x n board of 'X' and 'O' characters, capture all regions of 'O' that are completely surrounded by 'X'. A region is surrounded if none of its 'O' cells touch the board's border. Replace all captured 'O' cells with 'X' in-place.

### Constraints
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'

### Examples
```
[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]  →  [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
[["X"]]  →  [["X"]]
```

### Next solve approach
1. Brute Force first — find all 'O' regions via DFS, check if any cell in the region touches a border; if not, flip to 'X'
2. Optimized — DFS/BFS from every 'O' on the border, mark safe cells with a temporary marker '.'; then flip remaining 'O' to 'X' and restore '.' to 'O'

---

### Java

```java
import java.util.Arrays;

public class Solution {

    // TODO: implement
    public void solve(char[][] board) {
        // TODO
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        char[][] board1 = {
            {'X','X','X','X'},
            {'X','O','O','X'},
            {'X','X','O','X'},
            {'X','O','X','X'}
        };
        sol.solve(board1);
        System.out.println(Arrays.deepToString(board1));
        // expected: [[X,X,X,X],[X,X,X,X],[X,X,X,X],[X,O,X,X]]

        char[][] board2 = {{'X'}};
        sol.solve(board2);
        System.out.println(Arrays.deepToString(board2)); // expected: [[X]]
    }
}
```

### Python

```python
def solve(board: list[list[str]]) -> None:
    # TODO: implement
    pass


board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(board1)
print(board1)  # expected: [['X','X','X','X'],['X','X','X','X'],['X','X','X','X'],['X','O','X','X']]
```
