class Solution:
    def partitionString(self, s: str) -> int:

        res = 1
        char_ar = [-1 for _ in range(26)]
        substringStart = 0

        for i in range(len(s)):

            if char_ar[ord(s[i]) - 97] >= substringStart:
                res += 1
                substringStart = i

            char_ar[ord(s[i]) - 97] = i

        return res
