class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #memo = {} # store subproblem
        # init dp table:
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
        
        for rem in range(1, amount + 1):
            for c in coins:
                if rem - c >= 0: 
                    dp[rem] = min(dp[rem], dp[rem - c] + 1)   # same combine + cost

        return dp[amount] if dp[amount] != float('inf') else -1

        # def dfs(rem):
        #     # base cases:
        #     if rem in memo:
        #         return memo[rem]
        #     if rem == 0:
        #         return 0
        #     if rem < 0:
        #         return float('inf')
        #     best = float('inf')

        #     for c in coins:
        #         subproblem = rem - c
        #         if subproblem < 0: 
        #             continue
        #         result = dfs(subproblem)  # min coins for the smaller amount
        #         best = min(best, result + 1)                 # +1 for coin c

        #     memo[rem] = best
        #     return best

        # result = dfs(amount)
        # return result if result != float('inf') else -1