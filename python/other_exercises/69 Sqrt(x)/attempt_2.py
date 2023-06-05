class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        left = 2
        right = x // 2

        while left <= right:

            mid = left + ((right - left) // 2)
            prod = mid * mid

            if prod == x:
                return mid

            elif prod < x:
                left = mid + 1

            else:
                right = mid - 1

        return right
