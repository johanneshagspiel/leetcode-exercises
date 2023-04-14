class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        max_length = len(s)
        max_palindrom = 1

        def is_palindrome(sequence):
            return sequence == sequence[::-1]

        def get_longest_palindrome(prev_sequence, index):

            nonlocal max_palindrom

            if index == max_length:
                if is_palindrome(prev_sequence):
                    max_palindrom = max(max_palindrom, len(prev_sequence))

            else:

                old_copy = prev_sequence
                get_longest_palindrome(old_copy, index + 1)
                new_sequence = prev_sequence + s[index]
                get_longest_palindrome(new_sequence, index + 1)

        get_longest_palindrome("", 0)
        return max_palindrom
