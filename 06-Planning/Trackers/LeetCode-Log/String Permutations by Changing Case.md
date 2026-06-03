---
difficulty: Medium
status: Not started
topic: [Subsets, Strings, Backtracking]
tags: [subsets, string, backtracking, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a string, generate all permutations by toggling the case of each letter while keeping the character sequence unchanged. Digits stay as-is. Each letter independently contributes a lowercase and uppercase branch, producing up to 2^(letter count) results.

### Constraints
- 1 <= str.length <= 12
- String contains ASCII letters and digits only
- Digit characters do not change

### Examples
```
"ad52"  →  "ad52", "Ad52", "aD52", "AD52"
"ab7c"  →  "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
```

### Next solve approach
1. Brute Force first — recursive DFS, at each letter branch into lowercase and uppercase variants
2. Optimized (Subsets/BFS) — start with the string in a list; for each letter, duplicate all current strings and toggle case in the new copies

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static List<String> findLetterCaseStringPermutations(String str) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        System.out.println(findLetterCaseStringPermutations("ad52"));
        // expected: [ad52, Ad52, aD52, AD52]
        System.out.println(findLetterCaseStringPermutations("ab7c"));
        // expected: [ab7c, Ab7c, aB7c, AB7c, ab7C, Ab7C, aB7C, AB7C]
    }
}
```

### Python

```python
def find_letter_case_string_permutations(str: str) -> list[str]:
    # TODO: implement
    pass


print(find_letter_case_string_permutations("ad52"))  # expected: ['ad52', 'Ad52', 'aD52', 'AD52']
print(find_letter_case_string_permutations("ab7c"))  # expected: ['ab7c', 'Ab7c', 'aB7c', 'AB7c', 'ab7C', 'Ab7C', 'aB7C', 'AB7C']
```
