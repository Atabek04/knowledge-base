---
difficulty: Hard
status: Not started
topic: [Subsets, Strings, Backtracking, Bit Manipulation]
tags: [subsets, string, backtracking, bit-manipulation, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a word, generate all unique generalized abbreviations. An abbreviation replaces any contiguous substring with the count of its characters — for example "BAT" → "B2" replaces "AT" with 2. Every possible combination of replaced and kept characters must appear in the output exactly once.

### Constraints
- 1 <= word.length <= 15
- word contains only ASCII letters
- Output has exactly 2^word.length entries

### Examples
```
"BAT"   →  "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"
"code"  →  "code", "cod1", "co1e", "co2", "c1de", "c1d1", "c2e", "c3",
            "1ode", "1od1", "1o1e", "1o2", "2de", "2d1", "3e", "4"
```

### Next solve approach
1. Brute Force first — iterate all 2^N bitmasks; '0' = keep char, '1' = abbreviate; compress consecutive 1-bits into their count
2. Optimized (Subsets/Backtracking) — at each position branch: keep the character (flush any running count first) OR increment running count; flush at end of string

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static List<String> generateGeneralizedAbbreviation(String word) {
        // TODO
        return new ArrayList<String>();
    }

    public static void main(String[] args) {
        System.out.println(generateGeneralizedAbbreviation("BAT"));
        // expected: [BAT, BA1, B1T, B2, 1AT, 1A1, 2T, 3]
        System.out.println(generateGeneralizedAbbreviation("code"));
        // expected: [code, cod1, co1e, co2, c1de, c1d1, c2e, c3, 1ode, 1od1, 1o1e, 1o2, 2de, 2d1, 3e, 4]
    }
}
```

### Python

```python
def generate_generalized_abbreviation(word: str) -> list[str]:
    # TODO: implement
    pass


print(generate_generalized_abbreviation("BAT"))
# expected: ['BAT', 'BA1', 'B1T', 'B2', '1AT', '1A1', '2T', '3']
print(generate_generalized_abbreviation("code"))
# expected: ['code', 'cod1', 'co1e', 'co2', 'c1de', 'c1d1', 'c2e', 'c3', '1ode', '1od1', '1o1e', '1o2', '2de', '2d1', '3e', '4']
```
