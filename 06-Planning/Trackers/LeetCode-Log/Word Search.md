---
difficulty: Medium
status: Not started
topic: [Backtracking]
tags: [dfs, array, string, backtracking, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/word-search/"
---

### Problem
Given an m x n grid of characters and a target word, determine whether the word can be formed by tracing a path through adjacent (horizontally or vertically neighboring) cells. Each cell may only be used once per path. Return true if such a path exists, false otherwise.

### Constraints
- m == board.length
- n == board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consist of only lowercase and uppercase English letters

### Examples
```
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"  →  true
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"     →  true
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"    →  false  (can't reuse B)
```

### Next solve approach
1. Brute Force first — try every cell as a starting point and recursively check all directions
2. Optimized — DFS with in-place cell marking (replace with sentinel) to avoid extra visited array; restore on backtrack

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean exist(char[][] board, String word) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        char[][] board1 = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        System.out.println(sol.exist(board1, "ABCCED")); // expected: true
        char[][] board2 = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        System.out.println(sol.exist(board2, "SEE"));    // expected: true
        char[][] board3 = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        System.out.println(sol.exist(board3, "ABCB"));   // expected: false
    }
}
```

### Python

```python
def exist(board: list[list[str]], word: str) -> bool:
    # TODO: implement
    pass


board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(exist(board1, "ABCCED"))  # expected: True
board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(exist(board2, "SEE"))     # expected: True
board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(exist(board3, "ABCB"))    # expected: False
```
