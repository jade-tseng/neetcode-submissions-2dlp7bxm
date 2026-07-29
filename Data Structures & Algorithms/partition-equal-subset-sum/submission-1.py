class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        
        target = totalSum // 2 

        memo = {} # state: (i, remaining) // cache on the pair since index can be reached with diff remaining (Target)
        
        def dfs(i, target):
        # base cases:
            if i >= len(nums):
                return target == 0 
            if target < 0:
                return False
        
            # check memo:
            if (i, target) in memo:
                return memo[(i, target)] 

            include = dfs(i + 1, target - nums[i])
            skip    = dfs(i + 1, target)
            result  = include or skip

            # store result before returning
            memo[(i, target)] = result
            return result
        
        return dfs(0, target)
