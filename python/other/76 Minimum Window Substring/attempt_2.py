import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        r = 0

        dict_t = collections.Counter(t)
        required = len(dict_t)

        formed = 0

        window_count = collections.defaultdict(int)

        ans = float("inf"), None, None

        while r < len(s):

            character = s[r]

            window_count[character] += 1

            if character in dict_t and dict_t[character] == window_count[character]:
                formed += 1

            while l <= r and formed == required:

                character = s[l]

                if (r - l + 1) < ans[0]:
                    ans = (r - l + 1, l, r)

                window_count[character] -= 1

                if character in dict_t and window_count[character] < dict_t[character]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
