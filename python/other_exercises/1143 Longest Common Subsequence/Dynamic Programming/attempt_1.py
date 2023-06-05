import copy
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)

        start = [0 for _ in range(m + 1)]

        current = copy.deepcopy(start)
        previous = copy.deepcopy(start)

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if text1[i - 1] == text2[j - 1]:
                    current[j] = 1 + previous[j - 1]
                else:
                    current[j] = max(previous[j], current[j - 1])

            previous = current
            current = copy.deepcopy(start)

        return previous[-1]
