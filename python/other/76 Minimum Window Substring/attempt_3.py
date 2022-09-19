import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left = 0
        right = 0

        frequency_counter = collections.Counter(t)
        window_counter = collections.defaultdict(int)

        needed = len(frequency_counter)
        formed = 0

        min_len = float("inf")
        ans = ""

        while right < len(s):

            right_character = s[right]

            if right_character in frequency_counter:
                window_counter[right_character] += 1

                if window_counter[right_character] == frequency_counter[right_character]:
                    formed += 1


            while left <= right and formed == needed:

                left_character = s[left]

                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    ans = s[left:(right+1)]

                if left_character in frequency_counter:
                    window_counter[left_character] -= 1

                    if window_counter[left_character] < frequency_counter[left_character]:
                        formed -= 1

                left += 1

            right += 1

        return ans

