class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])   # sort by END time

        prev_end = float('-inf')
        removals = 0
        
        for start, end in intervals:
            if start >= prev_end:            # no overlap → keep it
                prev_end = end
            else:                            # overlaps → must remove
                removals += 1
        return removals