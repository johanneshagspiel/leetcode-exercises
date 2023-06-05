import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        counter = collections.Counter(t)
        window_counter = collections.defaultdict(int)

        needed = len(counter)
        formed = 0

        left = 0
        right = 0

        ans = ""
        min_substring = float("inf")

        while right < len(s):

            right_char = s[right]

            if right_char in counter:
                window_counter[right_char] += 1

                if window_counter[right_char] == counter[right_char]:
                    formed += 1

            right += 1

            while formed == needed:

                if right - left < min_substring:
                    min_substring = right - left
                    ans = s[left:right]

                left_char = s[left]

                if left_char in counter:
                    window_counter[left_char] -= 1

                    if window_counter[left_char] < counter[left_char]:
                        formed -= 1

                left += 1

        return ans
