class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # init dp array
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2, len(dp)): # no base cases here bc already baked into 0 initialized dp array            
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]