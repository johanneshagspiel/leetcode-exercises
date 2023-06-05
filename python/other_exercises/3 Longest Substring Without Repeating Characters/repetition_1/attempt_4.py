class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        pdic = {}
        i = 0
        maxlen = 0
        N = len(s)

        for j in range(N):

            letter = s[j]

            if letter in pdic:
                i = max(i, pdic[letter])

            maxlen = max(maxlen, j - i + 1)
            pdic[letter] = j + 1

        return maxlen



