class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ""
        index_1 = 0
        index_2 = 0

        odd = True

        while index_1 < len(word1) and index_2 < len(word2):

            if odd:
                res += word1[index_1]
                index_1 += 1
                odd = False
            else:
                res += word2[index_2]
                index_2 += 1
                odd = True

        if index_1 < len(word1):
            res += word1[index_1:]

        if index_2 < len(word2):
            res += word2[index_2:]

        return res
