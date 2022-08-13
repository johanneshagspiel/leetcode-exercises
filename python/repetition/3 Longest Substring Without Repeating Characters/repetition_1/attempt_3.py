class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        pdic = {}
        i = 0
        N = len(s)
        max_len = 0

        for j in range(N):
            letter = s[j]

            if letter in pdic:
                i = max(pdic[letter], i)

            max_len = max(max_len, j - i + 1)
            pdic[letter] = j + 1

        return max_len
