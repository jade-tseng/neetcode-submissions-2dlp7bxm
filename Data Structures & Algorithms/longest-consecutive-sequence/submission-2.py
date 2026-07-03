class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        best = 0

        for elem in nums: 
            if elem - 1 not in seen:
                length = 1

                while elem + length in seen:
                    length += 1
                    
                best = max(best, length)

        return best

