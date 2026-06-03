---
difficulty: Hard
status: Not started
topic: [Tries]
tags: [trie, array, string, backtracking, matrix, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/word-search-ii/"
---

### Problem
Given an m x n grid of characters and a list of words, find every word from the list that can be spelled by tracing a path through adjacent cells (horizontally or vertically). Each cell may be used at most once per word. Return all words that can be found on the board — order does not matter.

### Constraints
- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters
- All strings in words are unique

### Examples
```
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
→  ["eat","oath"]

board = [["a","b"],["c","d"]], words = ["abcb"]
→  []
```

### Next solve approach
1. Brute Force first — for each word, run a separate DFS/backtracking search across the entire board
2. Optimized — build a trie from all words, then run a single DFS from every cell and prune early when no trie path exists

---

### Java

```java
import java.util.ArrayList;
import java.util.List;

public class Solution {

    static class Trie {
        Trie[] children = new Trie[26];
        int ref = -1;

        public void insert(String w, int ref) {
            // TODO
        }
    }

    // TODO: implement
    public List<String> findWords(char[][] board, String[] words) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        char[][] board1 = {
            {'o','a','a','n'},
            {'e','t','a','e'},
            {'i','h','k','r'},
            {'i','f','l','v'}
        };
        String[] words1 = {"oath","pea","eat","rain"};
        System.out.println(sol.findWords(board1, words1)); // expected: [eat, oath]

        char[][] board2 = {
            {'a','b'},
            {'c','d'}
        };
        String[] words2 = {"abcb"};
        System.out.println(sol.findWords(board2, words2)); // expected: []
    }
}
```

### Python

```python
from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.ref = -1

    def insert(self, w: str, ref: int) -> None:
        # TODO: implement
        pass


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    # TODO: implement
    pass


board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words1 = ["oath","pea","eat","rain"]
print(find_words(board1, words1))  # expected: ['eat', 'oath']

board2 = [["a","b"],["c","d"]]
words2 = ["abcb"]
print(find_words(board2, words2))  # expected: []
```
