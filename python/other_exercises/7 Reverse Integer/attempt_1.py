import math


class Solution:
    def reverse(self, x: int) -> int:
        max_int = math.pow(2, 31) - 1
        min_int = math.pow(-2, 31)
        reverse = 0

        while x != 0:

            pow = x % 10 if x >= 0 else (abs(x) % 10) * (-1)
            x = x // 10 if x >= 0 else math.ceil(x / 10)

            if (reverse > (max_int // 10)) or (reverse == max_int // 10 and pow >= 7):
                return 0

            if (reverse < (math.ceil(min_int / 10))) or (reverse == (math.ceil(min_int)) and pow < -8):
                return 0

            reverse = reverse * 10 + pow

        return reverse
