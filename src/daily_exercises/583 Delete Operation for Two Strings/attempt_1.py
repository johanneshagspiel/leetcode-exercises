class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        return len(word1) + len(word2) - 2*self.longest_subsequence(word1, word2, len(word1), len(word2))

    def longest_subsequence(self, word1, word2, m ,n):
        if (m == 0) or (n == 0):
            return 0
        elif word1[m-1] == word2[n-1]:
            return 1 + self.longest_subsequence(word1, word2, m-1, n-1)
        else:
            return max(self.longest_subsequence(word1, word2, m, n-1), self.longest_subsequence(word1, word2, m-1, n))