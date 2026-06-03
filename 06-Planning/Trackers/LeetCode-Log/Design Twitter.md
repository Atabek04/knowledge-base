---
difficulty: Medium
status: Not started
topic: [Heap / Priority Queue]
tags: [design, hash-table, linked-list, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/design-twitter/"
---

### Problem
Design a simplified Twitter where users can post tweets, follow or unfollow other users, and retrieve their news feed. The news feed returns the 10 most recent tweet IDs from the user themselves and everyone they follow, ordered newest first.

### Constraints
- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 10^4
- All tweet IDs are unique
- At most 3 * 10^4 calls across all methods
- A user cannot follow themselves

### Examples
```
postTweet(1,5), getNewsFeed(1)             →  [5]
follow(1,2), postTweet(2,6), getNewsFeed(1) →  [6,5]
unfollow(1,2), getNewsFeed(1)              →  [5]
```

### Next solve approach
1. Brute Force first — store all tweets with timestamps, filter by followed users, sort, take top 10
2. Optimized — per-user tweet lists + max-heap merging last 10 from each followed user's list

---

### Java

```java
import java.util.*;

public class Solution {

    static class Twitter {

        // TODO: implement
        public Twitter() {
            // TODO
        }

        public void postTweet(int userId, int tweetId) {
            // TODO
        }

        public List<Integer> getNewsFeed(int userId) {
            // TODO
            return new ArrayList<>();
        }

        public void follow(int followerId, int followeeId) {
            // TODO
        }

        public void unfollow(int followerId, int followeeId) {
            // TODO
        }
    }

    public static void main(String[] args) {
        Twitter twitter = new Twitter();
        twitter.postTweet(1, 5);
        System.out.println(twitter.getNewsFeed(1));  // expected: [5]
        twitter.follow(1, 2);
        twitter.postTweet(2, 6);
        System.out.println(twitter.getNewsFeed(1));  // expected: [6, 5]
        twitter.unfollow(1, 2);
        System.out.println(twitter.getNewsFeed(1));  // expected: [5]
    }
}
```

### Python

```python
from typing import List

class Twitter:
    def __init__(self):
        # TODO: implement
        pass

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        # TODO
        pass

    def get_news_feed(self, user_id: int) -> List[int]:
        # TODO
        pass

    def follow(self, follower_id: int, followee_id: int) -> None:
        # TODO
        pass

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        # TODO
        pass


twitter = Twitter()
twitter.post_tweet(1, 5)
print(twitter.get_news_feed(1))   # expected: [5]
twitter.follow(1, 2)
twitter.post_tweet(2, 6)
print(twitter.get_news_feed(1))   # expected: [6, 5]
twitter.unfollow(1, 2)
print(twitter.get_news_feed(1))   # expected: [5]
```
