import copy
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text1) < len(text2):
            text1, text2 = text2, text1

        start_current = [0 for _ in range(len(text2) + 1)]
        previous = copy.deepcopy(start_current)
        current = copy.deepcopy(start_current)

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    current[j] = 1 + previous[j - 1]
                else:
                    current[j] = max(current[j-1], previous[j])
            previous = current
            current = copy.deepcopy(start_current)

        return previous[-1]