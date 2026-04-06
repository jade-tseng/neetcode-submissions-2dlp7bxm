class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Output: 36, with index 1 and 7 (7 and 6 vals) , or 6 * 6
        # we initialize pointers i, j = 0, len(height) - 1
        i, j = 0, len(heights) - 1
        result = 0

        while i < j:
            h = min(heights[i], heights[j])
            w = j - i
            result = max(result, h * w)
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return result