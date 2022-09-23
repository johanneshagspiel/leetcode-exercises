import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        s_counter = collections.defaultdict(int)
        t_counter = collections.Counter(t)

        needed = len(t_counter)
        formed = 0

        right = 0
        left = 0

        min_substring = float("inf")
        ans = ""

        while right < len(s):

            right_char = s[right]

            if right_char in t_counter:
                s_counter[right_char] += 1

                if t_counter[right_char] == s_counter[right_char]:
                    formed += 1


            while formed == needed:

                if right - left < min_substring:
                    min_substring = right - left
                    ans = s[left:(right+1)]

                left_char = s[left]

                if left_char in t_counter:
                    s_counter[left_char] -= 1

                    if s_counter[left_char] < t_counter[left_char]:
                        formed -= 1

                left += 1

            right += 1

        return ans
