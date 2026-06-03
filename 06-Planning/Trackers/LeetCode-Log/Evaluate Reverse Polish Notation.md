---
difficulty: Medium
status: Not started
topic: [Stack]
tags: [stack, array, math, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/evaluate-reverse-polish-notation/"
---

### Problem
You are given a sequence of tokens representing an arithmetic expression in Reverse Polish Notation (postfix), where operands come before their operator. Evaluate the expression and return the integer result. Division truncates toward zero, and all intermediate values fit within a 32-bit integer.

### Constraints
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator `+`, `-`, `*`, `/`, or an integer in the range [-200, 200].

### Examples
```
["2","1","+","3","*"]                                          →  9    (((2+1)*3) = 9)
["4","13","5","/","+"]                                         →  6    ((4+(13/5)) = 6)
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]      →  22
```

### Next solve approach
1. Brute Force first — convert to infix, parse with standard operator precedence rules
2. Optimized — stack: push numbers, pop two operands when operator is encountered and push result

---

### Java

```java
public class Solution {

    // TODO: implement
    public int evalRPN(String[] tokens) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.evalRPN(new String[]{"2", "1", "+", "3", "*"}));
        // expected: 9

        System.out.println(sol.evalRPN(new String[]{"4", "13", "5", "/", "+"}));
        // expected: 6

        System.out.println(sol.evalRPN(new String[]{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}));
        // expected: 22
    }
}
```

### Python

```python
from typing import List


def eval_rpn(tokens: List[str]) -> int:
    # TODO: implement
    pass


print(eval_rpn(["2", "1", "+", "3", "*"]))                                            # expected: 9
print(eval_rpn(["4", "13", "5", "/", "+"]))                                           # expected: 6
print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # expected: 22
```
