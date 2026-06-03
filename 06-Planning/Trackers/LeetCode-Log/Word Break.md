---
difficulty: Medium
status: Not started
topic: [1-D Dynamic Programming]
tags: [trie, memoization, array, hash-table, string, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/word-break/"
---

### Problem
Given a string s and a dictionary of words, determine whether s can be split into a sequence of one or more dictionary words separated by spaces. Dictionary words may be reused multiple times. Return true if such a segmentation exists, false otherwise.

### Constraints
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters
- All strings in wordDict are unique

### Examples
```
s = "leetcode", wordDict = ["leet","code"]                     →  true    ("leet code")
s = "applepenapple", wordDict = ["apple","pen"]                →  true    ("apple pen apple")
s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]  →  false
```

### Next solve approach
1. Brute Force first — recursively try every prefix at each position to see if it's in the dictionary
2. Optimized — bottom-up DP array where dp[i] = can s[0..i] be segmented; check all j < i where dp[j] is true and s[j..i] is in the dict set

---

### Java

```java
import java.util.List;
import java.util.Arrays;

public class Solution {

    // TODO: implement
    public boolean wordBreak(String s, List<String> wordDict) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.wordBreak("leetcode", Arrays.asList("leet", "code")));                          // expected: true
        System.out.println(sol.wordBreak("applepenapple", Arrays.asList("apple", "pen")));                     // expected: true
        System.out.println(sol.wordBreak("catsandog", Arrays.asList("cats", "dog", "sand", "and", "cat")));   // expected: false
    }
}
```

### Python

```python
from typing import List

def word_break(s: str, word_dict: List[str]) -> bool:
    # TODO: implement
    pass


print(word_break("leetcode", ["leet", "code"]))                          # expected: True
print(word_break("applepenapple", ["apple", "pen"]))                     # expected: True
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))   # expected: False
```
