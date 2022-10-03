class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        mod = pow(10, 9) + 7

        dp = [[0]*(target + 1) for _ in range(n + 1)]

        for i in range(1, min(k + 1, target + 1)):
            dp[1][i] = 1

        for dice_throw in range(2, n + 1):

            for potential_value in range(1, target + 1):

                for face in range(1, k + 1):

                    remainder = potential_value - face

                    if remainder >= 0:
                        dp[dice_throw][potential_value] += dp[dice_throw-1][remainder]

                dp[dice_throw][potential_value] %= mod

        return dp[-1][-1]

