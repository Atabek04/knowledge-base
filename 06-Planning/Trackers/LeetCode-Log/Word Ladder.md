---
difficulty: Hard
status: Not started
topic: [Graphs]
tags: [bfs, hash-table, string, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/word-ladder/"
---

### Problem
Given a beginWord, an endWord, and a wordList dictionary, find the length of the shortest transformation sequence from beginWord to endWord where each step changes exactly one letter and every intermediate word must be in wordList. Return the number of words in the shortest sequence, or 0 if no sequence exists.

### Constraints
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters
- beginWord != endWord
- All words in wordList are unique

### Examples
```
beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]  →  5    (hit->hot->dot->dog->cog)
beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]        →  0    (cog not in wordList)
```

### Next solve approach
1. Brute Force first — BFS from beginWord; at each step try all single-character mutations, enqueue those in wordList
2. Optimized — bidirectional BFS from both beginWord and endWord simultaneously, expanding the smaller frontier each round; reduces search space from O(b^d) to O(b^(d/2))

---

### Java

```java
import java.util.Arrays;
import java.util.List;

public class Solution {

    // TODO: implement
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.ladderLength("hit", "cog",
            Arrays.asList("hot","dot","dog","lot","log","cog"))); // expected: 5

        System.out.println(sol.ladderLength("hit", "cog",
            Arrays.asList("hot","dot","dog","lot","log")));       // expected: 0
    }
}
```

### Python

```python
def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    # TODO: implement
    pass


print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # expected: 5
print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log"]))        # expected: 0
```
