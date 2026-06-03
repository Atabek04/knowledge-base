---
difficulty: Hard
status: Not started
topic: [Advanced Graphs]
tags: [dfs, graph, array, string, sorting, eulerian-circuit, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/reconstruct-itinerary/"
---

### Problem
Given a list of airline tickets where each ticket is a [from, to] pair, reconstruct the full travel itinerary starting from "JFK". Every ticket must be used exactly once. If multiple valid itineraries exist, return the one that is lexicographically smallest when the airport codes are read as a single string.

### Constraints
- 1 <= tickets.length <= 300
- tickets[i].length == 2
- fromi.length == 3
- toi.length == 3
- fromi and toi consist of uppercase English letters
- fromi != toi

### Examples
```
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]  →  ["JFK","MUC","LHR","SFO","SJC"]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]  →  ["JFK","ATL","JFK","SFO","ATL","SFO"]   (lexicographically smallest)
```

### Next solve approach
1. Brute Force first — try all permutations of tickets, check validity, pick lexicographically smallest
2. Optimized — Hierholzer's algorithm for Eulerian path: DFS with sorted adjacency lists, post-order append then reverse

---

### Java

```java
import java.util.*;

public class Solution {

    private Map<String, List<String>> g = new HashMap<>();
    private List<String> ans = new ArrayList<>();

    // TODO: implement
    public List<String> findItinerary(List<List<String>> tickets) {
        // TODO
        return new ArrayList<>();
    }

    private void dfs(String f) {
        // TODO
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        List<List<String>> tickets1 = Arrays.asList(
            Arrays.asList("MUC","LHR"),
            Arrays.asList("JFK","MUC"),
            Arrays.asList("SFO","SJC"),
            Arrays.asList("LHR","SFO")
        );
        System.out.println(sol.findItinerary(tickets1)); // expected: [JFK, MUC, LHR, SFO, SJC]

        sol = new Solution();
        List<List<String>> tickets2 = Arrays.asList(
            Arrays.asList("JFK","SFO"),
            Arrays.asList("JFK","ATL"),
            Arrays.asList("SFO","ATL"),
            Arrays.asList("ATL","JFK"),
            Arrays.asList("ATL","SFO")
        );
        System.out.println(sol.findItinerary(tickets2)); // expected: [JFK, ATL, JFK, SFO, ATL, SFO]
    }
}
```

### Python

```python
from typing import List
from collections import defaultdict

def find_itinerary(tickets: List[List[str]]) -> List[str]:
    # TODO: implement
    pass


print(find_itinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))  # expected: ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
print(find_itinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))  # expected: ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
```
