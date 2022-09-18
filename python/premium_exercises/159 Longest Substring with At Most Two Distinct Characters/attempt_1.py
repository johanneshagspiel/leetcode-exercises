import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        left = 0
        right = 0

        letter_counter = collections.defaultdict(int)
        unique_letter_count = 0

        longest_substring = 0

        for char in s:

            if letter_counter[char] == 0:
                letter_counter[char] += 1
                unique_letter_count += 1
            else:
                letter_counter[char] += 1

            right += 1

            if unique_letter_count > 2:

                while unique_letter_count > 2:

                    left_letter = s[left]
                    letter_counter[left_letter] -= 1

                    if letter_counter[left_letter] == 0:
                        unique_letter_count -= 1

                    left += 1

            longest_substring = max(longest_substring, right - left)

        return longest_substring