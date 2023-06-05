class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        longest_palindrome = s[0]
        longest_palindrome_length = 1

        if n == 2:
            if s[0] == s[1]:
                return s
            else:
                return longest_palindrome

        def expand_around_center(left, right):

            while left > 0 and right < n - 1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            return left, right

        for index in range(n - 1):
            left, right = expand_around_center(index, index)
            palindrome_length = right - left + 1
            if palindrome_length > longest_palindrome_length:
                longest_palindrome = s[left:(right + 1)]
                longest_palindrome_length = palindrome_length

            if s[index] == s[index + 1]:
                left, right = expand_around_center(index, index + 1)
                palindrome_length = right - left + 1
                if palindrome_length > longest_palindrome_length:
                    longest_palindrome = s[left:(right + 1)]
                    longest_palindrome_length = palindrome_length

        return longest_palindrome

