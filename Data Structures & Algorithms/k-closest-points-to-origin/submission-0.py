class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for p in points:
            x, y = p
            distance = x**2 + y**2
            # push to min heap:
            heapq.heappush(heap, (distance, (x, y)))

        for _ in range(k):
            distance, coordinates = heapq.heappop(heap)
            result.append(coordinates)

        return result