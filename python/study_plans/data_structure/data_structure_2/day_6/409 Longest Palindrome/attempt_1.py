import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:

        counter = collections.Counter(s)

        odd_taken = False
        count = 0

        for letter, num in counter.items():
            if num % 2 == 0:
                count += num
            else:
                if odd_taken:
                    count += (num - 1)
                else:
                    count += num
                    odd_taken = True

        return count
