class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        len_1 = len(s)
        len_2 = len(t)

        if len_1 != len_2:
            return False

        letter_list = [0 for _ in range(26)]

        for point in range(len_1):

            letter_1_ind = ord(s[point]) - ord('a')
            letter_list[letter_1_ind] += 1

            letter_2_ind = ord(t[point]) - ord('a')
            letter_list[letter_2_ind] -= 1


        for letter_in in range(26):
            if letter_list[letter_in] > 0:
                return False

        return True
