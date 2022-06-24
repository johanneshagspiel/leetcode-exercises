class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for number in range(3, n + 1):
            dp[number] = dp[number - 1] + dp[number - 2]

        return dp[n]
