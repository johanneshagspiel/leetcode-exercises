# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        left = 0
        right = n

        while left <= right:
            pivot = left + ((right - left) // 2)

            response = guess(pivot)

            if response == 0:
                return pivot

            elif response == 1:
                left = pivot + 1

            else:
                right = pivot - 1

        return left
