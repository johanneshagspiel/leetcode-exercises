class Solution:
    def reverse(self, x: int) -> int:

        min_int = pow(-2, 31)
        max_int = pow(2, 31) - 1

        reverse = 0

        while x != 0:

            pop = (x % 10) if x >= 0 else (abs(x) % 10) * (-1)
            x = (x // 10) if x >= 0 else (math.ceil(x / 10))

            if (reverse > max_int // 10) or (reverse == (max_int // 10) and pop > 7):
                return 0

            if (reverse < math.ceil(min_int / 10)) or (reverse == math.ceil(min_int / 10) and pop < -8):
                return 0

            reverse = reverse * 10 + pop

        return reverse
