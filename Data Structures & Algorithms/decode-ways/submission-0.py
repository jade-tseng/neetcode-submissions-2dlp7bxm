class Solution:
    def numDecodings(self, s: str) -> int:
        # initialize dp array
        dp = [0] * (len(s) + 1)

        # base case
        dp[0] = 1

        # loop through each position
        for i in range(1, len(s) + 1):

            # can I take 1 digit?
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            # can I take 2 digits?
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]