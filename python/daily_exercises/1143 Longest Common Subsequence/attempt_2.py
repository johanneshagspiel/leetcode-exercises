class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if len(text1) < len(text2):
            temp = text2
            text2 = text1
            text1 = temp

        prev_row = [0 for _ in range(len(text2) + 1)]
        current_row = [0 for _ in range(len(text2) + 1)]

        for i, char_1 in enumerate(text1):
            for j, char_2 in enumerate(text2):

                if char_1 == char_2:
                    current_row[j + 1] += 1 + prev_row[j]
                else:
                    current_row[j + 1] += max(prev_row[j + 1], current_row[j])

            prev_row = current_row
            current_row = [0 for _ in range(len(text2) + 1)]

        return prev_row[-1]
