class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        we do a sliding window of prices[i:j]
        profit = prices[j] - prices[i]
        we keep sliding j right until the max_profit decreases
        we record that max profit
        then we slide i right
        """

        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            
            r += 1
        
        return max_profit

            