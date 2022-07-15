import copy


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        len_1 = len(text1)
        len_2 = len(text2)

        if len_2 > len_1:
            text1, text2 = text2, text1

        start_array = [0 for _ in range(len(text2)+1)]

        current = copy.deepcopy(start_array)
        previous = copy.deepcopy(start_array)

        for i in range(1, len_1+1):
            for j in range(1, len_2+1):
                if text1[i-1] == text2[j-1]:
                    current[j] = 1 + previous[j-1]
                else:
                    current[j] = max(current[j-1], previous[j])

            previous = current
            current = copy.deepcopy(start_array)

        return previous[-1]
