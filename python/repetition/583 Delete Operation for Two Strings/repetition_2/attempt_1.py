class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        len_1 = len(word1)
        len_2 = len(word2)

        dp = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]

        for index in range(len_1 + 1):
            dp[index][0] = index

        for index in range(len_2 + 1):
            dp[0][index] = index

        for i in range(1, len_1 + 1):
            for j in range(1, len_2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]
