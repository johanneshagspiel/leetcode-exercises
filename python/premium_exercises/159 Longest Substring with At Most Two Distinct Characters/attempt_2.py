import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        map = collections.defaultdict(int)
        unique_characters = 0

        left = 0
        right = 0

        max_substring = 0

        for char in s:

            if map[char] == 0:
                map[char] += 1
                unique_characters += 1
            else:
                map[char] += 1

            right += 1

            if unique_characters > 2:

                while unique_characters > 2:

                    left_char = s[left]
                    map[left_char] -= 1

                    if map[left_char] == 0:
                        unique_characters -= 1

                    left += 1

            max_substring = max(max_substring, right - left)

        return max_substring

