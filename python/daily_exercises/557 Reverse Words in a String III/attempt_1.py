import collections


class Solution:
    def reverseWords(self, s: str) -> str:

        def reverse_word(s):

            left = 0
            right = len(s) - 1

            while left <= right:
                s[left], s[right] = s[right],s[left]
                left += 1
                right -= 1

            return "".join(s)

        word_list = s.split(" ")

        res = ""

        for word in word_list:
            reversed = reverse_word(list(word))
            res += reversed + " "

        return res[:-1]

