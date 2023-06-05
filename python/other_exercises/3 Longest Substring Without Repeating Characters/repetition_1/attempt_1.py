class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        alph = [0 for _ in range(26)]
        max_len = 0
        left = 0
        right = 0

        for letter in s:
            letter_index = ord(letter) - ord('a')

            if alph[letter_index] == 0:
                right += 1
                alph[letter_index] += 1

            else:
                cr_len = right - left
                max_len = max(cr_len, max_len)

                while s[left] != letter:
                    del_letter_in = ord(s[left]) - ord('a')
                    alph[del_letter_in] -= 1
                    left += 1

                del_letter_in = ord(s[left]) - ord('a')
                alph[del_letter_in] = 1
                left += 1

                right += 1

        cr_len = right - left
        max_len = max(cr_len, max_len)

        return max_len

