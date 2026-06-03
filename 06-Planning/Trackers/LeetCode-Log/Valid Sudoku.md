---
difficulty: Medium
status: Not started
topic: [Arrays & Hashing]
tags: [array, hash-table, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/valid-sudoku/"
---

### Problem
Determine whether a partially filled 9x9 Sudoku board is valid according to three rules: each row, each column, and each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition. Empty cells are marked with '.'. A board can be valid yet still unsolvable — only the filled cells need to satisfy the rules.

### Constraints
- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'.

### Examples
```
board (standard valid Sudoku)  →  true
board (8 in top-left, duplicate 8 in top-left 3x3 box)  →  false
```

### Next solve approach
1. Brute Force first — for each row/col/box collect digits and check for duplicates using sets, O(81)
2. Optimized — single pass with three 9x9 boolean arrays (row, col, box); compute box index as i/3*3 + j/3, O(81)

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean isValidSudoku(char[][] board) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        char[][] valid = {
            {'5','3','.','.','7','.','.','.','.'},
            {'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},
            {'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},
            {'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},
            {'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}
        };
        System.out.println(s.isValidSudoku(valid)); // expected: true

        char[][] invalid = {
            {'8','3','.','.','7','.','.','.','.'},
            {'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},
            {'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},
            {'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},
            {'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}
        };
        System.out.println(s.isValidSudoku(invalid)); // expected: false
    }
}
```

### Python

```python
from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    # TODO: implement
    pass


valid = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],
]
print(is_valid_sudoku(valid))  # expected: True

invalid = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],
]
print(is_valid_sudoku(invalid))  # expected: False
```
