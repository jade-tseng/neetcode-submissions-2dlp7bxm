import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)

        heap = [0]
        rooms = len(heap)
        intervals.sort(key=lambda iv: iv.start)

        for i in intervals:
            if heap[0] <= i.start:
                heapq.heappop(heap)
                heapq.heappush(heap, i.end)
                rooms = max(rooms, len(heap))

            else:
                heapq.heappush(heap, i.end)
                rooms = max(rooms, len(heap))

        return rooms

    