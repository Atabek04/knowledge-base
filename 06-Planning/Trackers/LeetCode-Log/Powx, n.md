---
difficulty: Medium
status: Not started
topic: [Math & Geometry]
tags: [recursion, math, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/powx-n/"
---

### Problem
Implement pow(x, n), which raises the floating-point number x to the integer power n. The exponent n can be negative, meaning you compute 1 / x^|n|. A naive loop would time out for large n — the efficient approach is fast exponentiation (binary exponentiation), which halves the problem at every step.

### Constraints
- -100.0 < x < 100.0
- -2^31 <= n <= 2^31 - 1
- n is an integer
- Either x is not zero or n > 0
- -10^4 <= x^n <= 10^4

### Examples
```
x=2.00000, n=10   →  1024.00000
x=2.10000, n=3    →  9.26100
x=2.00000, n=-2   →  0.25000   (2^-2 = 1/4 = 0.25)
```

### Next solve approach
1. Brute Force first — multiply x by itself n times (O(n), will TLE for large n)
2. Optimized — fast power (binary exponentiation): square x and halve n each iteration, O(log n)

---

### Java

```java
public class Solution {

    // TODO: implement
    public double myPow(double x, int n) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.myPow(2.00000, 10));  // expected: 1024.0
        System.out.println(sol.myPow(2.10000, 3));   // expected: ~9.261
        System.out.println(sol.myPow(2.00000, -2));  // expected: 0.25
    }
}
```

### Python

```python
def my_pow(x: float, n: int) -> float:
    # TODO: implement
    pass


print(my_pow(2.0, 10))   # expected: 1024.0
print(my_pow(2.1, 3))    # expected: ~9.261
print(my_pow(2.0, -2))   # expected: 0.25
```
