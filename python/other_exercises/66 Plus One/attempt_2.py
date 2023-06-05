from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        N = len(digits)

        for position in range(N-1, -1, -1):

            if digits[position] == 9:
                digits[position] = 0
            else:
                digits[position] += 1
                return digits

        digits.insert(0, 1)
        return digits

