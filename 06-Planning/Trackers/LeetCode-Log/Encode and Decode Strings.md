---
difficulty: Medium
status: Cheated
topic:
  - Arrays & Hashing
tags:
  - design
  - array
  - string
  - neetcode-150
solved: 0
last_solved: 2026-06-11
link: https://www.lintcode.com/problem/659/
---

### Problem
Design a codec that serializes a list of strings into a single string for transmission, and deserializes it back to the original list. The strings may contain any of the 256 ASCII characters, including the delimiter you choose, so the encoding scheme must be self-delimiting. Standard serialization methods like eval are not allowed.

### Constraints
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] contains any possible characters out of 256 valid ASCII characters.

### Examples
```
encode(["Hello","World"])  →  some string  →  decode  →  ["Hello","World"]
encode([""])               →  some string  →  decode  →  [""]
```

### Next solve approach
1. Brute Force first — join with a rare delimiter character (fragile, breaks if strings contain it)
2. Optimized — length-prefixed encoding: prepend each string's length as a char/int before the string so decode can always read the exact boundary

---

### Java

```java
import java.util.ArrayList;
import java.util.List;

public class Codec {

    // TODO: implement
    public String encode(List<String> strs) {
        // TODO
        return "";
    }

    // TODO: implement
    public List<String> decode(String s) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Codec codec = new Codec();

        List<String> input1 = java.util.Arrays.asList("Hello", "World");
        List<String> result1 = codec.decode(codec.encode(input1));
        System.out.println(result1); // expected: [Hello, World]

        List<String> input2 = java.util.Arrays.asList("");
        List<String> result2 = codec.decode(codec.encode(input2));
        System.out.println(result2); // expected: []
    }
}
```

### Python

Length-prefixed encoding: each string is written as `len(s) + '#' + s`. The `#` marks where the length digits end; decode reads the length, then slices exactly that many chars. Self-delimiting, so `#` inside the payload never confuses the parser.

```python
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        # ''.join is O(n); repeated += rebuilds the string each iter → O(n²)
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            delim = s.find('#', i)          # end of the length digits
            length = int(s[i:delim])
            start = delim + 1
            res.append(s[start:start + length])  # length=0 → '' (empty string preserved)
            i = start + length
        return res


codec = Codec()
print(codec.decode(codec.encode(["Hello", "World"])))  # expected: ['Hello', 'World']
print(codec.decode(codec.encode([""])))                # expected: ['']
```

**Complexity:** encode O(n) total chars, decode O(n) — single pass, `str.find` and slicing run in C.
