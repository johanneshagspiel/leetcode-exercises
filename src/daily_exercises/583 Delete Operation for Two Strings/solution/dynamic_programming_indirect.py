class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for number in range(m + 1)]

        for m_index in range(m+1):
            for n_index in range(n+1):
                if (m_index == 0) or (n_index == 0):
                    continue
                if word1[m_index - 1] == word2[n_index - 1]:
                    dp[m_index][n_index] = 1 + dp[m_index-1][n_index-1]
                else:
                    dp[m_index][n_index] = max(dp[m_index-1][n_index], dp[m_index][n_index-1])

        return m + n - (2*dp[m][n])