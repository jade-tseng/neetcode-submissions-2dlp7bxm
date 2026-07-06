class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) == 1:
            return True

        intervals.sort(key=lambda x: x.start)

        for prev, curr in zip(intervals, intervals[1:]):
            if curr.start < prev.end:
                return False
        
        return True
            
            
            