
class Solution:
    MIN_INT = pow(-2, 31)
    MAX_INT = pow(2, 31) - 1

    def divide(self, dividend: int, divisor: int) -> int:

        positive_sign = ((dividend > 0) & (divisor > 0)) | ((dividend < 0) & (divisor < 0))
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)

        if abs_divisor > abs_dividend:
            result = 0
        elif abs_divisor == abs_dividend:
            result = 1
        else:
            result = self.recursive_divide(abs_dividend, abs_divisor)

        if positive_sign:
            result = result
        else:
            result = - result

        if result > Solution.MAX_INT:
            result = Solution.MAX_INT
        elif result < Solution.MIN_INT:
            result = Solution.MIN_INT

        return result

    def recursive_divide(self, dividend, divisor):
        quotient = 1
        accumulator = divisor

        if dividend < divisor:
            return 0
        elif dividend == divisor:
            return 1

        while accumulator < dividend:
            accumulator = accumulator << 1
            quotient = quotient << 1

        accumulator = accumulator >> 1
        quotient = quotient >> 1

        return quotient + self.recursive_divide(dividend - accumulator, divisor)


if __name__ == '__main__':
    solution = Solution()
    dividend = -2147483648
    divisor = -1
    output = solution.divide(dividend, divisor)
    print(output)
