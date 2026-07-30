class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {} # store subproblem

        def dfs(rem):
            # base cases:
            if rem in memo:
                return memo[rem]
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            best = float('inf')
            for c in coins:
                subproblem = rem - c
                if subproblem < 0: 
                    continue
                result = dfs(subproblem)  # min coins for the smaller amount
                best = min(best, result + 1)                 # +1 for coin c

            memo[rem] = best
            return best

        result = dfs(amount)
        return result if result != float('inf') else -1