class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        dp = [0 for number in range(n + 1)]

        for m_index in range(m + 1):
            temp = [0 for number in range(n + 1)]
            for n_index in range(n + 1):
                if (m_index == 0) or (n_index == 0):
                    temp[n_index] = m_index + n_index
                else:
                    if (word1[m_index - 1] == word2[n_index - 1]):
                        temp[n_index] = dp[n_index - 1]
                    else:
                        temp[n_index] = 1 + min(temp[n_index - 1], dp[n_index])
            dp = temp

        return dp[n]