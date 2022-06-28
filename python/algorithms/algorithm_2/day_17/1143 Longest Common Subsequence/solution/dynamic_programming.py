class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        i_total = len(text1)
        j_total = len(text2)

        dp = [[0]*(j_total+1) for _ in range(i_total+1)]

        for i in range(1, i_total+1):
            for j in range(1, j_total+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]