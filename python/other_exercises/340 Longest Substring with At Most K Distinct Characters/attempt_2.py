import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        map = collections.defaultdict(int)

        left = 0
        right = 0

        unique_characters = 0

        maximum_substring = 0

        for char in s:

            if map[char] == 0:
                map[char] += 1
                unique_characters += 1
            else:
                map[char] += 1

            right += 1

            if unique_characters > k:

                while unique_characters > k:

                    left_char = s[left]
                    map[left_char] -= 1

                    if map[left_char] == 0:
                        unique_characters -= 1

                    left += 1

            maximum_substring = max(maximum_substring, right - left)

        return maximum_substring