class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i, char_1 in enumerate(text1):
            for j, char_2 in enumerate(text2):

                if char_1 == char_2:
                    dp[i + 1][j + 1] += 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] += max(dp[i][j + 1], dp[i + 1][j])

        return dp[-1][-1]
