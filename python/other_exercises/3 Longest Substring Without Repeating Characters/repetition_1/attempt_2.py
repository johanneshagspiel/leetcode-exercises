class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        pdic = {}
        N = len(s)
        i = 0
        ans = 0

        for j in range(N):

            if s[j] in pdic:
                i = max(i, pdic[s[j]])

            ans = max(ans, j - i + 1)
            pdic[s[j]] = j + 1

        return ans
