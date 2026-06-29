import heapq

class MedianFinder:
    def __init__(self):
        self.lower = [] # max heap
        self.upper = []

    def addNum(self, num: int) -> None: # O(log n)
        heapq.heappush(self.lower, -num) 

        if self.upper and -self.lower[0] > self.upper[0]:
            l = heapq.heappop(self.lower)
            heapq.heappush(self.upper, -l)
        
        # BALANCE:
        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) > len(self.lower) + 1:
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float: # O(1)
        if len(self.upper) > len(self.lower):
            return self.upper[0]
        elif len(self.lower) > len(self.upper):
            return -self.lower[0]
        return (-self.lower[0] + self.upper[0]) / 2