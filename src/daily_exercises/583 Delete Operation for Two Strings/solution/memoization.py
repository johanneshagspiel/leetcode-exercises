class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        memo = [[0] * (n + 1) for number in range(m + 1)]

        return len(word1) + len(word2) - 2 * self.longest_subsequence(word1, word2, m, n, memo)

    def longest_subsequence(self, word1, word2, m, n, memo):
        if (m == 0) or (n == 0):
            return 0
        if memo[m][n] > 0:
            return memo[m][n]
        elif word1[m - 1] == word2[n - 1]:
            memo[m][n] = 1 + self.longest_subsequence(word1, word2, m - 1, n - 1, memo)
        else:
            memo[m][n] = max(self.longest_subsequence(word1, word2, m, n - 1, memo),
                             self.longest_subsequence(word1, word2, m - 1, n, memo))
        return memo[m][n]