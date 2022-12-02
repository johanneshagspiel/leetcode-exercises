class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        word1_count_arr = [0] * 26
        word2_count_arr = [0] * 26

        for i in range(len(word1)):
            word1_count_arr[ord(word1[i]) - ord("a")] += 1
            word2_count_arr[ord(word2[i]) - ord("a")] += 1

        for i in range(26):
            count_1 = word1_count_arr[i]
            count_2 = word2_count_arr[i]

            if count_1 == 0 and count_2 != 0:
                return False

            if count_2 == 0 and count_1 != 0:
                return False

        word1_count_arr.sort()
        word2_count_arr.sort()

        return word1_count_arr == word2_count_arr
