class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)

        if len_s == 1:
            return s
        else:
            longest_palindrome = s[0]

            for mid_index in range(1, len_s - 1, 1):
                left_pointer = mid_index - 1
                right_pointer = mid_index + 1
                palindrome_length = 1

                while left_pointer >= 0 and right_pointer <= (len_s - 1):
                    if s[left_pointer] == s[right_pointer]:
                        left_pointer -= 1
                        right_pointer += 1
                        palindrome_length += 2
                    else:
                        break

                left_pointer += 1
                right_pointer -= 1

                palindrome = s[left_pointer:(right_pointer+1)]
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome

                if s[mid_index] == s[mid_index+1]:
                    palindrome = s[mid_index:(mid_index+2)]
                    if len(palindrome) > len(longest_palindrome):
                        longest_palindrome = palindrome

        return longest_palindrome

if __name__ == "__main__":
    solution = Solution()
    solution.longestPalindrome("ac")