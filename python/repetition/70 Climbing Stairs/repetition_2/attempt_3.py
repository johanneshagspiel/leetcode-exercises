class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0 for _ in range(n + 1)]
        dp[n] = 1
        dp[n-1] = 2

        for position in range(n-2, -1, -1):
            dp[position] = dp[position+1] + dp[position+2]

        return dp[0]
