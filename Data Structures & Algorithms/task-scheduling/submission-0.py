import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        heap = []
        freq = Counter(tasks)
        cycle = 0

        # invert the frequency for max-heap
        heap = [(-count, task) for task, count in freq.items()]
        heapq.heapify(heap)

        while heap or q:
            cycle += 1

            if heap:
                count, task = heapq.heappop(heap) # pop highest count
                count += 1
                if count != 0:
                    q.append((cycle + n, count, task))

            if q and q[0][0] == cycle:
                _, count, task = q.popleft()
                heapq.heappush(heap, (count, task))
        
        return cycle
            

        


