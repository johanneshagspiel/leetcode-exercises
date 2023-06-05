from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        N = len(digits)
        carry = 0
        start = True

        for position in range(N-1, -1, -1):

            if start:
                if digits[position] == 9:
                    digits[position] = 0
                    carry = 1
                else:
                    digits[position] += 1

                start = False
            else:
                if carry == 1:
                    if digits[position] == 9:
                        digits[position] = 0
                    else:
                        digits[position] += 1
                        carry = 0
                else:
                    break

        if carry == 1:
            digits.insert(0, 1)

        return digits
