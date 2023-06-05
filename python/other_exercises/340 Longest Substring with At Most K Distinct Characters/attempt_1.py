import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        left = 0
        right = 0

        longest_substring = 0
        counter = collections.defaultdict(int)

        unique_chars = 0

        for char in s:

            if counter[char] == 0:
                counter[char] += 1
                unique_chars += 1

            else:
                counter[char] += 1

            right += 1

            if unique_chars > k:

                while unique_chars > k:

                    left_char = s[left]
                    counter[left_char] -= 1

                    if counter[left_char] == 0:
                        unique_chars -= 1

                    left += 1

            longest_substring = max(longest_substring, right - left)

        return longest_substring

