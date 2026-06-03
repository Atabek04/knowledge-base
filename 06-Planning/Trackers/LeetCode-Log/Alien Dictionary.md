---
difficulty: Hard
status: Not started
topic: [Topological Sort, Graphs, Strings]
tags: [topological-sort, graph, string, grokking-patterns, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/alien-dictionary/"
---

### Problem
You are given a list of words sorted lexicographically according to the rules of an unknown alien language. By comparing adjacent words character by character, deduce the relative ordering of characters in that language and return one valid character ordering as a string. If no consistent ordering exists, return an empty string.

### Constraints
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 100
- All characters are lowercase English letters
- The input is sorted per the alien language rules

### Examples
```
["ba","bc","ac","cab"]                →  "bac"    (a<c from ba/bc, b<a from bc/ac → bac)
["cab","aaa","aab"]                   →  "cab"    (c<a from cab/aaa, a<b from aaa/aab → cab)
["ywx","wz","xww","xz","zyy","zwz"]   →  "ywxz"   (y<w, w<x, w<z, x<z → ywxz)
```

### Next solve approach
1. Brute Force first — compare every adjacent word pair to extract ordering rules, then try all permutations to find one satisfying all rules
2. Optimized (Topological Sort) — build a directed char graph from adjacent word comparisons, run Kahn's BFS to get topological order; detect cycles → return ""

---

### Java

```java
import java.util.*;

class AlienDictionary {

    // TODO: implement
    public static String findOrder(String[] words) {
        // TODO
        return "";
    }

    public static void main(String[] args) {
        System.out.println("Character order: " +
            AlienDictionary.findOrder(new String[] { "ba", "bc", "ac", "cab" }));
        // expected: bac

        System.out.println("Character order: " +
            AlienDictionary.findOrder(new String[] { "cab", "aaa", "aab" }));
        // expected: cab

        System.out.println("Character order: " +
            AlienDictionary.findOrder(new String[] { "ywx", "wz", "xww", "xz", "zyy", "zwz" }));
        // expected: ywxz
    }
}
```

### Python

```python
def find_order(words: list[str]) -> str:
    # TODO: implement
    pass


print(find_order(["ba", "bc", "ac", "cab"]))               # expected: bac
print(find_order(["cab", "aaa", "aab"]))                   # expected: cab
print(find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))  # expected: ywxz
```
