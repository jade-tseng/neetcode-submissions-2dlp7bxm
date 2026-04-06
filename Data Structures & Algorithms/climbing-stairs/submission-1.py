class Solution:
    def climbStairs(self, n: int) -> int:
        # base case:
        if n <= 2:
            return n
        #
        l, r = 1, 2
        for _ in range(3, n+1):
            l, r = r, l + r
        
        return r