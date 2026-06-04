import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            x = heapq.heappop_max(stones)
            print(x)
            y = heapq.heappop_max(stones)
            print(y)
            if x == y:
                continue
            else:
                z = x - y
                heapq.heappush_max(stones, z)
        last = 0 if not stones else stones[0]
        return last

                


