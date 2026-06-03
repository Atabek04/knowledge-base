---
difficulty: Medium
status: Cheated
topic:
  - Arrays & Hashing
tags:
  - array
  - hash-table
  - string
  - sorting
  - neetcode-150
solved: 0
last_solved: 2026-06-02
link: https://leetcode.com/problems/group-anagrams/
---

### Problem
Given an array of strings, group all anagrams together and return the groups in any order. Two strings are anagrams if one can be rearranged to form the other — they share the same sorted character sequence. Each group must contain all strings from the input that are mutual anagrams.

### Constraints
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

### Examples
```
strs = ["eat","tea","tan","ate","nat","bat"]  →  [["bat"],["nat","tan"],["ate","eat","tea"]]
strs = [""]                                   →  [[""]]
strs = ["a"]                                  →  [["a"]]
```

### Next solve approach
1. Brute Force first — for each string compare sorted version to every other string, O(n² * k log k)
2. Optimized — hash map keyed by sorted string (or char-count tuple); O(n * k log k)

---

### Java

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {

    // TODO: implement
    public List<List<String>> groupAnagrams(String[] strs) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.groupAnagrams(new String[]{"eat", "tea", "tan", "ate", "nat", "bat"}));
        // expected: [["bat"],["nat","tan"],["ate","eat","tea"]] (any order)
        System.out.println(s.groupAnagrams(new String[]{""}));   // expected: [[""]]
        System.out.println(s.groupAnagrams(new String[]{"a"}));  // expected: [["a"]]
    }
}
```

### Python

```python
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    # TODO: implement
    pass


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# expected: [["bat"],["nat","tan"],["ate","eat","tea"]] (any order)
print(group_anagrams([""]))   # expected: [[""]]
print(group_anagrams(["a"]))  # expected: [["a"]]
```
