class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        dp = [0 for _ in range(n + 1)]

        two_ago = 1
        one_ago = 0 if s[0] == "0" else 1

        for i in range(2, n + 1):

            current = 0

            if 1 <= int(s[i - 1:i]) <= 9:
                current += one_ago

            if 10 <= int(s[i - 2:i]) <= 26:
                current += two_ago

            two_ago = one_ago
            one_ago = current

        return one_ago
