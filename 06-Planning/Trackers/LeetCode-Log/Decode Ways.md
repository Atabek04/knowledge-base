---
difficulty: Medium
status: Not started
topic: [1-D Dynamic Programming]
tags: [string, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/decode-ways/"
---

### Problem
A string of digits encodes letters where "1" maps to 'A', "2" to 'B', ..., "26" to 'Z'. Given an encoded string, count the total number of distinct ways it can be decoded. A '0' by itself or a two-digit number above 26 is invalid; leading zeros make a decoding invalid. Return the total count, or 0 if no valid decoding exists.

### Constraints
- 1 <= s.length <= 100
- s contains only digits and may contain leading zeros

### Examples
```
s = "12"   →  2    ("AB" or "L")
s = "226"  →  3    ("BZ", "VF", or "BBF")
s = "06"   →  0    (leading zero, invalid)
```

### Next solve approach
1. Brute Force first — recursively try decoding 1-digit and 2-digit chunks at each position, memoize results
2. Optimized — bottom-up DP array where dp[i] counts decodings of s[0..i]; add dp[i-1] if s[i-1] != '0', add dp[i-2] if s[i-2..i-1] is between 10 and 26

---

### Java

```java
public class Solution {

    // TODO: implement
    public int numDecodings(String s) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.numDecodings("12"));  // expected: 2
        System.out.println(sol.numDecodings("226")); // expected: 3
        System.out.println(sol.numDecodings("06"));  // expected: 0
    }
}
```

### Python

```python
def num_decodings(s: str) -> int:
    # TODO: implement
    pass


print(num_decodings("12"))  # expected: 2
print(num_decodings("226")) # expected: 3
print(num_decodings("06"))  # expected: 0
```
