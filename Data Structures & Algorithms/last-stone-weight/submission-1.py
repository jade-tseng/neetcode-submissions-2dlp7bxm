import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        print(stones)
        while len(stones) >= 2:
            x = heapq.heappop_max(stones)
            print(x)
            y = heapq.heappop_max(stones)
            print(y)
            if x == y:
                continue
            else:
                z = x - y
                print(z)
                heapq.heappush_max(stones, z)
                print(stones)
        last = 0 if not stones else stones[0]
        return last

                


