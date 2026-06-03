---
difficulty: Medium
status: Not started
topic: [Math & Geometry]
tags: [math, string, simulation, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/multiply-strings/"
---

### Problem
Given two non-negative integers represented as strings num1 and num2, return their product also as a string. You must not use any built-in big integer library or convert the strings directly to integers. Instead, simulate the grade-school digit-by-digit multiplication algorithm, accumulating partial products into a result array of length m+n.

### Constraints
- 1 <= num1.length, num2.length <= 200
- num1 and num2 consist of digits only
- Both num1 and num2 do not contain any leading zero, except the number 0 itself

### Examples
```
num1="2", num2="3"    →  "6"
num1="123", num2="456"  →  "56088"
```

### Next solve approach
1. Brute Force first — multiply digit by digit into a positional array, then propagate carries
2. Optimized — same O(m*n) approach is the standard; allocate result array of size m+n upfront

---

### Java

```java
public class Solution {

    // TODO: implement
    public String multiply(String num1, String num2) {
        // TODO
        return "";
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.multiply("2", "3"));      // expected: "6"
        System.out.println(sol.multiply("123", "456"));  // expected: "56088"
    }
}
```

### Python

```python
def multiply(num1: str, num2: str) -> str:
    # TODO: implement
    pass


print(multiply("2", "3"))     # expected: "6"
print(multiply("123", "456")) # expected: "56088"
```
