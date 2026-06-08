import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)   # userId -> [(count, tweetId), ...]
        self.follows = defaultdict(set)   # userId -> {followeeIds}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1 
        self.tweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        feed = []

        self.follows[userId].add(userId)
        for p in self.follows[userId]:
            if self.tweets[p]:
                idx = len(self.tweets[p]) - 1
                count, tweetId = self.tweets[p][idx]
                heapq.heappush(heap, (count, tweetId, p, idx - 1))
        
        #push (-count, tweetId, p, last_index - 1) to the heap

        # now pop 10 times:
        while heap and len(feed) < 10:
            count, tweetId, p, next_idx = heapq.heappop(heap)
            feed.append(tweetId)

            if next_idx >= 0:
                count, tweetId = self.tweets[p][next_idx]
                heapq.heappush(heap, (count, tweetId, p, next_idx - 1))

        return feed
        # pop, append tweetId to result, and if there's a next-older tweet for that user, push it.


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        print(self.follows)      

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        print(self.follows)
