class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:

            longest_palindrome = ""
            longest_palindrome_length = 0

            n = len(s)

            for index in range(1, n):

                left = index - 1
                right = index + 1

                if left >= 0 and right < n and s[left] == s[right]:
                    while left > 0 and right < n - 1:
                        if s[left+1] == s[right+1]:
                            left -= 1
                            right += 1
                        else:
                            break

                    if left < 0 or right >= n:
                        left += 1
                        right -= 1

                    palindrome_length = right - left + 1
                    if palindrome_length > longest_palindrome_length:
                        longest_palindrome = s[left:(right+1)]
                        longest_palindrome_length = palindrome_length

                if index < n - 2:
                    left = index
                    right = index + 1

                    if s[left] == s[right]:

                        while left > 0 and right < n - 1:
                            if s[left+1] == s[right+1]:
                                left -= 1
                                right += 1
                            else:
                                break

                        if left < 0 or right >= n:
                            left += 1
                            right -= 1

                        palindrome_length = right - left + 1
                        if palindrome_length > longest_palindrome_length:
                            longest_palindrome = s[left:(right+1)]
                            longest_palindrome_length = palindrome_length

            return longest_palindrome
