class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        mod = pow(10, 9) + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        for face in range(1, min(k + 1, target + 1)):
            dp[1][face] = 1

        for dice in range(2, n + 1):
            for target_value in range(1, target + 1):
                for face in range(1, k + 1):
                    remainder = target_value - face

                    if remainder >= 0:
                        dp[dice][target_value] += dp[dice - 1][remainder]
                        dp[dice][target_value] %= mod

        return dp[-1][-1]
