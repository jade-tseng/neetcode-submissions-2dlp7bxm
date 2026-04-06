class Solution:
    def trap(self, height: List[int]) -> int:
        # The formula for the trapped water at index i is given by:
        # min(height[l], height[r]) - height[i]

        i, j = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while i < j:
            if height[i] < height[j]:
                left_max = max(left_max, height[i])
                water += left_max - height[i]
                i += 1
            else:
                right_max = max(right_max, height[j])
                water += right_max - height[j]
                j -= 1
        
        return water
