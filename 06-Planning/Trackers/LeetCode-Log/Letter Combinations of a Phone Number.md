---
difficulty: Medium
status: Not started
topic: [Backtracking]
tags: [hash-table, string, backtracking, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/letter-combinations-of-a-phone-number/"
---

### Problem
Given a string of digits (2–9), return all possible letter combinations that the digit sequence could represent on a phone keypad. Each digit maps to a set of letters just like on a telephone (e.g. 2 maps to "abc", 9 maps to "wxyz"). The answer can be in any order.

### Constraints
- 1 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9']

### Examples
```
digits = "23"  →  ["ad","ae","af","bd","be","bf","cd","ce","cf"]
digits = "2"   →  ["a","b","c"]
```

### Next solve approach
1. Brute Force first — iteratively expand combinations digit by digit using nested loops
2. Optimized — backtracking DFS through digits, appending each possible letter and recursing to the next digit

---

### Java

```java
public class Solution {

    // TODO: implement
    public List<String> letterCombinations(String digits) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.letterCombinations("23")); // expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        System.out.println(sol.letterCombinations("2"));  // expected: ["a","b","c"]
    }
}
```

### Python

```python
def letter_combinations(digits: str) -> list[str]:
    # TODO: implement
    pass


print(letter_combinations("23"))  # expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letter_combinations("2"))   # expected: ["a","b","c"]
```
