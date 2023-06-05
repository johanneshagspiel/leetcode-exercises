class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_palindrome = s[0]
        longest_palindrome_length = 1
        n = len(s)

        if n == 2:
            if s[0] == s[1]:
                return s
            else:
                return longest_palindrome

        for index in range(1, n - 1):

            if s[index - 1] == s[index + 1]:
                left = index - 1
                right = index + 1

                while left > 0 and right < n - 1 and s[left - 1] == s[right + 1]:
                    left -= 1
                    right += 1

                palindrome_length = right - left + 1
                if palindrome_length > longest_palindrome_length:
                    longest_palindrome = s[left: (right + 1)]
                    longest_palindrome_length = palindrome_length

            if s[index] == s[index - 1]:
                left = index - 1
                right = index

                while left > 0 and right < n - 1 and s[left - 1] == s[right + 1]:
                    left -= 1
                    right += 1

                palindrome_length = right - left + 1
                if palindrome_length > longest_palindrome_length:
                    longest_palindrome = s[left: (right + 1)]
                    longest_palindrome_length = palindrome_length
            
            if s[index] == s[index + 1]:
                left = index
                right = index + 1

                while left > 0 and right < n - 1 and s[left - 1] == s[right + 1]:
                    left -= 1
                    right += 1

                palindrome_length = right - left + 1
                if palindrome_length > longest_palindrome_length:
                    longest_palindrome = s[left: (right + 1)]
                    longest_palindrome_length = palindrome_length


        return longest_palindrome
