class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0 for _ in range(n + 1)]
        dp[1] = 1

        for i in range(n+1):
            for j in range(i+1):
                factor_1 = max(dp[j], j)
                factor_2 = max(dp[i-j], (i-j))
                dp[i] = max(dp[i], factor_1 * factor_2)

        return dp[-1]