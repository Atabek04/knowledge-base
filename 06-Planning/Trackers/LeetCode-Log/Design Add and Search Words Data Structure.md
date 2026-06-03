---
difficulty: Medium
status: Not started
topic: [Tries]
tags: [dfs, design, trie, string, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/design-add-and-search-words-data-structure/"
---

### Problem
Design a `WordDictionary` that supports adding words and searching for them with wildcard support. The `search` method accepts patterns where a dot `'.'` can match any single letter, so a search for `".ad"` would match "bad", "dad", "mad", etc. Words are added without wildcards; only searches can contain dots. At most two dots will appear in any single search pattern.

### Constraints
- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters
- word in search consists of '.' or lowercase English letters
- There will be at most 2 dots in word for search queries
- At most 10^4 calls will be made to addWord and search

### Examples
```
addWord("bad"), addWord("dad"), addWord("mad")
search("pad")  →  false   (no match)
search("bad")  →  true    (exact match)
search(".ad")  →  true    (matches bad/dad/mad)
search("b..")  →  true    (matches bad)
```

### Next solve approach
1. Brute Force first — store words in a list and regex-match each one on search
2. Optimized — trie with DFS that branches across all 26 children when a '.' wildcard is encountered

---

### Java

```java
public class Solution {

    static class Trie {
        Trie[] children = new Trie[26];
        boolean isEnd;
    }

    static class WordDictionary {

        // TODO: implement
        private Trie trie;

        public WordDictionary() {
            trie = new Trie();
        }

        public void addWord(String word) {
            // TODO
        }

        public boolean search(String word) {
            // TODO
            return false;
        }
    }

    public static void main(String[] args) {
        WordDictionary wordDictionary = new WordDictionary();
        wordDictionary.addWord("bad");
        wordDictionary.addWord("dad");
        wordDictionary.addWord("mad");
        System.out.println(wordDictionary.search("pad")); // expected: false
        System.out.println(wordDictionary.search("bad")); // expected: true
        System.out.println(wordDictionary.search(".ad")); // expected: true
        System.out.println(wordDictionary.search("b..")); // expected: true
    }
}
```

### Python

```python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def add_word(self, word: str) -> None:
        # TODO: implement
        pass

    def search(self, word: str) -> bool:
        # TODO: implement
        pass


word_dictionary = WordDictionary()
word_dictionary.add_word("bad")
word_dictionary.add_word("dad")
word_dictionary.add_word("mad")
print(word_dictionary.search("pad"))  # expected: False
print(word_dictionary.search("bad"))  # expected: True
print(word_dictionary.search(".ad"))  # expected: True
print(word_dictionary.search("b.."))  # expected: True
```
