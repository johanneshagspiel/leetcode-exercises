class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)

        two_back = 1
        one_back = 0 if s[0] == "0" else 1

        for i in range(2, n + 1):

            current = 0

            if 1 <= int(s[i - 1:i]) <= 9:
                current += one_back

            if 10 <= int(s[i - 2:i]) <= 26:
                current += two_back

            two_back = one_back
            one_back = current

        return one_back
