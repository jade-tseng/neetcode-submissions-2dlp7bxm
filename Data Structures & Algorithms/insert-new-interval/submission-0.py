class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        check if newInterval[0] > intervals[-1][1] :
        we iterate over intervals until we find a value 'end' < newInterval[0] and 'start' < newInterval[1]
        if overlap: merge
        """
        result = []
        i = 0
        n = len(intervals)

        # phase 1: add all intervals that end before newInterval starts (no overlap, come first)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # phase 2: merge all intervals that overlap with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        result.append(newInterval)

        # phase 3: add whatever's left (comes after, no overlap)
        while i < n:
            result.append(intervals[i])
            i += 1

        return result