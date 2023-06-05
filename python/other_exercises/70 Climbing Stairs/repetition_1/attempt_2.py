class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        dp = [0 for _ in range(n)]
        dp[-1] = 0
        dp[-2] = 1

        for position in range(n-3, -1, -1):
            dp[position] = 1 + dp[position+1] + dp[position+2]

        return dp[0]

