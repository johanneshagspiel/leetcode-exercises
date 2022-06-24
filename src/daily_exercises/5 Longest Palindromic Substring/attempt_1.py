class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        len_s = len(s)

        for start_index in range(len_s):
            for end_index in range(start_index, len_s, 1):
                substring = s[start_index:end_index]
                valid = self.is_valid(substring)
                if valid:
                    if len(substring) > len(longest_palindrome):
                        longest_palindrome = substring

        return longest_palindrome

    def is_valid(self, string):
        return string == string[::-1]