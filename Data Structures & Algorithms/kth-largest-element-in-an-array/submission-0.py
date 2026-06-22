import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we push k elements onto a min heap where heap[0] is the kth element
        heap = []
        # heapq.heapify(nums)

        for n in nums:
            heapq.heappush(heap, n)

        while len(heap) > k:
            heapq.heappop(heap)      # evict the weakest of the club
        return heap[0]                   # kth largest
