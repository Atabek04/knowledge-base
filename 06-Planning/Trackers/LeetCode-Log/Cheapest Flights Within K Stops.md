---
difficulty: Medium
status: Not started
topic: [Advanced Graphs]
tags: [dfs, bfs, graph, dynamic-programming, shortest-path, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/cheapest-flights-within-k-stops/"
---

### Problem
There are n cities connected by directed flights. Each flight has a source city, destination city, and a ticket price. Given a source src, destination dst, and a maximum number of intermediate stops k, return the cheapest total price to fly from src to dst using at most k stops. If no valid route exists, return -1.

### Constraints
- 2 <= n <= 100
- 0 <= flights.length <= n * (n - 1) / 2
- flights[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= pricei <= 10^4
- No multiple flights between the same pair of cities
- 0 <= src, dst, k < n
- src != dst

### Examples
```
n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src=0, dst=3, k=1  →  700   (0→1→3, cheapest with at most 1 stop)
n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1                      →  200   (0→1→2)
n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=0                      →  500   (direct only)
```

### Next solve approach
1. Brute Force first — DFS/BFS exploring all paths up to k+1 edges, tracking minimum cost
2. Optimized — Bellman-Ford limited to k+1 relaxation rounds, copying dist array each round to avoid using edges from the same round

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.findCheapestPrice(4,
            new int[][]{{0,1,100},{1,2,100},{2,0,100},{1,3,600},{2,3,200}}, 0, 3, 1)); // expected: 700

        System.out.println(sol.findCheapestPrice(3,
            new int[][]{{0,1,100},{1,2,100},{0,2,500}}, 0, 2, 1)); // expected: 200

        System.out.println(sol.findCheapestPrice(3,
            new int[][]{{0,1,100},{1,2,100},{0,2,500}}, 0, 2, 0)); // expected: 500
    }
}
```

### Python

```python
from typing import List

def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # TODO: implement
    pass


print(find_cheapest_price(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))  # expected: 700
print(find_cheapest_price(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))                       # expected: 200
print(find_cheapest_price(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))                       # expected: 500
```
