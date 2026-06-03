---
difficulty: Medium
status: Not started
topic: [Tries]
tags: [design, trie, hash-table, string, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/implement-trie-prefix-tree/"
---

### Problem
A trie (pronounced "try"), also called a prefix tree, is a tree structure designed to store and retrieve strings efficiently. You need to implement the `Trie` class with three operations: inserting a word, searching for an exact word, and checking whether any stored word starts with a given prefix. The trie is especially useful for applications like autocomplete and spellcheckers where prefix lookups are frequent.

### Constraints
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith

### Examples
```
insert("apple"), search("apple")   →  true    (exact match)
insert("apple"), search("app")     →  false   (not inserted yet)
insert("apple"), startsWith("app") →  true    (prefix exists)
insert("apple"), insert("app"), search("app") →  true
```

### Next solve approach
1. Brute Force first — store all words in a HashSet, iterate to check prefix matches
2. Optimized — build a trie where each node holds a 26-slot children array and an isEnd flag

---

### Java

```java
public class Solution {

    static class Trie {
        private Trie[] children;
        private boolean isEnd;

        // TODO: implement
        public Trie() {
            children = new Trie[26];
        }

        public void insert(String word) {
            // TODO
        }

        public boolean search(String word) {
            // TODO
            return false;
        }

        public boolean startsWith(String prefix) {
            // TODO
            return false;
        }
    }

    public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insert("apple");
        System.out.println(trie.search("apple"));   // expected: true
        System.out.println(trie.search("app"));     // expected: false
        System.out.println(trie.startsWith("app")); // expected: true
        trie.insert("app");
        System.out.println(trie.search("app"));     // expected: true
    }
}
```

### Python

```python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        # TODO: implement
        pass

    def search(self, word: str) -> bool:
        # TODO: implement
        pass

    def starts_with(self, prefix: str) -> bool:
        # TODO: implement
        pass


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))    # expected: True
print(trie.search("app"))      # expected: False
print(trie.starts_with("app")) # expected: True
trie.insert("app")
print(trie.search("app"))      # expected: True
```
