class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0

        elif n == 1:
            return 1

        else:
            dp = [0 for _ in range(n+1)]
            dp[0] = 0
            dp[1] = 1

            for num in range(2, n + 1):
                dp[num] = dp[num - 1] + dp[num - 2]

            return dp[n]
