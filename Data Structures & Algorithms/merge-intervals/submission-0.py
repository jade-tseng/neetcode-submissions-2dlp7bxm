class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            # print(start, end)
            if start <= merged[-1][1]: # compare start with last elems end
                # merge these intervals: write to last entry in merged
                merged[-1] = [merged[-1][0], max(end, merged[-1][1])]
            else:
                # append un-merged interval to merged list
                merged.append([start, end])
        
        return merged
  