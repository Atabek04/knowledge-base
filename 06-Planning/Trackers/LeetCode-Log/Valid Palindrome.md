---
difficulty: Easy
status: Not started
topic: [Two Pointers]
tags: [two-pointers, string, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/valid-palindrome/"
---

### Problem
A string is a palindrome if, after lowercasing all letters and stripping every non-alphanumeric character, it reads the same forwards and backwards. Given a string `s`, return `true` if it is a palindrome, or `false` otherwise. An empty string (after cleaning) is considered a palindrome. Only letters and digits count — spaces, punctuation, and symbols are ignored.

### Constraints
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

### Examples
```
"A man, a plan, a canal: Panama"  →  true     ("amanaplanacanalpanama" is a palindrome)
"race a car"                      →  false    ("raceacar" is not a palindrome)
" "                               →  true     (empty after stripping non-alphanumeric chars)
```

### Next solve approach
1. Brute Force first — filter out non-alphanumeric characters, lowercase, then compare string to its reverse.
2. Optimized — two pointers from both ends, skip non-alphanumeric, compare characters in-place (O(n) time, O(1) space).

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean isPalindrome(String s) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isPalindrome("A man, a plan, a canal: Panama")); // expected: true
        System.out.println(sol.isPalindrome("race a car"));                     // expected: false
        System.out.println(sol.isPalindrome(" "));                              // expected: true
    }
}
```

### Python

```python
def is_palindrome(s: str) -> bool:
    # TODO: implement
    pass


print(is_palindrome("A man, a plan, a canal: Panama"))  # expected: True
print(is_palindrome("race a car"))                      # expected: False
print(is_palindrome(" "))                               # expected: True
```
