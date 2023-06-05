import math


class Solution:
    def reverse(self, x: int) -> int:

        min_int = pow(-2, 31)
        max_int = pow(2, 31) - 1

        reverse = 0

        while x != 0:

            power = x % 10 if x >= 0 else (-1) * (abs(x) % 10)
            x = x // 10 if x >= 0 else math.ceil(x / 10)

            if (reverse > (max_int // 10)) or (reverse == (max_int // 10) and power > 7):
                return 0

            if (reverse < (math.ceil(min_int / 10))) or (reverse == (math.ceil(min_int / 10)) and power < -8):
                return 0

            reverse = reverse * 10 + power

        return reverse
