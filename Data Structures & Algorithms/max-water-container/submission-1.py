class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        water = (j - i) * min(height[j], height[i])
        """
        i, j = 0, len(heights) - 1
        current_max = 0

        while i < j:
            water = (j - i) * min(heights[j], heights[i])

            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1

            current_max = max(water, current_max)
        
        return current_max

            

