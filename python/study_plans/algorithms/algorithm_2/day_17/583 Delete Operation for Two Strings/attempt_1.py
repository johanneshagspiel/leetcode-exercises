class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        dp = [[0]*(n+1) for _ in range(m + 1)]

        for temp in range(1, m + 1):
            dp[temp][0] = temp

        for temp in range(1, n + 1):
            dp[0][temp] = temp

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]